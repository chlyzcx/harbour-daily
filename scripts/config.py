"""Configuration for underwater acoustic daily paper fetcher."""

# Research directions and their search keywords
RESEARCH_DIRECTIONS = {
    # ============ 水声通信信道 ============
    "声传播建模": [
        "acoustic propagation model",
        "normal mode propagation",
        "ray tracing underwater",
        "parabolic equation",
        "waveguide propagation",
    ],
    "信道建模": [
        "underwater acoustic channel model",
        "ocean acoustic channel model",
        "underwater channel modeling",
        "statistical channel model underwater",
    ],
    "信道测量": [
        "underwater acoustic channel measurement",
        "channel sounding underwater",
        "underwater acoustic sea trial",
        "underwater acoustic experiment",
    ],
    "信道估计": [
        "underwater acoustic channel estimation",
        "channel estimation underwater",
        "underwater channel estimation",
    ],
    "信道均衡": [
        "underwater acoustic channel equalization",
        "channel equalization underwater",
        "underwater equalizer",
    ],
    "时变特性": [
        "time-varying underwater channel",
        "underwater channel time variation",
        "non-stationary underwater channel",
    ],
    "多径效应": [
        "underwater multipath",
        "multipath propagation underwater",
        "underwater acoustic multipath",
    ],
    "多普勒效应": [
        "underwater doppler effect",
        "doppler shift underwater",
        "underwater acoustic doppler",
    ],
    "海洋声学层析": [
        "ocean acoustic tomography",
        "acoustic tomography ocean",
    ],
    "海底声学": [
        "geoacoustic inversion",
        "seabed acoustics",
        "seafloor acoustic properties",
        "sediment acoustics",
    ],
    # ============ 水声通信 ============
    "OFDM": [
        "underwater acoustic OFDM",
        "underwater OFDM communication",
        "OFDM underwater acoustic",
        "OFDM",
    ],
    "单载波通信": [
        "single carrier underwater acoustic",
        "underwater SC-FDE",
        "time domain equalization underwater acoustic",
    ],
    "扩频通信": [
        "underwater spread spectrum",
        "spread spectrum underwater acoustic",
        "underwater DSSS",
    ],
    "MIMO": [
        "underwater acoustic MIMO",
        "MIMO underwater communication",
        "underwater MIMO system",
    ],
    "调制解调": [
        "underwater acoustic modulation",
        "underwater acoustic demodulation",
        "underwater acoustic modem modulation",
    ],
    "多用户接入": [
        "underwater multiple access",
        "underwater acoustic CDMA",
        "underwater acoustic TDMA",
        "underwater acoustic FDMA",
    ],
    "全双工通信": [
        "full-duplex underwater acoustic",
        "underwater in-band full duplex",
        "underwater acoustic self-interference cancellation",
    ],
    "网络协议": [
        "underwater acoustic network protocol",
        "underwater MAC protocol",
        "underwater acoustic networking",
        "underwater acoustic network",
    ],
    "中继通信": [
        "underwater acoustic relay",
        "underwater relay communication",
        "underwater acoustic repeater",
    ],
    "水声调制解调器": [
        "underwater acoustic modem",
        "underwater modem design",
        "acoustic modem underwater",
    ],
    "水下传感器网络": [
        "underwater sensor network",
        "underwater wireless sensor network",
        "underwater acoustic sensor network",
        "UWSN",
    ],
    # ============ 水声侦察 ============
    "目标检测": [
        "underwater target detection",
        "underwater acoustic target detection",
        "underwater object detection",
    ],
    "目标跟踪": [
        "underwater target tracking",
        "underwater acoustic target tracking",
    ],
    "水声定位": [
        "underwater acoustic localization",
        "underwater acoustic positioning",
        "acoustic localization underwater",
        "underwater localization",
    ],
    "基线定位系统": [
        "USBL",
        "ultra-short baseline",
        "long baseline positioning",
        "LBL positioning",
    ],
    "水下导航": [
        "underwater navigation",
        "Doppler velocity log",
        "INS DVL underwater",
    ],
    "被动定位": [
        "passive underwater localization",
        "underwater passive positioning",
        "passive acoustic localization",
    ],
    "信号识别": [
        "underwater acoustic signal recognition",
        "underwater signal classification",
        "underwater acoustic signal identification",
        "underwater acoustic target recognition",
        "underwater target recognition",
    ],
    "特征提取": [
        "underwater acoustic feature extraction",
        "underwater signal feature",
        "acoustic feature extraction underwater",
    ],
    "阵列处理": [
        "underwater acoustic array processing",
        "hydrophone array processing",
        "underwater array signal processing",
    ],
    "波束形成": [
        "underwater beamforming",
        "adaptive beamforming underwater",
        "MVDR underwater acoustic",
    ],
    "声呐信号处理": [
        "sonar signal processing",
        "underwater sonar signal",
        "sonar array processing",
    ],
    "主动声呐": [
        "active sonar",
        "active underwater acoustic",
        "active sonar signal",
    ],
    "被动声呐": [
        "passive sonar",
        "passive underwater acoustic",
        "passive sonar signal",
    ],
    "水声成像": [
        "underwater acoustic imaging",
        "synthetic aperture sonar",
        "forward-looking sonar",
    ],
    "混响抑制": [
        "reverberation suppression",
        "reverberation cancellation underwater",
        "anti-reverberation sonar",
    ],
    # ============ 海洋生物声学信号处理 ============
    "鲸豚叫声检测": [
        "whale call detection",
        "dolphin whistle detection",
        "cetacean vocalization detection",
        "marine mammal call detection",
    ],
    "鱼类声学": [
        "fish acoustic signal",
        "fish sound detection",
        "fish vocalization",
        "fish bioacoustics",
    ],
    "生物声呐": [
        "biosonar",
        "biological sonar",
        "echolocation",
        "bat echolocation underwater",
    ],
    "海洋哺乳动物声学": [
        "marine mammal acoustics",
        "marine mammal vocalization",
        "cetacean acoustics",
    ],
    "生物声学信号分类": [
        "bioacoustic signal classification",
        "marine bioacoustic classification",
        "underwater bioacoustic signal",
    ],
    "海洋环境噪声": [
        "ocean ambient noise",
        "underwater ambient noise",
        "marine environmental noise",
    ],
    "被动声学监测": [
        "passive acoustic monitoring",
        "passive acoustic survey marine",
    ],
    "声学标记跟踪": [
        "acoustic telemetry fish",
        "acoustic tagging tracking",
        "acoustic transmitter tracking fish",
    ],
}

# Umbrella search terms for OpenAlex — cover every direction group instead of
# truncating the keyword list (previously only the first 15 keywords, all
# channel-related, ever reached the OpenAlex query).
OPENALEX_SEARCH_TERMS = [
    "underwater acoustic",
    "ocean acoustic",
    "underwater communication",
    "underwater acoustic localization",
    "sonar",
    "marine bioacoustics",
    "ocean acoustic tomography",
]

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

# Journal cover images mapping (local cache)
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

# Journal homepage URLs for automatic cover fetching
JOURNAL_HOMEPAGES = {
    "journal of the acoustical society of america": "https://pubs.aip.org/jasa",
    "jasa": "https://pubs.aip.org/jasa",
    "jasa express letters": "https://pubs.aip.org/jel",
    "jasa-el": "https://pubs.aip.org/jel",
    "ieee journal of oceanic engineering": "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=48",
    "ieee transactions on signal processing": "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=78",
    "ieee transactions on communications": "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=26",
    "ieee transactions on aerospace and electronic systems": "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=7",
    "applied acoustics": "https://www.sciencedirect.com/journal/applied-acoustics",
    "ocean engineering": "https://www.sciencedirect.com/journal/ocean-engineering",
}

# Default cover for other journals
DEFAULT_COVER = "/journal-covers/default.png"

# Cover fetch settings
COVER_FETCH_TIMEOUT = 10
COVER_CACHE_DIR = "docs/public/journal-covers"

# API endpoints
OPENALEX_API = "https://api.openalex.org/works"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"
ARXIV_API = "http://export.arxiv.org/api/query"

# Fetch parameters
DAILY_TARGET = 15  # Site limit: at most 15 articles per day (papers + news)
PAPER_TARGET = 10  # Papers are capped to leave room for up to 5 news items
MAX_AGE_DAYS = 14  # Maximum age for fallback (increased from 7 to 14 days)
MIN_SCORE = 45  # Minimum score threshold (lowered from 50 to 45)

# Dataset repositories: records with these DOI prefixes are datasets, not
# papers — no abstract, no figures, machine-generated titles ("Dive
# 20210916_152707_turbot_ros_dense images and metadata"). Filtered at fetch
# time: they waste paper slots and can never produce a real preview image.
# (10.5281=Zenodo, 10.17632=Mendeley Data, 10.6084=Figshare, 10.7910=Dataverse)
DATASET_DOI_PREFIXES = ("10.5281/", "10.17632/", "10.6084/", "10.7910/")

# Domain relevance gate for PAPERS. Every candidate (all four sources) must
# contain at least one of these broad domain terms in title+abstract. This
# is deliberately wider than the direction keywords: direction matching is
# phrase-exact and brittle (word order, plurals, synonyms), so it is only
# used for tagging, never as an admission gate.
PAPER_DOMAIN_KEYWORDS = [
    "underwater acoustic", "underwater sound", "ocean acoustic",
    "marine acoustic", "hydroacoustic", "sonar", "hydrophone",
    "underwater communication", "underwater channel",
    "underwater localization", "underwater positioning",
    "underwater navigation", "underwater sensor network",
    "underwater target", "underwater noise", "underwater vehicle",
    "underwater wireless", "underwater optical",
    "bioacoustic", "marine mammal", "cetacean", "whale", "dolphin",
    "echolocation", "geoacoustic", "seabed acoustic", "seafloor acoustic",
    "acoustic tomography", "ocean ambient noise",
]

# Score weights
SCORE_WEIGHTS = {
    "journal": 0.40,      # Journal quality
    "recency": 0.20,      # Publication recency
    "direction": 0.20,    # Research direction match
    "citation": 0.10,     # Citation count
    "open_access": 0.10,  # Open access bonus
}

# News sources, in three tiers:
# - official: societies / institutions (highest authority)
# - media: industry media with RSS feeds (verified reachable from CI)
# - company: company newsrooms
# - university: Chinese university news pages (webpage scraping, keyword-filtered)
# Feeds behind Cloudflare anti-bot (oceannews, sonardyne, UST, kongsberg) are
# excluded — they return 403 to plain HTTP clients.
NEWS_RSS_SOURCES = {
    "Acoustical Society of America": {
        "url": "https://acousticalsociety.org/feed/",
        "tier": "official",
    },
    "Marine Technology News": {
        "url": "https://www.marinetechnologynews.com/rss/",
        "tier": "media",
    },
    "Naval News": {
        "url": "https://www.navalnews.com/feed/",
        "tier": "media",
    },
    "Offshore Energy": {
        "url": "https://www.offshore-energy.biz/feed/",
        "tier": "media",
    },
}

# Webpage sources (no RSS available); links are keyword-filtered.
# NOTE: previously configured URLs (hrbeu.edu.cn/xyxw.htm, nwpu.edu.cn/xwzx.htm)
# returned 404 as of 2026-08-21; these are the working ones.
NEWS_WEBPAGE_SOURCES = {
    "哈尔滨工程大学新闻网": {
        "url": "https://news.hrbeu.edu.cn/",
        "tier": "university",
    },
}

# Extra English keywords for news relevance filtering, on top of
# UNDERWATER_ACOUSTIC_KEYWORDS (which is mostly Chinese + a few English).
# Keywords for news relevance filtering (self-contained; the older
# UNDERWATER_ACOUSTIC_KEYWORDS below is defined later in this file).
NEWS_RELEVANCE_KEYWORDS = [
    # English
    "underwater acoustic", "ocean acoustic", "marine acoustic", "hydroacoustic",
    "sonar", "hydrophone",
    "uuv", "auv", "unmanned underwater", "underwater vehicle",
    "anti-submarine", "asw", "subsea acoustic",
    "marine mammal", "bioacoustic", "ocean observing",
    "whale call", "whale song", "dolphin whistle", "cetacean",
    # 中文
    "水声", "水下声学", "海洋声学", "声呐", "水声工程", "声学", "水下",
]

# Negative keywords: terms that indicate offshore oil & gas / shipping news
# that frequently false-positive on relevance keywords (e.g. "Dolphin
# Drilling" matching "dolphin"). Checked before the positive filter.
NEWS_NEGATIVE_KEYWORDS = [
    "drilling", "oil rig", "gas field", "fpso", "lng",
    "offshore wind", "wind farm", "oil and gas", "fpso",
]

# News selection parameters
NEWS_TARGET = 5         # hard site limit: News + Policy <= 5 per day
NEWS_MIN_SCORE = 62     # tier base 65 + anything => passes; media without recency bonus fails
NEWS_MAX_AGE_DAYS = 14

# News scoring
NEWS_TIER_SCORES = {
    "official": 75,
    "university": 70,
    "company": 70,
    "media": 65,
}

# University news sources (RSS or webpage)
UNIVERSITY_NEWS_SOURCES = {
    "哈尔滨工程大学": {
        "name": "哈尔滨工程大学",
        "url": "https://www.hrbeu.edu.cn/",
        "news_url": "https://www.hrbeu.edu.cn/xyxw.htm",
        "type": "webpage",
    },
    "西北工业大学": {
        "name": "西北工业大学",
        "url": "https://www.nwpu.edu.cn/",
        "news_url": "https://www.nwpu.edu.cn/xwzx.htm",
        "type": "webpage",
    },
    "上海交通大学": {
        "name": "上海交通大学",
        "url": "https://www.sjtu.edu.cn/",
        "news_url": "https://www.sjtu.edu.cn/xwzx.htm",
        "type": "webpage",
    },
    "中科院声学所": {
        "name": "中科院声学所",
        "url": "http://www.ioa.ac.cn/",
        "news_url": "http://www.ioa.ac.cn/xwzx.htm",
        "type": "webpage",
    },
}

# Policy sources
POLICY_SOURCES = {
    "国家海洋局": {
        "name": "国家海洋局",
        "url": "https://www.mnr.gov.cn/",
        "type": "webpage",
    },
    "自然科学基金委": {
        "name": "国家自然科学基金委员会",
        "url": "https://www.nsfc.gov.cn/",
        "type": "webpage",
    },
}

# Keywords for filtering news/policy related to underwater acoustics
UNDERWATER_ACOUSTIC_KEYWORDS = [
    "水声", "水下声学", "海洋声学", "声呐", "水声工程",
    "underwater acoustic", "ocean acoustic", "sonar",
    "marine acoustic", "hydroacoustic",
]
