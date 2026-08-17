"""Fetch policy information from government websites."""

import re
import requests
from datetime import date, timedelta
from typing import Optional
from config import POLICY_SOURCES, UNDERWATER_ACOUSTIC_KEYWORDS, MAX_AGE_DAYS
from models import Paper, Source


def is_underwater_acoustic_related(text: str) -> bool:
    """Check if text is related to underwater acoustics."""
    text_lower = text.lower()
    for keyword in UNDERWATER_ACOUSTIC_KEYWORDS:
        if keyword.lower() in text_lower:
            return True
    return False


def fetch_policy_info(target_date: date) -> list[Paper]:
    """Fetch policy information from government websites."""
    # TODO: Policy URLs need manual configuration
    # Government websites often have access restrictions and changing URLs
    # For now, return empty list - you can manually add policy or configure specific URLs
    print("  Policy fetching is disabled (URLs need manual configuration)")
    return []


if __name__ == "__main__":
    # Test
    items = fetch_policy_info(date.today())
    for item in items:
        print(f"{item.title} - {item.journal}")
