"""Configuration for underwater acoustic daily paper fetcher."""

# Research directions and their search keywords
RESEARCH_DIRECTIONS = {
    "水声通信信道": [
        "underwater acoustic channel",
        "underwater acoustic communication channel",
        "ocean acoustic channel",
        "underwater channel estimation",
        "underwater channel modeling",
        "time-varying underwater channel",
        "underwater acoustic propagation",
    ],
    "水声通信": [
        "underwater acoustic communication",
        "underwater wireless communication",
        "underwater acoustic modem",
        "underwater acoustic OFDM",
        "underwater acoustic networking",
        "underwater acoustic telemetry",
        "underwater acoustic signal processing",
    ],
    "水声侦察": [
        "underwater acoustic reconnaissance",
        "underwater acoustic surveillance",
        "passive acoustic monitoring",
        "underwater target detection",
        "underwater acoustic signal classification",
        "underwater acoustic localization",
        "underwater acoustic array processing",
    ],
    "海洋生物声学信号处理": [
        "marine bioacoustics",
        "marine mammal acoustics",
        "underwater bioacoustic signal",
        "whale call detection",
        "dolphin whistle classification",
        "fish acoustic signal",
        "ocean biological acoustics",
        "marine animal acoustic",
    ],
}

# Top journals with quality scores (0-100)
TOP_JOURNALS = {
    "journal of the acoustical society of america": 100,
    "jasa": 100,
    "ieee journal of oceanic engineering": 95,
    "ieee transactions on signal processing": 95,
    "ieee transactions on communications": 90,
    "ieee transactions on aerospace and electronic systems": 90,
    "jasa express letters": 90,
    "jasa-el": 90,
    "applied acoustics": 85,
    "ocean engineering": 85,
}

# Journal cover images mapping
JOURNAL_COVERS = {
    "journal of the acoustical society of america": "/journal-covers/jasa.png",
    "jasa": "/journal-covers/jasa.png",
    "jasa express letters": "/journal-covers/jasa-el.png",
    "jasa-el": "/journal-covers/jasa-el.png",
    "ieee journal of oceanic engineering": "/journal-covers/ieee-joe.png",
    "ieee transactions on signal processing": "/journal-covers/ieee-tsp.png",
    "ieee transactions on communications": "/journal-covers/ieee-tcom.png",
    "ieee transactions on aerospace and electronic systems": "/journal-covers/ieee-taes.png",
    "applied acoustics": "/journal-covers/applied-acoustics.png",
    "ocean engineering": "/journal-covers/ocean-engineering.png",
}

# Default cover for other journals
DEFAULT_COVER = "/journal-covers/default.png"

# API endpoints
OPENALEX_API = "https://api.openalex.org/works"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"
ARXIV_API = "http://export.arxiv.org/api/query"

# Fetch parameters
DAILY_TARGET = 2  # Daily target number of papers
MAX_AGE_DAYS = 7  # Maximum age for fallback
MIN_SCORE = 60  # Minimum score threshold
