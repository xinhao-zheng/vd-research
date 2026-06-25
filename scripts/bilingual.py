# -*- coding: utf-8 -*-
"""Rebuild *-Bilingual.md from per-page EN/ZH JSON cache. See README.md."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from config import DIR_BILINGUAL, DIR_EXTRACT_CACHE

TEXT_DIR = DIR_BILINGUAL
CACHE_DIR = DIR_EXTRACT_CACHE

TODAY = date.today().isoformat()


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in fm_block.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body


def blockquote_body(text: str) -> list[str]:
    lines: list[str] = []
    for para in re.split(r"\n{2,}", text.strip()):
        if not para.strip():
            continue
        lines.append(f"> {para.strip().replace(chr(10), ' ')}")
        lines.append("")
    return lines


def build_bilingual_md(
    meta: dict,
    pages: list[dict],
    *,
    translation_note: str = "professional human-quality retranslation",
    extraction_note: str | None = None,
) -> str:
    title = meta.get("document", "Report")
    issuer = meta.get("issuer", "Unknown")
    report_date = meta.get("report_date", "N/A")
    source = meta.get("source", "")
    src_lang = meta.get("source_language", "")
    pages_n = meta.get("pages", len(pages))

    header: list[str] = [
        "---",
        f"document: {title}",
        f"source: {source}",
        f"issuer: {issuer}",
        f"report_date: {report_date}",
        f"extracted: {TODAY}",
        f"pages: {pages_n}",
        "languages: en, zh-CN",
        f"source_language: {src_lang}",
        f"translation: {translation_note}",
        "extraction_style: equity research - bilingual parallel text with structural markup",
    ]
    if extraction_note:
        header.append(f"extraction: {extraction_note}")
    header += [
        "---",
        "",
        f"# {title}",
        "",
        f"**{issuer}** | Research Report / 研究报告",
        f"Report date / 报告日期: **{report_date}** | {pages_n} pages / 页",
        "",
        "> 本文档按源 PDF 页码分页提取，英文与中文并列对照。",
        "> 原文语言保留提取字面；译文为专业研报译法（非机器直译堆码）。",
        "> Source language verbatim from PDF extract; translation is professional research-grade (not raw MT).",
        "",
        "---",
        "",
        "## Document Metadata / 文档元数据",
        "",
        "| Field / 字段 | Value / 内容 |",
        "| --- | --- |",
        f"| **Issuer / 发行方** | {issuer} |",
        f"| **Title / 标题** | {title} |",
        f"| **Date / 日期** | {report_date} |",
        f"| **Pages / 页数** | {pages_n} |",
        f"| **Source PDF** | {source} |",
        f"| **Source language / 原文语言** | {src_lang} |",
        "",
        "---",
        "",
    ]
    lines = header

    for p in pages:
        n = p["page"]
        en = p.get("en", "").strip() or "*[No EN text / \u65e0\u82f1\u6587\u5185\u5bb9]*"
        zh = p.get("zh", "").strip() or "*[No ZH text / \u65e0\u4e2d\u6587\u5185\u5bb9]*"
        lines.extend([
            f"<!-- PDF Page {n} -->",
            "",
            f"## Page {n} / \u7b2c {n} \u9875",
            "",
            "**EN**",
            "",
        ])
        lines.extend(blockquote_body(en))
        lines.extend(["**ZH**", ""])
        lines.extend(blockquote_body(zh))
        lines.extend(["---", ""])

    lines.extend(["", "## End of Document / \u6587\u6863\u7ed3\u675f", ""])
    return "\n".join(lines)


def json_path_for_bilingual(bf: Path) -> Path:
    stem = bf.name.replace("-Bilingual.md", "")
    return CACHE_DIR / f"{stem}_extracted_pages.json"


def load_meta_from_bilingual(bf: Path) -> dict:
    meta, _ = parse_front_matter(bf.read_text(encoding="utf-8"))
    return meta


def write_bilingual(bf: Path, pages: list[dict], meta: dict | None = None) -> None:
    meta = meta or load_meta_from_bilingual(bf)
    bf.write_text(build_bilingual_md(meta, pages), encoding="utf-8")
