"""Shared HTTP helper with retry/backoff for flaky API endpoints.

GitHub Actions runners share IP pools, so Semantic Scholar (and
occasionally OpenAlex / CrossRef) answer 429. A short retry absorbs
most transient failures instead of silently returning zero candidates.
"""

import time

import requests

_RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def get_with_retry(url, *, params=None, headers=None, timeout=30,
                   retries=2, backoff=5):
    """GET with limited retries on 429/5xx and connection errors."""
    last_exc = None
    for attempt in range(retries + 1):
        try:
            response = requests.get(url, params=params, headers=headers,
                                    timeout=timeout)
            if response.status_code in _RETRYABLE_STATUS and attempt < retries:
                wait = backoff * (attempt + 1)
                print(f"  HTTP {response.status_code}, retrying in {wait}s...")
                time.sleep(wait)
                continue
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            last_exc = e
            if attempt < retries:
                wait = backoff * (attempt + 1)
                print(f"  Request failed ({e}), retrying in {wait}s...")
                time.sleep(wait)
    raise last_exc
