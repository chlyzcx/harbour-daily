"""Generate preview images for papers."""

import re
from pathlib import Path
from models import Paper


def sanitize_filename(text: str) -> str:
    """Sanitize text for use in filename."""
    # Remove special characters
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


def generate_svg_cover(paper: Paper, date_str: str) -> str:
    """Generate SVG cover for a paper."""
    # Extract first keyword or use default
    keyword = paper.keywords[0] if paper.keywords else "Research"

    # Truncate title if too long
    title = paper.title
    if len(title) > 60:
        title = title[:57] + "..."

    # Get first author
    first_author = paper.authors[0] if paper.authors else "Unknown"
    if len(first_author) > 30:
        first_author = first_author[:27] + "..."

    # Generate SVG
    svg = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e293b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="400" height="300" fill="url(#grad)"/>

  <!-- Grid pattern -->
  <g opacity="0.1">
    <line x1="0" y1="75" x2="400" y2="75" stroke="#60a5fa" stroke-width="1"/>
    <line x1="0" y1="150" x2="400" y2="150" stroke="#60a5fa" stroke-width="1"/>
    <line x1="0" y1="225" x2="400" y2="225" stroke="#60a5fa" stroke-width="1"/>
    <line x1="100" y1="0" x2="100" y2="300" stroke="#60a5fa" stroke-width="1"/>
    <line x1="200" y1="0" x2="200" y2="300" stroke="#60a5fa" stroke-width="1"/>
    <line x1="300" y1="0" x2="300" y2="300" stroke="#60a5fa" stroke-width="1"/>
  </g>

  <!-- Header -->
  <text x="20" y="40" font-family="Inter, sans-serif" font-size="14" fill="#60a5fa" font-weight="600">
    UWA / {date_str[5:]}
  </text>

  <!-- Keyword badge -->
  <rect x="20" y="60" width="{len(keyword) * 8 + 20}" height="28" rx="14" fill="#3b82f6" opacity="0.2"/>
  <text x="30" y="79" font-family="Inter, sans-serif" font-size="13" fill="#60a5fa" font-weight="500">
    {keyword}
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
      {title}
    </div>
  </foreignObject>

  <!-- Author -->
  <text x="20" y="250" font-family="Inter, sans-serif" font-size="13" fill="#94a3b8">
    {first_author}
  </text>

  <!-- Footer -->
  <text x="20" y="275" font-family="Inter, sans-serif" font-size="11" fill="#64748b">
    {paper.journal}
  </text>

  <!-- Score badge -->
  <circle cx="360" cy="40" r="24" fill="#3b82f6" opacity="0.2"/>
  <text x="360" y="46" font-family="Inter, sans-serif" font-size="14" fill="#60a5fa" font-weight="700" text-anchor="middle">
    {int(paper.score)}
  </text>
</svg>'''

    return svg


def generate_preview_image(paper: Paper, date_str: str, output_dir: Path) -> str:
    """Generate preview image for a paper and return the public URL path."""
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
    """Generate preview images for all papers."""
    print(f"Generating preview images for {len(papers)} papers...")

    for paper in papers:
        preview_path = generate_preview_image(paper, date_str, project_root)
        paper.preview_image = preview_path
        print(f"  Generated: {preview_path}")
