"""Generate Chinese analysis using LLM API (Kimi preferred, DeepSeek fallback)."""

import os
import time
import requests


KIMI_API = "https://api.moonshot.cn/v1/chat/completions"
DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"

KIMI_API_KEY = os.environ.get("KIMI_API_KEY", "")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
KIMI_MODEL = os.environ.get("KIMI_MODEL", "kimi-k2.5")

# Delay between papers. Moonshot free tier is ~3 requests/minute,
# so 25s keeps us safely under the limit.
REQUEST_INTERVAL = 25

PROMPT_TEMPLATE = """请分析以下水声工程领域的学术论文，生成两部分中文内容：

论文标题：{title}

论文摘要：{abstract}

请按以下格式输出：

【关键技术与数据】
（分析论文使用的关键技术、方法、算法、数据集等，100-150字）

【结果与结论】
（总结论文的主要实验结果、性能指标、结论和创新点，100-150字）

要求：
1. 使用专业的水声工程术语
2. 内容准确、简洁、有条理
3. 不要添加任何额外的标记或说明
"""


def _get_providers() -> list[tuple[str, str, str, str]]:
    """Return available providers as (name, api_url, api_key, model)."""
    providers = []
    if KIMI_API_KEY:
        providers.append(("Kimi", KIMI_API, KIMI_API_KEY, KIMI_MODEL))
    if DEEPSEEK_API_KEY:
        providers.append(("DeepSeek", DEEPSEEK_API, DEEPSEEK_API_KEY, "deepseek-chat"))
    return providers


def _is_quota_error(body: str) -> bool:
    """Detect quota/balance exhaustion (as opposed to transient rate limiting)."""
    lower = body.lower()
    return ("quota" in lower or "balance" in lower or "insufficient" in lower
            or "余额" in body or "欠费" in body)


def _call_llm(api_url: str, api_key: str, model: str, prompt: str,
              provider: str, max_retries: int = 3) -> tuple[str, bool]:
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
        "max_tokens": 500
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(api_url, headers=headers, json=data, timeout=60)

            if response.status_code == 429:
                body = response.text[:300]
                print(f"    {provider} 429 (attempt {attempt + 1}/{max_retries}): {body}")
                if _is_quota_error(body):
                    print(f"    {provider} quota/balance exhausted, giving up on this provider")
                    return "", True
                wait_time = (2 ** attempt) * 60  # 60, 120, 240 seconds
                print(f"    Rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            if response.status_code in (401, 403):
                print(f"    {provider} auth error {response.status_code}: {response.text[:300]}")
                return "", True

            if response.status_code != 200:
                print(f"    {provider} API error {response.status_code}: {response.text[:300]}")
                if attempt < max_retries - 1:
                    time.sleep(10)
                    continue
                return "", False

            result = response.json()
            return result["choices"][0]["message"]["content"], False

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


def _parse_content(content: str) -> tuple[str, str]:
    """Parse LLM output into (key_tech, results)."""
    if "【关键技术与数据】" in content and "【结果与结论】" in content:
        parts = content.split("【结果与结论】")
        key_tech = parts[0].replace("【关键技术与数据】", "").strip()
        results = parts[1].strip()
        return key_tech, results
    # Fallback: use the whole content as key_tech
    return content[:200], "（详见原文）"


def generate_analysis(title: str, abstract: str, max_retries: int = 3) -> tuple[str, str]:
    """
    Generate key_technology and results_conclusion using LLM API.
    Tries each configured provider in order (Kimi, then DeepSeek).
    Returns (key_tech, results) as Chinese text.
    """
    providers = _get_providers()
    if not providers:
        print("Warning: No LLM API key set (KIMI_API_KEY / DEEPSEEK_API_KEY), skipping analysis generation")
        return "", ""

    prompt = PROMPT_TEMPLATE.format(title=title, abstract=abstract)

    for provider, api_url, api_key, model in providers:
        content, _fatal = _call_llm(api_url, api_key, model, prompt, provider, max_retries)
        if content:
            return _parse_content(content)
        # Any failure on this provider -> try the next one

    return "", ""


def generate_all_analyses(papers: list) -> None:
    """Generate analyses for all papers."""
    providers = _get_providers()
    if not providers:
        print("Warning: No LLM API key set (KIMI_API_KEY / DEEPSEEK_API_KEY), skipping all analyses")
        return

    provider_names = ", ".join(f"{name}({model})" for name, _, _, model in providers)
    print(f"Generating Chinese analyses for {len(papers)} papers, providers: {provider_names}")

    for i, paper in enumerate(papers, start=1):
        print(f"  [{i}/{len(papers)}] Analyzing: {paper.title[:50]}...")

        key_tech, results = generate_analysis(paper.title, paper.summary)

        if key_tech:
            paper.key_tech = key_tech
        if results:
            paper.results = results

        # Delay between requests to stay under rate limits
        if i < len(papers):
            print(f"    Waiting {REQUEST_INTERVAL}s before next request...")
            time.sleep(REQUEST_INTERVAL)

    print("Analysis generation completed!")


if __name__ == "__main__":
    # Test
    title = "An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks"
    abstract = "Time Division Multiple Access (TDMA)-based Medium Access Control (MAC) protocols have proven their practicality..."

    key_tech, results = generate_analysis(title, abstract)
    print("关键技术与数据：", key_tech)
    print("结果与结论：", results)
