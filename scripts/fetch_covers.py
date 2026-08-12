"""Automatic journal cover fetching and caching."""

import re
import requests
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

from config import (
    JOURNAL_HOMEPAGES,
    JOURNAL_COVERS,
    DEFAULT_COVER,
    COVER_FETCH_TIMEOUT,
    COVER_CACHE_DIR,
)


def normalize_journal_name(name: str) -> str:
    """Normalize journal name for matching."""
    return name.lower().strip()


def get_local_cover_path(journal_name: Optional[str]) -> str:
    """Get local cover path for a journal."""
    if not journal_name:
        return DEFAULT_COVER
    normalized = normalize_journal_name(journal_name)
    return JOURNAL_COVERS.get(normalized, DEFAULT_COVER)


def get_cover_filename(journal_name: str) -> str:
    """Generate filename for a journal cover."""
    normalized = normalize_journal_name(journal_name)
    # Create safe filename
    safe_name = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return f"{safe_name}.png"


def fetch_og_image(url: str, timeout: int = COVER_FETCH_TIMEOUT) -> Optional[str]:
    """Fetch og:image from a webpage."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Try og:image first
        og_match = re.search(
            r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
            response.text,
            re.IGNORECASE,
        )
        if og_match:
            image_url = og_match.group(1)
            # Handle relative URLs
            if image_url.startswith("/"):
                parsed = urlparse(url)
                image_url = f"{parsed.scheme}://{parsed.netloc}{image_url}"
            return image_url

        # Try twitter:image as fallback
        twitter_match = re.search(
            r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']',
            response.text,
            re.IGNORECASE,
        )
        if twitter_match:
            image_url = twitter_match.group(1)
            if image_url.startswith("/"):
                parsed = urlparse(url)
                image_url = f"{parsed.scheme}://{parsed.netloc}{image_url}"
            return image_url

        # Try to find journal cover image in common patterns
        # Pattern 1: cover image in img tag
        img_match = re.search(
            r'<img[^>]+src=["\']([^"\']*cover[^"\']*)["\'][^>]*>',
            response.text,
            re.IGNORECASE,
        )
        if img_match:
            image_url = img_match.group(1)
            if image_url.startswith("/"):
                parsed = urlparse(url)
                image_url = f"{parsed.scheme}://{parsed.netloc}{image_url}"
            return image_url

    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")

    return None


def download_image(url: str, save_path: Path, timeout: int = COVER_FETCH_TIMEOUT) -> bool:
    """Download an image and save it locally."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Check if it's actually an image
        content_type = response.headers.get("content-type", "")
        if not content_type.startswith("image/"):
            print(f"  Not an image: {content_type}")
            return False

        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_bytes(response.content)
        print(f"  Saved cover: {save_path}")
        return True

    except requests.RequestException as e:
        print(f"  Error downloading {url}: {e}")
        return False


def ensure_journal_cover(journal_name: Optional[str], project_root: Path) -> str:
    """
    Ensure a journal cover exists locally.
    Returns the local path to the cover image.
    """
    if not journal_name:
        return DEFAULT_COVER

    normalized = normalize_journal_name(journal_name)
    local_path = JOURNAL_COVERS.get(normalized, DEFAULT_COVER)

    # If already cached, return local path
    cover_file = project_root / COVER_CACHE_DIR / get_cover_filename(journal_name)
    if cover_file.exists():
        return local_path

    # Try to fetch from journal homepage
    homepage = JOURNAL_HOMEPAGES.get(normalized)
    if homepage:
        print(f"Fetching cover for {journal_name}...")
        image_url = fetch_og_image(homepage)
        if image_url:
            success = download_image(image_url, cover_file)
            if success:
                return local_path

    # Return default if fetch failed
    return DEFAULT_COVER


def prefetch_all_covers(project_root: Path) -> None:
    """Prefetch all known journal covers."""
    print("Prefetching journal covers...")
    for journal_name in JOURNAL_HOMEPAGES.keys():
        ensure_journal_cover(journal_name, project_root)
    print("Cover prefetch complete.")


if __name__ == "__main__":
    # Test
    from pathlib import Path
    project_root = Path(__file__).parent.parent
    prefetch_all_covers(project_root)
