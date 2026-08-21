"""Generate preview images for papers."""

import hashlib
import math
import re
from html import escape
from pathlib import Path
from models import Paper


def sanitize_filename(text: str) -> str:
    """Sanitize text for use in filename."""
    # Remove special characters
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


# Color themes: (gradient_start, gradient_end, accent). One theme is picked
# deterministically per paper based on its research direction, so cards in
# the same topic share a color and different topics are distinguishable.
_THEMES = [
    ("#0f172a", "#1e3a8a", "#60a5fa"),  # 深海蓝（默认）
    ("#042f2e", "#115e59", "#2dd4bf"),  # 声学青
    ("#2e1065", "#5b21b6", "#a78bfa"),  # 信号紫
    ("#431407", "#9a3412", "#fb923c"),  # 探测橙
    ("#052e16", "#166534", "#4ade80"),  # 生物绿
]


def _stable_seed(text: str) -> int:
    """Deterministic hash — Python's built-in hash() varies between runs."""
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)


def _wave_points(seed: int, y_base: float, amp: float, width: int = 400) -> str:
    """Generate a deterministic waveform (two superimposed sines) as an SVG
    polyline point list, seeded by the paper title so every card differs."""
    freq1 = 0.018 + (seed % 5) * 0.004
    phase1 = (seed % 628) / 100.0
    freq2 = 0.050 + ((seed >> 4) % 3) * 0.012
    phase2 = ((seed >> 8) % 628) / 100.0
    points = []
    for x in range(0, width + 1, 8):
        y = y_base + amp * math.sin(freq1 * x + phase1) \
                  + (amp * 0.4) * math.sin(freq2 * x + phase2)
        points.append(f"{x},{y:.1f}")
    return " ".join(points)


def generate_svg_cover(paper: Paper, date_str: str) -> str:
    """Generate a themed SVG cover for a paper.

    The color theme comes from the research direction and the waveform
    decoration from the title, so fallback cards no longer look identical.
    """
    keyword = paper.keywords[0] if paper.keywords else "Research"

    # News items expose display_title (Chinese) in addition to title
    raw_title = getattr(paper, "display_title", None) or paper.title

    # Theme by research direction (falls back to keyword)
    direction = paper.research_directions[0] if paper.research_directions else keyword
    bg1, bg2, accent = _THEMES[_stable_seed(direction) % len(_THEMES)]

    title = raw_title
    if len(title) > 60:
        title = title[:57] + "..."

    first_author = paper.authors[0] if paper.authors else "Unknown"
    if len(first_author) > 30:
        first_author = first_author[:27] + "..."

    journal = paper.journal or ""

    # Three waveform layers seeded by the title (sonar-echo feel)
    wave_seed = _stable_seed(paper.title)
    waves = []
    for i, (y_base, amp, opacity) in enumerate([(205, 14, 0.35), (232, 18, 0.22), (262, 22, 0.13)]):
        points = _wave_points(wave_seed + i * 7919, y_base, amp)
        waves.append(
            f'  <polyline points="{points}" fill="none" stroke="{accent}" '
            f'stroke-width="1.5" opacity="{opacity}"/>'
        )
    waves_svg = "\n".join(waves)

    # Generate SVG (all interpolated text is XML-escaped)
    svg = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{bg1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{bg2};stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="400" height="300" fill="url(#grad)"/>

  <!-- Grid pattern -->
  <g opacity="0.1">
    <line x1="0" y1="75" x2="400" y2="75" stroke="{accent}" stroke-width="1"/>
    <line x1="0" y1="150" x2="400" y2="150" stroke="{accent}" stroke-width="1"/>
    <line x1="0" y1="225" x2="400" y2="225" stroke="{accent}" stroke-width="1"/>
    <line x1="100" y1="0" x2="100" y2="300" stroke="{accent}" stroke-width="1"/>
    <line x1="200" y1="0" x2="200" y2="300" stroke="{accent}" stroke-width="1"/>
    <line x1="300" y1="0" x2="300" y2="300" stroke="{accent}" stroke-width="1"/>
  </g>

  <!-- Waveform decoration (deterministic per title) -->
  <g>
{waves_svg}
  </g>

  <!-- Header -->
  <text x="20" y="40" font-family="Inter, sans-serif" font-size="14" fill="{accent}" font-weight="600">
    UWA / {date_str[5:]}
  </text>

  <!-- Keyword badge -->
  <rect x="20" y="60" width="{len(keyword) * 8 + 20}" height="28" rx="14" fill="{accent}" opacity="0.2"/>
  <text x="30" y="79" font-family="Inter, sans-serif" font-size="13" fill="{accent}" font-weight="500">
    {escape(keyword)}
  </text>

  <!-- Title -->
  <foreignObject x="20" y="110" width="360" height="120">
    <div xmlns="http://www.w3.org/1999/xhtml" style="
      font-family: Inter, sans-serif;
      font-size: 18px;
      font-weight: 600;
      color: #e2e8f0;
      line-height: 1.4;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      -webkit-box-orient: vertical;
    ">
      {escape(title)}
    </div>
  </foreignObject>

  <!-- Author -->
  <text x="20" y="250" font-family="Inter, sans-serif" font-size="13" fill="#94a3b8">
    {escape(first_author)}
  </text>

  <!-- Footer -->
  <text x="20" y="275" font-family="Inter, sans-serif" font-size="11" fill="#64748b">
    {escape(journal)}
  </text>

  <!-- Score badge -->
  <circle cx="360" cy="40" r="24" fill="{accent}" opacity="0.2"/>
  <text x="360" y="46" font-family="Inter, sans-serif" font-size="14" fill="{accent}" font-weight="700" text-anchor="middle">
    {int(paper.score)}
  </text>
</svg>'''

    return svg


def generate_preview_image(paper: Paper, date_str: str, output_dir: Path) -> str:
    """Generate SVG preview image for a paper and return the public URL path."""
    # Create assets directory
    assets_dir = output_dir / "docs" / "public" / "daily" / date_str / "assets" / paper.candidate_id
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Generate SVG
    svg_content = generate_svg_cover(paper, date_str)

    # Save SVG file
    svg_path = assets_dir / "preview.svg"
    svg_path.write_text(svg_content, encoding="utf-8")

    # Return public URL path
    return f"/daily/{date_str}/assets/{paper.candidate_id}/preview.svg"


def generate_all_previews(papers: list[Paper], date_str: str, project_root: Path) -> None:
    """
    Generate preview images for all papers.
    For arXiv papers, try PDF extraction first; fallback to SVG.
    For other papers, use SVG.
    """
    from generate_pdf_previews import generate_preview_from_pdf

    print(f"Generating preview images for {len(papers)} papers...")

    for paper in papers:
        # Check if it's an arXiv paper
        has_arxiv = any("arxiv.org" in source.url for source in paper.sources)

        if has_arxiv:
            # Try PDF extraction first
            print(f"  Trying PDF extraction for: {paper.title[:50]}...")
            pdf_preview = generate_preview_from_pdf(paper, date_str, project_root)

            if pdf_preview:
                paper.preview_image = pdf_preview
                print(f"    Generated PDF preview: {pdf_preview}")
            else:
                # Fallback to SVG
                print(f"    PDF extraction failed, using SVG fallback")
                paper.preview_image = generate_preview_image(paper, date_str, project_root)
        else:
            # Use SVG for non-arXiv papers
            paper.preview_image = generate_preview_image(paper, date_str, project_root)
            print(f"  Generated SVG preview: {paper.preview_image}")
