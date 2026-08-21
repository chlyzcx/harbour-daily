"""Fetch daily news from RSS feeds and institution webpages.

Three tiers of sources (configured in config.py):
- official: societies / institutions (e.g. Acoustical Society of America)
- media: industry media RSS feeds
- university: Chinese university news pages (webpage scraping)

Items are keyword-filtered for underwater-acoustics relevance, scored by
tier + recency, and deduplicated across runs via a persistent seen-store
(so the same news never appears twice, even on different days).
"""

import hashlib
import json
import re
import requests
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

from config import (
    NEWS_RSS_SOURCES, NEWS_WEBPAGE_SOURCES, NEWS_RELEVANCE_KEYWORDS,
    NEWS_NEGATIVE_KEYWORDS, NEWS_TIER_SCORES, NEWS_MIN_SCORE, NEWS_TARGET,
    NEWS_MAX_AGE_DAYS, RESEARCH_DIRECTIONS,
)
from models import NewsItem


SEEN_STORE_PATH = Path(__file__).parent / "data" / "seen_news.json"

_UA = {"User-Agent": "harbour-daily/1.0 (underwater acoustics daily news bot)"}


# ==================== 工具函数 ====================

def strip_html(text: str) -> str:
    """Remove HTML tags and normalize whitespace."""
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def is_relevant(text: str) -> bool:
    """Check if text is related to underwater acoustics / marine tech.
    Negative keywords (oil & gas, offshore wind…) win over positive ones —
    e.g. "Dolphin Drilling" must not match "dolphin"."""
    text_lower = text.lower()
    if any(kw in text_lower for kw in NEWS_NEGATIVE_KEYWORDS):
        return False
    return any(kw.lower() in text_lower for kw in NEWS_RELEVANCE_KEYWORDS)


def match_directions(text: str) -> list[str]:
    """Map news text to valid research_direction values (may be empty)."""
    text_lower = text.lower()
    matched = []
    for direction, keywords in RESEARCH_DIRECTIONS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            matched.append(direction)
    return matched[:2]  # keep it focused


def score_news(published: Optional[date], tier: str, target_date: date) -> float:
    """Tier base score + recency bonus. Items without a date get no bonus
    but can still pass if the tier base alone clears the threshold."""
    score = float(NEWS_TIER_SCORES.get(tier, 60))
    if published:
        age = (target_date - published).days
        if age <= 1:
            score += 25
        elif age <= 3:
            score += 18
        elif age <= 7:
            score += 10
        elif age <= NEWS_MAX_AGE_DAYS:
            score += 5
        else:
            return 0.0  # too old
    return min(score, 100.0)


def make_candidate_id(url: str) -> str:
    """Filesystem-safe id derived from the URL (the URL itself is the dedup key)."""
    return "news--" + hashlib.md5(url.encode("utf-8")).hexdigest()[:12]


# ==================== 已发布新闻去重 ====================

def load_seen_urls() -> set[str]:
    """Load URLs that were published in previous runs."""
    try:
        data = json.loads(SEEN_STORE_PATH.read_text(encoding="utf-8"))
        return set(data.get("urls", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()


def save_seen_urls(seen: set[str]) -> None:
    """Persist the seen-store (bounded to the most recent 2000 URLs)."""
    SEEN_STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
    urls = sorted(seen)[-2000:]
    SEEN_STORE_PATH.write_text(
        json.dumps({"urls": urls}, indent=1, ensure_ascii=False), encoding="utf-8"
    )


# ==================== RSS 抓取 ====================

def _parse_rss_date(raw: Optional[str]) -> Optional[date]:
    """Parse RSS pubDate (RFC 822) or Atom updated (ISO 8601)."""
    if not raw:
        return None
    raw = raw.strip()
    try:
        return parsedate_to_datetime(raw).date()
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def _parse_feed(content: bytes) -> list[dict]:
    """Minimal RSS 2.0 / Atom parser using only the stdlib."""
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return []

    items = []
    # RSS 2.0: <channel><item>; Atom: <entry> (namespaced)
    entries = root.findall(".//item")
    if not entries:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        entries = root.findall(".//a:entry", ns)
        for entry in entries:
            link_el = entry.find("a:link[@href]", ns)
            items.append({
                "title": strip_html(entry.findtext("a:title", "", ns)),
                "url": link_el.get("href") if link_el is not None else "",
                "published": _parse_rss_date(
                    entry.findtext("a:updated", "", ns) or entry.findtext("a:published", "", ns)
                ),
                "snippet": strip_html(
                    entry.findtext("a:summary", "", ns) or entry.findtext("a:content", "", ns)
                )[:500],
            })
        return items

    for item in entries:
        items.append({
            "title": strip_html(item.findtext("title", "")),
            "url": (item.findtext("link", "") or "").strip(),
            "published": _parse_rss_date(item.findtext("pubDate")),
            "snippet": strip_html(item.findtext("description", ""))[:500],
        })
    return items


def fetch_rss_news(target_date: date, seen: set[str]) -> list[NewsItem]:
    """Fetch keyword-filtered news from all configured RSS feeds."""
    results = []
    for name, cfg in NEWS_RSS_SOURCES.items():
        try:
            response = requests.get(cfg["url"], timeout=30, headers=_UA)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"  Error fetching RSS from {name}: {e}")
            continue

        count = 0
        for entry in _parse_feed(response.content):
            if not entry["title"] or not entry["url"]:
                continue
            if entry["url"] in seen:
                continue
            text = f"{entry['title']} {entry['snippet']}"
            if not is_relevant(text):
                continue
            score = score_news(entry["published"], cfg["tier"], target_date)
            if score < NEWS_MIN_SCORE:
                continue
            results.append(NewsItem(
                candidate_id=make_candidate_id(entry["url"]),
                title=entry["title"],
                url=entry["url"],
                source_name=name,
                tier=cfg["tier"],
                published=entry["published"],
                snippet=entry["snippet"],
                score=score,
                research_directions=match_directions(text),
            ))
            count += 1
        print(f"  {name}: {count} relevant items")
    return results


# ==================== 高校网页抓取 ====================

_DATE_RE = re.compile(r"(20\d{2})[-/年](\d{1,2})[-/月](\d{1,2})")


def fetch_webpage_news(target_date: date, seen: set[str]) -> list[NewsItem]:
    """Scrape university news list pages; links are keyword-filtered."""
    from bs4 import BeautifulSoup

    results = []
    for name, cfg in NEWS_WEBPAGE_SOURCES.items():
        try:
            response = requests.get(cfg["url"], timeout=30, headers=_UA)
            response.raise_for_status()
            response.encoding = response.apparent_encoding or "utf-8"
        except requests.RequestException as e:
            print(f"  Error fetching webpage from {name}: {e}")
            continue

        soup = BeautifulSoup(response.text, "lxml")
        count = 0
        for a in soup.find_all("a", href=True):
            title = strip_html(a.get_text())
            if len(title) < 8 or not is_relevant(title):
                continue

            url = urljoin(cfg["url"], a["href"])
            if url in seen:
                continue

            # Try to find a date near the link (same element or parent)
            context = a.get_text() + " " + (a.parent.get_text() if a.parent else "")
            published = None
            m = _DATE_RE.search(context)
            if m:
                try:
                    published = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                except ValueError:
                    published = None

            score = score_news(published, cfg["tier"], target_date)
            if score < NEWS_MIN_SCORE:
                continue
            results.append(NewsItem(
                candidate_id=make_candidate_id(url),
                title=title,
                url=url,
                source_name=name,
                tier=cfg["tier"],
                published=published,
                snippet="",
                score=score,
                research_directions=match_directions(title),
            ))
            count += 1
        print(f"  {name}: {count} relevant items")
    return results


# ==================== 主入口 ====================

def fetch_daily_news(target_date: date) -> list[NewsItem]:
    """Fetch, filter, score and rank today's news (top NEWS_TARGET)."""
    seen = load_seen_urls()

    print("Fetching news from RSS feeds...")
    items = fetch_rss_news(target_date, seen)
    print("Fetching news from institution webpages...")
    items.extend(fetch_webpage_news(target_date, seen))

    # Deduplicate within today (same URL reachable from two sources)
    unique = {item.url: item for item in items}
    items = sorted(unique.values(), key=lambda i: i.score, reverse=True)

    selected = items[:NEWS_TARGET]
    print(f"  Selected {len(selected)} news items (from {len(items)} candidates)")

    # Mark selected URLs as seen so they never reappear on later days
    if selected:
        seen.update(item.url for item in selected)
        save_seen_urls(seen)

    return selected


if __name__ == "__main__":
    for news in fetch_daily_news(date.today()):
        print(f"[{news.score:.0f}] {news.title} ({news.source_name})")
