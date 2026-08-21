"""Generate Chinese analysis using LLM API (Kimi preferred, DeepSeek fallback)."""

import os
import re
import time
import requests


KIMI_API = "https://api.moonshot.cn/v1/chat/completions"
DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"

def _clean_api_key(raw: str) -> str:
    """
    Remove characters that are illegal in HTTP headers — embedded newlines,
    tabs, spaces, control characters and quotes, commonly introduced when
    a key is copy-pasted into a GitHub secret (e.g. wrapped across lines).
    Real API keys contain none of these, so removing them is always safe.
    """
    return re.sub(r"[\s\x00-\x1f\x7f\"'`]", "", raw)


def _load_api_key(env_name: str) -> str:
    """Load an API key from the environment, sanitized for header use."""
    raw = os.environ.get(env_name, "")
    key = _clean_api_key(raw)
    if raw and key != raw:
        print(f"Warning: {env_name} contained hidden/invalid characters "
              f"(copy-paste artifact in the secret); sanitized automatically. "
              f"Please re-save the secret cleanly.")
    if key and not (key.isascii() and key.isprintable()):
        print(f"Warning: {env_name} contains non-ASCII characters and is unusable; ignoring it.")
        return ""
    return key


KIMI_API_KEY = _load_api_key("KIMI_API_KEY")
DEEPSEEK_API_KEY = _load_api_key("DEEPSEEK_API_KEY")
KIMI_MODEL = os.environ.get("KIMI_MODEL", "kimi-k2.5").strip()

# Delay between papers, only used by the per-paper fallback path.
# Moonshot free tier is ~3 requests/minute, so 25s keeps us safely under it.
REQUEST_INTERVAL = int(os.environ.get("LLM_REQUEST_INTERVAL", "25"))

PROMPT_TEMPLATE = """请分析以下水声工程领域的学术论文，生成三部分中文内容（论文标题保持英文，不要翻译）：

论文标题：{title}

论文摘要：{abstract}

请按以下格式输出：

【简介】
（用中文概括论文的研究背景、目标和主要内容，100-150字）

【关键技术与数据】
（分析论文使用的关键技术、方法、算法、数据集等，100-150字）

【结果与结论】
（总结论文的主要实验结果、性能指标、结论和创新点，100-150字）

要求：
1. 使用专业的水声工程术语
2. 内容准确、简洁、有条理
3. 不要添加任何额外的标记或说明
"""

BATCH_PROMPT_TEMPLATE = """请分析以下水声工程领域的 {n} 篇学术论文，为每篇生成三部分中文内容（论文标题保持英文，不要翻译）：

{papers_block}

请严格按以下格式逐篇输出，不要输出任何其它内容：

【论文1】
【简介】
（用中文概括该论文的研究背景、目标和主要内容，100-150字）
【关键技术与数据】
（分析该论文使用的关键技术、方法、算法、数据集等，100-150字）
【结果与结论】
（总结该论文的主要实验结果、性能指标、结论和创新点，100-150字）

【论文2】
【简介】
……
【关键技术与数据】
……
【结果与结论】
……

要求：
1. 使用专业的水声工程术语
2. 内容准确、简洁、有条理
3. 每篇都必须有【论文N】编号，编号与输入顺序一致
"""


# Providers that failed fatally (bad key / auth error / quota exhausted).
# There is no point retrying them for every remaining paper.
_DEAD_PROVIDERS: set[str] = set()


def _get_providers() -> list[tuple[str, str, str, str]]:
    """Return available providers as (name, api_url, api_key, model)."""
    providers = []
    if KIMI_API_KEY and "Kimi" not in _DEAD_PROVIDERS:
        providers.append(("Kimi", KIMI_API, KIMI_API_KEY, KIMI_MODEL))
    if DEEPSEEK_API_KEY and "DeepSeek" not in _DEAD_PROVIDERS:
        providers.append(("DeepSeek", DEEPSEEK_API, DEEPSEEK_API_KEY, "deepseek-chat"))
    return providers


def _is_quota_error(body: str) -> bool:
    """Detect quota/balance exhaustion (as opposed to transient rate limiting)."""
    lower = body.lower()
    return ("quota" in lower or "balance" in lower or "insufficient" in lower
            or "余额" in body or "欠费" in body)


def _call_llm(api_url: str, api_key: str, model: str, prompt: str,
              provider: str, max_retries: int = 3,
              max_tokens: int = 500) -> tuple[str, bool]:
    """
    Call one LLM provider with retries.
    Returns (content, fatal_error). fatal_error=True means retrying this
    provider is pointless (quota exhausted / auth failed) — move on.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": max_tokens
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(api_url, headers=headers, json=data, timeout=60)

            if response.status_code == 429:
                body = response.text[:300]
                print(f"    {provider} 429 (attempt {attempt + 1}/{max_retries}): {body}")
                if _is_quota_error(body):
                    print(f"    {provider} quota/balance exhausted, giving up on this provider")
                    _DEAD_PROVIDERS.add(provider)
                    return "", True
                wait_time = (2 ** attempt) * 60  # 60, 120, 240 seconds
                print(f"    Rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            if response.status_code in (401, 403):
                print(f"    {provider} auth error {response.status_code}: {response.text[:300]}")
                _DEAD_PROVIDERS.add(provider)
                return "", True

            if response.status_code != 200:
                print(f"    {provider} API error {response.status_code}: {response.text[:300]}")
                if attempt < max_retries - 1:
                    time.sleep(10)
                    continue
                return "", False

            result = response.json()
            return result["choices"][0]["message"]["content"], False

        except requests.exceptions.InvalidHeader as e:
            # Bad header (e.g. whitespace/newline in the API key) — the request
            # was never sent, retrying is pointless.
            print(f"    {provider} invalid API key format: {e}")
            print(f"    -> Check the {provider.upper()} secret for stray spaces/newlines")
            _DEAD_PROVIDERS.add(provider)
            return "", True
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) * 5
                print(f"    {provider} request error: {e}, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"    {provider} request failed after {max_retries} attempts: {e}")
                return "", False
        except (KeyError, IndexError) as e:
            print(f"    {provider} response parse error: {e}")
            return "", False

    return "", False


def _parse_content(content: str) -> tuple[str, str, str]:
    """Parse LLM output into (summary_zh, key_tech, results)."""
    summary_zh, key_tech, results = "", "", ""
    rest = content
    has_intro = "【简介】" in rest
    if has_intro:
        _, rest = rest.split("【简介】", 1)
    if "【关键技术与数据】" in rest:
        before, rest = rest.split("【关键技术与数据】", 1)
        if has_intro:
            summary_zh = before
    if "【结果与结论】" in rest:
        key_tech, rest = rest.split("【结果与结论】", 1)
        results = rest
    else:
        key_tech = rest
    summary_zh, key_tech, results = summary_zh.strip(), key_tech.strip(), results.strip()
    if not key_tech and not results:
        # Fallback: use the whole content as key_tech
        return summary_zh, content[:200], "（详见原文）"
    return summary_zh, key_tech, results


def _parse_batch(content: str, n: int) -> dict[int, tuple[str, str, str]]:
    """Parse batched LLM output into {paper_index: (summary_zh, key_tech, results)}."""
    parsed = {}
    # Split on 【论文N】 markers; split keeps the captured numbers
    parts = re.split(r"【\s*论文\s*(\d+)\s*】", content)
    for i in range(1, len(parts) - 1, 2):
        idx = int(parts[i]) - 1
        if 0 <= idx < n:
            parsed[idx] = _parse_content(parts[i + 1])
    return parsed


def generate_batch_analyses(papers: list) -> dict[int, tuple[str, str, str]]:
    """
    Analyze all papers in ONE LLM request instead of one request per paper.
    This avoids per-request rate-limit waits entirely, cutting the analysis
    phase from ~9 requests / several minutes to a single call.
    Returns {paper_index: (summary_zh, key_tech, results)}; may be partial or empty.
    """
    providers = _get_providers()
    if not providers:
        return {}

    papers_block = "\n\n".join(
        f"论文{i}标题：{p.title}\n论文{i}摘要：{p.summary or '（无摘要）'}"
        for i, p in enumerate(papers, start=1)
    )
    prompt = BATCH_PROMPT_TEMPLATE.format(n=len(papers), papers_block=papers_block)

    # 9 papers x ~450 Chinese chars of output needs much more than the
    # per-paper 500-token cap.
    batch_max_tokens = max(4096, len(papers) * 700)

    for provider, api_url, api_key, model in providers:
        content, fatal = _call_llm(api_url, api_key, model, prompt, provider,
                                   max_tokens=batch_max_tokens)
        if content:
            parsed = _parse_batch(content, len(papers))
            if parsed:
                print(f"  Batch analysis succeeded via {provider}: "
                      f"{len(parsed)}/{len(papers)} papers parsed")
                return parsed
            print(f"  {provider} batch output could not be parsed, trying next provider")
        if fatal:
            continue  # next provider

    return {}


def generate_analysis(title: str, abstract: str, max_retries: int = 3) -> tuple[str, str, str]:
    """
    Generate Chinese summary, key_technology and results_conclusion via LLM API.
    Tries each configured provider in order (Kimi, then DeepSeek).
    Returns (summary_zh, key_tech, results) as Chinese text.
    """
    providers = _get_providers()
    if not providers:
        print("Warning: No LLM API key set (KIMI_API_KEY / DEEPSEEK_API_KEY), skipping analysis generation")
        return "", "", ""

    prompt = PROMPT_TEMPLATE.format(title=title, abstract=abstract)

    for provider, api_url, api_key, model in providers:
        content, _fatal = _call_llm(api_url, api_key, model, prompt, provider, max_retries,
                                    max_tokens=800)
        if content:
            return _parse_content(content)
        # Any failure on this provider -> try the next one

    return "", "", ""


def generate_all_analyses(papers: list) -> None:
    """Generate analyses for all papers (batch first, per-paper fallback)."""
    providers = _get_providers()
    if not providers:
        print("Warning: No LLM API key set (KIMI_API_KEY / DEEPSEEK_API_KEY), skipping all analyses")
        return

    provider_names = ", ".join(f"{name}({model})" for name, _, _, model in providers)
    print(f"Generating Chinese analyses for {len(papers)} papers, providers: {provider_names}")

    # Fast path: one batched request for all papers
    results = generate_batch_analyses(papers)

    # Slow path: per-paper calls for anything the batch missed
    missing = [i for i in range(len(papers)) if i not in results]
    for count, i in enumerate(missing, start=1):
        if not _get_providers():
            print("  All LLM providers are unavailable, skipping remaining analyses")
            break
        paper = papers[i]
        print(f"  [fallback {count}/{len(missing)}] Analyzing: {paper.title[:50]}...")
        results[i] = generate_analysis(paper.title, paper.summary)

        # Delay between requests to stay under rate limits
        if count < len(missing):
            print(f"    Waiting {REQUEST_INTERVAL}s before next request...")
            time.sleep(REQUEST_INTERVAL)

    applied = 0
    for i, paper in enumerate(papers):
        summary_zh, key_tech, res = results.get(i, ("", "", ""))
        if summary_zh:
            paper.summary_zh = summary_zh
        if key_tech:
            paper.key_tech = key_tech
        if res:
            paper.results = res
        if summary_zh or key_tech or res:
            applied += 1

    print(f"Analysis generation completed! ({applied}/{len(papers)} papers analyzed)")


# ==================== 新闻分析 ====================

NEWS_BATCH_PROMPT_TEMPLATE = """请将以下 {n} 条水声工程/海洋科技领域的新闻改写为结构化中文新闻稿，为每条生成四部分内容：

{news_block}

请严格按以下格式逐条输出，不要输出任何其它内容：

【新闻1】
【中文标题】
（一句通顺的中文标题，不超过30字）
【事件概述】
（概括事件主体、时间、核心内容，80-120字）
【事实与证据】
（列出新闻中明确提到的事实、数据、引语，不添加推测，80-150字）
【影响与观察】
（分析该事件对水声工程/海洋技术领域的意义和值得关注的后续进展，60-100字）

【新闻2】
……

要求：
1. 使用专业术语，事实部分不得虚构原文没有的内容
2. 如果输入信息不足，事实与证据部分简短说明即可，不要编造
3. 每条都必须有【新闻N】编号，编号与输入顺序一致
"""


def _parse_news_content(content: str) -> tuple[str, str, str, str]:
    """Parse one news item's LLM output into (title_zh, overview, facts, impact)."""
    sections = {}
    rest = content
    for marker, key in [("【中文标题】", "title"), ("【事件概述】", "overview"),
                        ("【事实与证据】", "facts"), ("【影响与观察】", "impact")]:
        if marker in rest:
            before, rest = rest.split(marker, 1)
            if sections:
                sections[list(sections)[-1]] = before
            sections[key] = ""
    if sections:
        sections[list(sections)[-1]] = rest
    return (
        sections.get("title", "").strip(),
        sections.get("overview", "").strip(),
        sections.get("facts", "").strip(),
        sections.get("impact", "").strip(),
    )


def _parse_news_batch(content: str, n: int) -> dict[int, tuple[str, str, str, str]]:
    """Parse batched news LLM output into {index: (title_zh, overview, facts, impact)}."""
    parsed = {}
    parts = re.split(r"【\s*新闻\s*(\d+)\s*】", content)
    for i in range(1, len(parts) - 1, 2):
        idx = int(parts[i]) - 1
        if 0 <= idx < n:
            parsed[idx] = _parse_news_content(parts[i + 1])
    return parsed


def generate_all_news_analyses(news_items: list) -> None:
    """Rewrite all news items into structured Chinese articles in ONE request."""
    if not news_items:
        return
    providers = _get_providers()
    if not providers:
        print("Warning: No LLM API key set, news will use original titles/snippets")
        return

    news_block = "\n\n".join(
        f"新闻{i}标题：{item.title}\n新闻{i}来源：{item.source_name}\n"
        f"新闻{i}摘要：{item.snippet or '（无摘要，请仅根据标题概括，并在事实部分注明信息有限）'}"
        for i, item in enumerate(news_items, start=1)
    )
    prompt = NEWS_BATCH_PROMPT_TEMPLATE.format(n=len(news_items), news_block=news_block)
    batch_max_tokens = max(4096, len(news_items) * 800)

    parsed = {}
    for provider, api_url, api_key, model in providers:
        content, _fatal = _call_llm(api_url, api_key, model, prompt, provider,
                                    max_tokens=batch_max_tokens)
        if content:
            parsed = _parse_news_batch(content, len(news_items))
            if parsed:
                print(f"  News rewriting succeeded via {provider}: "
                      f"{len(parsed)}/{len(news_items)} items parsed")
                break
            print(f"  {provider} news output could not be parsed, trying next provider")

    for i, item in enumerate(news_items):
        title_zh, overview, facts, impact = parsed.get(i, ("", "", "", ""))
        if title_zh:
            item.title_zh = title_zh
        if overview:
            item.overview = overview
        if facts:
            item.facts = facts
        if impact:
            item.impact = impact


if __name__ == "__main__":
    # Test
    title = "An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks"
    abstract = "Time Division Multiple Access (TDMA)-based Medium Access Control (MAC) protocols have proven their practicality..."

    summary_zh, key_tech, results = generate_analysis(title, abstract)
    print("简介：", summary_zh)
    print("关键技术与数据：", key_tech)
    print("结果与结论：", results)
