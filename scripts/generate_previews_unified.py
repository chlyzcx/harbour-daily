"""Unified preview image generation for all data sources."""

import os
import re
import requests
from io import BytesIO
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from models import Paper


# Unpaywall requires an email address; reuse the OpenAlex contact.
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "2770820299@qq.com")

# A polite User-Agent helps with publisher sites that block default agents.
_UA = {"User-Agent": f"harbour-daily/1.0 (mailto:{UNPAYWALL_EMAIL})"}


def sanitize_filename(text: str) -> str:
    """Sanitize text for use in filename."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


def _paper_doi(paper: Paper) -> Optional[str]:
    """Extract the DOI string from the paper, if any."""
    if paper.doi:
        return paper.doi
    for source in paper.sources:
        if source.name == "DOI" and "doi.org/" in source.url:
            return source.url.split("doi.org/")[-1]
    return None


def _save_image_bytes(data: bytes, output_path: Path,
                      min_w: int = 250, min_h: int = 150) -> bool:
    """Validate image bytes with PIL and save as PNG.

    Rejects tiny images (site logos, icons, tracking pixels).
    """
    try:
        from PIL import Image
        img = Image.open(BytesIO(data))
        if img.width < min_w or img.height < min_h:
            print(f"    Image too small ({img.width}x{img.height}), skipping")
            return False
        if img.mode in ("RGBA", "P", "CMYK", "LA"):
            img = img.convert("RGB")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, "PNG")
        return True
    except Exception as e:
        print(f"    Image decode failed: {e}")
        return False


# ==================== arXiv HTML 首图 ====================

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
        response = requests.get(html_url, timeout=30, headers=_UA)

        if response.status_code != 200:
            print(f"    HTML version not available (status {response.status_code})")
            return False

        soup = BeautifulSoup(response.content, 'lxml')

        # Find first figure image
        img = soup.find('img', {'class': 'ltx_graphics'})
        if not img or not img.get('src'):
            print(f"    No image found in HTML")
            return False

        # Resolve the image src against the HTML page URL — src can be an
        # absolute path ("/html/<id>/pic/x.png") or relative ("<id>/pic/x.png"),
        # so naive string concatenation mangles the host.
        img_url = urljoin(html_url, img['src'])

        # Download image
        print(f"    Downloading image: {img_url}")
        img_response = requests.get(img_url, timeout=30, headers=_UA)
        img_response.raise_for_status()
        return _save_image_bytes(img_response.content, output_path)

    except Exception as e:
        print(f"    Error extracting arXiv HTML image: {e}")
        return False


# ==================== PDF 处理 ====================

def _download_pdf(pdf_url: str) -> Optional[bytes]:
    """Download a URL and return its bytes only if it is really a PDF.

    Some journals serve an HTML page at the "PDF" link (e.g. jidmis.org),
    which previously got fed into the PDF parsers and spammed hundreds of
    syntax-error lines. The %PDF- magic number is more reliable than the
    Content-Type header, which misconfigured servers often get wrong.
    """
    try:
        print(f"    Downloading PDF: {pdf_url}")
        response = requests.get(pdf_url, timeout=60, headers=_UA)
        response.raise_for_status()
        if not response.content[:5] == b"%PDF-":
            print(f"    Not a real PDF (server returned HTML/other), skipping")
            return None
        return response.content
    except requests.RequestException as e:
        print(f"    PDF download failed: {e}")
        return None


def extract_pdf_figure(pdf_data: bytes, output_path: Path, max_pages: int = 6) -> bool:
    """Extract the largest embedded figure image from PDF bytes.

    Scans the first few pages for embedded raster images and picks the
    largest one (most likely a figure, not an icon or logo).
    """
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("    PyMuPDF not installed, skipping figure extraction")
        return False

    try:
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        best = None  # (area, image_bytes)
        for page_num in range(min(len(doc), max_pages)):
            for img in doc[page_num].get_images(full=True):
                xref = img[0]
                try:
                    info = doc.extract_image(xref)
                except Exception:
                    continue
                w, h = info.get("width", 0), info.get("height", 0)
                # Skip small images (icons, logos, ornaments)
                if w < 250 or h < 150:
                    continue
                area = w * h
                if best is None or area > best[0]:
                    best = (area, info["image"])
        doc.close()

        if not best:
            print("    No embedded figure found in PDF")
            return False

        ok = _save_image_bytes(best[1], output_path)
        if ok:
            from PIL import Image
            img = Image.open(BytesIO(best[1]))
            print(f"    Extracted embedded figure ({img.size[0]}x{img.size[1]})")
        return ok

    except Exception as e:
        print(f"    Error extracting PDF figure: {e}")
        return False


def extract_pdf_page(pdf_data: bytes, output_path: Path, page: int = 1) -> bool:
    """Render a specific page of PDF bytes as an image.

    PyMuPDF first (pure Python, no system dependency); pdf2image/poppler
    as backup.
    """
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        if page <= len(doc):
            pix = doc[page - 1].get_pixmap(dpi=150)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            pix.save(output_path)
            doc.close()
            print(f"    Rendered page {page} with PyMuPDF")
            return True
        doc.close()
        print(f"    No page {page} found in PDF")
        return False
    except ImportError:
        pass
    except Exception as e:
        print(f"    PyMuPDF render failed: {e}")

    try:
        from pdf2image import convert_from_bytes
        print(f"    Rendering page {page} from PDF...")
        images = convert_from_bytes(pdf_data, dpi=150, first_page=page, last_page=page)

        if not images:
            print(f"    No page {page} found in PDF")
            return False

        output_path.parent.mkdir(parents=True, exist_ok=True)
        images[0].save(output_path, "PNG")
        return True

    except Exception as e:
        print(f"    Error rendering PDF page: {e}")
        return False


# ==================== 出版商 CDN 图片 ====================

def _resolve_doi(doi: str) -> Optional[str]:
    """Follow a DOI's redirect chain and return the final URL.

    The publisher page itself may block us (Elsevier 403s bots), but the
    redirect chain still reveals the target URL — e.g. doi.org sends
    Elsevier DOIs to linkinghub.elsevier.com/retrieve/pii/<PII>, and the
    PII is all we need to build figure URLs on the (unblocked) CDN.
    """
    try:
        response = requests.get(f"https://doi.org/{doi}", timeout=30,
                                headers=_UA, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        print(f"    DOI resolution failed: {e}")
        return None


def extract_publisher_figure(doi: str, output_path: Path) -> bool:
    """Download a figure straight from the publisher's image CDN.

    Covers the two publisher families that dominate our journal list and
    block their article pages to bots:
    - MDPI (J. Mar. Sci. Eng., Sensors, ...): page 403s, but figures on
      mdpi-res.com are open and their URLs derive from the DOI itself.
    - Elsevier (Ocean Engineering, Applied Acoustics, ...): page 403s,
      but figures on ars.els-cdn.com are open once the PII is known
      (recovered from the DOI redirect chain).
    """
    # --- MDPI: DOI suffix = <journal><vol2><issue2><article4> ---
    # File naming on the CDN drops the issue and zero-pads the article
    # number to 5 digits: 10.3390/jmse14161511 -> jmse-14-01511-g001.png.
    # A few journals use a different path acronym than the DOI one.
    m = re.match(r"10\.3390/([a-z]+)(\d{2})(\d{2})(\d{4})$", doi)
    if m:
        MDPI_PATH_ALIASES = {"s": "sensors", "rs": "remotesensing"}
        acr, vol, _issue, art = m.groups()
        path_acrs = dict.fromkeys([MDPI_PATH_ALIASES.get(acr, acr), acr])
        for path_acr in path_acrs:
            stem = f"{path_acr}-{vol}-{int(art):05d}"
            base = (f"https://mdpi-res.com/d_attachment/{path_acr}/{stem}/"
                    f"article_deploy/html/images/{stem}")
            for n in range(1, 9):
                found_200 = False
                for ext in ("png", "jpg", "jpeg"):
                    url = f"{base}-g{n:03d}.{ext}"
                    try:
                        r = requests.get(url, timeout=20, headers=_UA)
                    except requests.RequestException:
                        continue
                    if r.status_code != 200:
                        continue
                    found_200 = True
                    if _save_image_bytes(r.content, output_path):
                        print(f"    MDPI figure: {url}")
                        return True
                    break  # 200 but too small; try next figure number
                if not found_200:
                    break  # no figure N at all -> no point trying N+1
        return False

    # --- Elsevier: resolve DOI -> PII -> ars.els-cdn.com figure ---
    final_url = _resolve_doi(doi)
    if final_url and ("elsevier" in final_url or "sciencedirect" in final_url):
        pii_m = re.search(r"/pii/([A-Za-z0-9]+)", final_url)
        if pii_m:
            pii = pii_m.group(1)
            base = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}"
            # ga1 = graphical abstract, grN = figure N; _lrg = high-res
            candidates = ([f"-ga1_lrg.jpg", "-ga1.jpg"]
                          + [f"-gr{n}{v}.jpg" for n in (1, 2, 3) for v in ("_lrg", "")])
            for suffix in candidates:
                try:
                    r = requests.get(base + suffix, timeout=20, headers=_UA)
                except requests.RequestException:
                    continue
                if r.status_code == 200 and _save_image_bytes(r.content, output_path):
                    print(f"    Elsevier figure: {base}{suffix}")
                    return True
    return False


# ==================== 出版商页面 og:image ====================

def extract_og_image(page_url: str, output_path: Path) -> bool:
    """Fetch a landing page (e.g. DOI redirect to the publisher) and grab
    its og:image / twitter:image, which is often the article's key figure
    or graphical abstract."""
    try:
        response = requests.get(page_url, timeout=30, headers=_UA, allow_redirects=True)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.content, 'lxml')
        tag = (soup.find("meta", property="og:image")
               or soup.find("meta", attrs={"name": "twitter:image"}))
        if not tag or not tag.get("content"):
            print("    No og:image on landing page")
            return False

        img_url = urljoin(response.url, tag["content"])
        print(f"    Downloading og:image: {img_url}")
        img_response = requests.get(img_url, timeout=30, headers=_UA)
        img_response.raise_for_status()
        return _save_image_bytes(img_response.content, output_path)

    except Exception as e:
        print(f"    og:image extraction failed: {e}")
        return False


# ==================== Unpaywall 开放获取 PDF ====================

def find_oa_pdf_urls(doi: str) -> list[str]:
    """Query Unpaywall for legal open-access PDFs of this DOI.

    Returns URLs from ALL OA locations (best first) — repository copies
    often have a PDF even when the primary location doesn't.
    """
    try:
        response = requests.get(
            f"https://api.unpaywall.org/v2/{doi}",
            params={"email": UNPAYWALL_EMAIL},
            timeout=20,
        )
        if response.status_code != 200:
            return []
        data = response.json()
        urls = []
        best = data.get("best_oa_location")
        locations = ([best] if best else []) + data.get("oa_locations", [])
        for loc in locations:
            if not loc:
                continue
            pdf = loc.get("url_for_pdf")
            if pdf and pdf not in urls:
                urls.append(pdf)
        return urls
    except Exception as e:
        print(f"    Unpaywall lookup failed: {e}")
        return []


# ==================== 统一预览图生成 ====================

def try_real_preview(paper: Paper, output_path: Path) -> bool:
    """Try every real-image source for a paper, best quality first:

    1. arXiv HTML first figure (cheapest, best quality)
    2. Publisher CDN figure (MDPI / Elsevier) — single small request,
       works even when the article page itself blocks bots
    3. Largest embedded figure from any available PDF
       (arXiv PDF, known OA URL, Unpaywall-discovered OA PDFs)
    4. Publisher landing page og:image
    5. Full-page render of the PDF (page 2, then page 1) — last resort
    """
    pdf_urls: list[str] = []

    arxiv_url = next((s.url for s in paper.sources if "arxiv.org" in s.url), None)
    if arxiv_url:
        if extract_arxiv_html_image(arxiv_url, output_path):
            return True
        pdf_url = arxiv_url.replace("/abs/", "/pdf/")
        if not pdf_url.endswith(".pdf"):
            pdf_url += ".pdf"
        pdf_urls.append(pdf_url)

    doi = _paper_doi(paper)
    if doi and extract_publisher_figure(doi, output_path):
        return True

    if paper.oa_url:
        pdf_urls.append(paper.oa_url)

    if doi:
        pdf_urls.extend(find_oa_pdf_urls(doi))

    # Deduplicate, preserving priority order
    seen = set()
    pdf_urls = [u for u in pdf_urls if not (u in seen or seen.add(u))]

    # Download each candidate at most once (previously the same PDF was
    # downloaded up to 3 times: figure attempt, page 2, page 1)
    first_pdf: Optional[bytes] = None
    for url in pdf_urls:
        data = _download_pdf(url)
        if not data:
            continue
        if first_pdf is None:
            first_pdf = data
        if extract_pdf_figure(data, output_path):
            return True

    if doi and extract_og_image(f"https://doi.org/{doi}", output_path):
        return True

    # Ugliest fallback among the real sources: a full page render
    if first_pdf:
        if extract_pdf_page(first_pdf, output_path, page=2):
            return True
        if extract_pdf_page(first_pdf, output_path, page=1):
            return True

    return False


def generate_preview_unified(paper: Paper, date_str: str, project_root: Path) -> str:
    """
    Generate preview image for a paper from any data source.
    Returns the public URL path to the preview image.
    """
    assets_dir = project_root / "docs" / "public" / "daily" / date_str / "assets" / paper.candidate_id
    preview_path = assets_dir / "preview.png"

    print(f"  Generating preview for: {paper.title[:50]}...")
    if try_real_preview(paper, preview_path):
        return f"/daily/{date_str}/assets/{paper.candidate_id}/preview.png"

    # Fall back to the themed SVG cover
    from generate_previews import generate_preview_image
    return generate_preview_image(paper, date_str, project_root)


def generate_all_previews_unified(papers: list[Paper], date_str: str, project_root: Path) -> None:
    """Generate preview images for all papers using the unified approach."""
    print(f"Generating unified preview images for {len(papers)} papers...")

    real_count = 0
    svg_count = 0

    for paper in papers:
        preview_url = generate_preview_unified(paper, date_str, project_root)
        paper.preview_image = preview_url
        if preview_url.endswith("preview.png"):
            real_count += 1
        else:
            svg_count += 1

    print(f"\nPreview generation summary:")
    print(f"  - Real images: {real_count}")
    print(f"  - SVG fallback: {svg_count}")
