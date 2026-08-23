"""Fetch papers from arXiv API."""

import re
import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from typing import Optional
from config import RESEARCH_DIRECTIONS, ARXIV_API, MAX_AGE_DAYS
from models import Paper, Source
from fetch_openalex import match_research_directions, extract_keywords, is_domain_relevant
from http_utils import get_with_retry


def fetch_arxiv_papers(target_date: date, max_results: int = 50) -> list[Paper]:
    """Fetch recent papers from arXiv related to underwater acoustics."""
    papers = []

    # Use broader search terms for arXiv (fewer underwater acoustic papers)
    broad_keywords = [
        "underwater acoustic",
        "ocean acoustic",
        "sonar signal",
        "marine acoustic",
        "hydroacoustic",
        "underwater communication",
        "underwater channel",
        "bioacoustic",
    ]

    # Build arXiv query with broader terms
    query_terms = []
    for kw in broad_keywords:
        query_terms.append(f'all:"{kw}"')
    query = " OR ".join(query_terms)

    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    try:
        response = get_with_retry(ARXIV_API, params=params, timeout=30)
        response.raise_for_status()

        # Parse Atom XML
        root = ET.fromstring(response.content)
        ns = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }

        for entry in root.findall("atom:entry", ns):
            title_elem = entry.find("atom:title", ns)
            if title_elem is None or not title_elem.text:
                continue
            title = re.sub(r"\s+", " ", title_elem.text.strip())

            summary_elem = entry.find("atom:summary", ns)
            abstract = summary_elem.text.strip() if summary_elem is not None else ""

            # Authors
            authors = []
            for author in entry.findall("atom:author", ns):
                name_elem = author.find("atom:name", ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())

            # Published date
            published_elem = entry.find("atom:published", ns)
            pub_date = None
            pub_year = None
            if published_elem is not None and published_elem.text:
                try:
                    pub_date = date.fromisoformat(published_elem.text[:10])
                    pub_year = pub_date.year
                except ValueError:
                    pass

            # Filter by date
            if pub_date and (target_date - pub_date).days > MAX_AGE_DAYS:
                continue

            # arXiv ID
            id_elem = entry.find("atom:id", ns)
            arxiv_url = id_elem.text if id_elem is not None else ""
            arxiv_id = arxiv_url.split("/abs/")[-1] if "/abs/" in arxiv_url else ""

            # Admission gate: domain relevance (tagging is best-effort)
            full_text = f"{title} {abstract}"
            if not is_domain_relevant(full_text):
                continue

            # Tag with research directions
            directions = match_research_directions(full_text)

            # Extract keywords
            keywords = extract_keywords(title, abstract, directions)

            # arXiv papers get moderate score (preprints)
            score = 70.0

            # Sources
            sources = [Source(name="arXiv", url=arxiv_url)]
            pdf_url = arxiv_url.replace("/abs/", "/pdf/")
            sources.append(Source(name="PDF", url=pdf_url))

            paper = Paper(
                candidate_id=f"arxiv--{arxiv_id.replace('v', '-')}",
                title=title,
                authors=authors[:10],
                summary=abstract[:500] + "..." if len(abstract) > 500 else abstract,
                keywords=keywords,
                research_directions=directions,
                score=score,
                sources=sources,
                journal="arXiv preprint",
                publisher="arXiv",
                publication_year=pub_year,
                publication_date=pub_date,
                preview_image=None,  # Use pseudo-cover instead of journal cover
            )
            papers.append(paper)

    except requests.RequestException as e:
        print(f"Error fetching from arXiv: {e}")
    except ET.ParseError as e:
        print(f"Error parsing arXiv response: {e}")

    return papers


if __name__ == "__main__":
    # Test
    papers = fetch_arxiv_papers(date.today(), max_results=5)
    for p in papers:
        print(f"{p.title} ({p.journal}) - Score: {p.score}")
