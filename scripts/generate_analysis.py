"""Generate Chinese analysis using DeepSeek API."""

import os
import time
import requests
from typing import Optional


DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")


def generate_analysis(title: str, abstract: str, max_retries: int = 3) -> tuple[str, str]:
    """
    Generate key_technology and results_conclusion using DeepSeek API.
    Returns (key_tech, results) as Chinese text.
    """
    if not DEEPSEEK_API_KEY:
        print("Warning: DEEPSEEK_API_KEY not set, skipping analysis generation")
        return "", ""

    prompt = f"""请分析以下水声工程领域的学术论文，生成两部分中文内容：

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

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 500
    }

    # Retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            response = requests.post(DEEPSEEK_API, headers=headers, json=data, timeout=60)

            # Handle rate limiting (429)
            if response.status_code == 429:
                wait_time = (2 ** attempt) * 5  # 5, 10, 20 seconds
                print(f"    Rate limited (429), waiting {wait_time}s before retry {attempt + 1}/{max_retries}...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            result = response.json()

            content = result["choices"][0]["message"]["content"]

            # Parse the response
            key_tech = ""
            results = ""

            if "【关键技术与数据】" in content and "【结果与结论】" in content:
                parts = content.split("【结果与结论】")
                key_tech_part = parts[0].replace("【关键技术与数据】", "").strip()
                results_part = parts[1].strip()

                key_tech = key_tech_part
                results = results_part
            else:
                # Fallback: use the whole content as key_tech
                key_tech = content[:200]
                results = "（详见原文）"

            return key_tech, results

        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) * 5
                print(f"    Error: {e}, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"    Error calling DeepSeek API after {max_retries} attempts: {e}")
                return "", ""
        except (KeyError, IndexError) as e:
            print(f"    Error parsing DeepSeek response: {e}")
            return "", ""

    return "", ""


def generate_all_analyses(papers: list) -> None:
    """Generate analyses for all papers."""
    if not DEEPSEEK_API_KEY:
        print("Warning: DEEPSEEK_API_KEY not set, skipping all analyses")
        return

    print(f"Generating Chinese analyses for {len(papers)} papers using DeepSeek...")

    for i, paper in enumerate(papers, start=1):
        print(f"  [{i}/{len(papers)}] Analyzing: {paper.title[:50]}...")

        key_tech, results = generate_analysis(paper.title, paper.summary)

        if key_tech:
            paper.key_tech = key_tech
        if results:
            paper.results = results

        # Add delay between requests to avoid rate limiting
        # DeepSeek allows ~60 requests/minute, so we wait 2 seconds between calls
        if i < len(papers):
            time.sleep(2)

    print("Analysis generation completed!")


if __name__ == "__main__":
    # Test
    title = "An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks"
    abstract = "Time Division Multiple Access (TDMA)-based Medium Access Control (MAC) protocols have proven their practicality..."

    key_tech, results = generate_analysis(title, abstract)
    print("关键技术与数据：", key_tech)
    print("结果与结论：", results)
