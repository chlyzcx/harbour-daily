"""Fetch papers from OpenAlex API."""

import requests
from datetime import date, timedelta
from typing import Optional
from config import (
    RESEARCH_DIRECTIONS,
    TOP_JOURNALS,
    JOURNAL_COVERS,
    DEFAULT_COVER,
    OPENALEX_API,
    MAX_AGE_DAYS,
    SCORE_WEIGHTS,
)
from models import Paper, Source


def normalize_journal_name(name: str) -> str:
    """Normalize journal name for matching."""
    return name.lower().strip()


def get_journal_score(journal_name: Optional[str]) -> int:
    """Get quality score for a journal."""
    if not journal_name:
        return 50
    normalized = normalize_journal_name(journal_name)
    return TOP_JOURNALS.get(normalized, 50)


def get_journal_cover(journal_name: Optional[str]) -> str:
    """Get cover image path for a journal."""
    if not journal_name:
        return DEFAULT_COVER
    normalized = normalize_journal_name(journal_name)
    return JOURNAL_COVERS.get(normalized, DEFAULT_COVER)


def match_research_directions(text: str) -> list[str]:
    """Match research directions based on text content."""
    text_lower = text.lower()
    matched = []
    for direction, keywords in RESEARCH_DIRECTIONS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                matched.append(direction)
                break
    return matched if matched else ["水声通信"]  # Default fallback


def extract_keywords(title: str, abstract: str, directions: list[str]) -> list[str]:
    """Extract keywords from title and abstract."""
    keywords = set()
    text = f"{title} {abstract}".lower()

    # Extract from direction keywords
    for direction in directions:
        for kw in RESEARCH_DIRECTIONS.get(direction, []):
            if kw.lower() in text:
                keywords.add(kw)

    # Add common signal processing terms if present
    common_terms = [
        "deep learning", "machine learning", "neural network",
        "ofdm", "channel estimation", "equalization",
        "beamforming", "detection", "classification",
        "localization", "tracking", "sparse",
        "compressed sensing", "time-varying", "doppler",
    ]
    for term in common_terms:
        if term in text:
            keywords.add(term)

    return sorted(list(keywords))[:8]  # Limit to 8 keywords


def calculate_score(
    journal_score: int,
    publication_date: Optional[date],
    citation_count: int,
    is_oa: bool,
    direction_match: int,
) -> float:
    """Calculate overall paper score (0-100) using weighted formula."""
    weights = SCORE_WEIGHTS

    # Journal score (0-100)
    journal_component = journal_score * weights["journal"]

    # Recency score (0-100)
    recency_score = 0
    if publication_date:
        days_old = (date.today() - publication_date).days
        if days_old <= 1:
            recency_score = 100
        elif days_old <= 3:
            recency_score = 90
        elif days_old <= 7:
            recency_score = 80
        elif days_old <= 30:
            recency_score = 60
        else:
            recency_score = 40
    recency_component = recency_score * weights["recency"]

    # Direction match score (0-100)
    direction_score = min(direction_match * 30, 100)
    direction_component = direction_score * weights["direction"]

    # Citation score (0-100)
    citation_score = min(citation_count * 5, 100)
    citation_component = citation_score * weights["citation"]

    # Open access bonus (0 or 100)
    oa_score = 100 if is_oa else 0
    oa_component = oa_score * weights["open_access"]

    total = journal_component + recency_component + direction_component + citation_component + oa_component
    return round(total, 1)


def fetch_openalex_papers(target_date: date, max_results: int = 100) -> list[Paper]:
    """Fetch papers from OpenAlex for a given date."""
    papers = []

    # Build search query from all direction keywords
    all_keywords = []
    for keywords in RESEARCH_DIRECTIONS.values():
        all_keywords.extend(keywords)

    # OpenAlex search query
    query = " OR ".join([f'"{kw}"' for kw in all_keywords[:15]])

    params = {
        "search": query,
        "filter": f"from_publication_date:{target_date - timedelta(days=MAX_AGE_DAYS)},to_publication_date:{target_date}",
        "sort": "publication_date:desc",
        "per_page": max_results,
        "mailto": "2770820299@qq.com",
    }

    try:
        response = requests.get(OPENALEX_API, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        for work in data.get("results", []):
            # Extract basic info
            title = work.get("title", "")
            if not title:
                continue

            abstract = work.get("abstract", "")
            if not abstract:
                # Try to get abstract from inverted index
                abstract_inverted = work.get("abstract_inverted_index", {})
                if abstract_inverted:
                    words = []
                    for word, positions in abstract_inverted.items():
                        for pos in positions:
                            words.append((pos, word))
                    words.sort()
                    abstract = " ".join([w for _, w in words])

            # Authors
            authors = []
            for authorship in work.get("authorships", []):
                author = authorship.get("author", {})
                name = author.get("display_name", "")
                if name:
                    authors.append(name)

            # Journal info
            primary_location = work.get("primary_location") or {}
            source = primary_location.get("source") or {}
            journal_name = source.get("display_name", "")
            publisher = source.get("host_organization_name", "")

            # DOI
            doi = work.get("doi", "")
            if doi:
                doi = doi.replace("https://doi.org/", "")

            # Publication date
            pub_date_str = work.get("publication_date")
            pub_date = None
            pub_year = None
            if pub_date_str:
                try:
                    pub_date = date.fromisoformat(pub_date_str)
                    pub_year = pub_date.year
                except ValueError:
                    pass

            # Citation count
            citation_count = work.get("cited_by_count", 0)

            # Open access
            is_oa = work.get("open_access", {}).get("is_oa", False)

            # Match research directions
            full_text = f"{title} {abstract}"
            directions = match_research_directions(full_text)

            # Extract keywords
            keywords = extract_keywords(title, abstract, directions)

            # Calculate score
            journal_score = get_journal_score(journal_name)
            score = calculate_score(
                journal_score, pub_date, citation_count, is_oa, len(directions)
            )

            # Build sources
            sources = []
            openalex_id = work.get("id", "")
            if openalex_id:
                sources.append(Source(name="OpenAlex", url=openalex_id))
            if doi:
                sources.append(Source(name="DOI", url=f"https://doi.org/{doi}"))

            # Create paper
            paper = Paper(
                candidate_id=f"openalex--{work.get('id', '').split('/')[-1]}",
                title=title,
                authors=authors[:10],
                summary=abstract[:500] + "..." if len(abstract) > 500 else abstract,
                keywords=keywords,
                research_directions=directions,
                score=score,
                sources=sources,
                journal=journal_name,
                publisher=publisher,
                doi=doi,
                publication_year=pub_year,
                publication_date=pub_date,
                preview_image=None,  # Use pseudo-cover instead of journal cover
            )
            papers.append(paper)

    except requests.RequestException as e:
        print(f"Error fetching from OpenAlex: {e}")

    return papers


if __name__ == "__main__":
    # Test
    papers = fetch_openalex_papers(date.today(), max_results=5)
    for p in papers:
        print(f"{p.title} ({p.journal}) - Score: {p.score}")
