"""Main daily fetch script - orchestrates all data sources."""

import os
import sys
from datetime import date, timedelta
from pathlib import Path

from config import DAILY_TARGET, MIN_SCORE
from models import DailySelection, Paper
from fetch_openalex import fetch_openalex_papers
from fetch_arxiv import fetch_arxiv_papers


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
        slug = paper.title.lower()
        slug = "".join(c if c.isalnum() or c in " -" else "" for c in slug)
        slug = slug.replace(" ", "-")[:50]

        filename = f"{rank:02d}-{slug}.md"
        filepath = daily_dir / filename

        markdown = paper.to_markdown(date_str, rank)
        filepath.write_text(markdown, encoding="utf-8")
        print(f"Generated: {filepath}")


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

    # Deduplicate
    print("Deduplicating...")
    unique_papers = deduplicate_papers(all_papers)
    print(f"  {len(unique_papers)} unique papers")

    # Filter by minimum score
    filtered = [p for p in unique_papers if p.score >= MIN_SCORE]
    print(f"  {len(filtered)} papers above minimum score ({MIN_SCORE})")

    # Sort by score descending
    filtered.sort(key=lambda p: p.score, reverse=True)

    # Select top N
    selected = filtered[:DAILY_TARGET]
    print(f"Selected {len(selected)} papers for {target_date}")

    # Create selection
    selection = DailySelection(date=target_date.isoformat())
    for paper in selected:
        selection.add_paper(paper)

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
