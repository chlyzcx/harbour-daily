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
    # TODO: University news URLs need manual configuration
    # Most university websites have anti-crawler mechanisms and frequently changing URLs
    # For now, return empty list - you can manually add news or configure specific URLs
    print("  University news fetching is disabled (URLs need manual configuration)")
    return []


if __name__ == "__main__":
    # Test
    items = fetch_university_news(date.today())
    for item in items:
        print(f"{item.title} - {item.journal}")
