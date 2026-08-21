"""Fetch papers from CrossRef API."""

import requests
from datetime import date, timedelta
from typing import Optional
from config import RESEARCH_DIRECTIONS, MAX_AGE_DAYS, DATASET_DOI_PREFIXES
from models import Paper, Source
from fetch_openalex import match_research_directions, extract_keywords, is_domain_relevant


CROSSREF_API = "https://api.crossref.org/works"


def fetch_crossref_papers(target_date: date, max_results: int = 100) -> list[Paper]:
    """Fetch recent papers from CrossRef related to underwater acoustics."""
    papers = []

    # Calculate date range
    start_date = target_date - timedelta(days=MAX_AGE_DAYS)

    # Search queries
    search_queries = [
        "underwater acoustic",
        "ocean acoustic",
        "underwater communication",
        "sonar",
    ]

    for query in search_queries:
        params = {
            "query": query,
            "filter": f"from-pub-date:{start_date.isoformat()},until-pub-date:{target_date.isoformat()}",
            "rows": max_results // len(search_queries),
            "sort": "published",
            "order": "desc",
            "select": "DOI,title,author,abstract,published,container-title,publisher",
        }

        try:
            response = requests.get(CROSSREF_API, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            for item in data.get("message", {}).get("items", []):
                # Skip dataset-repository records (not papers)
                if item.get("DOI", "").startswith(DATASET_DOI_PREFIXES):
                    continue

                # Skip if no title
                if not item.get("title") or not item["title"]:
                    continue

                title = item["title"][0] if isinstance(item["title"], list) else item["title"]
                abstract = item.get("abstract", "")

                # Admission gate: domain relevance (tagging is best-effort)
                full_text = f"{title} {abstract}"
                if not is_domain_relevant(full_text):
                    continue

                # Tag with research directions
                directions = match_research_directions(full_text)

                # Parse publication date
                pub_date = None
                pub_year = None
                if "published" in item:
                    date_parts = item["published"].get("date-parts", [[]])[0]
                    if date_parts:
                        pub_year = date_parts[0]
                        if len(date_parts) >= 3:
                            try:
                                pub_date = date(date_parts[0], date_parts[1], date_parts[2])
                            except (ValueError, TypeError):
                                pass

                # Extract keywords
                keywords = extract_keywords(title, abstract, directions)

                # Calculate score (CrossRef papers get lower score due to incomplete metadata)
                score = 55.0

                # Sources
                sources = []
                if item.get("DOI"):
                    doi = item["DOI"]
                    sources.append(Source(name="DOI", url=f"https://doi.org/{doi}"))

                if not sources:
                    continue

                # Authors
                authors = []
                for author in item.get("author", []):
                    given = author.get("given", "")
                    family = author.get("family", "")
                    full_name = f"{given} {family}".strip()
                    if full_name:
                        authors.append(full_name)
                authors = authors[:10]  # Limit to 10 authors

                # Journal name
                journal = ""
                if item.get("container-title"):
                    journal = item["container-title"][0] if isinstance(item["container-title"], list) else item["container-title"]

                paper = Paper(
                    candidate_id=f"crossref--{item['DOI'].replace('/', '-')}",
                    title=title,
                    authors=authors,
                    summary=abstract[:500] + "..." if len(abstract) > 500 else abstract,
                    keywords=keywords,
                    research_directions=directions,
                    score=score,
                    sources=sources,
                    journal=journal or "Unknown",
                    publisher=item.get("publisher", "Unknown"),
                    publication_year=pub_year,
                    publication_date=pub_date,
                    preview_image=None,
                )
                papers.append(paper)

        except requests.RequestException as e:
            print(f"Error fetching from CrossRef (query: {query}): {e}")
            continue

    return papers


if __name__ == "__main__":
    # Test
    papers = fetch_crossref_papers(date.today(), max_results=10)
    for p in papers:
        print(f"{p.title} ({p.journal}) - Score: {p.score}")
