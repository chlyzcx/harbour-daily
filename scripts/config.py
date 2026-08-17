"""Configuration for underwater acoustic daily paper fetcher."""

# Research directions and their search keywords
RESEARCH_DIRECTIONS = {
    # 水声通信信道
    "信道建模": [
        "underwater acoustic channel model",
        "ocean acoustic channel model",
        "underwater channel modeling",
        "acoustic propagation model",
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
    # 水声通信
    "OFDM": [
        "underwater acoustic OFDM",
        "underwater OFDM communication",
        "OFDM underwater acoustic",
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
        "underwater acoustic modem",
    ],
    "网络协议": [
        "underwater acoustic network protocol",
        "underwater MAC protocol",
        "underwater acoustic networking",
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
    # 水声侦察
    "目标检测": [
        "underwater target detection",
        "underwater acoustic target detection",
        "underwater object detection",
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
    # 海洋生物声学信号处理
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
DAILY_TARGET = 15  # Daily target number of papers (upper limit)
MAX_AGE_DAYS = 7  # Maximum age for fallback
MIN_SCORE = 60  # Minimum score threshold

# Score weights
SCORE_WEIGHTS = {
    "journal": 0.40,      # Journal quality
    "recency": 0.20,      # Publication recency
    "direction": 0.20,    # Research direction match
    "citation": 0.10,     # Citation count
    "open_access": 0.10,  # Open access bonus
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
