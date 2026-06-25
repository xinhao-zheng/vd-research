---
name: vd-latex-render
description: >-
  Typeset a chosen vd-research document — a public essay, a synthesis file, a
  summary, or any specified markdown — into a professional, brand-aligned LaTeX
  source and compile it to PDF under latex/, CJK-safe via XeLaTeX + ctexart, with
  figures pulled from figures/. The .tex is the audit artifact; the .pdf is its
  compile. Self-contained: carries its own skill-doc voice and LaTeX-output
  typesetting rules; no other skill need be loaded. 把指定的 vd-research 文档——公众
  号文稿、综合研判、摘要，或任意 markdown——排成专业、契合品牌的 LaTeX 源，并在 latex/
  下编译为 PDF：XeLaTeX + ctexart 中文安全，配图取自 figures/。.tex 是审计工件，.pdf 是
  其编译产物。自洽完整：内含 skill 文档文体与 LaTeX 输出排版规则；无需加载其他 skill。
  Use when the user asks to 出 PDF / 做 LaTeX / 排版 / 生成 PDF, typeset an essay or
  synthesis, or render a chosen document to a PDF.
---

# Research LaTeX Render · 文稿 LaTeX 排版

## What this is | 这是什么

In one line: **a deterministic typesetting stage that turns a finished markdown
document into a brand LaTeX source and a compiled PDF — the `.tex` is the audit
artifact, the `.pdf` its compile, both named by slug under `latex/`.**
一句话：**一个确定性的排版阶段，把已完成的 markdown 文档变成品牌 LaTeX 源与编译出的
PDF——`.tex` 是审计工件，`.pdf` 是其编译产物，二者以 slug 命名置于 `latex/`。**

Its opposite is ad-hoc "export to PDF": print-to-PDF from an editor, no source
kept, no brand, no reproducible build. The page looks fine once and cannot be
regenerated or audited.
它的反面是临时"导出 PDF"：从编辑器打印成 PDF，不留源、无品牌、不可复现。看一眼还行，
既不能重生成、也无法审计。

In Vertex Dimension's terms: the analysis is already done — modeled, priced,
allocated. Typesetting is the last mile: it gives a finished judgment the firm's
**monochrome, austere form**, and adds nothing to the argument.
用 Vertex Dimension 的话说：分析已完成——建模、定价、配置。排版是最后一公里：把已成型的
判断赋予本机构**纯黑白、冷峻**的形态，不向论证增添任何东西。

---

## Style fingerprint | 风格指纹（八项，与 logic.md 八步一一对应）

1. **Bound source → one slug** — one markdown input maps to exactly one
   `latex/<slug>.tex` and one `latex/<slug>.pdf`; the slug mirrors the source stem.
   **界定源 → 一 slug**——一个 markdown 输入对应唯一的 `latex/<slug>.tex` 与
   `latex/<slug>.pdf`；slug 沿用源文件 stem。
2. **Engine + CJK gate first** — confirm XeLaTeX with `ctexart` before authoring;
   `pdflatex` cannot set Chinese. A missing engine is a defect found before render.
   **先验引擎与中文闸门**——排版前确认 XeLaTeX + `ctexart`；`pdflatex` 排不了中文。
   缺引擎是开排前就能发现的缺陷。
3. **Front matter → title block** — title is the document's first H1; the date
   line is composed from YAML (`window`/`date_range`, `generated_at`, `note`);
   never invent metadata the source lacks.
   **元数据 → 标题块**——标题取文档首个 H1；日期行由 YAML 组成（`window`/`date_range`、
   `generated_at`、`note`）；绝不臆造源文没有的元数据。
4. **Structure-preserving conversion** — headings, lists, tables, blockquotes,
   bold, em-dash map 1:1 via pandoc; the PDF carries the same skeleton as the md —
   nothing added, nothing dropped, no rewriting of prose.
   **结构保真转换**——标题、列表、表格、引用、粗体、破折号经 pandoc 一比一映射；PDF 与
   md 同骨架——不增、不删、不改写正文。
5. **Austere brand typography** — pure black on white, generous margins, the
   `VERTEX DIMENSION` wordmark in the running head, zero decoration; figures
   resolve from `figures/` via `\graphicspath`.
   **冷峻品牌排版**——纯黑白、宽页边、页眉置 `VERTEX DIMENSION` 字标、零装饰；配图经
   `\graphicspath` 从 `figures/` 解析。
6. **Deterministic compile** — `scripts/render_pdf.py` runs pandoc → `.tex`, then
   XeLaTeX twice (headers/refs), then cleans aux; re-running on unchanged source
   yields the same PDF.
   **确定性编译**——`scripts/render_pdf.py` 跑 pandoc → `.tex`，再 XeLaTeX 两遍
   （页眉/交叉引用），随后清 aux；源未变则重跑产出同一 PDF。
7. **Falsifiable build gate** — success means the PDF exists with pages > 0; a
   failed compile surfaces the last lines of the `.log`, never a silent miss.
   **可证伪的构建闸门**——成功＝PDF 存在且页数 > 0；编译失败则抛出 `.log` 末尾数行，
   绝不静默放过。
8. **Artifact coda, not distribution** — render ends at `latex/<slug>.pdf`;
   publishing (公众号 etc.) is a separate task, out of this skill's scope.
   **工件收束，非分发**——排版止于 `latex/<slug>.pdf`；发布（公众号等）是独立任务，
   不在本 skill 范围。

---

## How to use | 怎么用

**Rendering fresh** — name the document(s) to typeset. Read [logic.md](logic.md)
for the advance order (bound → engine gate → title block → convert → typography →
compile → build gate → coda), then run per [style.md](style.md): skill docs in the
austere voice (Voice A); the LaTeX/PDF artifact follows the typesetting voice
(Voice B). Output to `latex/<slug>.tex` + `latex/<slug>.pdf`.
**新排版**——指明要排的文档。先读 [logic.md](logic.md) 定推进顺序（界定 → 引擎闸门 →
标题块 → 转换 → 排版 → 编译 → 构建闸门 → 收束），再依 [style.md](style.md) 执行：skill
文档用冷峻体（Voice A）；LaTeX/PDF 工件遵循排版体（Voice B）。输出到 `latex/<slug>.tex`
与 `latex/<slug>.pdf`。

**Fixing a broken build** — read the `.log` tail the tool prints, fix the cause
(missing CJK font, an unmapped symbol, a malformed table), then re-render only.
**修复构建失败**——读工具打印的 `.log` 末尾，定位原因（缺中文字体、未映射符号、表格
畸形），再仅重排。

```bash
python scripts/render_pdf.py public-essays/<file>.md   # one document · 单篇
python scripts/render_pdf.py synthesis/*.md            # several · 多篇
```

| File | Role |
|------|------|
| [logic.md](logic.md) | Advance order, document-type variants, build gate · 推进顺序、文档类型变体、构建闸门 |
| [style.md](style.md) | Skill-doc voice + LaTeX-output typesetting voice · skill 文档体 + LaTeX 输出排版体 |

---

## One contrast | 一个最小对照

> Before (export) — *"I opened the markdown in an editor and printed it to PDF."*
> 原做法——*"我在编辑器里打开 markdown，打印成了 PDF。"*

> After (this skill) — *Strip YAML → lift H1 to a title block → pandoc body →
> `latex/<slug>.tex` → XeLaTeX → `latex/<slug>.pdf`. The `.tex` is the source of
> record; the PDF is its compile; both regenerate from one command.*
> 改后（本 skill）——*剥 YAML → 提 H1 为标题块 → pandoc 转正文 → `latex/<slug>.tex` →
> XeLaTeX → `latex/<slug>.pdf`。`.tex` 是定稿源，PDF 是其编译；二者由一条命令重生成。*

The difference is entirely: a reproducible source-to-PDF chain in the firm's form,
not a one-off print that no one can rebuild.
差别全在：一条以本机构形态呈现、可复现的"源到 PDF"链，而非无人能重建的一次性打印。
