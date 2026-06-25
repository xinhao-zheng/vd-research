# Language: Skill Doc + Synthesis Output · 语言风格：Skill 文档 + 综合研判输出

Two voices live in this file — separated by artifact type, both self-contained.
本文件内嵌两种声音——按产出类型区分，均自洽，不依赖其他 skill 文件。

---

## Voice A — Skill documentation (SKILL.md, logic.md, this file's meta sections) | Skill 文档

The austere analytical voice — same execution rules as the sibling skills in
this repository: zero filler, load-bearing verbs, em-dash qualification, short
sentence stress, honesty over rhetoric. Most rules carry ✓ and ✗.
冷峻思辨学术体——与本仓库 sibling skill 同一执行规则：零套话、承重动词、破折号限定、
短句重音、诚实压过修辞。多数规则配 ✓ 与 ✗。

### Diction | 用词

1. **Zero filler.** Cut "comprehensive / in-depth / it is worth noting". Name the
   mode, the gate, the output path.
   **零套话。** 删 comprehensive/in-depth/值得注意的是。写模式、闸门、输出路径。
   - ✗ *This skill provides a comprehensive overview of market themes.*
     本 skill 全面概述市场主题。
   - ✓ *Mode B outputs `cross-report-audit.md` — agreement and conflict as
     pairs, each with a falsifier.*
     模式 B 输出 `cross-report-audit.md`——一致与冲突成对，各带证伪。

2. **Verbs:** bound, calibrate, refute, diff, anchor — not "cover / discuss /
   touch on".
   **动词：** bound、calibrate、refute、diff、anchor——而非 cover/discuss。

3. **"We" for the act, "this synthesis" for the document** — never "笔者".
   **"我们"述行动，"本综合稿"指文档**——不用"笔者"。

### One-pass clean (skill docs) | 一键清洗（skill 文档）

1. Delete filler; swap mood for mechanism. | 删套话；情绪换机制。
2. Check paragraphs join by cause. | 检查段落因果连接。
3. End skill sections on a load-bearing line, not a slogan. | 小节以承重句收，非口号。

---

## Voice B — Synthesis output (`synthesis/*.md`) | 综合研判正文

Structured plain expression — embedded here; **never cite another skill by name
in the synthesis file itself.**
结构化白话——规则内嵌于此；**综合研判文件本身绝不写其他 skill 名称。**

### Opening | 开篇

1. **YAML carries the real `generated_at`; body repeats it once.** Use the actual
   UTC wall-clock at write time — never a round placeholder (`12:00:00Z`), never a
   reused value.
   **YAML 含真实 `generated_at`；正文重复一次。** 用写入时的真实 UTC 墙钟——不用整点
   占位（`12:00:00Z`），不沿用旧值。
   ```markdown
   **生成时间（UTC）：** 2026-06-23T07:48:22Z
   ```

2. **30-second blockquote immediately after title.**
   **标题后紧跟 30 秒引用块。**
   ```markdown
   > **30 秒带走：** <consensus + new friction + what to watch>
   ```

3. **Plain recap after every table** — one line: *"读法：…"* or *"一句话：…"*
   **每张表后一句白话收束**——*"读法：…"* 或 *"一句话：…"*
   - ✗ table → next heading with no bridge.
     表 → 直接下一标题。
   - ✓ *"一句话：2026 仍按存储多头做；2027 顶点与 OEM 破坏是同一链的两端。"*

### Mechanism paragraphs | 机制段

4. **Fixed four-beat block for non-obvious claims:**
   **非显然主张固定四拍块：**
   ```
   **机制：** A → B → C
   **数字：** <plain source words> — <number>
   **怎么判断继续成立：** <observable by date>
   **有人会问：** <objection> — **答：** <answer>
   ```
   - ✗ *"Storage is tight."* — ✓ mechanism chain + falsifier.
     ✗ "存储很紧。" — ✓ 机制链 + 证伪。

5. **Plain sentence first, evidence behind** — lead with human Chinese; tickers
   and report titles may stay; never stack jargon before meaning.
   **先一句人话，证据在后**——中文大白话先行；ticker 与报告标题可保留；不把术语堆在意思前。

6. **External numbers name the source AND get triangulated** — *"Bernstein 6/23
   报告"*, not *"see above"*; derived numbers show the arithmetic in one line. For
   any load-bearing external number, cross-check a live source and add an
   `**外部核对：**` line naming the corroborating outlet(s); flag any single-source
   figure that nothing external confirms.
   **外部数字点出处并三角验证**——*"Bernstein 6/23 报告"*，非"见上文"；推导数字一行
   摊开算式。凡承重外部数字，对照在线来源核对，并加一行 `**外部核对：**` 点名印证媒体；
   无外部印证的单一信源数字须标"待核"。

### Tables & fixed sets | 表格与固定词表

7. **Form follows relation** — parallel/contrast → table; sequence → numbered
   list or ASCII arrow flow; single thread → short prose.
   **形式随关系**——并列/对比 → 表；时序 → 编号列表或 ASCII 箭头；单线 → 短段。

8. **Fixed stance column** (declare once at table top):
   `看多` · `看空` · `中性` · `中性偏多` · `中性偏空` · `混合` · `谨慎`
   **固定态度列**（表首声明一次）

9. **Fixed confidence column** (mode C lookup tables):
   `高` · `中高` · `中` · `低`
   **固定置信度列**（模式 C 速查表）

10. **BEAR/BASE/BULL tables** — probabilities sum to 100%; footer line:
    *工作假设，非投资建议*.
    **BEAR/BASE/BULL 表**——概率合计 100%；脚注：*工作假设，非投资建议*。

### Section numbering | 编号

11. **Long docs: progressive numbering** — `## 1.` `## 2.` `### 2.1`; short
    headings; the number is the map.
    **长文连续编号**——`## 1.` `## 2.` `### 2.1`；标题短；编号即地图。

### Cross-reference & close | 交叉引用与收束

12. **By address only** — `§4.2`, `synthesis/all-reports-index.md`, `report-summaries/…`
    — never *"如前所述"* / *"see above"*.
    **仅按地址**——`§4.2`、文件路径——不用"如前所述"。

13. **Aphoristic coda** — one contrastive sentence; not *"综上三点"*.
    **格言式收束**——一句对照；非"综上三点"。
    - ✓ *"原厂拿晶圆税，云厂付 capex 税，OEM 付 BOM 税——同一条链，三张账单。"*

14. **Footer timestamp line** (modes B and C) — real `generated_at`, and note
    external verification when bearish/bullish numbers were triangulated:
    ```markdown
    *基于 N 份摘要；生成于 <generated_at>；关键看空/看多数字已对照公开报道交叉验证；概率为工作假设。*
    ```

15. **No emoji** — navigation by headings, numbers, and tables only.
    **无 emoji**——导航靠标题、编号、表格。

### One-pass clean (synthesis body) | 一键清洗（综合正文）

1. Hoist 30-second blockquote to first screen. | 30 秒块提到第一屏。
2. Turn parallel theme prose into tables + one-line recap. | 平行主题散文改表 + 一句收束。
3. Add A → B → C to every surprising claim. | 每个意外主张补机制链。
4. Add falsifier column or line to every conflict table. | 每个冲突表补证伪列或证伪句。
5. Replace "见上文" with § or path. | "见上文"换 § 或路径。
6. Close on one sharp line; run self-check in logic.md backstage. | 一句锋利收束；幕后跑 logic.md 自检。
