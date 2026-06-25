# vd-research

The equity-research workflow at **Vertex Dimension** — a research-distillation
pipeline: drop a PDF, image, or note into one folder, and it descends a fixed
chain of layers — verbatim bilingual transcript, falsifiable summary, timestamped
cross-report synthesis. The corpus grows by addition; the layers do not change.
What the repository stores is traceable text, not a view.
**Vertex Dimension** 的研报工作流——一条提炼流水线：把一份 PDF、图片或纪要放进入口
文件夹，它便沿固定的层级链下沉——逐字双语文稿、可证伪摘要、带时间戳的跨报告综合
研判。语料以"新增"扩张，层级不变。本库储存的是可追溯的文本，而非某个观点。

---

## Thesis | 命题

The hard part of a research archive is not collecting documents — it is keeping
every later claim answerable to an earlier artifact. So each stage emits a named
file before the next reads it, and nothing downstream may assert what an upstream
file does not carry. Add a thousand reports and the guarantee holds unchanged:
any line can be walked back to the page it came from.
研报库真正难的不是收集文档，而是让每一个后续结论都能回答到更早的工件上。于是每个
阶段先产出一份具名文件，下一阶段才读它；下游不得断言上游文件未承载之物。哪怕新增
上千份研报，这条保证不变——任何一句都能回溯到它出自的那一页。

---

## Pipeline | 流水线

Causal order, not habit. Each arrow is a stage; each stage leaves an artifact the
next one is checked against. Skip a stage and the downstream claim floats without
an anchor.
因果顺序，而非习惯。每个箭头是一个阶段；每个阶段留下供下一阶段比对的工件。跳过任一
层，下游主张即失去锚点。

```
source            → verbatim bilingual transcript   (one file per source · 一源一稿)
transcript        → falsifiable per-report summary   (one digest per report · 一报一摘)
summaries         → chronological index              (timestamped · 带时间戳)
index + summaries → cross-report synthesis           (agreement, conflict, falsifier · 一致/冲突/证伪)
synthesis         → public essay                      (on request · 按需)
essay / synthesis → brand LaTeX + PDF                 (on request · 按需排版)
```

Every synthesis and essay artifact carries `generated_at` (UTC ISO-8601), so any
two regenerations of the same scope can be diffed across time.
每份综合研判与文稿都带 `generated_at`（UTC ISO-8601），使同一范围的两次重生成可跨时
diff。

---

## Layout | 目录

```
vd-research/
├── README.md                 # this file · 本文件
├── .gitignore
├── scripts/                  # the pipeline, one module per stage · 流水线，每阶段一模块
│   ├── config.py             # path constants — single source of truth · 路径常量
│   ├── ingest.py             # source → bilingual scaffold · 入库提取
│   ├── bilingual.py          # bilingual-MD builder imported by ingest.py · ingest.py 调用的双语稿构建库
│   ├── index.py              # summaries → timestamped index · 编译带时间戳索引
│   ├── render_pdf.py         # md → brand LaTeX + PDF · 文稿排版为 LaTeX/PDF
│   └── vd-latex-header.tex   # brand typesetting header (pandoc -H) · 品牌排版头
├── source-pdfs/              # inputs · PDFs and images · 输入：PDF/图片
├── bilingual-transcripts/    # *-Bilingual.md — EN/ZH, page-marked · 逐页中英并列
├── report-summaries/         # *-Summary.md — one falsifiable digest each · 单篇可证伪摘要
├── synthesis/                # index + cross-report audit + rolling windows · 综合研判
├── public-essays/            # essays distilled from synthesis · 由综合研判提炼的文稿
├── figures/                  # illustration & chart assets for layout · 配图与图表资产
└── latex/                    # <slug>.tex + <slug>.pdf, compiled artifacts · 排版产物
```

| Path | Role |
|------|------|
| `scripts/` | The pipeline — one module per stage, all paths via `config.py` · 流水线，每阶段一模块 |
| `source-pdfs/` | Inputs, untouched originals · 输入，原件不改 |
| `bilingual-transcripts/` | Verbatim text, EN/ZH, page-marked · 逐字双语、带页标记 |
| `report-summaries/` | One falsifiable digest per report · 每报告一份可证伪摘要 |
| `synthesis/` | Index, conflict audit, rolling windows — all timestamped · 索引、审计、滚动窗口，均带时间戳 |
| `public-essays/` | Synthesis distilled for a public reader · 为公众读者提炼的文稿 |
| `figures/` | Illustration & chart assets, resolved via `\graphicspath` · 配图资产，经 `\graphicspath` 解析 |
| `latex/` | Brand `<slug>.tex` + compiled `<slug>.pdf` · 品牌 LaTeX 源与编译 PDF |

---

## Usage | 用法

Python 3.11+, PyMuPDF (`fitz`); for `render_pdf.py` also pandoc 3.x and a TeX Live
install with XeLaTeX + `ctexart` (CJK). All paths resolve through `scripts/config.py`;
no path is hard-coded in a script. Image-only / scan sources carry no extractable
text — the agent transcribes them by vision (its own token), never a third-party
OCR or free machine translation.
Python 3.11+、PyMuPDF（`fitz`）；`render_pdf.py` 另需 pandoc 3.x 与含 XeLaTeX + `ctexart`
（中文）的 TeX Live。所有路径经 `scripts/config.py` 解析；脚本中不硬编码路径。图片/扫描源
无可提取文本——由 agent 用自身 token 视觉转写，不用第三方 OCR 或免费机翻。

```bash
python scripts/ingest.py --only "<substring>"        # ingest new sources · 入库新材料
python scripts/index.py                               # rebuild the index · 重建索引
python scripts/render_pdf.py public-essays/<file>.md  # typeset to LaTeX + PDF · 排版出 PDF
```

Interpretive stages — retranslation, summary, synthesis, essay — are run by an
agent against the documents, not by a fixed script. Each leaves a timestamped
artifact. Typesetting (`render_pdf.py`) is the one deterministic, script-driven
deliverable stage: it sets finished text in the firm's form and adds nothing to it.
解读性阶段——重译、摘要、综合研判、文稿——由 agent 对文档执行，而非固定脚本驱动；
每一步都留下带时间戳的工件。排版（`render_pdf.py`）是唯一确定性的、脚本驱动的交付阶段：
把已成型的文本赋予本机构的形态，不向其增添任何东西。

---

## Conventions | 约定

The invariants that hold as the corpus grows — the reason a thousand additions
still read as one hand:
语料扩张时不变的约束——也是新增上千份后仍读如一人之手的原因：

- **One source, one slug, one summary** — `YYYYMMDD_<Issuer>-<Topic>`; no duplicate stems. · 一源一 slug 一摘要。
- **Bilingual, English first, page-marked** — every transcript carries `<!-- PDF Page N -->`. · 双语英文在前、带页标记。
- **English directory names; UTC timestamps** — every synthesis and essay output stamps `generated_at`. · 英文目录名；UTC 时间戳。
- **Voice by artifact** — documentation austere and precise; deliverables plain and readable; neither stacks jargon or dumps numbers. · 文体随产物：文档冷峻精确，交付物白话可读，二者皆不堆术语、不罗列数据。
- **Not investment advice** — stance tags carry analysis, not recommendations; verify any line against its transcript before acting. · 非投资建议；行动前以双语文稿逐条核对。

---

## Encoding | 编码

UTF-8, no BOM. · UTF-8，无 BOM。

---

## License | 许可

Code under `scripts/` is MIT. Source PDFs, transcripts, and summaries remain the
property of their original issuers; this repository is a private research
workspace, not a redistribution channel.
`scripts/` 下代码采用 MIT。原始 PDF、文稿与摘要的版权归各自原始发行方；本仓库为
私人研究工作区，非再分发渠道。

---

*Artifacts are frozen; narratives are not. Read the transcript first — the summary is a map, not the terrain. · 原件已冻结，叙事未冻结。先读文稿——摘要是地图，不是地形。*
