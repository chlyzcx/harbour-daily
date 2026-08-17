"""Main daily fetch script - orchestrates all data sources."""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

from config import DAILY_TARGET, MIN_SCORE
from models import DailySelection, Paper
from fetch_openalex import fetch_openalex_papers
from fetch_arxiv import fetch_arxiv_papers
from fetch_news import fetch_university_news
from fetch_policy import fetch_policy_info
from fetch_covers import prefetch_all_covers


def deduplicate_papers(papers: list[Paper]) -> list[Paper]:
    """Remove duplicate papers based on title similarity."""
    seen_titles = set()
    unique_papers = []

    for paper in papers:
        # Normalize title for comparison
        normalized = paper.title.lower().strip()
        # Remove common punctuation
        normalized = normalized.replace(":", "").replace("-", " ").replace("  ", " ")

        if normalized not in seen_titles:
            seen_titles.add(normalized)
            unique_papers.append(paper)

    return unique_papers


def generate_markdown_files(selection: DailySelection, output_dir: Path) -> None:
    """Generate Markdown files for selected papers."""
    date_str = selection.date
    daily_dir = output_dir / "docs" / "daily" / date_str
    assets_dir = daily_dir / "assets"
    daily_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(exist_ok=True)

    for rank, paper in enumerate(selection.papers, start=1):
        # Generate slug from title
        slug = DailySelection._slugify(paper.title)

        filename = f"{rank:02d}-{slug}.md"
        filepath = daily_dir / filename

        markdown = paper.to_markdown(date_str, rank)
        filepath.write_text(markdown, encoding="utf-8")
        print(f"Generated: {filepath}")

    # Generate managed-manifest.json
    manifest = selection.to_manifest()
    manifest_path = daily_dir / ".managed-manifest.json"
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

    print("Fetching university news...")
    news_items = fetch_university_news(target_date)
    print(f"  Found {len(news_items)} news items")
    all_papers.extend(news_items)

    print("Fetching policy information...")
    policy_items = fetch_policy_info(target_date)
    print(f"  Found {len(policy_items)} policy items")
    all_papers.extend(policy_items)

    # Deduplicate
    print("Deduplicating...")
    unique_papers = deduplicate_papers(all_papers)
    print(f"  {len(unique_papers)} unique papers")

    # Filter by minimum score
    filtered = [p for p in unique_papers if p.score >= MIN_SCORE]
    print(f"  {len(filtered)} papers above minimum score ({MIN_SCORE})")

    # Sort by score descending and assign ranks
    filtered.sort(key=lambda p: p.score, reverse=True)

    # Select top N (up to DAILY_TARGET)
    selected = filtered[:DAILY_TARGET]
    print(f"Selected {len(selected)} papers for {target_date}")

    # Create selection
    selection = DailySelection(date=target_date.isoformat())
    for paper in selected:
        selection.add_paper(paper)

    # Sort by score and assign ranks
    selection.sort_by_score()

    return selection


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

    # Prefetch journal covers
    prefetch_all_covers(project_root)

    # Fetch papers
    selection = fetch_daily_papers(target_date, project_root)

    if not selection.papers:
        print("No papers found for today. Trying yesterday...")
        target_date = target_date - timedelta(days=1)
        selection = fetch_daily_papers(target_date, project_root)

    if not selection.papers:
        print("No papers found. Exiting.")
        sys.exit(1)

    # Generate markdown files
    generate_markdown_files(selection, project_root)
    print(f"Successfully generated {len(selection.papers)} papers for {selection.date}")


if __name__ == "__main__":
    main()
