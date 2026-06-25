# LaTeX Render Skeleton · 排版推进骨架

The advance order for typesetting one markdown document into brand LaTeX + PDF.
The skeleton is field-independent; the path names are fixed for vd-research.
本文件给出"把单份 markdown 排成品牌 LaTeX + PDF"的推进顺序。骨架与领域无关；路径名
固定为 vd-research 约定。

**Prerequisite | 前置：** this skill typesets a **finished** document — prose the
agent already wrote and (for essays) cross-validated. It adds no analysis; it sets
existing text in type. Source documents live under `public-essays/`, `synthesis/`,
or `report-summaries/`.
本 skill 排版**已完成**的文档——agent 已写就、（文稿则）已交叉验证的正文。它不增添分析；
只把既有文本排版。源文档位于 `public-essays/`、`synthesis/` 或 `report-summaries/`。

---

## Order of advance | 推进顺序（默认骨架）

1. **Bound the source → one slug** — one markdown input maps to exactly one
   `latex/<slug>.tex` and one `latex/<slug>.pdf`; the slug is the source stem. A
   second render of the same source overwrites in place, never forks a name.
   **界定源 → 一 slug**——一个 markdown 输入对应唯一的 `latex/<slug>.tex` 与
   `latex/<slug>.pdf`；slug 即源文件 stem。对同一源二次排版就地覆盖，不另起名字。
   - e.g. *`public-essays/20260623_who-pays.md` → `latex/20260623_who-pays.{tex,pdf}`.*
     范例：*同名 stem，一源一对工件。*

2. **Engine + CJK gate first** — the substrate problem is not "we lack a PDF" but
   "the engine must set Chinese": confirm XeLaTeX and `ctexart` before authoring.
   `pdflatex` cannot render CJK; a missing engine or font is correctable before render.
   **先验引擎与中文闸门**——基底问题不是"缺 PDF"，而是"引擎须能排中文"：排版前确认
   XeLaTeX 与 `ctexart`。`pdflatex` 排不了中文；缺引擎或字体在开排前即可修正。
   - Anti-pattern: compile with `pdflatex`, then patch boxes where Chinese dropped out.
     反模式：用 `pdflatex` 编译，再去补中文掉字的方框。

3. **Front matter → title block** — strip the YAML; lift the document's first H1
   to the title; compose the date line from YAML (`window`/`date_range`,
   `generated_at`, `note`). Map only what the source carries — never invent a
   number, a date, or an author.
   **元数据 → 标题块**——剥掉 YAML；把文档首个 H1 提为标题；日期行由 YAML 组成
   （`window`/`date_range`、`generated_at`、`note`）。只映射源文承载之物——绝不臆造
   数字、日期或作者。

4. **Structure-preserving conversion** — pandoc maps headings, lists, tables,
   blockquotes, bold, em-dash 1:1 into LaTeX. The PDF carries the same skeleton as
   the markdown: nothing added, nothing dropped, prose never rewritten. Section
   numbering stays off — bodies that already read "一、二、三" must not gain a
   second machine number.
   **结构保真转换**——pandoc 把标题、列表、表格、引用、粗体、破折号一比一映射为 LaTeX。
   PDF 与 markdown 同骨架：不增、不删、不改写正文。章节编号关闭——正文已写"一、二、三"者
   不得再叠加机器编号。

5. **Austere brand typography** — pure black on white; generous margins; the
   `VERTEX DIMENSION` wordmark in the running head; a thin rule under the title;
   no-indent paragraphs with modest leading; zero color, zero ornament. Figures
   resolve from `figures/` via `\graphicspath`; symbols the Latin font lacks
   (→ × ≈ ≥ ≤ ↑ ↓) are routed to math glyphs so nothing drops.
   **冷峻品牌排版**——纯黑白；宽页边；页眉置 `VERTEX DIMENSION` 字标；标题下一道细线；
   段落不缩进、行距适中；零彩色、零纹饰。配图经 `\graphicspath` 从 `figures/` 解析；
   拉丁字体缺失的符号（→ × ≈ ≥ ≤ ↑ ↓）路由到数学字形，确保不掉字。

6. **Deterministic compile** — `scripts/render_pdf.py` runs pandoc → `.tex`, then
   XeLaTeX twice from inside `latex/` (so `figures/` resolves and the running head
   settles), then deletes aux files (`.aux .log .out .toc .fls …`). Re-running on
   an unchanged source yields the same PDF.
   **确定性编译**——`scripts/render_pdf.py` 跑 pandoc → `.tex`，再在 `latex/` 内
   XeLaTeX 两遍（使 `figures/` 解析、页眉稳定），随后删除 aux 文件。源未变则重跑产出
   同一 PDF。

7. **Falsifiable build gate** — success is observable: the `.pdf` exists with
   pages > 0. A failed compile prints the last ~30 lines of the `.log` and stops;
   a render is never reported done on a missing or zero-page PDF.
   **可证伪的构建闸门**——成功可观测：`.pdf` 存在且页数 > 0。编译失败则打印 `.log`
   末约 30 行并停止；绝不在缺失或零页 PDF 上报告完成。
   - e.g. *"If `xelatex` returns non-zero, surface the log tail; do not emit a partial PDF."*
     范例：*"若 `xelatex` 返回非零，抛出 log 末尾；不产出半成品 PDF。"*

8. **Artifact coda, not distribution** — render ends at `latex/<slug>.pdf` plus
   its `.tex`. Publishing, image sourcing, or posting to a public account is a
   separate task — run only when the user asks.
   **工件收束，非分发**——排版止于 `latex/<slug>.pdf` 及其 `.tex`。发布、配图采集、
   投放公众号是独立任务——仅在用户要求时运行。

---

## Document-type variants | 文档类型变体

The chain order does not change; only the source shape differs.
链条顺序不变——仅源文形态不同。

| Source · 源 | Title · 标题 | Body shape · 正文形态 |
|------|------|------|
| `public-essays/*.md` | first H1 | narrative prose, em-dash rhythm · 叙事散文 |
| `synthesis/*.md` | first H1 | tables + chained sections + BEAR/BASE/BULL · 表 + 链式节 |
| `report-summaries/*.md` | first H1 (`摘要：…`) | one-line conclusion + bullets · 一句话结论 + bullet |

Tables (synthesis) rely on pandoc's `booktabs`/`longtable` output; wide tables get
`\small`. Long essays paginate; the running head repeats the wordmark on each page.
表格（综合研判）依赖 pandoc 的 `booktabs`/`longtable` 输出；过宽表降为 `\small`。
长文稿自动分页；页眉每页重复字标。

---

## Self-check | 自检清单

- [ ] One source → one `latex/<slug>.tex` and one `latex/<slug>.pdf` (slug = stem)? |
      一源 → 一 `latex/<slug>.tex` 与一 `latex/<slug>.pdf`（slug = stem）？
- [ ] Compiled with XeLaTeX + ctexart (not pdflatex), CJK rendered, no dropped glyphs? |
      是否用 XeLaTeX + ctexart（非 pdflatex）编译，中文正常、无掉字？
- [ ] Title from the first H1, date line from YAML — no invented metadata? |
      标题取首个 H1、日期行来自 YAML——无臆造元数据？
- [ ] Does the PDF carry the same skeleton as the md (nothing added or dropped, prose unaltered)? |
      PDF 是否与 md 同骨架（不增不删、正文未改）？
- [ ] No double section numbering when the body already reads "一、二、三"? |
      正文已是"一、二、三"时是否无重复章节编号？
- [ ] Monochrome, wordmark head, figures from `figures/` — brand typography held? |
      纯黑白、字标页眉、配图取自 `figures/`——品牌排版是否守住？
- [ ] Were aux files cleaned, leaving only `.tex` + `.pdf` in `latex/`? |
      aux 是否已清，`latex/` 仅余 `.tex` + `.pdf`？
- [ ] On failure, was the `.log` tail surfaced rather than a partial PDF shipped? |
      失败时是否抛出 `.log` 末尾，而非交付半成品 PDF？
