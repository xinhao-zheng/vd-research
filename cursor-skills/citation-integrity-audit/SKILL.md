---
name: citation-integrity-audit
description: >-
  Turns the citations of a paper or report into a re-checkable provenance
  ledger — every reference resolved to a primary source, the load-bearing source
  sentence quoted verbatim and set bilingually against the paper's own wording,
  every row carrying a resolvable link, and three separate verdicts on
  existence, content-match, and placement.
  把论文/报告的引用核验成一张可复核的溯源台账：每条引用回溯到一手来源，把承重的
  被引原文逐字、双语地与论文措辞对照，每行附可解析链接，并就"真实性、内容吻合、
  落点合理"分别给出判定。Use when the user asks to 核查/核实引用·参考文献真实性,
  做被引原文对照, 判断引用是否乱引/合规, verify or fact-check citations or
  references, build a citation / source-comparison table, or vet a bibliography
  before submission.
---

# Citation Integrity Audit · 引证核验与溯源对照

## What this is | 这是什么

In one line: **a way to turn a paper's citations from claims you must trust into
a ledger you can re-check — each reference resolved to a primary source, the
load-bearing sentence quoted verbatim and set bilingually against the paper's
own words, linked, and graded on three separate axes.**
一句话：**一种把论文引用从"只能采信的断言"转为"可复核的台账"的做法——每条引用
回溯到一手来源，把承重原句逐字、双语地与论文措辞并置，附链接，并在三条独立轴上
分级判定。**

Its opposite is the "trust-me" reference list: an entry asserts that a source
exists and supports a point, paraphrased rather than quoted, unlinked, graded by
a single word of praise. The reader must take the citation on faith — which is
the one thing a citation exists to remove.
它的反面是"信我"式参考文献：条目断言某来源存在且支持某点，用转述代替原句、不附
链接、用一个褒义词草草定级。读者只能采信引用——而采信恰是引用本应消除的东西。

---

## Style fingerprint | 风格指纹（八项，与 logic.md 八步一一对应）

1. **Closed citation set** — intersect every in-text key with every bibliography
   entry; an uncited entry (orphan) or a cited-but-absent key (dangling) is a
   defect found before any source is opened.
   **闭合引用集**——把正文每个引用键与文献表每个条目求交；未被引用的条目（孤儿）
   或被引却缺失的键（悬空）是开任何来源之前就能发现的缺陷。
2. **Audit the pair, not the reference** — the unit is (claim-in-text, source),
   pinned to the exact sentence the citation is made to support.
   **核查"对"，而非孤立引用**——单元是"（正文主张，来源）"，钉在该引用被用来支撑
   的那一句上。
3. **Existence gate** — resolve the work to a primary record (author, venue,
   year, pages); what cannot be resolved fails before its content is weighed.
   **存在性闸门**——把作品解析到一手记录（作者、出处、年份、页码）；无法解析者，
   在称量其内容之前即判失败。
4. **Verbatim provenance** — pull the single sentence in the source that bears
   the support, and quote it; a paraphrase removes the reader's power to re-check.
   **逐字溯源**——抽出来源中承载支撑的那一句并逐字引用；转述会剥夺读者复核的能力。
5. **Bilingual confrontation** — set the source sentence (original + translation)
   beside the paper's wording in each language edition, so the match is read,
   not asserted.
   **双语对质**——把被引原句（原文＋译文）与论文各语种版本的措辞并置，让吻合被
   "读出"，而非被"宣称"。
6. **Placement test** — a true, well-matched source filed under the wrong claim
   is still a defect; judge where it sits, not only whether it is real.
   **落点检验**——真实且吻合的来源若挂在错误的主张下，仍是缺陷；判其位置，不只判
   其真伪。
7. **Every row carries a link** — a resolvable pointer to the primary source; an
   audit that cannot itself be re-checked is just another assertion.
   **每行附链接**——指向一手来源的可解析地址；一份自身无法被复核的核查，不过是
   又一句断言。
8. **Graded verdict, named residue** — one verdict per row drawn from a fixed
   lexical set, a named note for every nuance, and a closing line for what stays
   unresolved.
   **分级判定，点名残差**——每行给一个取自固定词面集的判定，每处微妙之处一条点名
   备注，并以一句"尚未解决者"收束。

---

## How to use | 怎么用

**Auditing fresh** — first read [logic.md](logic.md) for the order (close the set
→ locate the pair → resolve existence → extract verbatim → confront bilingually →
test placement → attach link → grade), then render the ledger per
[style.md](style.md).
**新做核查**——先读 [logic.md](logic.md) 定推进顺序（闭合集合 → 定位"对" → 解析
存在 → 逐字摘录 → 双语对质 → 检验落点 → 附链接 → 定级），再依 [style.md](style.md)
落成台账。

**Polishing existing** — first apply [style.md](style.md) to the existing table
(replace every paraphrase with the verbatim sentence, add the missing link to
every row, reduce verdicts to the fixed set), then check [logic.md](logic.md)
for orphans, mis-placement, and a missing "unresolved" note.
**润色旧表**——先按 [style.md](style.md) 处理旧表（把每处转述换成逐字原句、给每行
补缺失的链接、把判定收敛到固定集合），再按 [logic.md](logic.md) 检查孤儿、错位与
缺失的"未解"备注。

| File | Role |
|------|------|
| [logic.md](logic.md) | Audit procedure, order of advance · 核查流程、推进顺序 |
| [style.md](style.md) | Ledger format, diction, verdicts · 台账格式、用词、判定 |

---

## One contrast | 一个最小对照

> Before (trust-me) — *[12] supports our claim that account abstraction enables
> bounded delegation.*
> 原句（信我式）：[12] 支持我们关于账户抽象可实现有界委托的主张。

> After (this skill) — a row carrying: **full title · authors · venue · year ·
> pages**; the **verbatim source sentence + translation**; the **paper's own
> wording in both editions**; a **resolvable link**; and **three verdicts** —
> *exists · matches · well-placed*, or the named gap.
> 改后（本技能）：一行承载——**全名 · 作者 · 出处 · 年份 · 页码**；**逐字被引原句
> ＋译文**；**论文中英双稿各自的措辞**；**可解析链接**；以及**三项判定**——*存在 ·
> 吻合 · 落点正*，或点名其缺口。

The difference is entirely: the reference stops asking to be trusted and starts
inviting a re-check — link, verbatim quote, and a verdict that locates the gap
rather than praises the match.
差别全在：引用不再要求被采信，而开始邀请复核——链接、逐字原句，以及一个"定位
缺口"而非"赞美吻合"的判定。
