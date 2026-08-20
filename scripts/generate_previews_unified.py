"""Unified preview image generation for all data sources."""

import re
import requests
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
from models import Paper


def sanitize_filename(text: str) -> str:
    """Sanitize text for use in filename."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


# ==================== arXiv 预览图 ====================

def extract_arxiv_html_image(arxiv_url: str, output_path: Path) -> bool:
    """Extract first image from arXiv HTML page."""
    try:
        # Extract arXiv ID from URL
        match = re.search(r'arxiv\.org/abs/([^/]+)', arxiv_url)
        if not match:
            return False

        arxiv_id = match.group(1)
        html_url = f"https://arxiv.org/html/{arxiv_id}"

        print(f"    Trying arXiv HTML: {html_url}")
        response = requests.get(html_url, timeout=30)

        if response.status_code != 200:
            print(f"    HTML version not available (status {response.status_code})")
            return False

        soup = BeautifulSoup(response.content, 'lxml')

        # Find first figure image
        img = soup.find('img', {'class': 'ltx_graphics'})
        if not img or not img.get('src'):
            print(f"    No image found in HTML")
            return False

        img_url = img['src']
        if not img_url.startswith('http'):
            img_url = f"https://arxiv.org{img_url}"

        # Download image
        print(f"    Downloading image: {img_url}")
        img_response = requests.get(img_url, timeout=30)
        img_response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(img_response.content)
        return True

    except Exception as e:
        print(f"    Error extracting arXiv HTML image: {e}")
        return False


def extract_pdf_page(pdf_url: str, output_path: Path, page: int = 1) -> bool:
    """Extract specific page from PDF as image."""
    try:
        print(f"    Downloading PDF: {pdf_url}")
        response = requests.get(pdf_url, timeout=60)
        response.raise_for_status()

        # Save PDF temporarily
        temp_pdf = output_path.parent / "temp.pdf"
        temp_pdf.parent.mkdir(parents=True, exist_ok=True)
        temp_pdf.write_bytes(response.content)

        # Convert page to image
        print(f"    Extracting page {page} from PDF...")
        images = convert_from_path(temp_pdf, dpi=150, first_page=page, last_page=page)

        if not images:
            print(f"    No page {page} found in PDF")
            temp_pdf.unlink()
            return False

        # Save image
        output_path.parent.mkdir(parents=True, exist_ok=True)
        images[0].save(output_path, "PNG")

        # Clean up
        temp_pdf.unlink()
        return True

    except Exception as e:
        print(f"    Error extracting PDF page: {e}")
        return False


def generate_arxiv_preview(paper: Paper, output_path: Path) -> bool:
    """Generate preview for arXiv paper."""
    # Find arXiv URL
    arxiv_url = None
    for source in paper.sources:
        if "arxiv.org" in source.url:
            arxiv_url = source.url
            break

    if not arxiv_url:
        return False

    # Try HTML first
    if extract_arxiv_html_image(arxiv_url, output_path):
        return True

    # Fallback to PDF page 2 (usually has Figure 1)
    pdf_url = arxiv_url.replace("/abs/", "/pdf/")
    if not pdf_url.endswith(".pdf"):
        pdf_url += ".pdf"

    if extract_pdf_page(pdf_url, output_path, page=2):
        return True

    # Fallback to PDF page 1
    if extract_pdf_page(pdf_url, output_path, page=1):
        return True

    return False


# ==================== OpenAlex 预览图 ====================

def generate_openalex_preview(paper: Paper, output_path: Path) -> bool:
    """Generate preview for OpenAlex paper."""
    # Check if it's open access and has PDF URL
    if paper.is_oa and paper.oa_url:
        print(f"    Open access paper, trying PDF: {paper.oa_url}")
        # Try to extract from PDF (page 2 usually has Figure 1)
        if extract_pdf_page(paper.oa_url, output_path, page=2):
            return True
        # Fallback to page 1
        if extract_pdf_page(paper.oa_url, output_path, page=1):
            return True

    # Not open access or PDF extraction failed
    # Return False to use SVG fallback
    return False


# ==================== Semantic Scholar 预览图 ====================

def generate_semantic_scholar_preview(paper: Paper, output_path: Path) -> bool:
    """Generate preview for Semantic Scholar paper."""
    # Check if paper has open access PDF URL
    if paper.oa_url:
        print(f"    Has open access PDF, trying: {paper.oa_url}")
        # Try to extract from PDF (page 2 usually has Figure 1)
        if extract_pdf_page(paper.oa_url, output_path, page=2):
            return True
        # Fallback to page 1
        if extract_pdf_page(paper.oa_url, output_path, page=1):
            return True

    # No OA PDF or extraction failed
    # Return False to use SVG fallback
    return False


# ==================== 统一预览图生成 ====================

def generate_preview_unified(paper: Paper, date_str: str, project_root: Path) -> str:
    """
    Generate preview image for a paper from any data source.
    Returns the public URL path to the preview image.
    """
    # Create output directory
    assets_dir = project_root / "docs" / "public" / "daily" / date_str / "assets" / paper.candidate_id
    preview_path = assets_dir / "preview.png"

    # Determine source type
    is_arxiv = any("arxiv.org" in source.url for source in paper.sources)
    is_openalex = "openalex" in paper.candidate_id.lower()
    is_semantic_scholar = "s2--" in paper.candidate_id or "semanticscholar" in paper.candidate_id.lower()

    success = False

    # Try to generate real preview based on source
    if is_arxiv:
        print(f"  [arXiv] Generating preview for: {paper.title[:50]}...")
        success = generate_arxiv_preview(paper, preview_path)

    elif is_openalex:
        print(f"  [OpenAlex] Generating preview for: {paper.title[:50]}...")
        success = generate_openalex_preview(paper, preview_path)

    elif is_semantic_scholar:
        print(f"  [Semantic Scholar] Generating preview for: {paper.title[:50]}...")
        success = generate_semantic_scholar_preview(paper, preview_path)

    else:
        print(f"  [Other] Using SVG for: {paper.title[:50]}...")

    # If real preview failed, use SVG fallback
    if not success:
        from generate_previews import generate_preview_image
        return generate_preview_image(paper, date_str, project_root)

    # Return public URL
    return f"/daily/{date_str}/assets/{paper.candidate_id}/preview.png"


def generate_all_previews_unified(papers: list[Paper], date_str: str, project_root: Path) -> None:
    """Generate preview images for all papers using unified approach."""
    print(f"Generating unified preview images for {len(papers)} papers...")

    arxiv_count = 0
    openalex_count = 0
    s2_count = 0
    svg_count = 0

    for paper in papers:
        preview_url = generate_preview_unified(paper, date_str, project_root)
        paper.preview_image = preview_url

        # Count by type
        if "preview.png" in preview_url:
            if "arxiv" in paper.candidate_id:
                arxiv_count += 1
            elif "openalex" in paper.candidate_id:
                openalex_count += 1
            elif "s2" in paper.candidate_id:
                s2_count += 1
        else:
            svg_count += 1

    print(f"\nPreview generation summary:")
    print(f"  - arXiv real images: {arxiv_count}")
    print(f"  - OpenAlex real images: {openalex_count}")
    print(f"  - Semantic Scholar real images: {s2_count}")
    print(f"  - SVG fallback: {svg_count}")
