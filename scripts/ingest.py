# -*- coding: utf-8 -*-
"""Ingest PDF equity research into bilingual markdown. See README.md."""
from __future__ import annotations

import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import fitz

from config import ROOT, DIR_BILINGUAL, DIR_EXTRACT_CACHE, DIR_SOURCE

# Extraction only: verbatim page text + an empty bilingual scaffold. Translation
# and summaries are agent-authored (professional retranslation), never free MT;
# image-only / scan sources are transcribed by agent vision.
# See cursor-skills/vd-report-ingest/logic.md.

PDF_DIR = DIR_SOURCE
TEXT_DIR = DIR_BILINGUAL
CACHE_DIR = DIR_EXTRACT_CACHE
META_FILE = CACHE_DIR / "_extraction_manifest.json"


def slugify(name: str, max_len: int = 120) -> str:
    stem = name
    for ext in (".pdf", ".jpg", ".jpeg", ".png", ".webp", ".md"):
        if stem.lower().endswith(ext):
            stem = stem[: -len(ext)]
            break
    # Do not use Path.stem here — titles like "20260623_1.China …" would truncate at the first dot.
    stem = unicodedata.normalize("NFKC", stem)
    stem = re.sub(r"[^\w\s\-\u2014\uFF08\uFF09().,&+]", " ", stem, flags=re.UNICODE)
    stem = re.sub(r"\s+", "-", stem.strip())
    stem = re.sub(r"-+", "-", stem)
    if len(stem) > max_len:
        stem = stem[:max_len].rstrip("-")
    return stem or "report"


def parse_filename(pdf_name: str) -> dict:
    stem = Path(pdf_name).stem
    m_date = re.match(r"^(\d{8})_", stem)
    report_date = m_date.group(1) if m_date else ""
    rest = stem[len(m_date.group(0)) :] if m_date else stem

    source = "Unknown"
    title = rest
    for pat in (
        r"^(K-Research(?:-GOLD)?)",
        r"^(Goldman Sachs)",
        r"^(Morgan Stanley)",
        r"^(J\.P\. Morgan)",
        r"^(Bernstein)",
        r"^(Deutsche Bank)",
        r"^(HSBC)",
        r"^(CITI|Citigroup)",
        r"^(Jefferies)",
    ):
        m = re.match(pat, rest, re.I)
        if m:
            source = m.group(1)
            title = rest[m.end() :].lstrip("-_ ")
            break

    title = title.strip(" -_") or stem
    return {
        "report_date": report_date,
        "source": source,
        "title": title,
        "slug": slugify(stem),
    }


def strip_trailing_page_num(text: str, page: int) -> str:
    lines = text.strip().split("\n")
    while lines and lines[-1].strip() in {str(page), f"- {page}", f"\u2013 {page}"}:
        lines.pop()
    return "\n".join(lines).strip()


def detect_language(text: str) -> str:
    sample = text[:4000]
    cjk = len(re.findall(r"[\u4e00-\u9fff]", sample))
    latin = len(re.findall(r"[A-Za-z]", sample))
    if cjk > max(80, latin * 0.25):
        return "zh"
    return "en"


def extract_pages(pdf_path: Path) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages = []
    for i in range(doc.page_count):
        raw = doc[i].get_text("text")
        pages.append({"page": i + 1, "text": strip_trailing_page_num(raw, i + 1)})
    doc.close()
    return pages


def process_pdf(pdf_path: Path, *, force: bool = False) -> dict:
    file_meta = parse_filename(pdf_path.name)
    base = file_meta["slug"]
    json_path = CACHE_DIR / f"{base}_extracted_pages.json"
    bilingual_path = TEXT_DIR / f"{base}-Bilingual.md"

    if not force and bilingual_path.exists() and json_path.exists():
        pages_n = len(json.loads(json_path.read_text(encoding="utf-8")))
        return {
            "pdf": pdf_path.name,
            "slug": base,
            "pages": pages_n,
            "source_language": "skipped",
            "bilingual_md": bilingual_path.name,
            "status": "skipped",
        }

    pages = extract_pages(pdf_path)
    combined = "\n".join(p["text"] for p in pages)
    src_lang = detect_language(combined)

    json_path.write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8")

    # Bilingual MD: source verbatim; translation via professional retranslation workflow only.
    if not bilingual_path.exists() or force:
        if src_lang == "zh":
            page_rows = [{"page": p["page"], "zh": p["text"], "en": ""} for p in pages]
        else:
            page_rows = [{"page": p["page"], "en": p["text"], "zh": ""} for p in pages]
        doc_meta = {
            "document": file_meta["title"],
            "source": pdf_path.name,
            "issuer": file_meta["source"],
            "report_date": file_meta["report_date"],
            "source_language": src_lang,
            "pages": len(pages),
        }
        from bilingual import build_bilingual_md

        bilingual_path.write_text(
            build_bilingual_md(doc_meta, page_rows, translation_note="pending professional retranslation"),
            encoding="utf-8",
        )

    return {
        "pdf": pdf_path.name,
        "slug": base,
        "pages": len(pages),
        "source_language": src_lang,
        "bilingual_md": bilingual_path.name,
        "json": json_path.name,
    }


def move_pdfs() -> list[Path]:
    PDF_DIR.mkdir(exist_ok=True)
    TEXT_DIR.mkdir(exist_ok=True)
    CACHE_DIR.mkdir(exist_ok=True)
    pdfs = sorted(ROOT.glob("*.pdf"))
    moved: list[Path] = []
    for pdf in pdfs:
        dest = PDF_DIR / pdf.name
        if pdf.resolve() != dest.resolve():
            shutil.move(str(pdf), str(dest))
        moved.append(dest)
    if not moved and PDF_DIR.exists():
        moved = sorted(PDF_DIR.glob("*.pdf"))
    return moved


def main(*, force: bool = False, only: list[str] | None = None) -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    pdfs = move_pdfs()
    if only:
        pdfs = [p for p in pdfs if any(s in p.name for s in only)]
    manifest: list[dict] = []
    total = len(pdfs)
    print(f"Processing {total} PDFs...")
    for i, pdf in enumerate(pdfs, 1):
        print(f"[{i}/{total}] {pdf.name}")
        try:
            info = process_pdf(pdf, force=force)
            if info.get("status") == "skipped":
                manifest.append({**info, "status": "skipped"})
                print(f"  -> skip (exists) {info['slug']}")
            else:
                manifest.append({**info, "status": "ok"})
                print(f"  -> {info['slug']} ({info['pages']} pages, src={info['source_language']})")
        except Exception as exc:  # noqa: BLE001
            # One bad PDF must not abort the batch; record it and move on.
            err = str(exc).encode("ascii", "backslashreplace").decode("ascii")
            manifest.append({"pdf": pdf.name, "status": "error", "error": err})
            print(f"  !! ERROR: {err[:500]}")
    META_FILE.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(1 for m in manifest if m.get("status") == "ok")
    print(f"\nDone: {ok}/{total} succeeded")
    print(f"PDFs -> {PDF_DIR}")
    print(f"Markdown -> {TEXT_DIR}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Reprocess even if outputs exist")
    parser.add_argument("--only", nargs="*", help="Process only PDFs matching substrings")
    args = parser.parse_args()
    main(force=args.force, only=args.only)
