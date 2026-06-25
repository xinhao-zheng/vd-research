# -*- coding: utf-8 -*-
"""Compile per-report summaries into a chronological index. See README.md."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from config import DIR_SUMMARIES, DIR_SYNTHESIS, FILE_ALL_INDEX, PROJECT_NAME

GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_field(text: str, field: str) -> str:
    m = re.search(rf"^{field}:\s*(.+)$", text, re.M)
    if m:
        return m.group(1).strip().strip('"')
    m = re.search(rf"^\*\*{field}\*\*:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def extract_section(text: str, heading: str) -> str:
    pat = rf"##\s*{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pat, text, re.S)
    return m.group(1).strip() if m else ""


def parse_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm: dict[str, str] = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
            text = text[end + 4 :]

    one_line = extract_section(text, "一句话结论")
    if not one_line:
        one_line = extract_section(text, "一句结论")
    insights = extract_section(text, "核心洞见")
    conclusion = extract_section(text, "结论与建议") or extract_section(text, "结论")
    stance = fm.get("stance") or extract_field(text, "stance") or "未标注"
    title = fm.get("title") or path.stem.replace("-Summary", "").replace("-Bilingual-Summary", "")
    date = fm.get("report_date") or path.name[:8]
    issuer = fm.get("issuer") or "未知"
    topics = fm.get("topics", "")

    return {
        "path": path.name,
        "date": date,
        "issuer": issuer,
        "title": title,
        "stance": stance,
        "topics": topics,
        "one_line": one_line.replace("\n", " ").strip(),
        "insights": insights,
        "conclusion": conclusion,
    }


def date_range(items: list[dict]) -> str:
    if not items:
        return "N/A"
    dates = sorted(it["date"] for it in items if it["date"])
    return f"{dates[0]} — {dates[-1]}" if dates else "N/A"


def main() -> None:
    DIR_SYNTHESIS.mkdir(exist_ok=True)
    items = [parse_summary(p) for p in sorted(DIR_SUMMARIES.glob("*-Summary.md"))]
    items.sort(key=lambda x: x["date"])
    dr = date_range(items)

    lines = [
        "---",
        f"document: {PROJECT_NAME} — All Reports Index",
        f"generated_at: {GENERATED_AT}",
        f"reports: {len(items)}",
        f"date_range: {dr}",
        "language: zh-CN",
        "style: structured plain expression — overview first, chronological body",
        "---",
        "",
        f"# {PROJECT_NAME} · 全部研报摘要汇总",
        "",
        f"> **30 秒带走：** 共 **{len(items)}** 份摘要，区间 **{dr}**。第一屏看时间线表；需要细节再往下按日期读单条。",
        "",
        "本索引由 `report-summaries/` 自动编译。每条含：日期、机构、态度、一句话、核心洞见、结论。",
        "",
        "---",
        "",
        "## 1. 时间线速查",
        "",
        "| 日期 | 机构 | 标题 | 态度 |",
        "| --- | --- | --- | --- |",
    ]

    for it in items:
        title_short = it["title"][:50] + ("..." if len(it["title"]) > 50 else "")
        stance_short = it["stance"][:30]
        lines.append(f"| {it['date']} | {it['issuer']} | {title_short} | {stance_short} |")

    lines.extend(["", "---", "", "## 2. 按时间序全文", ""])

    for i, it in enumerate(items, 1):
        lines.extend([
            f"### 2.{i} [{it['date']}] {it['issuer']} — {it['title']}",
            "",
            f"**态度：** {it['stance']}",
            "",
            f"**一句话：** {it['one_line']}",
            "",
        ])
        if it["insights"]:
            lines.append("**核心洞见：**")
            lines.append(it["insights"])
            lines.append("")
        if it["conclusion"]:
            lines.append("**结论：**")
            lines.append(it["conclusion"])
            lines.append("")
        lines.extend(["---", ""])

    lines.extend([
        "",
        f"*Compiled at {GENERATED_AT} from {len(items)} files in `report-summaries/`.*",
        "",
    ])

    FILE_ALL_INDEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {FILE_ALL_INDEX} ({len(items)} reports)")


if __name__ == "__main__":
    main()
