# Language: Expression, Voice, Stance · 语言风格：表达、语气、姿态

The rules of execution for structured plain expression. Most carry an example
(✓) and a counter-example (✗).
本文件给出"结构化白话"的落笔规则。多数规则配范例（✓）与反例（✗）。

---

## Expression | 表达

1. **A plain recap after every table.** A table never hangs alone; one line
   lands its point — "in one line / read it as / the key".
   **每张表后必有白话收束**。表不孤悬；一句话落点——"一句话／读法／关键"。
   - ✓ after a comparison table: *"In one line: A for text, B for scale."*
     在对比表后：*"一句话：文本选 A，规模选 B。"*
   - ✗ a table followed immediately by the next heading.
     表格后直接进下一个标题。

2. **No bare jargon — say it plain, or unpack it on first use.** Prefer a plain
   word to a term, and give the picture before the name. Where a proper term is
   unavoidable, its first mention says in one human sentence what it is and why it
   matters here, with the term in parentheses for later — a term the reader cannot
   decode is a wall, not a shortcut.
   **不甩术语——能说人话就说，非用不可就在首次出现处拆开**。能用大白话就别用术语，
   先给画面再给名字。确需专有名词时，第一次出现先用一句人话讲清"它是什么、在这儿为何
   重要"，原词放进括号备查——读者解不开的术语是堵墙，不是捷径。
   - ✗ *"The service targets four-nines SLA with horizontal sharding."*
     "该服务目标为 four-nines SLA，采用 horizontal sharding。"
   - ✓ *"The service must stay up 99.99% of the time — about 52 minutes of
     downtime a year (often called a four-nines SLA). To handle more load, split
     the data across machines and route each request to the right shard."*
     "服务必须 99.99% 的时间在线——一年大约只能宕 52 分钟（行话叫 four-nines SLA）。
     要扛更多流量，就把数据拆到多台机器上，每条请求路由到对应分片（horizontal
     sharding）。"

3. **Plain sentence first, evidence behind it.** Lead with one human sentence
   that lands the point; let numbers, sources, and section refs follow as support —
   never stack terms and citations between the reader and the meaning.
   **先一句人话，证据跟在后面**。先用一句大白话把意思砸下来；数字、出处、小节号跟在
   后面做支撑——别把一串术语和引用堆在读者与意思之间。
   - ✗ *"Per §3.2 (Table 4), the module exhibits p99 latency regression of 18%
     QoQ under burst load."*
     "据 §3.2（表 4），该模块在 burst load 下 p99 latency QoQ 回退 18%。"
   - ✓ *"The module got noticeably slower under traffic spikes — the slowest 1%
     of requests took 18% longer than last quarter (see §3.2, Table 4)."*
     "模块在流量尖峰时明显变慢——最慢那 1% 的请求比上季慢了 18%（见 §3.2、表 4）。"

4. **Concrete over vague.** When support is due, give a number or a shape, not
   "significantly" or "greatly improved".
   **具体胜于空泛**。该给支撑时，给数字或形态，而非"显著""大幅提升"。
   - ✗ "performance improved markedly" — ✓ "error rate fell from 2.1% to 0.4%".
     ✗ "性能大幅提升" — ✓ "错误率从 2.1% 降到 0.4%"。
   - **Name the source in plain words, and show the breakdown — not a cryptic
     tag.** Every external number says who said it in words a stranger can use
     ("a third-party benchmark", "the vendor's own datasheet", "the standards
     body") — never a "§7 / p.12" code the reader cannot look up. Every derived
     number is unfolded into the steps and the condition that produce it; a
     result with no visible "how" is magic, not analysis. This is the backbone of
     the whole voice — non-negotiable.
     **用人话点名出处，并把拆解摊开——不要甩暗号。** 每个外部数字都用陌生读者能懂的
     话说清"谁说的"（"一份第三方基准测试""厂商自己的规格书""标准组织"），绝不用
     "§7／第 12 页"这种读者查不了的代号。每个推导出来的数字，都把得出它的步骤和成立
     条件摊开；没有可见"怎么来的"的结果，是魔术不是分析。这是整套风格的脊梁，不可妥协。
     - ✗ *"About 3× faster after the migration."* — ✓ *"About 3× faster after the
       migration — the figure from the vendor's published benchmark (single node,
       read-heavy load)."*
       ✗ "迁移后大约快 3 倍。" — ✓ "迁移后大约快 3 倍——这是官方基准测试报告里的数字
       （单机、读密集负载）。"
     - ✗ *"~$1.2M saved per year (see §7)."* — ✓ *"The $1.2M annual saving builds
       up like this: each old machine costs $4k/yr in power, the new one $1k,
       across 400 machines — ($4k − $1k) × 400 = $1.2M."*
       ✗ "一年省约 120 万（见 §7）。" — ✓ "一年省约 120 万是这么来的：每台旧机年电费
       4 千、换新后 1 千，共 400 台，(4000 − 1000) × 400 ＝ 120 万。"

---

## Voice & rhythm | 语气与节奏

5. **Dialogic self-Q&A.** Use the second person; at each turn, ask the reader's
   own question, then answer it. Avoid the "this paper studies…" register.
   **对话式自问自答**。用第二人称；在转折处替读者问出他的问题，再回答；不用
   "本文研究了……"的腔调。
   - ✓ *"It works — but why? And if there is an order, who moves first?"*
     "它有效——但为什么？若有先后，谁先动？"
   - ✗ *"This section first argues existence, then discusses the mechanism."*
     "本节首先论证存在性，继而讨论机制。"

6. **Let structure navigate, not emoji.** Do not sprinkle decorative or
   "navigational" emoji (📌 📊 ⭐ ⚠️ and the like) in headings or prose — they
   read as gaudy and AI-generated; headings, numbering, and tables do the
   navigating.
   **导航靠结构，不靠 emoji**。标题与正文不撒装饰性或"导航性"emoji（📌 📊 ⭐ ⚠️
   之类）——它们显得浮夸、一眼 AI 味；导航交给标题、编号与表格。

7. **A fixed status set, declared once, list/table only.** When a list or table
   needs a status column, grade on a closed set of bare words in the document's
   primary language — *verified · partial · pending* (English) or *已核对 ·
   部分成立 · 待核对* (Chinese). Define the set once at the top; use plain words
   a colleague would say aloud; never emoji, never improvise a label per row.
   **固定状态集，表首声明，仅用于列表／表格**。列表或表格需要状态列时，用文档主语言
   的三个白话短词定级——英文 *verified · partial · pending*，中文 *已核对 · 部分成立 ·
   待核对*。该集合于表首一次定清；选同事真会念出口的词；不用 emoji，不逐行临时起意。
   - ✓ at the top: *Status (this draft): verified = checked against source ·
     partial = partly holds, still checking · pending = not yet checked or may
     change.*
     表首：*状态（本稿）：已核对＝来源对过了 · 部分成立＝一部分对、还在验 · 待核对＝
     还没底或可能被推翻。*
   - ✓ in a cell: *已核对* — ✗ in a cell: *✅* · *confirmed* · *done*.
     单元格写 *已核对* — ✗ 单元格写 *✅* · *confirmed* · *done*。

---

## Stance | 姿态

8. **Say it as you would to a colleague.** Plain and direct; cut jargon walls;
   readable but not cute — no memes, no padded enthusiasm.
   **像对同事那样讲**。平实、直接；拆掉术语墙；好读但不卖萌——无梗、无注水的热情。

9. **End each unit on one carried-away line — and let it bite.** Every section
   closes on a single takeaway; for a claim, shape it as a sharp, often
   contrastive line (the austere-analytical-prose coda), not a flat restatement.
   **每个单元以一句可被带走、且有锋芒的话收束**。每节都以一句要点结尾；若是结论，
   就打磨成一句锋利、常带对照的话（冷峻思辨学术体的收法），而非平铺复述。
   - ✓ *"The method scales; the judgment does not."* — ✗ *"In summary, this
     section made three points."*
     ✓ "方法可以扩展，判断不能。" — ✗ "综上，本节讲了三点。"

---

## One-pass clean | 一键清洗流程（润色旧文时）

1. Hoist a 30-second overview to the first screen. | 把"30 秒概览"提到第一屏。
2. Turn every parallel / contrast / mapping prose block into a table. |
   把每段并列／对比／映射的散文改成表格。
3. Add a one-line recap under every table. | 给每张表补一句白话收束。
4. Replace every term with plain words; for one that must stay, unpack it in a
   human sentence on first use, with the term in parentheses. |
   把每个术语换成人话；非留不可的，第一次出现用一句人话拆开，原词入括号。
5. Strip decorative / navigational emoji (📌 📊 ⭐ ⚠️); replace status emoji
   (✅ 🟡 🔴) with the fixed plain-word set (verified · partial · pending /
   已核对 · 部分成立 · 待核对) in lists and tables only. |
   删掉装饰／导航 emoji（📌 📊 ⭐ ⚠️）；把状态 emoji（✅ 🟡 🔴）换成固定白话词集
   （verified · partial · pending／已核对 · 部分成立 · 待核对），且只用于列表与表格。
6. Replace "see above / as mentioned" with specific section or file numbers. |
   把"见上文／如前所述"换成具体小节或文件号。
7. Tag every external number with its source, and add a one-line arithmetic
   under every derived number. | 给每个外部数字补出处，给每个推导数字补一句算式。
8. Give long-doc headings a short title and progressive numbering (1 / 1.1 / 1.2). |
   给长文标题配简短标题与连续编号（1 / 1.1 / 1.2）。
9. Reread: does any section bury its point below the first screen, hang a table
   with no recap, or close flat instead of on a line? Fix it. |
   通读：是否还有小节把要点埋在第一屏之下、让表格无收束、或收尾平铺而非落在一句
   话上？改之。
