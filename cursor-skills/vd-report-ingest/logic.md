# Ingest Skeleton · 入库推进骨架

The advance order of research report ingest. The illustrations are
domain-neutral where possible; the path names are fixed for vd-research.
本文件给出研报入库的推进顺序。范例尽量领域中性；路径名固定为本项目约定。

---

## Order of advance | 推进顺序（默认骨架）

1. **Close the intake set** — one file in `source-pdfs/` maps to exactly one
   slug; intersect filename, existing `*-Bilingual.md`, and `*-Summary.md`
   before opening the PDF. A duplicate slug or dateless filename is a defect
   correctable without extraction. The slug carries the **full** title: strip
   only the real extension, never split on an interior dot — a slug collapsed to
   `YYYYMMDD_<n>` (e.g. `20260623_1` from `20260623_1.China …`) is a naming bug,
   not a name.
   **闭合入库集**——`source-pdfs/` 中一个文件对应唯一 slug；开 PDF 前先求交
   文件名、已有 `*-Bilingual.md` 与 `*-Summary.md`。重复 slug 或无日期文件名
   是无需提取即可修正的缺陷。slug 须承载**完整**标题：只去真实扩展名，绝不在
   内部点号处截断——被压成 `YYYYMMDD_<n>` 的 slug（如从 `20260623_1.China …`
   得到 `20260623_1`）是命名 bug，不是名字。
   - e.g. *One PDF, one slug `20260623_Bernstein-Memory-…`, no prior `-Bilingual.md`
     with the same stem — set closed.*
     范例：*一份 PDF、一个 slug，无同 stem 的旧 `-Bilingual.md`——集合闭合。*

2. **Gap first: opaque substrate** — the problem is not "we lack a summary" but
   "the substrate is wrong": binary layout, no page index, language split.
   Extraction supplies structure; it does not supply judgment.
   **缺口先行：不透明基底**——问题不是"缺摘要"，而是"基底错误"：版式封闭、无页码、
   语种割裂。提取供给结构；不供给判断。
   - Anti-pattern: summarize from a single read while pages stay unmarked.
     反模式：页码未标记时读一遍就写摘要。

3. **Extract verbatim, then translate** — run `scripts/ingest.py` (no `--force`
   unless source changed); write `.extract-cache/<slug>_extracted_pages.json`
   and scaffold `bilingual-transcripts/<slug>-Bilingual.md`. Translation fills
   empty blocks — it does not replace the extract pass.
   **先逐字提取，再翻译**——运行 `scripts/ingest.py`（源未变则不 `--force`）；
   写入 cache JSON 与双语 scaffold。翻译填充空块——不替代提取。
   - Gate: page count > 0; combined text > 500 chars, else flag *low-confidence*
     in summary front matter.
     闸门：页数 > 0；合计文本 > 500 字，否则在摘要元数据标 *low-confidence*。

4. **A binary spine: artifact vs opinion** — the whole ingest stands on one
   contrast: named files (evidence) vs claims in the agent's head (non-evidence).
   No `-Summary.md` until `*-Bilingual.md` body pages are populated.
   **二分脊柱：工件 vs 观点**——全流程立在一个对照上：具名文件（证据）vs
   代理记忆中的主张（非证据）。正文页未填齐之前，不写 `-Summary.md`。

5. **Proposition-shape the summary** — the one-line conclusion must be
   checkable: *who wins, through which mechanism, on what horizon* — not
   "bullish on AI".
   **摘要命题化**——一句话结论须可检验：*谁因何机制在何窗口受益*——而非
   "看多 AI"。
   - Required YAML: `report_date`, `issuer`, `title`, `topics`, `stance`, `source`
     pointing to the bilingual path.
     必填 YAML：`report_date`, `issuer`, `title`, `topics`, `stance`, `source`
     指向双语路径。

6. **Evidence by stage** — map each stage to its artifact in one table so the
   chain is readable line by line:
   **分阶段证据对照**——用一张表把每步映射到工件，使链条可逐行检读：

   | Stage · 阶段 | Artifact · 工件 | Gate · 闸门 |
   | --- | --- | --- |
   | Intake · 接收 | `source-pdfs/<file>` | unique slug · slug 唯一 |
   | Extract · 提取 | `.extract-cache/*.json`, `*-Bilingual.md` | pages + markers · 页数 + 标记 |
   | Retranslate · 重译 | both **EN** / **ZH** blocks | not raw MT · 非直译终态 |
   | Summarize · 摘要 | `report-summaries/*-Summary.md` | stance from mechanism · 立场来自机制 |
   | Index · 索引 | `synthesis/all-reports-index.md` | fresh `generated_at` · 时间戳刷新 |

7. **Falsifiability + limitations** — the summary's closing line names one
   observation that would refute the one-line conclusion; thin OCR/scan extractions
   carry an explicit confidence caveat in YAML or body. A surprising headline
   number that will anchor the stance may be triangulated against a live source
   before it is trusted (the full triangulation discipline lives in
   `vd-synthesis-refresh`; here it is a spot-check, not a mandate).
   **可证伪 + 局限**——摘要收束行点明一条将推翻一句话结论的观察；OCR/扫描提取
   稀薄时在 YAML 或正文写明置信度局限。会锚定立场的反常 headline 数字，可在采信前
   对照在线来源抽查（完整三角验证纪律在 `vd-synthesis-refresh`；此处只是抽查，
   非硬性要求）。
   - e.g. *"If 2Q26 DRAM contracts print negative QoQ, the structural-tightness
     thesis fails for H2."*
     范例：*"若 2Q26 DRAM 合约价 QoQ 转负，H2 结构性紧张论题即失败。"*

8. **Index coda, not synthesis coda** — ingest ends at `scripts/index.py`; full
   cross-report audit or rolling window is a separate task — run only when the
   user asks, not on every single file.
   **索引收束，非综合收束**——入库止于 `scripts/index.py`；跨报告审计或滚动窗口
   是独立任务——仅在用户要求时运行，非每文件自动触发。

9. **Interpretive output on agent token** — retranslation (filling EN/ZH blocks)
   and `-Summary.md` are agent-authored against `*-Bilingual.md`, spending the
   operator's agent token; `scripts/ingest.py` only extracts verbatim text and
   scaffolds empty blocks — it never replaces the agent step. Free Google MT or a
   third-party OCR plugin is not a shippable final state.
   **解读产出用 agent token**——重译（填 EN/ZH 块）与 `-Summary.md` 由 agent 对照
   `*-Bilingual.md` 执笔，消耗操作者 agent token；`scripts/ingest.py` 只逐字提取并
   scaffold 空块——不替代 agent 步骤。Google 免费机翻或第三方 OCR 插件不是可交付终态。
   - ✓ Agent reads `*-Bilingual.md`, writes the summary, fills empty EN/ZH blocks,
     marks `translation: professional human-quality retranslation`.
     Agent 读 `*-Bilingual.md`、写摘要、填空块，并标 `professional human-quality retranslation`。
   - ✗ `deep_translator.GoogleTranslator` (or any free MT) as the final bilingual
     or summary text; batch-summarizing via an external MT script.
     以 Google 免费机翻作为双语/摘要终态；用外部 MT 脚本批量生成摘要。

---

## Image / scan variant | 图片与扫描变体

When `fitz` returns no text (scan PDF, JPG, PNG, long screenshot): **agent vision
transcription**, not a plugin. JPG/PNG are read directly; a scan PDF is rendered
to one PNG per page (`fitz` `get_pixmap`, ~2× zoom) which the agent then reads.
Transcribe into page-shaped blocks → same front matter schema → tag
`extraction: agent vision transcription / infographic` → lower confidence if
numbers are unreadable. Do **not** use free Google MT or third-party OCR plugins
for shippable bilingual or summary artifacts; the render PNGs are scratch — delete
them after transcription, never commit them under `scripts/` or the corpus dirs.
当 `fitz` 无文本（扫描 PDF、JPG、PNG、长截图）：由 **agent 视觉转写**，而非插件。
JPG/PNG 直接读；扫描 PDF 先逐页渲染为 PNG（`fitz` `get_pixmap`，约 2× 缩放）再由
agent 读图。转写为分页块 → 同一元数据 schema → 标
`extraction: agent vision transcription / infographic` → 数字不可读则降置信度。
**不得**用 Google 免费机翻或第三方 OCR 插件作为可交付双语稿/摘要终态；渲染 PNG 是
临时件——转写后删除，不得提交进 `scripts/` 或语料目录。

---

## Self-check | 自检清单

- [ ] Is the intake set closed (one file → one slug, no duplicate)? |
      入库集是否闭合（一文件 → 一 slug、无重复）？
- [ ] Does the slug carry the full title (not truncated at a dot to `YYYYMMDD_<n>`)? |
      slug 是否承载完整标题（未在点号处截断为 `YYYYMMDD_<n>`）？
- [ ] Was extract run before summary, with page markers on every body page? |
      是否在摘要前先提取，且每个正文页有页标记？
- [ ] Does published bilingual MD carry `professional human-quality retranslation`? |
      发布的双语 MD 是否标注专业人工重译？
- [ ] Does every summary claim map to a page in the bilingual file? |
      摘要每条主张是否可映射到双语文件某页？
- [ ] Is `stance` derived from mechanism, not headline mood alone? |
      `stance` 是否来自机制，而非仅标题情绪？
- [ ] Was `scripts/index.py` run with a fresh `generated_at`? |
      是否已运行 `scripts/index.py` 且时间戳已刷新？
- [ ] Does each summary name one falsifier for its one-line conclusion? |
      每份摘要是否为一句话结论点明一条证伪条件？
- [ ] Was cross-report synthesis deferred unless explicitly requested? |
      跨报告综合是否仅在明确要求时才运行？
- [ ] Were summary and retranslation written by the agent (not free Google MT)? |
      摘要与重译是否由 agent 执笔（非 Google 免费机翻）？
