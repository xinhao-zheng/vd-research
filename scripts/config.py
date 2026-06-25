# -*- coding: utf-8 -*-
"""Path constants for vd-research (Vertex Dimension). See README.md."""
from __future__ import annotations

from pathlib import Path

# config.py lives in scripts/; the corpus dirs sit one level up, at the repo root.
ROOT = Path(__file__).resolve().parent.parent

DIR_SOURCE = ROOT / "source-pdfs"
DIR_BILINGUAL = ROOT / "bilingual-transcripts"
DIR_SUMMARIES = ROOT / "report-summaries"
DIR_SYNTHESIS = ROOT / "synthesis"
DIR_PUBLIC_ESSAYS = ROOT / "public-essays"
DIR_FIGURES = ROOT / "figures"
DIR_LATEX = ROOT / "latex"
DIR_EXTRACT_CACHE = ROOT / ".extract-cache"

FILE_ALL_INDEX = DIR_SYNTHESIS / "all-reports-index.md"
FILE_CROSS_AUDIT = DIR_SYNTHESIS / "cross-report-audit.md"
FILE_ROLLING_PREFIX = "rolling-window-"

PROJECT_NAME = "vd-research"
REPO_SLUG = "vd-research"
