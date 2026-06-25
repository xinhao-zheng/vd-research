# Language: Skill Doc + Summary Output · 语言风格：Skill 文档 + 摘要输出

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

1. **Zero filler in skill docs.** Cut "very important / strongly recommend / it is
   worth noting". State the gate, the artifact, the consequence.
   **Skill 文档零套话。** 删"非常重要／强烈建议／值得注意的是"。写闸门、工件、后果。
   - ✗ *It is crucial to extract before summarizing.*
     提取后再摘要非常重要。
   - ✓ *Without `*-Bilingual.md`, no `-Summary.md` — the chain stops at extract.*
     无 `*-Bilingual.md` 则无 `-Summary.md`——链条止于提取。

2. **Load-bearing verbs for stages:** extract, anchor, gate, map, refute — not
   "handle / process / deal with".
   **阶段用承重动词：** extract、anchor、gate、map、refute——而非 handle/process。

3. **Define paths on first use** — always English directory names for this project.
   **路径首次出现即定义**——本项目一律英文目录名。

### Syntax & stance | 句法与姿态

4. **Em-dash for qualification** — *"Translation fills empty blocks — it does
   not replace extract."*
   **破折号承载限定**——*"翻译填充空块——不替代提取。"*

5. **Short sentence after a long gate list** — *"The chain stops upstream."*
   **长闸门列表后用短句收重音**——*"链条在上游停止。"*

6. **Honesty over rhetoric** — flag low-confidence extraction plainly; do not
   paper over empty PDF text.
   **诚实压过修辞**——低置信提取直说；不掩盖空 PDF 文本。

### One-pass clean (skill docs) | 一键清洗（skill 文档）

1. Delete filler and mood-adjectives. | 删套话与情绪形容词。
2. Swap "important" for "what breaks if missing". | 把"重要"换成"缺了会怎样"。
3. Check every paragraph advances by cause, not parallel bullets without link. |
   检查段落是否因果推进，而非无关联的平行 bullet。

---

## Voice B — Summary output (`report-summaries/*-Summary.md`) | 摘要输出

Structured plain expression — embedded here; **never cite another skill by name
in the summary file itself.**
结构化白话——规则内嵌于此；**摘要文件本身绝不写其他 skill 名称。**

### Overview & layers | 概览与分层

1. **First screen: one-line conclusion before bullets.** The reader who stops
   after `## 一句话结论` still leaves with direction + mechanism.
   **第一屏：`## 一句话结论` 先于 bullet。** 读者只读到该节仍带走方向 + 机制。
   - ✗ open with five jargon bullets, conclusion at the end.
     开头五个术语 bullet，结论在文末。
   - ✓ one sentence: *"HBM eats wafer → commodity DRAM tight → OEM BOM pain in
     2026H2."* then bullets unpack.
     一句：*"HBM 吃晶圆 → 商品 DRAM 紧 → 2026H2 OEM BOM 承压。"* 再 bullet 展开。

2. **Three layers:** YAML metadata → body (结论 / 洞见 / 建议) → optional tags.
   No fourth layer unless the report demands it.
   **三层：** YAML → 正文（结论/洞见/建议）→ 可选标签。无必要不加第四层。

### Four-part units | 四件套

3. **Every bullet runs four beats where non-obvious:** point → mechanism
   (A → B → C) → falsifier → number if available.
   **每个 bullet 在非显然处走四拍：** 要点 → 机制（A → B → C）→ 证伪 → 有则给数。
   - ✗ *"DRAM prices are rising significantly."*
     DRAM 价格显著上涨。
   - ✓ *"Standard DRAM contracts +90% in 1Q26 — because HBM now uses 23% of
     cleanroom wafers, squeezing commodity supply. Falsifier: QoQ negative in
     2Q26."*
     标准 DRAM 合约 1Q26 +90%——因 HBM 占洁净室晶圆 23%，挤出商品供给。证伪：
     2Q26 QoQ 转负。

4. **Plain words over bare jargon** — unpack on first use; tickers and product
   codes may stay.
   **白话优先于裸术语**——首次出现拆开； ticker 与产品代号可保留。

5. **Source in plain words** — *"Bernstein 6/23 report, page-level anchor in
   bilingual file"* — not *"see above"*.
   **出处用人话**——*"Bernstein 6/23，页码见双语文件"*——不用"见上文"。

### Tables & stance set | 表格与立场集

6. **Use a table only when comparing parallel items** (e.g. bull vs bear drivers
   within one report). One-line recap under every table.
   **仅在并列对比时用表**（如一份报告内的多空驱动）。每张表下一句白话收束。

7. **Fixed stance vocabulary** — declare once in YAML; body must match:
   `看多` · `看空` · `中性` · `中性偏多` · `中性偏空` · `混合` · `谨慎`
   **固定立场词表**——YAML 声明一次；正文须一致。

### Close | 收束

8. **End `## 结论与建议` on one carried-away line** — sharp, often contrastive;
   not *"In summary, three points."*
   **`## 结论与建议` 以一句可带走的话收束**——锋利、常带对照；而非"综上三点"。
   - ✓ *"Long the wafer allocator; watch the BOM payer — same chain, opposite
     P&L."*
     做多分晶圆的人；盯 BOM 埋单的人——同一条链，相反损益。

### One-pass clean (summaries) | 一键清洗（摘要）

1. Hoist `## 一句话结论` to the first readable claim. | 把一句话结论提到首个可读主张。
2. Add A → B → C to any surprising bullet. | 给每个意外 bullet 补机制链。
3. Name one falsifier in the closing line. | 收束行点明一条证伪条件。
4. Replace "见上文" with file path or page marker. | "见上文"换文件路径或页标记。
5. Strip emoji; use the fixed stance set only. | 去 emoji；立场只用固定词表。

---

## Naming & code | 命名与代码

| Artifact · 工件 | Pattern · 模式 |
| --- | --- |
| Source · 源 | `source-pdfs/YYYYMMDD_<Issuer>-<Topic>.pdf` |
| Bilingual · 双语 | `bilingual-transcripts/YYYYMMDD_<Issuer>-<Topic>-Bilingual.md` |
| Summary · 摘要 | `report-summaries/YYYYMMDD_<Issuer>-<Topic>-Summary.md` |

Python comments: English only; module docstring points to project `README.md`.
Python 注释：仅英文；模块 docstring 指向项目 `README.md`。

---

## Bilingual MD front matter (reference) | 双语稿元数据（参考）

```yaml
---
document: <title>
source: <original-filename.pdf>
issuer: <Goldman Sachs | K-Research | ...>
report_date: YYYYMMDD
extracted: YYYY-MM-DD
pages: N
languages: en, zh-CN
source_language: en | zh
translation: professional human-quality retranslation
extraction_style: equity research - bilingual parallel text with structural markup
---
```
