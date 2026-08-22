"""Main daily fetch script - orchestrates all data sources."""

import json
import re
import shutil
import sys
from datetime import date, timedelta
from html import unescape
from pathlib import Path

from config import MIN_SCORE, PAPER_TARGET, NEWS_TARGET, MAX_AGE_DAYS
from models import DailySelection, NewsItem, Paper

SEEN_PAPERS_PATH = Path(__file__).parent / "data" / "seen_papers.json"
from fetch_openalex import fetch_openalex_papers
from fetch_arxiv import fetch_arxiv_papers
from fetch_semantic_scholar import fetch_semantic_scholar_papers
from fetch_crossref import fetch_crossref_papers
from fetch_news import fetch_daily_news
from generate_previews_unified import generate_all_previews_unified, extract_og_image
from generate_previews import generate_preview_image
from generate_analysis import generate_all_analyses, generate_all_news_analyses


def clean_text(text: str) -> str:
    """Strip XML/JATS tags, unescape HTML entities, normalize whitespace."""
    if not text:
        return text
    # Remove XML tags like <jats:p>, <jats:italic>, etc.
    text = re.sub(r"<[^>]+>", " ", text)
    # Decode HTML entities some sources leave in titles (&lt;b&gt; etc.)
    text = unescape(text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _paper_uid(paper: Paper) -> str:
    """Stable identifier for cross-day dedup: DOI if available, else candidate id."""
    if paper.doi:
        return "doi:" + paper.doi.lower()
    return "id:" + paper.candidate_id


def load_seen_papers(target_date: date) -> dict[str, str]:
    """Load the seen-paper store {uid: date_iso}, pruned to the fetch window.

    Entries older than MAX_AGE_DAYS cannot be re-fetched anyway (every source
    filters by the same window), so they are dropped to keep the file small.
    """
    if not SEEN_PAPERS_PATH.exists():
        return {}
    try:
        data = json.loads(SEEN_PAPERS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    cutoff = (target_date - timedelta(days=MAX_AGE_DAYS)).isoformat()
    return {uid: d for uid, d in data.get("papers", {}).items() if d >= cutoff}


def save_seen_papers(seen: dict[str, str]) -> None:
    SEEN_PAPERS_PATH.parent.mkdir(parents=True, exist_ok=True)
    SEEN_PAPERS_PATH.write_text(
        json.dumps({"papers": seen}, indent=1, ensure_ascii=False),
        encoding="utf-8",
    )


def deduplicate_papers(papers: list[Paper]) -> list[Paper]:
    """Remove duplicate papers based on DOI and title similarity."""
    seen_dois = set()
    seen_titles = set()
    unique_papers = []

    for paper in papers:
        # Check DOI first (most reliable)
        doi = None
        for source in paper.sources:
            if source.name == "DOI" and "doi.org/" in source.url:
                doi = source.url.split("doi.org/")[-1].lower()
                break

        if doi and doi in seen_dois:
            continue

        # Normalize title for comparison
        normalized = paper.title.lower().strip()
        # Remove common punctuation
        normalized = normalized.replace(":", "").replace("-", " ").replace("  ", " ")

        if normalized in seen_titles:
            continue

        # Add to unique list
        if doi:
            seen_dois.add(doi)
        seen_titles.add(normalized)
        unique_papers.append(paper)

    return unique_papers


def generate_markdown_files(selection: DailySelection, news_items: list[NewsItem],
                            output_dir: Path) -> None:
    """Generate Markdown files for selected papers and news, organized by category."""
    date_str = selection.date
    daily_dir = output_dir / "docs" / "daily" / date_str

    # A same-day re-run finds no *new* news (the seen-store blocks
    # re-selecting what an earlier run published), so without preservation
    # the rewrite below would erase today's news section. Keep the existing
    # news files when this run found nothing new.
    preserved_news: list[tuple[str, str]] = []  # (filename, content)
    news_dir = daily_dir / "news"
    if not news_items and news_dir.exists():
        preserved_news = [
            (p.name, p.read_text(encoding="utf-8"))
            for p in sorted(news_dir.glob("*.md"))
        ]
        if preserved_news:
            print(f"Preserving {len(preserved_news)} news items from an earlier run today")

    # Clean stale files from previous runs to avoid duplicate ranks
    if daily_dir.exists():
        shutil.rmtree(daily_dir)
    daily_dir.mkdir(parents=True, exist_ok=True)

    def write_article(article, rank: int) -> None:
        slug = DailySelection._slugify(article.title) or article.candidate_id
        category_dir = daily_dir / article.category.lower()
        category_dir.mkdir(exist_ok=True)
        filepath = category_dir / f"{rank:02d}-{slug}.md"
        filepath.write_text(article.to_markdown(date_str, rank), encoding="utf-8")
        print(f"Generated: {filepath}")

    for rank, paper in enumerate(selection.papers, start=1):
        write_article(paper, rank)

    paper_count = len(selection.papers)
    for i, item in enumerate(news_items, start=1):
        write_article(item, paper_count + i)

    # Restore preserved news from an earlier same-day run
    for name, content in preserved_news:
        news_dir.mkdir(exist_ok=True)
        (news_dir / name).write_text(content, encoding="utf-8")
        print(f"Preserved: {news_dir / name}")

    # Generate managed-manifest.json (papers + news)
    manifest = selection.to_manifest()
    for i, item in enumerate(news_items, start=1):
        manifest["articles"].append({
            "candidate_id": item.candidate_id,
            "category": item.category,
            "rank": paper_count + i,
            "path": f"docs/daily/{date_str}/news/"
                    f"{paper_count + i:02d}-{DailySelection._slugify(item.title) or item.candidate_id}.md"
        })
        if item.preview_image:
            manifest["assets"].append({
                "candidate_id": item.candidate_id,
                "path": f"docs/public{item.preview_image}"
            })
    manifest_path = daily_dir / ".managed-manifest.json"

    # Manifest entries for preserved news (parsed from their front matter)
    for name, content in preserved_news:
        cid_m = re.search(r'candidateId: "(.+?)"', content)
        rank_m = re.search(r'rank: (\d+)', content)
        if not (cid_m and rank_m):
            continue
        manifest["articles"].append({
            "candidate_id": cid_m.group(1),
            "category": "News",
            "rank": int(rank_m.group(1)),
            "path": f"docs/daily/{date_str}/news/{name}",
        })
        img_m = re.search(r'previewImage: "(.+?)"', content)
        if img_m:
            manifest["assets"].append({
                "candidate_id": cid_m.group(1),
                "path": f"docs/public{img_m.group(1)}",
            })

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated: {manifest_path}")


def fetch_daily_papers(target_date: date, project_root: Path) -> DailySelection:
    """Fetch and select daily papers."""
    print(f"Fetching papers for {target_date}...")

    # Fetch from all sources
    all_papers = []

    print("Fetching from OpenAlex...")
    openalex_papers = fetch_openalex_papers(target_date)
    print(f"  Found {len(openalex_papers)} papers")
    all_papers.extend(openalex_papers)

    print("Fetching from arXiv...")
    arxiv_papers = fetch_arxiv_papers(target_date)
    print(f"  Found {len(arxiv_papers)} papers")
    all_papers.extend(arxiv_papers)

    print("Fetching from Semantic Scholar...")
    s2_papers = fetch_semantic_scholar_papers(target_date)
    print(f"  Found {len(s2_papers)} papers")
    all_papers.extend(s2_papers)

    print("Fetching from CrossRef...")
    crossref_papers = fetch_crossref_papers(target_date)
    print(f"  Found {len(crossref_papers)} papers")
    all_papers.extend(crossref_papers)

    # Deduplicate
    print("Deduplicating...")
    unique_papers = deduplicate_papers(all_papers)
    print(f"  {len(unique_papers)} unique papers")

    # Cross-day dedup: skip papers already published on a previous day.
    # Same-day re-runs are exempt (their entries carry today's date) so a
    # re-run regenerates the same selection instead of erasing it.
    seen = load_seen_papers(target_date)
    today_iso = target_date.isoformat()
    fresh_papers = [p for p in unique_papers
                    if seen.get(_paper_uid(p)) in (None, today_iso)]
    skipped = len(unique_papers) - len(fresh_papers)
    if skipped:
        print(f"  Skipped {skipped} papers already published on previous days")

    # Clean XML/JATS tags from summaries (some sources embed markup)
    for paper in fresh_papers:
        paper.summary = clean_text(paper.summary)
        paper.title = clean_text(paper.title)

    # Filter by minimum score
    filtered = [p for p in fresh_papers if p.score >= MIN_SCORE]
    print(f"  {len(filtered)} papers above minimum score ({MIN_SCORE})")

    # Sort by score descending and assign ranks
    filtered.sort(key=lambda p: p.score, reverse=True)

    # Select top N (leave room for news: site limit is 15 articles/day total)
    selected = filtered[:PAPER_TARGET]
    print(f"Selected {len(selected)} papers for {target_date}")

    # Record the selection so later days skip these papers
    for paper in selected:
        seen[_paper_uid(paper)] = today_iso
    save_seen_papers(seen)

    # Create selection
    selection = DailySelection(date=target_date.isoformat())
    for paper in selected:
        selection.add_paper(paper)

    # Sort by score and assign ranks
    selection.sort_by_score()

    # Generate Chinese analyses using DeepSeek
    generate_all_analyses(selection.papers)

    # Generate preview images
    generate_all_previews_unified(selection.papers, target_date.isoformat(), project_root)

    return selection


def fetch_daily_news_section(target_date: date, project_root: Path,
                             paper_count: int) -> list[NewsItem]:
    """Fetch, rewrite and illustrate today's news items."""
    print("Fetching news...")
    # Site limit: News + Policy <= 5, and 15 articles total per day
    room = min(NEWS_TARGET, 15 - paper_count)
    if room <= 0:
        print("  No room left for news today")
        return []

    news_items = fetch_daily_news(target_date)[:room]
    if not news_items:
        print("  No relevant news found today")
        return []

    # Rewrite into structured Chinese articles (one batched LLM request)
    generate_all_news_analyses(news_items)

    # Preview images: og:image from the article page, themed SVG as fallback
    date_str = target_date.isoformat()
    for i, item in enumerate(news_items, start=1):
        item.rank = paper_count + i
        assets_dir = (project_root / "docs" / "public" / "daily"
                      / date_str / "assets" / item.candidate_id)
        preview_path = assets_dir / "preview.png"
        print(f"  News preview: {item.display_title[:40]}...")
        if extract_og_image(item.url, preview_path):
            item.preview_image = f"/daily/{date_str}/assets/{item.candidate_id}/preview.png"
        else:
            item.preview_image = generate_preview_image(item, date_str, project_root)

    return news_items


def main():
    """Main entry point."""
    # Determine target date
    if len(sys.argv) > 1:
        target_date = date.fromisoformat(sys.argv[1])
    else:
        target_date = date.today()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Fetch papers
    selection = fetch_daily_papers(target_date, project_root)

    if not selection.papers:
        print("No papers found for today. Trying yesterday...")
        target_date = target_date - timedelta(days=1)
        selection = fetch_daily_papers(target_date, project_root)

    if not selection.papers:
        print("No papers found. Skipping today's update.")
        # Exit with code 0 (success) to avoid failing the GitHub Actions workflow
        # This allows the workflow to continue and deploy existing content
        sys.exit(0)

    # Fetch news (ranks continue after the papers)
    news_items = fetch_daily_news_section(target_date, project_root, len(selection.papers))

    # Generate markdown files
    generate_markdown_files(selection, news_items, project_root)
    print(f"Successfully generated {len(selection.papers)} papers and "
          f"{len(news_items)} news items for {selection.date}")


if __name__ == "__main__":
    main()
