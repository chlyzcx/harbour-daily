"""Fetch papers from OpenAlex API."""

import requests
from datetime import date, timedelta
from typing import Optional
from config import (
    RESEARCH_DIRECTIONS,
    OPENALEX_SEARCH_TERMS,
    TOP_JOURNALS,
    JOURNAL_COVERS,
    DEFAULT_COVER,
    OPENALEX_API,
    MAX_AGE_DAYS,
    SCORE_WEIGHTS,
    DATASET_DOI_PREFIXES,
    PAPER_DOMAIN_KEYWORDS,
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


def is_domain_relevant(text: str) -> bool:
    """Broad admission gate for paper candidates (all four sources).

    Deliberately wider than direction matching: a candidate only has to be
    about underwater acoustics / marine bioacoustics at all. Direction
    keywords are phrase-exact and brittle, so they are used for tagging
    only — never for admission.
    """
    text_lower = text.lower()
    return any(kw in text_lower for kw in PAPER_DOMAIN_KEYWORDS)


def match_research_directions(text: str) -> list[str]:
    """Match research directions based on text content.

    Capped at 3: with the finer-grained taxonomy, overlapping keywords can
    match many directions on one paper; the first matches in dict order are
    the most specific (specific directions are listed before broad ones).
    """
    text_lower = text.lower()
    matched = []
    for direction, keywords in RESEARCH_DIRECTIONS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                matched.append(direction)
                break
        if len(matched) >= 3:
            break
    return matched  # Return empty list if no match


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
            recency_score = 95
        elif days_old <= 7:
            recency_score = 90
        elif days_old <= MAX_AGE_DAYS:
            # Aligned with the fetch window: candidates older than
            # MAX_AGE_DAYS never reach scoring, so no wider tier is needed.
            recency_score = 70
        else:
            recency_score = 50
    recency_component = recency_score * weights["recency"]

    # Direction match score (0-100)
    direction_score = min(direction_match * 40, 100)
    direction_component = direction_score * weights["direction"]

    # Citation score (0-100) - for new papers, use recency as proxy
    if citation_count > 0:
        citation_score = min(citation_count * 5, 100)
    else:
        # New papers get bonus based on recency
        citation_score = recency_score * 0.8  # 80% of recency score
    citation_component = citation_score * weights["citation"]

    # Open access bonus (0 or 100)
    oa_score = 100 if is_oa else 50  # Give some points even if not OA
    oa_component = oa_score * weights["open_access"]

    total = journal_component + recency_component + direction_component + citation_component + oa_component
    return round(total, 1)


def fetch_openalex_papers(target_date: date, max_results: int = 100) -> list[Paper]:
    """Fetch papers from OpenAlex for a given date."""
    papers = []

    # OpenAlex OR-query built from umbrella terms that cover every direction
    # group. (Previously this used the first 15 direction keywords, which were
    # all channel-related, so other directions were never discovered here.)
    query = " OR ".join(f'"{term}"' for term in OPENALEX_SEARCH_TERMS)

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
            # Skip datasets and other non-article record types (Zenodo /
            # Mendeley Data records surface as OpenAlex "dataset" works)
            work_type = work.get("type")
            if work_type and work_type not in ("article", "preprint", "review"):
                continue

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
            if doi and doi.startswith(DATASET_DOI_PREFIXES):
                continue

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

            # Admission gate: must be about our domain at all. The umbrella
            # search query is deliberately broad, so without this gate
            # off-topic works (LLM benchmarks, audio datasets…) get in
            # whenever they mention "underwater acoustic" in passing.
            full_text = f"{title} {abstract}"
            if not is_domain_relevant(full_text):
                continue

            # Tag with research directions (best-effort; may be empty)
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
                is_oa=is_oa,  # Pass open access flag for preview generation
                oa_url=work.get("open_access", {}).get("oa_url"),  # Open access PDF URL
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
