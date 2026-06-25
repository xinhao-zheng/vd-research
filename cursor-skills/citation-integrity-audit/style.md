# Language: Provenance, Verdicts, Stance · 语言风格：溯源、判定、姿态

The rules of execution for the audit ledger. Most carry an example (✓) and a
counter-example (✗).
本文件给出核查台账的落笔规则。多数规则配范例（✓）与反例（✗）。

---

## Provenance | 溯源

1. **Quote the source verbatim; never paraphrase the evidence.** The
   load-bearing sentence *is* the evidence — a paraphrase removes the reader's
   power to re-check, and quietly launders the auditor's reading into the
   record.
   **逐字引用来源；绝不转述证据**。承重句"即"证据——转述会剥夺读者复核的能力，并
   把核查者的解读悄悄洗入记录。
   - ✗ *the paper argues detection becomes unreliable as models improve.*
     该文论证检测随模型增强而不可靠。
   - ✓ *"even the best-possible detector may only perform marginally better than
     a random classifier" (verbatim, with `…` for any cut).*
     "即便最优检测器也可能仅比随机分类器略好"（逐字，省略处以 `…` 标记）。

2. **Every row carries a resolvable link to the primary source.** Prefer a
   stable, primary pointer — DOI, arXiv id, official spec, publisher, catalog —
   over a blog or content aggregator. A row without a link is an assertion, not
   an audit.
   **每行附一手来源的可解析链接**。优先稳定的一手地址——DOI、arXiv 号、官方规范、
   出版商、馆藏目录——而非博客或聚合站。无链接的行是断言，不是核查。
   - ✓ `https://doi.org/10.1109/SP.2014.36` · `https://eprint.iacr.org/2020/543`
   - ✗ *(see their paper)* · *(Google it)* — 见其论文／自行搜索

3. **Set source against paper, in both editions.** Place the source sentence
   (original + translation) next to the paper's own wording in each language
   edition; the columns let the match be read line by line, not taken on faith.
   **来源与论文并置，且双稿并载**。把被引原句（原文＋译文）紧挨论文各语种版本的
   措辞放置；列与列之间让吻合被逐行读出，而非被采信。

4. **Carry full identity once.** Title, authors, venue, year, pages — stated in
   the row itself, so the reader need not leave it to verify who and where.
   **完整身份一次写清**。标题、作者、出处、年份、页码——写在行内，使读者无须离开
   该行即可核对"谁"与"何处"。

---

## Verdicts | 判定

5. **A fixed verdict set, declared before the first row.** Grade on a small
   closed set of bare words — the austere table states a cell as *native / none /
   advisory*. Define the set once, at the top; never improvise a label per row,
   and let the word's meaning carry the weight.
   **固定的判定集，于首行之前声明**。用一个小型闭集的裸词来定级——冷峻表格把一格
   写成"原生／无／仅建议"。该集合于表首一次定清；不逐行临时起意，让词义承重。
   - ✓ a verdict column reading *match · true-but-misplaced · match-but-non-primary*,
     each defined once at the top.
     判定列写作"吻合 · 真实但落点偏移 · 吻合但来源非一手"，于表首各定义一次。
   - ✗ *an undeclared scale that drifts from row to row.*
     一套未声明、逐行漂移的刻度。

6. **A verdict locates; it does not praise.** State the match or name the gap;
   do not lift it with "excellent / perfect / flawless". Emphasis comes from the
   match itself, not from the adjective.
   **判定"定位"，不"赞美"**。陈述吻合，或点名缺口；不用"优秀／完美／无瑕"拔高。
   强调来自吻合本身，而非形容词。
   - ✗ *perfectly and excellently matched* — 完美且优秀地吻合
   - ✓ *source states X; paper says X — match* · *true, but the source treats
     capability, not hazard — mis-placed.*
     来源陈述 X；论文说 X——吻合 · 真实，但来源讲的是能力而非危害——落点错。

7. **Name the residue precisely; candor over reassurance.** Not "slightly off"
   but the exact nuance — what is simplified, mis-placed, or non-primary, and
   why it is still acceptable (or not).
   **精确点名残差；坦白胜过安抚**。不写"略有出入"，而写确切的微妙之处——何处被
   简化、被错置、或来源非一手，以及它为何仍可接受（或不可）。
   - ✓ *the source defines session keys via a later standard layered on this one
     — acceptable simplification, flagged.*
     来源是经一个建立在其上的较晚标准来定义会话密钥——可接受的简化，已标注。

---

## Stance | 姿态

8. **The audit is itself an object to be checked.** Write each row so a stranger
   can redo it from the row alone — link, verbatim quote, page. The audit holds
   the paper to "check, don't trust"; it must hold itself to the same.
   **核查自身也是受检之物**。把每行写到陌生人仅凭该行即可重做——链接、逐字原句、
   页码。核查要论文做到"核查而非采信"，它必须以同一标准要求自己。

9. **Separate the axes; never collapse them.** Existence (is it real?), match
   (does the source say it?), and placement (is it under the right claim?) are
   three verdicts, not one — a source can pass two and fail the third, and the
   row must show which.
   **分轴，绝不合并**。存在（是否真实？）、吻合（来源是否如是说？）、落点（是否
   落在对的主张下？）是三项判定而非一项——一条来源可过其二、败其一，行中须显示
   败在哪一轴。

10. **State method, not sentiment.** Use "我们" for the act of auditing —
    *resolved, extracted, confronted, graded*; use "本表 / 本台账" to frame the
    document. No "笔者", no praise of the paper under audit.
    **陈述方法，不抒情**。"我们"用于核查动作——*解析、抽取、对质、定级*；"本表／
    本台账"用于框定文档。不用"笔者"，不褒扬受核论文。

---

## One-pass clean | 一键清洗流程（润色旧表时）

1. Replace every paraphrase of a source with its verbatim sentence (+ translation). |
   把每处对来源的转述换成其逐字原句（＋译文）。
2. Add a resolvable primary-source link to every row that lacks one. |
   给每个缺链接的行补上一手来源的可解析链接。
3. Reduce all verdicts to the fixed set; strip "perfect / excellent / strong". |
   把所有判定收敛到固定集合；删去"完美／优秀／强有力"。
4. Split any row that fuses existence / match / placement into the three axes. |
   把任何熔合"存在／吻合／落点"的行拆成三轴。
5. Reread: does any row still ask to be trusted rather than re-checked? Fix it. |
   通读：是否还有行在要求被采信、而非被复核？改之。
