# Language: Skill Doc + LaTeX Output · 语言风格：Skill 文档 + LaTeX 输出

Two voices live in this file — separated by artifact type, both self-contained.
本文件内嵌两种声音——按产出类型区分，均自洽，不依赖其他 skill 文件。

---

## Voice A — Skill documentation (SKILL.md, logic.md, this file's meta sections) | Skill 文档

The austere analytical voice — same execution rules as the sibling skills in this
repository: zero filler, load-bearing verbs, em-dash qualification, short sentence
stress, honesty over rhetoric. Most rules carry ✓ and ✗.
冷峻思辨学术体——与本仓库 sibling skill 同一执行规则：零套话、承重动词、破折号限定、
短句重音、诚实压过修辞。多数规则配 ✓ 与 ✗。

### Diction | 用词

1. **Zero filler.** Cut "powerful / one-click / beautifully rendered". Name the
   engine, the gate, the artifact path.
   **零套话。** 删"强大／一键／精美渲染"。写引擎、闸门、工件路径。
   - ✗ *This skill beautifully renders your document into a stunning PDF.*
     本 skill 将文档精美渲染为惊艳 PDF。
   - ✓ *pandoc → `latex/<slug>.tex` → XeLaTeX → `latex/<slug>.pdf`; aux cleaned.*
     pandoc → `.tex` → XeLaTeX → `.pdf`；aux 已清。

2. **Verbs:** typeset, compile, map, route, gate — not "make / generate / handle".
   **动词：** typeset、compile、map、route、gate——而非 make/generate/handle。

3. **Define paths on first use** — always English directory names: `latex/`,
   `figures/`, `scripts/render_pdf.py`.
   **路径首次出现即定义**——一律英文目录名：`latex/`、`figures/`、`scripts/render_pdf.py`。

### One-pass clean (skill docs) | 一键清洗（skill 文档）

1. Delete filler and mood-adjectives. | 删套话与情绪形容词。
2. Swap "renders nicely" for "what breaks if the engine is wrong". | 把"渲染得好"换成"引擎错了会怎样"。
3. Check every paragraph advances by cause, not parallel feature bullets. | 检查段落因果推进，而非并列功能 bullet。

---

## Voice B — LaTeX output (`latex/*.tex` → `*.pdf`) | LaTeX 排版输出

Not a prose voice but a **typesetting voice** — the rules that give every PDF the
same austere, monochrome, Vertex Dimension form. Rules embedded here; **the `.tex`
and `.pdf` never name a skill, never carry build chatter.** The brand ethos:
restraint as premium ("能删就删"), pure black on white, the form serves the text.
不是行文声音，而是**排版声音**——让每份 PDF 拥有同一种冷峻、纯黑白、Vertex Dimension
形态的规则。规则内嵌于此；**`.tex` 与 `.pdf` 绝不点名任何 skill、不夹带构建絮语。**
品牌内核：克制即高级（"能删就删"）、纯黑白、形式服务于文本。

### Document class & engine | 文档类与引擎

1. **`ctexart` on XeLaTeX — non-negotiable for CJK.** The body is Chinese; the
   class must set it without dropped glyphs. `pdflatex` is not an option.
   **`ctexart` + XeLaTeX——中文不可让步。** 正文是中文；文档类须无掉字地排出。`pdflatex`
   不在选项内。

2. **Symbols the Latin font lacks route to math glyphs** — `→ ← ↑ ↓ × ≈ ≥ ≤` via
   `\newunicodechar`, so an arrow never renders as a blank box.
   **拉丁字体缺失的符号路由到数学字形**——`→ ← ↑ ↓ × ≈ ≥ ≤` 经 `\newunicodechar`，
   箭头绝不渲染成空方框。

### Page & color | 版面与色彩

3. **Pure black on white — zero color, zero ornament.** Color is an emotion tool;
   refusing it is the brand. No shading, no boxes, no rules except the title rule
   and the thin head rule.
   **纯黑白——零彩色、零纹饰。** 色彩是情绪工具；拒绝它即品牌。无底纹、无边框，除标题线与
   页眉细线外不画线。
   - ✗ colored section headers, highlight boxes, link colors. · 彩色标题、高亮框、彩色链接。
   - ✓ one ink, weight and whitespace carry the hierarchy. · 一种墨色，靠字重与留白承载层级。

4. **Generous margins, modest leading, no-indent paragraphs.** Whitespace is the
   premium; the page breathes.
   **宽页边、适中行距、段落不缩进。** 留白即高级；版面要透气。

5. **Running head = the wordmark.** `VERTEX DIMENSION` small-caps left, page number
   right, a 0.4pt rule beneath — the only standing mark on every page.
   **页眉＝字标。** `VERTEX DIMENSION` 小型大写居左、页码居右、下置 0.4pt 细线——每页唯一的
   常驻标记。

### Title block & structure | 标题块与结构

6. **Title block from the source, not invented** — the first H1 is the title; a
   thin rule beneath it; one italic small-caps date line (`window ｜ 生成于
   generated_at ｜ 非投资建议`). No subtitle the source did not write.
   **标题块取自源、非臆造**——首个 H1 为标题；下一道细线；一行斜体小号日期
   （`窗口 ｜ 生成于 generated_at ｜ 非投资建议`）。不加源文未写的副标题。

7. **Section numbering off; the body's own "一、二、三" stands.** The skeleton is
   the source's; typesetting reflects it, never re-numbers it.
   **关闭章节编号；正文自带的"一、二、三"成立。** 骨架属于源文；排版反映它，绝不重新编号。

8. **Tables: `booktabs`, no vertical rules.** Parallel/contrast data only; a wide
   table drops to `\small` rather than overflowing the text block.
   **表格：`booktabs`、无竖线。** 仅并列/对比数据；过宽表降 `\small`，不溢出版心。

### Figures | 配图

9. **Figures resolve from `figures/` via `\graphicspath`** — reference by filename;
   caption in the document's language; never embed a figure the source does not call.
   **配图经 `\graphicspath` 从 `figures/` 解析**——按文件名引用；图注用文档语言；绝不嵌入
   源文未引用的图。

### Close | 收束

10. **No emoji, no clickbait, `非投资建议` preserved.** The PDF inherits the
    source's note; the typesetting adds restraint, never volume.
    **无 emoji、无标题党、保留 `非投资建议`。** PDF 继承源文标注；排版只添克制，不添音量。

### One-pass clean (LaTeX output) | 一键清洗（LaTeX 输出）

1. Confirm `ctexart` + XeLaTeX; no `pdflatex`. | 确认 `ctexart` + XeLaTeX；无 `pdflatex`。
2. Strip color and every rule except title + head. | 去彩色与除标题/页眉外的所有线。
3. Map any missing symbol to a math glyph. | 缺失符号映射为数学字形。
4. Confirm no double section numbering. | 确认无重复章节编号。
5. Clean aux; leave only `.tex` + `.pdf`. | 清 aux；仅留 `.tex` + `.pdf`。

---

## Naming & code | 命名与代码

| Artifact · 工件 | Pattern · 模式 |
| --- | --- |
| Source · 源 | `public-essays/…md` · `synthesis/…md` · `report-summaries/…md` |
| LaTeX · 源码 | `latex/<slug>.tex` |
| PDF · 成品 | `latex/<slug>.pdf` |
| Figure · 配图 | `figures/YYYYMMDD_<topic>-<n>.png` |

Python comments: English only; module docstring points to project `README.md`.
The brand header lives at `scripts/vd-latex-header.tex` (pandoc include-in-header).
Python 注释：仅英文；模块 docstring 指向项目 `README.md`。品牌头位于
`scripts/vd-latex-header.tex`（pandoc include-in-header）。

---

## Toolchain (reference) | 工具链（参考）

```
pandoc 3.x  +  TeX Live (XeLaTeX, ctexart)  →  brand .tex  →  .pdf
fonts: ctexart auto-detects a CJK set (Windows: SimSun/SimHei; portable: Fandol)
```
