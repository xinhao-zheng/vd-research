---
name: vd-report-ingest
description: >-
  Ingest a new equity-research PDF, markdown, or image into the vd-research
  pipeline — extract pages, build bilingual transcript, professional
  retranslation, and per-report summary. Self-contained: carries its own skill-doc
  voice rules and summary-output rules; no other skill need be loaded. 将新 PDF、
  Markdown 或图片研报入库：分页提取、生成双语文稿、专业重译、单篇白话摘要。
  自洽完整：内含 skill 文档文体与摘要输出文体；无需加载其他 skill。Use when the
  user drops a new report file, asks to 入库/提取/翻译/摘要 a new PDF or image, or
  says "new report arrived" for this research project.
---

# Research Report Ingest · 研报入库

## What this is | 这是什么

In one line: **a fixed causal chain that turns an opaque PDF or image into a
traceable bilingual transcript and a falsifiable summary — each stage producing
a named artifact before the next runs, so downstream work can point to page N
without trusting memory.**
一句话：**一条固定因果链，把不透明 PDF 或图片变为可追溯的双语文稿与可证伪摘要——
每一阶段产出具名工件后才进入下一步，使下游工作可指向第 N 页而无需采信记忆。**

Its opposite is ad-hoc extraction: translate first, structure later, summarize
from a single read-through. That severs the audit chain — synthesis cannot
re-check a claim the transcript never anchored.
它的反面是临时提取：先译后结构、读一遍就写摘要。审计链由此切断——综合研判无法
复核一份从未锚定的主张。

In Vertex Dimension's terms: before the firm can *model, price, and allocate*, the
raw report must first become **traceable text** — making the substrate clean is
this stage's only job.
用 Vertex Dimension 的话说：在能*建模、定价、配置*之前，原始研报须先变成**可追溯的
文本**——把基底做干净，是本阶段唯一的任务。

---

## Style fingerprint | 风格指纹（九项，与 logic.md 九步一一对应）

1. **Closed intake set** — one source file maps to one slug carrying the full
   title (strip only the real extension, never split on an interior dot); a slug
   collapsed to `YYYYMMDD_<n>` or duplicated across `bilingual-transcripts/` /
   `report-summaries/` is a defect found before extraction opens.
   **闭合入库集**——一个源文件对应一个承载完整标题的 slug（只去真实扩展名、
   绝不在内部点号处截断）；被压成 `YYYYMMDD_<n>` 或在 `bilingual-transcripts/`/
   `report-summaries/` 中重复的 slug，是开提之前就能发现的缺陷。
2. **Verbatim before translation** — extract page text first; translation fills
   empty language blocks, never replaces the extract pass.
   **先逐字提取再翻译**——先提取分页文本；翻译填充空语言块，不替代提取步骤。
3. **Page-marker gate** — every body page carries `<!-- PDF Page N -->`; a
   summary claim with no mappable page fails the gate.
   **页标记闸门**——每个正文页带 `<!-- PDF Page N -->`；无法映射页码的摘要主张
   判失败。
4. **Human-grade translation boundary** — published bilingual MD carries
   `translation: professional human-quality retranslation`; raw MT is not a
   shippable final state.
   **人工级翻译边界**——发布的双语 MD 标注 `professional human-quality retranslation`；
   机器直译不是可交付终态。
5. **Summary from anchor only** — `-Summary.md` is written only against a
   completed `*-Bilingual.md`; no summary-from-PDF shortcut.
   **仅锚定写摘要**——`-Summary.md` 只对照完整的 `*-Bilingual.md` 写；禁止
   从 PDF 直写摘要的捷径。
6. **Stance from mechanism** — `stance` follows the causal chain in the body, not
   the headline mood-word alone.
   **立场来自机制**——`stance` 跟随正文因果链，不单跟标题情绪词。
7. **Index last, timestamp fresh** — run `scripts/index.py` after summaries;
   `synthesis/all-reports-index.md` must carry a new `generated_at` UTC.
   **最后索引、时间戳刷新**——摘要完成后运行 `scripts/index.py`；
   `all-reports-index.md` 须带新的 `generated_at` UTC。
8. **Named falsifiers** — each summary closes with one observable that would
   break its one-line conclusion.
   **具名证伪条件**——每份摘要以一条可观察项收束，说明何种情形将推翻一句话结论。
9. **Agent token for interpretive output** — retranslation and `-Summary.md`
   are agent-authored from `*-Bilingual.md`; free Google MT or a third-party OCR
   plugin is not a shippable final state (see [logic.md](logic.md) step 9).
   **解读产出用 agent token**——重译与摘要由 agent 对照双语稿撰写；免费 Google
   机翻或第三方 OCR 插件不是可交付终态（见 [logic.md](logic.md) 第 9 步）。

---

## How to use | 怎么用

**Ingesting fresh** — first read [logic.md](logic.md) for the advance order
(intake → extract → retranslate → summarize → index → falsifier check), then
execute per [style.md](style.md): skill docs in the austere voice; summary files
in the embedded plain-output voice (Voice B in that file).
**新入库**——先读 [logic.md](logic.md) 定推进顺序（接收 → 提取 → 重译 → 摘要 →
索引 → 证伪检验），再依 [style.md](style.md) 执行：skill 文档用冷峻体；摘要文件
用该文件内嵌的白话输出体（Voice B）。

**Repairing a broken chain** — first locate which artifact is missing or thin
(bilingual empty? summary ahead of transcript?), fix upstream per [logic.md](logic.md),
then re-run downstream only.
**修复断裂链**——先定位缺失或稀薄的工件（双语空？摘要早于文稿？），按 [logic.md](logic.md)
修上游，再仅重跑下游。

| File | Role |
|------|------|
| [logic.md](logic.md) | Advance order, gates, paths · 推进顺序、闸门、路径 |
| [style.md](style.md) | Skill-doc voice + summary output voice · skill 文档体 + 摘要输出体 |

---

## One contrast | 一个最小对照

> Before (ad-hoc) — *"I read the PDF and wrote a bullish summary."*
> 原做法——*"我读了一遍 PDF，写了一份看多摘要。"*

> After (this skill) — *Extract → `*-Bilingual.md` → retranslate → `*-Summary.md`
> → index row. Each file is evidence for the next; page N is the address of every
> claim.*
> 改后（本 skill）——*提取 → `*-Bilingual.md` → 重译 → `*-Summary.md` → 索引行。
> 每个文件都是下一步的证据；第 N 页是每条主张的地址。*

The difference is entirely: opinion deferred until the transcript exists; the
chain, not the reader's memory, carries the proof.
差别全在：观点延至文稿存在之后；链条——而非读者记忆——承载证据。
