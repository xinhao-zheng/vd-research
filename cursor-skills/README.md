# cursor-skills

A collection of Cursor Agent Skills, centered on writing. Each skill is a
self-contained folder defined by two things — its **argument logic** (how the
reasoning advances) and its **language style** (how each sentence reads); Cursor
loads it only when the skill's `description` matches the task. The repository is
flat: skills are added as sibling folders, not nested.
Cursor Agent Skills 集合，以写作为主。每个 skill 由两件事定义——**论证逻辑**
（论证如何推进）与**语言风格**（每句如何读起来）；仅当 skill 的 `description`
命中任务时，Cursor 才加载它。仓库保持扁平：skill 以同级文件夹新增，不嵌套。

---

## Skills | 技能


| Skill                                                         | Purpose                                                                          | Status       |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------ |
| [`austere-analytical-prose`](austere-analytical-prose/SKILL.md)       | An austere, analytical voice for papers and technical arguments · 论文与技术论证的冷峻思辨文体 | active · 已发布 |
| [`citation-integrity-audit`](citation-integrity-audit/SKILL.md)       | A re-checkable provenance ledger for a paper's citations · 论文引用的可复核溯源台账         | active · 已发布 |
| [`structured-plain-expression`](structured-plain-expression/SKILL.md) | A structured, plain-language voice for long-form documents — plain words over jargon · 长文档的结构化白话文体，说人话、不甩术语 | active · 已发布 |
| [`vd-report-ingest`](vd-report-ingest/SKILL.md) | Ingest new PDF/MD/image → bilingual transcript + summary · 新研报入库：提取、双语、摘要 | active · 已发布 |
| [`vd-synthesis-refresh`](vd-synthesis-refresh/SKILL.md) | Rebuild index, cross-report audit, or rolling window · 刷新索引、冲突审计或滚动窗口 | active · 已发布 |
| [`vd-essay-distill`](vd-essay-distill/SKILL.md) | Distill a chosen synthesis scope into a public-account essay · 综合研判转公众号文稿 | active · 已发布 |
| [`vd-latex-render`](vd-latex-render/SKILL.md) | Typeset a chosen document into brand LaTeX + PDF · 把文稿排成品牌 LaTeX + PDF | active · 已发布 |

Each of the seven skills is **self-contained**: its `SKILL.md`, `logic.md`, and `style.md`
carry every rule needed to execute that task. No other skill file need be loaded.
Every skill's documentation is written in one voice — the austere-analytical-prose
discipline (narrow claim → causal advance → evidence → falsifiability → aphoristic
coda; each skill's fingerprints mapped one-to-one onto its logic steps), so the whole
folder reads as one author; only the task differs.
七个 skill 均**自洽**：其 `SKILL.md`、`logic.md`、`style.md` 含执行该任务所需的全部规则，
无需加载其他 skill 文件。每个 skill 的文档共用一种声音——冷峻思辨学术体的纪律（收窄主张 →
因果推进 → 证据 → 可证伪 → 格言收束；每个 skill 的指纹与其 logic 步一一对应），故整座文件夹
读如一人之手；只是任务不同。

The four `vd-*` skills are **Vertex Dimension's research workflow** (ingest →
synthesis → essay → render). They embed two voices in `style.md` — **Voice A**
(austere, for the skill docs) and **Voice B** (the deliverable: structured plain for
`report-summaries/` and `synthesis/`, the austere-but-public, brand-aligned essay
voice for `public-essays/`, and the austere monochrome typesetting voice for the
`latex/` PDF) — and carry the brand ethos consistently (*traceable text*; *let the
better answer win, not the louder one*; restraint as premium), without naming
sibling skills in deliverable files.
四个 `vd-*` skill 是 **Vertex Dimension 的研报工作流**（入库 → 综合研判 → 文稿 → 排版）。
它们在 `style.md` 内嵌两种声音——**Voice A**（冷峻，用于 skill 文档）与 **Voice B**（交付物：
`report-summaries/`、`synthesis/` 用结构化白话，`public-essays/` 用冷峻但面向公众、契合
品牌的文稿体，`latex/` PDF 用冷峻纯黑白的排版体）——并一致承载品牌内核（*可追溯的文本*；
*让更好的答案胜出、而非更响的那个*；克制即高级），且交付物中不点名 sibling skill。


---

## Layout | 目录

Every skill folder has the same shape:
每个 skill 文件夹同构：

```
<skill>/
├── SKILL.md   # entry: name + description + overview · 入口
├── logic.md   # the logic layer — argument / structure · 逻辑层（论证／结构）
└── style.md   # the language layer · 语言层
```


| Path               | Role                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------ |
| `<skill>/SKILL.md` | Entry Cursor loads; carries `name` + `description` · Cursor 加载的入口；含 `name` 与 `description` |
| `<skill>/*.md`     | Optional detail, read on demand · 可选细节，按需读取                                                |


---

## Usage | 使用

A skill is active when its folder sits under a `skills/` directory Cursor reads.
Copy the folder you need:
将某个 skill 的文件夹放入 Cursor 读取的 `skills/` 目录，即生效。复制所需文件夹：

```bash
# project scope · 项目级（仅当前仓库）
cp -r austere-analytical-prose <project>/.cursor/skills/

# personal scope · 个人级（所有项目）
cp -r austere-analytical-prose ~/.cursor/skills/
```

Cursor then applies the skill automatically when a task matches its
`description`, or when you name it explicitly.
随后 Cursor 会在任务命中其 `description` 时自动应用，或在你显式指名时应用。

---

## Authoring | 新增 skill

Add one folder with a `SKILL.md` whose front matter carries `name` (lowercase,
hyphenated) and a `description` stating what the skill does and when to use it;
keep the body concise and move detail into side files; then add one row to
[Skills](#skills--技能).
新增一个文件夹，内含 `SKILL.md`，其 front matter 含 `name`（小写、连字符）与
`description`（说明做什么、何时用）；正文从简，细节移入子文件；然后在
[技能索引](#skills--技能)加一行。

---

## Documentation convention | 文档约定

Every README and `SKILL.md` here shares one documentation format:
本仓库每个 README 与 `SKILL.md` 共用一套文档格式：

1. Bilingual, English first, paired line by line. · 双语、英文在前、逐句配对。
2. Bilingual section headers `## English | 中文`. · 双语小节标题。
3. Tables or code blocks for any index, mapping, or layout. · 索引、映射、目录用表格或代码块。
4. `---` between sections. · `---` 分节。
5. Fixed lexical sets for graded table columns — declared once at the top, bare
   words only, never emoji, never per-row improvisation. · 表格定级列用固定词面集——
   表首声明一次，裸词承载，不用 emoji，不逐行起意。

This is a documentation format, not a prose style — each skill defines its own
voice (austere, plain, or otherwise).
这是文档格式，不是行文风格——每个 skill 自定义其声音（冷峻、白话或其他）。

---

## Encoding | 编码

UTF-8, no BOM. · UTF-8，无 BOM。

---

## Note | 说明

Each skill is a distilled style guide — a voice encoded as rules, with
domain-neutral examples — not a content generator. It shapes how your own
material reads; it does not supply the material.
每个 skill 是一份蒸馏出的风格指南——把一种声音编码为规则、配以领域中性的范例
——而非内容生成器。它只塑造你自己素材的"读法"，不替你提供素材。