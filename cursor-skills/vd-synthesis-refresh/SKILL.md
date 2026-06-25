---
name: vd-synthesis-refresh
description: >-
  Refresh vd-research synthesis outputs — optionally rebuild rolling
  window analysis, recompile all-reports index, or rewrite/polish cross-report
  conflict audit. Self-contained: carries its own skill-doc voice rules and
  synthesis-body output rules; no other skill need be loaded. 刷新综合研判：可选
  重建滚动窗口、重编全量摘要索引、或重写/润色跨报告冲突审计。自洽完整：内含
  skill 文档文体与综合研判正文文体；无需加载其他 skill。Use when the user asks
  to 更新综合研判/滚动窗口/冲突审计/重建索引, refresh synthesis, rolling window,
  cross-report audit, or after a batch of new summaries is complete.
---

# Research Synthesis Refresh · 综合研判刷新

## What this is | 这是什么

In one line: **three optional outputs — index, cross-report audit, rolling
window — each stamped with `generated_at`, each advancing by causal chains and
theme-level conflict pairs, closing on falsifiable checks rather than mood.**
一句话：**三种可选输出——索引、跨报告审计、滚动窗口——均带 `generated_at`，
均以因果链与主题级冲突对推进，以可证伪检验而非情绪收束。**

Its opposite is a one-shot "market recap": themes listed in parallel, conflicts
unnamed, no timestamp, no diff against last week's file — readable once,
unusable twice.
它的反面是一次性"市场回顾"：主题平行罗列、冲突不点名、无时间戳、无法与上周文件
diff——读一遍可以，读第二遍无用。

This is where Vertex Dimension lets **the better answer win, not the louder one**:
conflicts named in pairs, every load-bearing number triangulated against a live
source, probabilities declared as working assumptions — restraint over noise.
这是 Vertex Dimension **让更好的答案胜出、而非更响的那个**之处：冲突成对点名、每个
承重数字对照在线来源三角验证、概率只作工作假设——以克制胜过喧哗。

---

## Style fingerprint | 风格指纹（八项，与 logic.md 八步一一对应）

1. **Bound corpus first** — declare `date_range`, report count, and
   `generated_at` before any interpretive claim.
   **先界定语料**——在任何解读主张之前声明 `date_range`、报告数、`generated_at`。
2. **Index before audit** — chronological index is compiled from summaries;
   interpretive audit reads summaries, not memory.
   **先索引后审计**——时间线索引由摘要编译；解读审计读摘要，不读记忆。
3. **Overview map in 200 words** — first screen is a table or 30-second blockquote;
   80% graspable without scrolling.
   **200 字内概览地图**——第一屏是表或 30 秒引用块；不滚动看懂八成。
4. **Theme chains, not piles** — each section answers the question the previous
   section raised; adjacent sections must not swap order without breaking logic.
   **主题成链、不成堆**——每节回答上一节的问题；相邻节调换顺序逻辑须断裂。
5. **Conflict as pairs** — agreement and disagreement named in tables; each
   conflict row carries a falsifier column or line.
   **冲突成对**——一致与分歧用表点名；每个冲突行带证伪列或证伪句。
6. **Four-part mechanism units, externally triangulated** — non-obvious claims
   run: point → A → B → C → number → what would break it; every load-bearing
   external number is cross-checked against a live source (web) — decisive when
   the corpus is self-published or rests on a single sell-side note.
   **四件套机制单元，且外部三角验证**——非显然主张走：要点 → A → B → C → 数字 →
   何者推翻；每个承重的外部数字都对照在线来源（联网）核对——当语料为自有刊物或
   仅靠单一卖方时尤其必须。
7. **Limitations + working probabilities** — BEAR/BASE/BULL tables labeled
   *工作假设，非投资建议*; name what this synthesis does not do.
   **局限 + 工作概率**——BEAR/BASE/BULL 表标注*工作假设，非投资建议*；写明本稿未做什么。
8. **Aphoristic coda** — close on one contrastive sentence; self-check runs
   backstage unless the doc is an actionable runbook.
   **格言式收束**——以一句对照句收尾；自检在幕后跑，除非文档本身是可执行手册。

---

## How to use | 怎么用

**Refreshing fresh** — state which mode(s): A (index), B (audit), C (rolling
window). Read [logic.md](logic.md) for advance order, then write per
[style.md](style.md): skill docs in Voice A; `synthesis/*.md` body in Voice B.
**新刷新**——声明模式：A（索引）、B（审计）、C（滚动窗口）。先读 [logic.md](logic.md)
定顺序，再依 [style.md](style.md) 写：skill 文档用 Voice A；`synthesis/*.md`
正文用 Voice B。

**Polishing existing synthesis** — first apply Voice B habits (overview, mechanism
chains, table recaps), then check chain logic per [logic.md](logic.md) for
missing falsifiers or timestamp drift.
**润色已有综合稿**——先套 Voice B 习惯（概览、机制链、表后收束），再按 [logic.md](logic.md)
检查是否缺证伪或时间戳过期。

| Mode · 模式 | Action · 动作 | Output · 输出 |
| --- | --- | --- |
| A · 索引 | `python scripts/index.py` | `synthesis/all-reports-index.md` |
| B · 审计 | Agent rewrite | `synthesis/cross-report-audit.md` |
| C · 滚动窗口 | Agent rewrite | `synthesis/rolling-window-YYYYMMDD-YYYYMMDD.md` |

| File | Role |
|------|------|
| [logic.md](logic.md) | Modes, advance order, cross-mode gates · 模式、推进顺序、跨模式闸门 |
| [style.md](style.md) | Skill-doc voice + synthesis output voice · skill 文档体 + 综合正文体 |

---

## Window spans | 窗口跨度（Mode C）

Mode C is span-agnostic: the date range in the filename *is* the window — a single
day, 2 days, 7 days, or any n days. Files are added, never overwritten, so
`generated_at` diffs across spans stay readable.
模式 C 与跨度无关：文件名里的日期区间*即*窗口——单日、2 日、7 日，或任意 n 日。
文件只增不覆盖，使跨跨度的 `generated_at` diff 可读。

| Span · 跨度 | Filename · 文件名 | e.g. · 例 |
| --- | --- | --- |
| 1-day · 单日 | `rolling-window-YYYYMMDD-YYYYMMDD.md` (same date · 同日) | 当日新增的研判 |
| n-day · n 日 | `rolling-window-YYYYMMDD-YYYYMMDD.md` | 最近 2 日 / 7 日 |
| Month-to-date · 月初至今 | `rolling-window-YYYYMM01-YYYYMMDD.md` | 6/1 — now |

A wider span calibrates against more baselines, not a longer list — same conflict
chains, more triangulation points.
跨度越宽，对照的基线越多，而非清单越长——同一组冲突链，更多三角验证点。

---

## One contrast | 一个最小对照

> Before (recap) — *"Memory bullish, power bullish, buy everything AI."*
> 原句（回顾体）——*"存储看多、电力看多、AI 全买。"*

> After (this skill) — overview table first, then: *"2026 DRAM tightness is
> cross-report consensus; the dispute is who pays in 2027 — watch Q4 contract
> prints. Falsifier: negative QoQ in 2026Q4."*
> 改后（本 skill）——先概览表，再：*"2026 DRAM 紧张是跨报告共识；分歧在 2027 谁埋单——
> 盯 Q4 合约价。证伪：2026Q4 QoQ 转负。"*

The difference is entirely: parallel mood replaced by chained mechanism, conflict,
and a named refutation.
差别全在：平行情绪换成链式机制、冲突与具名反驳。
