"""Extract first page from arXiv PDF as preview image."""

import os
import requests
from pathlib import Path
from pdf2image import convert_from_path
from models import Paper


def download_arxiv_pdf(arxiv_url: str, output_path: Path) -> bool:
    """Download arXiv PDF file."""
    try:
        # Convert abs URL to pdf URL
        pdf_url = arxiv_url.replace("/abs/", "/pdf/")
        if not pdf_url.endswith(".pdf"):
            pdf_url += ".pdf"

        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True

    except requests.RequestException as e:
        print(f"    Error downloading PDF: {e}")
        return False


def extract_first_page_as_image(pdf_path: Path, output_path: Path) -> bool:
    """Extract first page of PDF as PNG image."""
    try:
        # Convert first page to image
        images = convert_from_path(pdf_path, dpi=150, first_page=1, last_page=1)

        if not images:
            print(f"    No pages found in PDF")
            return False

        # Save first page as PNG
        output_path.parent.mkdir(parents=True, exist_ok=True)
        images[0].save(output_path, "PNG")
        return True

    except Exception as e:
        print(f"    Error extracting PDF page: {e}")
        return False


def generate_preview_from_pdf(paper: Paper, date_str: str, project_root: Path) -> str:
    """
    Generate preview image from arXiv PDF.
    Returns the public URL path to the preview image.
    """
    # Only process arXiv papers
    arxiv_source = None
    for source in paper.sources:
        if "arxiv.org" in source.url:
            arxiv_source = source
            break

    if not arxiv_source:
        print(f"    Not an arXiv paper, skipping PDF preview")
        return ""

    # Create temp directory for PDF
    temp_dir = project_root / "temp_pdfs"
    temp_dir.mkdir(exist_ok=True)
    pdf_path = temp_dir / f"{paper.candidate_id}.pdf"

    # Download PDF
    print(f"    Downloading PDF from arXiv...")
    if not download_arxiv_pdf(arxiv_source.url, pdf_path):
        return ""

    # Create output directory
    assets_dir = project_root / "docs" / "public" / "daily" / date_str / "assets" / paper.candidate_id
    preview_path = assets_dir / "preview.png"

    # Extract first page
    print(f"    Extracting first page as image...")
    if not extract_first_page_as_image(pdf_path, preview_path):
        return ""

    # Clean up temp PDF
    try:
        pdf_path.unlink()
    except:
        pass

    # Return public URL
    return f"/daily/{date_str}/assets/{paper.candidate_id}/preview.png"


def generate_all_pdf_previews(papers: list[Paper], date_str: str, project_root: Path) -> None:
    """Generate PDF preview images for all arXiv papers."""
    print(f"Generating PDF preview images for arXiv papers...")

    arxiv_count = 0
    for paper in papers:
        # Check if it's an arXiv paper
        has_arxiv = any("arxiv.org" in source.url for source in paper.sources)
        if not has_arxiv:
            continue

        arxiv_count += 1
        print(f"  [{arxiv_count}] Processing: {paper.title[:50]}...")

        preview_url = generate_preview_from_pdf(paper, date_str, project_root)
        if preview_url:
            paper.preview_image = preview_url
            print(f"    Generated: {preview_url}")
        else:
            print(f"    Failed to generate PDF preview, will use SVG fallback")

    print(f"PDF preview generation completed! ({arxiv_count} arXiv papers)")


if __name__ == "__main__":
    # Test
    from models import Paper, Source

    paper = Paper(
        candidate_id="arxiv--2608.10533-1",
        title="Test Paper",
        authors=["Author 1"],
        summary="Test abstract",
        keywords=["test"],
        research_directions=["信道建模"],
        score=70.0,
        sources=[Source(name="arXiv", url="http://arxiv.org/abs/2608.10533v1")],
        journal="arXiv preprint",
        publisher="arXiv",
    )

    from pathlib import Path
    project_root = Path(__file__).parent.parent

    preview_url = generate_preview_from_pdf(paper, "2026-08-20", project_root)
    print(f"Preview URL: {preview_url}")
