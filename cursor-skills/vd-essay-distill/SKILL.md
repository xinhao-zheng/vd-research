---
name: vd-essay-distill
description: >-
  Distill a user-chosen slice of synthesis — one file, several, an n-day rolling
  window, a month-to-date span, or a named topic — into a public-account essay in
  Vertex Dimension's research voice: austere-aligned and precise yet told as a
  story, stating insights as the firm's own analysis (reports cited as evidence,
  never narrated), advancing by causal inference to a clear, defended viewpoint,
  naming the conflicts, and citing each number with its real source cross-validated
  against live sources (anti-hallucination) — not a dump of tables, not chatty. A
  general method, not a fixed report: the reader picks the scope, and a wider scope
  earns a deeper essay under one thesis. Self-contained — carries its own skill-doc
  voice and essay-output voice; no other skill need be loaded. 把用户指定的综合研判
  切片——单份、多份、某个 n 天滚动窗口、月初至今、或某个主题——以 Vertex Dimension
  的研究声音提炼为公众号文稿：向冷峻体对齐、精准却以故事讲出，把洞见作为本机构分析陈述
  （研报作引用证据、不复述），以因果推进到清晰有据的观点，点名矛盾、每个数字都带真实
  出处并对照在线来源交叉验证（防幻觉）——不堆表格、不闲聊。通用方法而非固定报表：范围由
  读者指定，范围越宽、越在同一主线下写得越深。
  自洽完整——内含 skill 文档文体与文稿文体，无需加载其他 skill。Use when the user asks
  to 写公众号/发表稿/把综合研判改成文章/提炼成稿/月初至今的稿, draft a public essay,
  or turn a named synthesis scope (a window, a file, a month-to-date span, a theme)
  into a readable post.

---

# Research Essay Distill · 综合研判转公众号文稿

## What this is | 这是什么

In one line: **a general method for projecting a chosen slice of synthesis onto
one page a non-specialist finishes — the reader sets the scope (a file, a window,
a theme), and the essay opens on one claim, advances by cause to a defended view,
spends numbers sparingly, and closes on one sharp line.**
一句话：**一种把指定的综合研判切片投影成"外行能读完的一页"的通用方法——范围由读者
设定（一份文件、一个窗口、一个主题），文稿开篇一条主张，以因果推进到有据的观点，
数字用得克制，并以一句锋利的话收束。**

Its register is **austere-aligned and precise, told as a story** — it takes the
austere-analytical-prose voice (one narrow falsifiable claim, causal advance, a
binary spine, an honest limit, an aphoristic coda) and keeps its discipline:
load-bearing words, em-dash rhythm, no filler. It is neither academic-cold (it
flows and carries the reader) nor colloquial (no chatty fillers, no hype). It
cites specific numbers with their real basis and names the conflicts — readable,
but precise.
它的调性是**向冷峻体对齐、精准，却以故事讲出**——取冷峻思辨学术体（收窄且可证伪的
主张、因果推进、二分脊柱、诚实局限、格言收束），并保留其纪律：承重用词、破折号节奏、
零套话。它既不学术冷峻（要流动、带读者走），也不口语（无闲笔、无炒作）。它给出带真实
依据的具体数字、并点名矛盾——可读，但精准。

It is **Vertex Dimension's research voice** — the firm whose work is to *model,
price, and allocate* what a civilization runs on, that writes reality as equations
and lets the equations decide. Restraint is premium ("能删就删"); the better answer
wins, not the louder one. The essay should feel substantial, not thin — a wide
scope (a month of reports) earns a longer, deeper piece, but always one argument,
never a list.
它是 **Vertex Dimension 的研究声音**——一家以*建模、定价、配置*文明赖以运转之物为业、
"把现实写成方程再让方程决定"的公司。克制即高级（"能删就删"）；让更好的答案胜出、
而非更响的那个。文稿应当厚实而非稀薄——范围越宽（一个月的研报），越值得写长、写深，
但始终是一条论证，绝非清单。

Its opposite is the "research dump for a feed": every table copied in, every
figure listed, jargon untranslated, the view buried under hedges. It looks
thorough and gets closed in five seconds.
它的反面是"把研报原样搬上信息流"：照搬每张表、罗列每个数字、术语不翻、观点埋在
对冲措辞里。看着详尽，五秒被关掉。

---

## Style fingerprint | 风格指纹（八项，与 logic.md 八步一一对应）

1. **Open on the insight, not the reports** — lead with one falsifiable thesis as
   the firm's own analysis; reports are cited as evidence, never narrated as the
   subject (no "我们读了 N 份研报 / 同一条主线").
   **开篇即洞见，而非研报本身**——以一条可证伪主张领起、作为本机构分析；研报作引用
   证据，不作叙述主体（不写"我们读了 N 份研报/同一条主线"）。
2. **Scope is the reader's** — the user names the input: one synthesis file,
   several, an n-day rolling window, or a theme. The essay names what it drew from
   and each source's `generated_at`; it adds no analysis the source lacks.
   **范围由读者定**——用户指定输入：单份综合研判、多份、某个 n 天滚动窗口，或某个
   主题。文稿点名所据材料及各自 `generated_at`；不新增源文没有的分析。
3. **Causal advance that names the conflicts** — move by *because → therefore*,
   and surface the real contradictions, cross-points, and audit-points from the
   synthesis, each with its evidence and a verdict. Prose more coherent than the
   audit, not the audit reprinted; no "第一、第二、第三", no copied tables.
   **因果推进且点名矛盾**——以*因为 → 所以*推进，并把综合研判里真实的矛盾、交叉点、
   审计点摆出来，各带证据与裁决。是比审计更连贯的散文，不是审计复印；无"一二三"、无照搬表。
4. **One binary spine** — stand the essay on a single contrast (upstream vs
   downstream, who raises the price vs who pays it) so a lay reader holds the shape.
   **一根二分脊柱**——把全文立在一个对照上（上游 vs 下游、谁涨价 vs 谁埋单），让外行
   也抓得住骨架。
5. **Cite, cross-validate, name consistently** — every load-bearing claim carries
   its number *and* its real basis (report, date, figure); before writing,
   cross-check each against a live source (web), correct conflicts, drop the
   uncorroborated (the anti-hallucination gate). Cite one canonical **English** name
   per house (no 花旗/Citi or 高盛/GS mixing); **never name the in-house source —
   carry K-Research's points as 第三方研报**. No number walls, no colloquial filler.
   **列数字、交叉验证、称谓统一**——每个承重主张都带数字*与*真实依据（报告、日期、数）；
   落笔前逐个对照在线来源（联网）交叉验证、更正冲突、删去无印证者（防幻觉闸门）。每家机构
   只用一个**英文**规范名（无花旗/Citi、高盛/GS 混用）；**自有研报不点名——K-Research 的
   观点以"第三方研报"承载**。无数字墙、无闲笔。
6. **A defended viewpoint** — state a clear stance and back each judgment with its
   plain reason; an essay may judge, but opinion without a "because" is noise.
   **有据的观点**——给出清晰立场，每个判断都附白话理由；文章可以判断，但无"因为"的
   观点是噪声。
7. **Audit in the open** — in plain prose, say what would change the view and what
   to watch next; no hedging fog, no false certainty.
   **审计敞开**——用白话写明"什么会改变这个判断、接下来盯什么"；不打太极、不装确定。
8. **Aphoristic coda + stamp** — close on one contrastive sentence; front matter
   carries `source`(s), `generated_at`, the scope, and a one-line *非投资建议*.
   **格言式收束 + 打戳**——以一句对照句收尾；front matter 记来源、`generated_at`、范围
   与一句*非投资建议*。

---

## How to use | 怎么用

**Drafting fresh** — the user sets the scope (a file under `synthesis/`, several,
an n-day window, or a theme). Read [logic.md](logic.md) for the advance order
(claim → scope → causal body → spine → viewpoint → audit → coda), then write per
[style.md](style.md): skill docs in the austere voice (Voice A); the essay in the
plain-professional voice (Voice B). Output to `public-essays/YYYYMMDD_<topic>.md`.
**新写稿**——用户设定范围（`synthesis/` 下一份文件、多份、某 n 天窗口，或某主题）。
先读 [logic.md](logic.md) 定推进顺序（主张 → 范围 → 因果主体 → 脊柱 → 观点 → 审计 →
收束），再依 [style.md](style.md) 落笔：skill 文档用冷峻体（Voice A）；正文用白话专业体
（Voice B）。输出到 `public-essays/YYYYMMDD_<topic>.md`。

**Polishing a draft** — first strip number-tables and jargon per [style.md](style.md),
then check the causal chain and the named falsifier per [logic.md](logic.md).
**润色草稿**——先按 [style.md](style.md) 删数字表与术语，再按 [logic.md](logic.md)
检查因果链与具名证伪。

| File | Role |
|------|------|
| [logic.md](logic.md) | Advance order, scope modes, self-check · 推进顺序、范围模式、自检 |
| [style.md](style.md) | Skill-doc voice + essay-output voice · skill 文档体 + 文稿体 |

---

## Scope modes | 范围模式

| Mode · 模式 | Input · 输入 | e.g. · 例 |
|------|------|------|
| Single · 单份 | one `synthesis/*.md` | 某一期滚动窗口 |
| Window · 窗口 | a date range → its rolling-window file(s) | 最近 7 天 / 任意 n 天 |
| Month-to-date · 月初至今 | the full period → audit + all windows in range | 6 月至今（6/1–now） |
| Multi · 多份 | several files (audit + window) | 审计 + 最新窗口 |
| Theme · 主题 | a topic sliced across synthesis | "存储" / "电力" |

A wider scope earns a **deeper** essay, never a longer list: more of the period's
threads are woven under one controlling thesis. For a month-to-date scope, read
the cross-report audit (full range) plus the rolling windows inside it, and find
the single pattern that runs through every theme — then develop it.
范围越宽，文稿越**深**，绝不越长成清单：把这一时期更多线索收进同一条主线。月初至今
范围下，读跨报告审计（全程）+ 区间内各滚动窗口，找出贯穿所有主题的那一个模式，再
展开它。

---

## One contrast | 一个最小对照

> Before (dump) — *"存储看多。1Q26 合约 +90–95%，2Q26 +58–63%，HBM 晶圆占比 23%，
> Rubin 机架 $9.1M，存储占 $3.2M……"*（把一张表念出来，数字无因果、无出处）

> Before (too colloquial) — *"道理不复杂，存储这波原厂赢麻了，下游就得扛着。"*（精度被闲笔吃掉）

> After (this skill) — *"涨价的起点不是需求暴增，而是产能被分走：HBM 单位晶圆面积是
> 普通内存的三到四倍，原厂把产线调向它，普通内存便被挤到供不应求。Bernstein 6/23
> 测算，商品内存自 25Q3 涨约 4.5 倍，而 HBM 因按年签约没跟上——同一块晶圆做商品内存
> 的毛利反高过 HBM，这才逼出 2027 年的 HBM 重新谈价。一句话：赚钱的不是卖芯片的，是
> 决定这块晶圆先做什么的人。"*（因果 + 带出处的数字 + 一个判断）

The difference is entirely: the number-wall and the chatty filler both yield to a
causal chain that carries each figure with its real source.
差别全在：数字墙与闲笔都让位于一条因果链，每个数字都带着它的真实出处。
