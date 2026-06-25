# -*- coding: utf-8 -*-
"""Render a vd-research markdown document to brand LaTeX + PDF. See README.md.

Pipeline: strip YAML front matter, lift the first H1 to a title block, convert
the body with pandoc into a standalone LaTeX file under latex/, then compile it
with XeLaTeX (ctexart, CJK-safe) to a PDF. Translation/prose are never machine
generated here — this stage only typesets text the agent already wrote.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from config import DIR_LATEX, ROOT

HEADER = Path(__file__).resolve().parent / "vd-latex-header.tex"
AUX_EXTS = (".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz")


def split_front_matter(text: str) -> tuple[dict, str]:
    meta: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].split("\n"):
                if ":" in line and not line.lstrip().startswith("-"):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = text[end + 4 :].lstrip("\n")
    return meta, body


def lift_title(body: str) -> tuple[str, str]:
    """Return (title, body-without-that-H1). Falls back to empty title."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            del lines[i]
            return title, "\n".join(lines).lstrip("\n")
    return "", body


def build_date_line(meta: dict) -> str:
    parts: list[str] = []
    if meta.get("window"):
        parts.append(meta["window"])
    elif meta.get("date_range"):
        parts.append(meta["date_range"])
    if meta.get("generated_at"):
        parts.append(f"生成于 {meta['generated_at']}")
    parts.append(meta.get("note", "非投资建议"))
    return " ｜ ".join(parts)


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def slug_of(path: Path) -> str:
    return path.stem


def render(md_path: Path, *, keep_aux: bool = False) -> Path:
    text = md_path.read_text(encoding="utf-8")
    meta, body = split_front_matter(text)
    title, body = lift_title(body)
    if not title:
        title = meta.get("document", md_path.stem)
    date_line = build_date_line(meta)

    DIR_LATEX.mkdir(exist_ok=True)
    slug = slug_of(md_path)
    tex_path = DIR_LATEX / f"{slug}.tex"
    pdf_path = DIR_LATEX / f"{slug}.pdf"

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        body_md = tmp / "body.md"
        meta_yaml = tmp / "meta.yaml"
        body_md.write_text(body, encoding="utf-8")
        meta_yaml.write_text(
            f'---\ntitle: "{yaml_escape(title)}"\ndate: "{yaml_escape(date_line)}"\n---\n',
            encoding="utf-8",
        )
        pandoc_cmd = [
            "pandoc",
            str(body_md),
            f"--metadata-file={meta_yaml}",
            "--standalone",
            "--wrap=preserve",
            "-V", "documentclass=ctexart",
            "-V", "classoption=12pt",
            "-V", "geometry:margin=2.4cm",
            "-H", str(HEADER),
            "-o", str(tex_path),
        ]
        run = subprocess.run(pandoc_cmd, capture_output=True, text=True, encoding="utf-8")
        if run.returncode != 0:
            sys.stderr.write(run.stderr)
            raise SystemExit(f"pandoc failed for {md_path.name}")

    # Compile twice for headers/refs; run from latex/ so figures/ resolves.
    for _ in range(2):
        comp = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{slug}.tex"],
            cwd=DIR_LATEX, capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if comp.returncode != 0:
            log = (DIR_LATEX / f"{slug}.log")
            tail = ""
            if log.exists():
                tail = "\n".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-30:])
            sys.stderr.write(tail + "\n")
            raise SystemExit(f"xelatex failed for {slug}.tex — see {log}")

    if not keep_aux:
        for ext in AUX_EXTS:
            p = DIR_LATEX / f"{slug}{ext}"
            if p.exists():
                p.unlink()

    size_kb = pdf_path.stat().st_size / 1024 if pdf_path.exists() else 0
    print(f"OK  {md_path.name}")
    print(f"  tex -> {tex_path.relative_to(ROOT)}")
    print(f"  pdf -> {pdf_path.relative_to(ROOT)} ({size_kb:.0f} KB)")
    return pdf_path


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Render a vd-research .md to brand LaTeX + PDF")
    parser.add_argument("inputs", nargs="+", help="markdown file(s): essay, synthesis, summary")
    parser.add_argument("--keep-aux", action="store_true", help="keep .aux/.log build files")
    args = parser.parse_args()
    for raw in args.inputs:
        p = Path(raw)
        if not p.is_absolute():
            p = (ROOT / raw).resolve()
        if not p.exists():
            raise SystemExit(f"not found: {raw}")
        render(p, keep_aux=args.keep_aux)


if __name__ == "__main__":
    main()
