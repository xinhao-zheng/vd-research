# Document Skeleton · 文档推进骨架

The advance order of structured plain expression. The illustrations are
domain-neutral; the skeleton is field-independent — it holds for a spec, a
guide, a research note, or a blueprint alike.
本文件给出"结构化白话"的推进顺序。范例均为领域中性；骨架与具体领域无关——无论
技术规范、指南、研究纪要还是蓝图皆适用。

---

## Order of advance | 推进顺序（默认骨架）

1. **Overview first** — the first screen is a map: a diagram, a big table, or a
   one-minute lookup, placed within the opening 200 words, so a reader who stops
   after the first screen still leaves with 80%.
   **概览先行**——第一屏是一张地图：图、大表或一分钟速查，落在开头 200 字内；
   读者即使只读第一屏也带走八成。
   - e.g. open with a "30-second lookup" section before any detail.
     范例：在任何细节之前，先放一节"30 秒速查"。

2. **Three layers, disclosed in order** — overview → detailed body → appendix;
   each layer stands on its own, and the reader descends only as far as the need.
   **三层，按序披露**——概览 → 详细主体 → 附录；每层自足，读者按需下探。
   - Overview = the map; body = the argument and examples; appendix = lookup
     tables, numbering, references.
     概览＝地图；主体＝论证与例子；附录＝映射表、编号、引用。
   - **Make the sections a chain, not a pile.** Each section answers the
     question the previous one just raised: what is it → does it work → at what
     cost → where does it break → so do we adopt it. Test: if two adjacent
     sections can swap order without anything breaking, the logic is not yet
     progressive — re-sequence until each step depends on the last.
     **让小节成链、不要成堆。** 每节都回答上一节刚抛出的问题：是什么 → 能用吗 →
     代价多大 → 在哪会崩 → 那要不要用。检验法：若相邻两节调换顺序也不影响阅读，说明
     还没层层递进——重排到每一步都依赖上一步为止。

3. **Form follows relation** — pick the form from the information relation, not
   from habit.
   **形式随关系**——按信息关系选形式，而非按习惯。
   - parallel / contrast / classification / mapping → a table; sequence → a
     numbered list or flow; a single thread → short prose.
     并列／对比／分类／映射 → 表格；时序 → 编号列表或流程；单一叙事 → 短段。
   - For a long doc, give headings a visible hierarchy and number them
     progressively (1 / 1.1 / 1.2 / 2 / 2.1); keep each heading short — the
     numbering itself becomes a map the reader can navigate by.
     长文给标题可见的层级并连续编号（1 / 1.1 / 1.2 / 2 / 2.1）；每个标题要短——
     编号本身就成了读者可循的地图。

4. **Every unit is four-part** — a task, step, or experiment runs: why (its role
   in the whole) → how (input / action / output) → how to judge (continue / redo
   / stop) → expected (a number or a shape). A claim or finding runs the same four
   beats: the point → why it holds (mechanism, A → B → C) → what would break it
   (the objection, step 5) → the number that pins it.
   **每个单元四件套**——任务／步骤／实验走：为什么（在整体中的角色）→ 怎么做
   （输入／操作／输出）→ 怎么判断（继续／回炉／停手）→ 预期（一个数字或形态）。
   结论或发现走同样四拍：要点 → 为何成立（机制，A → B → C）→ 什么会推翻它
   （反驳，第 5 步）→ 钉住它的那个数。
   - **Show the mechanism, not just the verdict.** For any claim that could
     surprise the reader, give the causal chain in plain steps (A → B → C); a
     number or conclusion without its "why" reads as an assertion. e.g. not
     "the database is the bottleneck" but "every request locks the whole table →
     writes can only queue → so throughput is capped however many servers you
     add".
     **给机制，不只给结论。** 凡可能让读者意外的结论，用大白话给出因果链
     （A → B → C）；只给数字或结论、不给"为什么"，读起来就是断言。例：不说
     "数据库是瓶颈"，而说"每个请求都锁住整张表 → 写操作只能排队 → 所以无论加
     多少台服务器，吞吐都封顶"。

5. **Anticipate the objection** — after "the conclusion is X", ask "how would a
   reviewer rebut X?" and answer it, rather than leaving the reader to.
   **预判反对**——给出"结论是 X"后，先问"审稿人会怎么反驳 X？"并作答，而非留给
   读者去问。
   - e.g. *"X. One will ask: only on your data? — reproduced on three public
     sets, all above baseline (see §6)."*
     范例："X。有人会问：只在你的数据上成立？——已在三个公开集复现，均高于基线
     （见 §6）。"

6. **Cross-reference by address** — point to a specific section or file; never
   "see above" or "as mentioned".
   **按地址交叉引用**——指向具体小节或文件；不用"见上文""如前所述"。
   - ✓ "as in §2.3" / "see `guide.md` §4" — ✗ "as mentioned earlier".
     ✓ "如 §2.3" / "见 `guide.md` §4" — ✗ "如前所述"。

7. **Close, then self-check** — close the document on one line the reader carries
   away; for an argument, make it a sharp contrastive coda (the
   austere-analytical-prose move), not a flat summary. Run the self-check below
   before shipping — print the checklist (5–8 boxes) at the end only for an
   actionable doc (spec / guide / manual); for a published piece, run it backstage
   and let the takeaway stand as the visible close.
   **先收束，再自检**——用一句读者能带走的话收尾；若是论证，就让它是一句锋利的
   对照式格言（冷峻思辨学术体的收法），而非平铺的总结。发布前跑一遍下面的自检——
   可执行文档（规范／指南／手册）才把清单（5–8 条）印在文末；公开文章则在幕后跑，
   让那句要点充当可见的收束。

---

## Self-check | 自检清单

- [ ] Does the first screen convey 80% in 30 seconds? |
      第一屏是否 30 秒传达八成？
- [ ] Are the three layers (overview / body / appendix) each complete? |
      三层（概览／主体／附录）是否各自自足？
- [ ] Is each information relation in its right form (table / list / prose)? |
      每种信息关系是否用了对的形式（表格／列表／散文）？
- [ ] Does every task or step run the four parts (why → how → judge → expected)? |
      每个任务／步骤是否走了四件套（为什么 → 怎么做 → 怎么判断 → 预期）？
- [ ] Does every surprising claim show its mechanism (A → B → C), not just a verdict? |
      每个会让人意外的结论，是否给了机制链（A → B → C），而非只甩结论？
- [ ] Do the sections form a chain (each answers the previous one's question), not a pile? |
      各小节是否成链（每节回答上一节的问题），而非散堆？
- [ ] Is every external number sourced in plain words, every derived number shown with its arithmetic? |
      每个外部数字是否用人话标了出处、每个推导数字是否摊开了算式？
- [ ] In a long doc, are headings short and progressively numbered (1 / 1.1 / 1.2)? |
      长文标题是否简短且连续编号（1 / 1.1 / 1.2）？
- [ ] Is each persuasive claim met with its own rebuttal-and-answer? |
      每个说服性结论是否自带反驳与回答？
- [ ] Are all cross-references specific (section / file), never "see above"? |
      所有交叉引用是否具体（小节／文件），无"见上文"？
- [ ] Does the document close on a carried-away line (a sharp coda for an
      argument), with the self-check run before shipping — printed only for an
      actionable doc? |
      文档是否以一句可带走的话收尾（论证则用一句锋利格言），并在发布前跑过自检、
      仅可执行文档才印出清单？
