"""Fetch news from university websites."""

import re
import requests
from datetime import date, timedelta
from typing import Optional
from config import UNIVERSITY_NEWS_SOURCES, UNDERWATER_ACOUSTIC_KEYWORDS, MAX_AGE_DAYS
from models import Paper, Source


def is_underwater_acoustic_related(text: str) -> bool:
    """Check if text is related to underwater acoustics."""
    text_lower = text.lower()
    for keyword in UNDERWATER_ACOUSTIC_KEYWORDS:
        if keyword.lower() in text_lower:
            return True
    return False


def fetch_university_news(target_date: date) -> list[Paper]:
    """Fetch news from university websites."""
    news_items = []

    for source_key, source_info in UNIVERSITY_NEWS_SOURCES.items():
        print(f"Fetching news from {source_info['name']}...")

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(
                source_info["news_url"],
                headers=headers,
                timeout=15
            )
            response.raise_for_status()

            # Simple pattern matching for news titles and links
            # This is a basic implementation - may need adjustment per website
            pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]{10,100})</a>'
            matches = re.findall(pattern, response.text)

            for url, title in matches[:20]:  # Limit to 20 per source
                title = title.strip()
                if not is_underwater_acoustic_related(title):
                    continue

                # Make URL absolute
                if url.startswith("/"):
                    base_url = source_info["url"].rstrip("/")
                    url = f"{base_url}{url}"
                elif not url.startswith("http"):
                    continue

                # Create news item
                news = Paper(
                    candidate_id=f"news--{source_key}--{hash(url) % 100000:05d}",
                    title=title,
                    authors=[source_info["name"]],
                    summary=f"来自{source_info['name']}的新闻：{title}",
                    keywords=["高校新闻", source_info["name"]],
                    research_directions=["水声通信"],  # Default direction
                    score=65.0,  # News get moderate score
                    sources=[Source(name=source_info["name"], url=url)],
                    category="News",
                    journal=source_info["name"],
                    publisher=source_info["name"],
                    publication_year=target_date.year,
                    publication_date=target_date,
                    preview_image="/journal-covers/default.png",
                )
                news_items.append(news)

        except requests.RequestException as e:
            print(f"  Error fetching from {source_info['name']}: {e}")

    print(f"  Found {len(news_items)} news items")
    return news_items


if __name__ == "__main__":
    # Test
    items = fetch_university_news(date.today())
    for item in items:
        print(f"{item.title} - {item.journal}")
