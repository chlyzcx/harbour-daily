"""Fetch papers from Semantic Scholar API."""

import requests
import time
from datetime import date, timedelta
from typing import Optional
from config import RESEARCH_DIRECTIONS, MAX_AGE_DAYS
from models import Paper, Source
from fetch_openalex import match_research_directions, extract_keywords


S2_API = "https://api.semanticscholar.org/graph/v1/paper/search"


def fetch_semantic_scholar_papers(target_date: date, max_results: int = 100) -> list[Paper]:
    """Fetch recent papers from Semantic Scholar related to underwater acoustics."""
    papers = []

    # Broad search terms for underwater acoustics
    search_queries = [
        "underwater acoustic",
        "ocean acoustic",
        "underwater communication",
        "sonar signal",
        "marine acoustic",
        "bioacoustic",
    ]

    # Calculate date range (last 7 days)
    start_date = target_date - timedelta(days=MAX_AGE_DAYS)

    for query in search_queries:
        params = {
            "query": query,
            "year": f"{start_date.year}-{target_date.year}",
            "fields": "title,authors,abstract,venue,year,citationCount,externalIds,publicationDate,openAccessPdf",
            "limit": max_results // len(search_queries),
        }

        try:
            # Add delay to avoid rate limiting (429 errors)
            time.sleep(3)  # Wait 3 seconds between requests

            response = requests.get(S2_API, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            for item in data.get("data", []):
                # Skip if no title
                if not item.get("title"):
                    continue

                # Parse publication date
                pub_date = None
                pub_year = item.get("year")
                if item.get("publicationDate"):
                    try:
                        pub_date = date.fromisoformat(item["publicationDate"])
                    except (ValueError, TypeError):
                        pass

                # Filter by date
                if pub_date and (target_date - pub_date).days > MAX_AGE_DAYS:
                    continue

                title = item["title"]
                abstract = item.get("abstract", "")

                # Match research directions
                full_text = f"{title} {abstract}"
                directions = match_research_directions(full_text)

                # Skip if no direction match
                if not directions:
                    continue

                # Extract keywords
                keywords = extract_keywords(title, abstract, directions)

                # Calculate score (S2 papers get moderate score)
                citation_count = item.get("citationCount", 0)
                score = 60.0 + min(citation_count * 2, 20)  # 60-80 range

                # Sources
                sources = []
                external_ids = item.get("externalIds", {})

                # Add DOI link if available
                if external_ids.get("DOI"):
                    doi = external_ids["DOI"]
                    sources.append(Source(name="DOI", url=f"https://doi.org/{doi}"))

                # Add S2 link
                if item.get("paperId"):
                    sources.append(Source(
                        name="Semantic Scholar",
                        url=f"https://www.semanticscholar.org/paper/{item['paperId']}"
                    ))

                # Add open access PDF if available
                if item.get("openAccessPdf") and item["openAccessPdf"].get("url"):
                    sources.append(Source(name="PDF", url=item["openAccessPdf"]["url"]))

                if not sources:
                    continue

                # Authors
                authors = [author.get("name", "") for author in item.get("authors", [])]
                authors = [a for a in authors if a][:10]  # Limit to 10 authors

                paper = Paper(
                    candidate_id=f"s2--{item['paperId']}",
                    title=title,
                    authors=authors,
                    summary=abstract[:500] + "..." if len(abstract) > 500 else abstract,
                    keywords=keywords,
                    research_directions=directions,
                    score=score,
                    sources=sources,
                    journal=item.get("venue", "Unknown"),
                    publisher="Semantic Scholar",
                    publication_year=pub_year,
                    publication_date=pub_date,
                    preview_image=None,
                )
                papers.append(paper)

        except requests.RequestException as e:
            print(f"Error fetching from Semantic Scholar (query: {query}): {e}")
            continue

    return papers


if __name__ == "__main__":
    # Test
    papers = fetch_semantic_scholar_papers(date.today(), max_results=10)
    for p in papers:
        print(f"{p.title} ({p.journal}) - Score: {p.score}")
