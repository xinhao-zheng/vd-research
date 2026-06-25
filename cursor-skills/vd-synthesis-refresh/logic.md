# Synthesis Refresh Skeleton · 综合研判刷新推进骨架

The advance order of synthesis refresh. Three modes (A/B/C) share gates 1–2;
modes B and C continue through 3–8. Paths are fixed for vd-research.
本文件给出综合研判刷新的推进顺序。三模式（A/B/C）共享闸门 1–2；B 与 C 延续
3–8。路径固定为本项目约定。

**Prerequisite | 前置：** this skill reads `report-summaries/`, not raw files. New
PDFs/images must first pass `vd-report-ingest` (→ bilingual transcript → summary).
Once the new summaries exist, the user-facing loop is exactly: name the reports
added → run refresh (A: `python scripts/index.py`; B/C: agent rewrite). Nothing
else need be said.
本 skill 读 `report-summaries/`，不读原始文件。新 PDF/图片须先经 `vd-report-ingest`
（→ 双语稿 → 摘要）。新摘要就位后，对用户而言的循环就是：说清加了哪几份 → 刷新
（A：`python scripts/index.py`；B/C：agent 重写）。无需多言。

---

## Order of advance | 推进顺序（默认骨架）

1. **Bound the corpus + stamp the real moment** — before interpretation, fix
   `generated_at`, `reports` / `reports_audited`, and `date_range`. The timestamp
   is the **actual wall-clock UTC at generation** (`date -u +%Y-%m-%dT%H:%M:%SZ`
   or Python `datetime.now(timezone.utc)`), repeated once in the body header
   (`**生成时间（UTC）：**`); never a round placeholder like `12:00:00Z`, never a
   reused old value. The window filename carries the *analysis window*
   (`rolling-window-YYYYMMDD-YYYYMMDD.md`); `generated_at` carries the *moment the
   file was written*. A synthesis without a real timestamp cannot be diffed — and
   diffing across regenerations is why this skill exists.
   **界定语料 + 打真实时刻**——解读之前，固定 `generated_at`、`reports` /
   `reports_audited`、`date_range`。时间戳是**生成时的真实 UTC 墙钟**（用
   `date -u +%Y-%m-%dT%H:%M:%SZ` 或 Python `datetime.now(timezone.utc)`），并在正文
   头部重复一次（`**生成时间（UTC）：**`）；不用 `12:00:00Z` 这类整点占位，也不沿用旧值。
   窗口文件名承载*分析区间*（`rolling-window-YYYYMMDD-YYYYMMDD.md`）；`generated_at`
   承载*文件写下的时刻*。无真实时间戳的综合稿无法 diff——而跨次重生成的 diff 正是
   本 skill 存在的原因。
   - e.g. *`generated_at: 2026-06-23T07:48:22Z`, `reports_audited: 69`,
     `date_range: 20260601 — 20260623`.*
     范例：*`generated_at: 2026-06-23T07:48:22Z`，`reports_audited: 69`，
     `date_range: 20260601 — 20260623`。*

2. **Index before audit (causal, not habitual)** — Mode A runs `scripts/index.py`
   from `report-summaries/`; modes B and C read summaries and optional
   `bilingual-transcripts/` for disputes — never the PDF directly for bulk
   synthesis. Because summaries exist, audit can run; because audit names
   conflicts, rolling window can calibrate probabilities.
   **先索引后审计（因果，非习惯）**——模式 A 从 `report-summaries/` 运行
   `scripts/index.py`；B 与 C 读摘要及必要时 `bilingual-transcripts/` 消歧——
   批量综合不直读 PDF。摘要存在，故审计可运行；审计点名冲突，故滚动窗口可校准概率。
   - Anti-pattern: rewrite audit from last week's memory without re-reading summaries.
     反模式：不重新读摘要，凭上周记忆重写审计。

3. **Overview first** — within the opening 200 words, place a 30-second
   blockquote or one-minute lookup table. A reader who stops at screen one
   still leaves with consensus, new friction, and what to watch.
   **概览先行**——开头 200 字内放 30 秒引用块或一分钟速查表。读者只读第一屏
   仍带走共识、新摩擦、待观察项。
   - Mode A: timeline table + carry-away count.
     模式 A：时间线表 + 条数带走句。
   - Mode B: one-line thesis + theme stance table.
     模式 B：一句话主线 + 主题态度表。
   - Mode C: window lookup table (theme | stance | vs baseline | key number | confidence).
     模式 C：窗口速查表（主题 | 态度 | vs 基线 | 关键数 | 置信度）。

4. **Theme chains, not piles** — sections must answer the previous question:
   what is it → where do reports agree → where do they conflict → who pays →
   what would refute. Test: if two adjacent sections can swap without breaking
   reading, re-sequence until each step depends on the last.
   **主题成链、不成堆**——各节须回答上一节问题：是什么 → 何处一致 → 何处冲突 →
   谁埋单 → 何者证伪。检验：相邻两节对调不影响阅读，则重排至每步依赖上一步。

5. **Conflict as paired claims** — do not write "mixed views on memory"; write
   the pair: *consensus: 2026 structural tightness* vs *dispute: 2027 peak
   timing* with sources and a falsifier each.
   **冲突成对写**——不写"存储看法不一"；写对子：*共识：2026 结构性紧张* vs
   *分歧：2027 顶点时点*，附来源与各自证伪。
   - Each conflict subsection: 一致 → 冲突表 → 审计结论 → 白话建议 → 证伪条件.
     每个冲突小节：一致 → 冲突表 → 审计结论 → 白话建议 → 证伪条件。

6. **Four-part mechanism units, externally triangulated** — for any claim that
   could surprise the reader: **point → mechanism (A → B → C) → number with plain
   source → falsifier**. A number without "why" is an assertion; a verdict without
   "what breaks it" is mood. Then **triangulate**: cross-check every load-bearing
   external number against a live source (web), combining (i) the local corpus,
   (ii) what public reporting says now, and (iii) your own judgment. This is
   non-negotiable when the corpus is self-published (e.g. K-Research) or rests on
   a single sell-side note — a single-source bearish or bullish number that no
   external source corroborates is flagged, not asserted.
   **四件套机制单元，且外部三角验证**——凡可能让读者意外的主张：**要点 → 机制
   （A → B → C）→ 带来处的人话数字 → 证伪**。无"为什么"的数字是断言；无"何者推翻"
   的判定是情绪。随后**三角验证**：把每个承重的外部数字对照在线来源（联网）核对，
   合并 (i) 本地语料、(ii) 当下公开报道、(iii) 你自己的判断。当语料为自有刊物
   （如 K-Research）或仅靠单一卖方时，这一步不可省——无任何外部来源印证的单一信源
   多空数字，应标注为"待核"，而非直接断言。
   - On confirmation: keep the number, add a one-line `**外部核对：**` note naming
     the corroborating outlet(s). On conflict: correct toward the better-sourced
     figure, or present both with the discrepancy named. Mind the caliber — e.g. an
     OEM *system* price hike (~15–20%) is not a *component/spot* figure (+30–60%+);
     correcting that mismatch is the anti-hallucination gate (same as `vd-essay-distill`).
     印证则保留数字，加一行 `**外部核对：**` 点名印证媒体；冲突则向证据更强的一方
     校正，或并列两者并点明差异。注意口径——OEM *整机* 提价（约 15–20%）≠ *组件/现货*
     涨幅（+30–60%+）；纠正这种错配即防幻觉闸门（与 `vd-essay-distill` 同一口径）。

7. **Limitations + working probabilities** — devote explicit space to what this
   synthesis does not do (not investment advice; PDF extraction gaps; single-source
   rumors). BEAR/BASE/BULL blocks sum to 100% per theme, labeled *工作假设，
   非投资建议*.
   **局限 + 工作概率**——专节写明本稿未做什么（非投资建议；PDF 提取缺口；单一信源传闻）。
   BEAR/BASE/BULL 每主题合计 100%，标注*工作假设，非投资建议*。
   - e.g. *"Four observations would disconfirm the BASE case: …"*
     范例：*"四项观察将证伪 BASE 情景：……"*

8. **Aphoristic coda + backstage self-check** — close on one contrastive sentence,
   not a bullet recap. Run the self-check below before shipping; print the
   checklist only for actionable runbooks, not for published audit/window files.
   **格言式收束 + 幕后自检**——以一句对照句收尾，非 bullet 复述。发布前跑下面自检；
   清单仅印可执行手册，不印已发布的审计/窗口稿。
   - ✓ *"Artifacts are frozen; who pays the bill is not — watch Q4 contracts."*
     原件已冻结；谁埋单尚未——盯 Q4 合约。
   - ✗ *"In summary, we discussed memory, power, and packaging."*
     综上，我们讨论了存储、电力与封装。

---

## Mode map | 模式对照

| Step · 步骤 | Mode A · 索引 | Mode B · 审计 | Mode C · 滚动窗口 |
| --- | --- | --- | --- |
| 1 Bound corpus · 界定语料 | ✓ | ✓ | ✓ + `window`, `baseline` |
| 2 Index · 索引 | ✓ (only output) | read index / summaries | read index / summaries |
| 3 Overview · 概览 | timeline table | thesis + theme table | window lookup table |
| 4–5 Chain + conflicts · 链与冲突 | — | §1–§7 theme chain | §2–§4 bull/bear mechanisms |
| 6 Mechanisms · 机制 | — | per conflict | per window claim |
| 7 Limits + probs · 局限与概率 | — | §8 false consensus | §6 BEAR/BASE/BULL |
| 8 Coda · 收束 | footer timestamp | §9 one line | §9 one line |

**Rolling window file rule:** `synthesis/rolling-window-YYYYMMDD-YYYYMMDD.md` —
do not delete prior windows; add new files so `generated_at` diffs remain readable.
**滚动窗口文件规则：** 不删旧窗口；新增文件，使 `generated_at` diff 可读。

**Cross-mode gates · 跨模式闸门:**
- Index `reports:` == audit `reports_audited` == window `total_corpus`.
- Audit §0 one-liner must not contradict window §9 coda without explicit reconciliation.
- File-index tables use English paths only: `source-pdfs/`, `bilingual-transcripts/`, etc.

---

## Self-check | 自检清单

- [ ] Is `generated_at` the real wall-clock UTC (not `12:00:00Z`, not reused) on every touched file, and repeated in the body header? |
      每个改动过的文件，`generated_at` 是否为真实 UTC 墙钟（非 `12:00:00Z`、非沿用旧值），并在正文头重复？
- [ ] Is every load-bearing external number triangulated against a live source, with single-source figures flagged? |
      每个承重外部数字是否对照在线来源三角验证，单一信源数字是否已标注？
- [ ] Does the first screen convey consensus + friction in ~30 seconds? |
      第一屏是否约 30 秒传达共识 + 摩擦？
- [ ] Do sections form a chain, not a swappable pile? |
      各节是否成链、而非可对调顺序的堆？
- [ ] Is every major conflict written as a named pair with a falsifier? |
      每个主要冲突是否写成具名对子并带证伪？
- [ ] Does every surprising claim show A → B → C, not just a verdict? |
      每个意外主张是否给出 A → B → C，而非只甩结论？
- [ ] Are BEAR/BASE/BULL blocks labeled as working assumptions? |
      BEAR/BASE/BULL 是否标注为工作假设？
- [ ] Is there a limitations / false-consensus section (mode B) or objection Q&A (mode C)? |
      是否有局限/假共识节（B）或预判反对（C）？
- [ ] Does the doc close on one contrastive line, not a summary list? |
      是否以一句对照句收束，而非总结列表？
- [ ] Are cross-references by address (`§2.3`, file path), never "见上文"? |
      交叉引用是否用地址（`§2.3`、文件路径），无"见上文"？
- [ ] Do report counts match across index, audit, and window front matter? |
      索引、审计、窗口 front matter 的报告数是否一致？
