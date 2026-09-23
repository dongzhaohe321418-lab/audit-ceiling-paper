**Not quotable as written.** The registered flag-rate arithmetic largely reproduces, but the report treats flags unrelated to the injected fault as evidence of fault detection. I reviewed `4ccdd84` without modifying files, using independent calculations rather than running the study’s analysis or builder.

1. **Two of the 20 “additional catches” do not identify a data fault.**

   The sole BLOCKER for [`airfoil.F1.1`, draw 4](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/cross.d4.jsonl:107) concerns missing column descriptions. The same is true for [`airfoil.F1.2`, draw 2](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/cross.d2.jsonl:108). Their injected faults affect chord length and frequency, respectively; their cards are identical to the clean airfoil cards.

   Consequently, **20 additional flagged items is correct; 20 additional fault detections is not**. Excluding these two documentation-only cases leaves 18 fault-relevant additional flags: nine F1 and nine F5. The registered union remains **112/140 = 80.0%**; an explicitly post hoc exclusion of those two yields **110/140 = 78.6%**. These must not be conflated. This affects the central interpretation in [RESULTS-DATA.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s/benchmarks/ai4s/RESULTS-DATA.md:114).

2. **The documentation-derived baseline omits a documented range.**

   Concrete’s source README explicitly gives **Age: 1–365 days**, also present on the [UCI page](https://archive.ics.uci.edu/dataset/165/concrete-compressive-strength). Yet [the frozen specification](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s/benchmarks/ai4s/data_spec.py:30) sets concrete’s ranges to `{}`, and its card leaves Age’s range blank.

   This matters: `concrete.F5.4`, counted as LLM-only, has Age values **594–945 days**. Adding this source-documented check alone would raise validator recall from **92/140 = 65.7%** to **93/140 = 66.4%**, with no additional clean flags, and reduce the registered LLM-only set from 20 to 19.

   Also, the cards never declare columns “continuous”; the validator receives that information through private specification lists. “Frozen before item construction” is supported. “From the card alone,” complete coverage of source-stated ranges, and independence from knowledge of the fault design are not established by that timing.

3. **The clean-flag adjudication is not reliable enough to quote.**

   I read all **four `cross` and 304 `self` clean-item BLOCKER texts**. The reported item totals reproduce: `cross` 4; `self` 67, comprising superconductivity 34, concrete 26 and power plant 7.

   For `cross`, all four flags concern documentation, but “all four … true remarks” overstates their accuracy. The findings for `airfoil.clean.11` and `.33` complain that the card does not identify or describe scaled sound pressure as the target. [The card explicitly states “Target column: scaled_sound_pressure_dB”](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_items/airfoil.clean.11/CARD.md:17), and its opening sentence describes the sound-pressure measurement. A request for fuller definitions is defensible; declaring the whole observation true is not.

   For `self`, the classification file contains exactly **62 `false-claim` labels**, but four of its five supposedly documentation-only items contain objectively incorrect row counts:

   | Item | Finding claims | Actual |
   |---|---:|---:|
   | `concrete.clean.9`, d2 | 130 data rows | 120 |
   | `concrete.clean.33`, d3 | 129 data rows | 120 |
   | `ccpp.clean.18`, d2 | 119 data rows | 120 |
   | `supercond.clean.1`, d1/d3 | 101/100 data rows | 120 |

   Conversely, items such as `concrete.clean.7` and `.28` are labelled false claims although their observations principally concern blank range cells and disputed documentation requirements. Some findings explicitly retract their initial allegations. The classification needs an observation-level distinction between false file facts, invented requirements, documentation judgments, retracted assertions and actual anomalies; I would not replace 62 with another purportedly definitive total without that rubric.

   The report’s rebuttal that **“both files were committed in every reading” is itself false**. [The runner](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s/benchmarks/ai4s/data_audit_run.py:176) passes an in-memory path-to-bytes mapping with an all-zero SHA; it does not commit the files. Their complete contents were supplied as named increment artifacts. That supports rebutting “absent from the increment,” but not asserting actual Git commits.

4. **The amendment history supports the instrument fixes, but contradicts the claimed analysis chronology.**

   Times below are UTC+8 on September 23:

   | Event | Commit/evidence | Assessment |
   |---|---|---|
   | Original registration | `7eb5eae`, 23:10:27; pilot starts about 23:12:22 | Precedes recorded model calls. |
   | Amendment 1 | `64fd36d`, 23:13:32; next calls start about 23:13:40 | Precedes subsequent calls. However, the same commit already includes rebuilt manifest hashes, so it was not committed before the rebuild it governs. |
   | Amendment 2 | `fcf6ac6`, 23:26:37; runner fix `6e6dfb0`, 23:36:13; valid `self` starts about 23:36:18 | Properly precedes valid calls. |
   | Analysis script | `abd2c9b`, 23:45:32 | **278 valid `self` completions already existed.** |
   | Amendment 3 | `28043ec`, 23:59:55 | Before either spending cap was reached; its progress description is inaccurate. |

   Amendment 1’s stated defects are directly supported by the pilot: all three flag the header mismatch; one additionally complains that no audit result was delivered. Amendment 2’s explanation is supported by the scope code and all **313 archived ESCALATE readings**.

   Amendment 3’s approximately **$20.04** checkpoint is supported: the ledger reaches **$20.04137375 at 23:59:27.496**. But `self` was on **draw 3**, not draw 2. At the commit itself, cumulative ledger value was **$20.24095475**.

   The statement “analysis committed before any valid reading existed” is demonstrably wrong in both registration Amendment 3 and the report. The commit message makes the weaker claim “before any valid reading is analysed.” Records do not establish when outcomes were inspected or prove private motivation; I found support for the instrument-fix reasons, but cannot certify “cost alone” or “no outcome computed.”

5. **Construction mostly reproduces, with a real formatting cue and imperfect clean controls.**

   All four ZIP hashes match. The converted source tables match their original spreadsheet/text data numerically. All 280 items reconstruct from their sampled source rows and recorded transformations; all CSV and reading task/program hashes match. Every item has 120 complete rows and a final newline. Cards are identical within dataset. I found no exposed fault label, manifest hash or clean/fault row-order convention in the model prompt.

   However, F1 arithmetic introduces conspicuous floating-point tails:

   - Airfoil F1: **17 cells with ≥14 decimal places**, versus **zero** across all clean airfoil cells.
   - Power-plant F1: **33 such cells**, versus **zero** across all clean power-plant cells.
   - Examples: `1.5268899999999999` and `290.84999999999997`.

   This is an exploitable construction cue beyond the intended unit mismatch. Uniform float casting fixes `800` versus `800.0`, but does not fix this precision cue. There is no evidence establishing whether the model used it.

   The reported **0.02 kg/m³ slag anomaly is real**, with next nonzero source value 11.0. It appears in five source rows and **16 clean items**, not just `concrete.clean.29`; that is the one item whose finding mentions it. Thus “clean” means uninjected and filtered, not independently established anomaly-free.

   One further accounting discrepancy: superconductivity has **66 duplicate full rows**, but the builder selects its 12 columns *before* deduplication and actually removes **84 rows**. The registration’s removal count does not describe the implemented pool.

6. **The numerical analysis is substantially correct, with interpretation limits.**

   My independent recomputation gives the following K=4 counts:

   | Outcome | Validator | Cross | Cross ∪ validator | Self |
   |---|---:|---:|---:|---:|
   | F1 | 6/20 | 17/20 | 17/20 | 15/20 |
   | F2 | 20/20 | 14/20 | 20/20 | 17/20 |
   | F3 | 20/20 | 0/20 | 20/20 | 13/20 |
   | F4 | 0/20 | 0/20 | 0/20 | 9/20 |
   | F5 | 6/20 | 15/20 | 15/20 | 15/20 |
   | F6 | 20/20 | 16/20 | 20/20 | 18/20 |
   | F7 | 20/20 | 3/20 | 20/20 | 10/20 |
   | All faulty | 92/140 | 65/140 | 112/140 | 97/140 |
   | Clean | 0/140 | 4/140 | 4/140 | 67/140 |

   **Every numerical table cell, all 36 Clopper–Pearson intervals, all reported bootstrap endpoints, K summaries and localisation counts in the report reproduce to their displayed decimal.** The LLM-only sets also reproduce exactly under the registered flag rule.

   There is one additional discrepancy in the result JSON, outside the report: `cross/K=1/F6` bootstrap lower endpoint is mathematically **63.75%, rounding to 63.8%**, versus stored **63.7%**. This is floating-point operation order: the study computes `100 × (12.75/20)` as `63.74999999999999`. Difference: **+0.1 percentage point**, a rounding issue rather than a substantive statistical disagreement.

   Union-at-K and exact subset averaging are implemented correctly. The bootstrap resamples items within fixed datasets, using 10,000 replicates and the specified seed. It is **dataset-stratified, not a dataset-cluster bootstrap**; the report should explicitly retain the registered warning about only four datasets. K=1–3 subset summaries are additional analyses, not explicitly specified in the registration.

   The added Clopper–Pearson intervals are numerically correct **binomial** intervals. They should be labelled supplementary/post hoc and should not be presented as resolving dataset-level uncertainty. Fixed dataset/fault strata and their heterogeneous rates do not become an exact binomial sampling design merely by pooling counts.

   Localisation implements the specified substring rule, but calling it “conservative” is incomplete: it can miss paraphrases and count irrelevant mentions. `airfoil.F1.2` is counted as localised because its documentation complaint mentions `frequency_Hz`, despite not identifying the frequency corruption.

7. **The reading and limits need narrower language.**

   Complementarity is supported as a statement about the registered flag sets. “Real value,” “catches,” and fault-detection claims need the qualification in finding 1.

   The statement that `self`’s F4 rate “equals” its clean rate is numerically false: **45.0% versus 47.9%, a −2.9 percentage-point difference**. Similar aggregate rates do not prove absence of detection, and they certainly do not establish that all its higher recall is spurious. For example, `self` correctly identifies the RH sentinel in `ccpp.F6.0`, although some accompanying counts are wrong. Its high clean flag rate and route-specific limitation are well supported.

   The outside citation is real and broadly relevant: [Bendinelli, Dox and Holz](https://arxiv.org/html/2503.06664v1) report difficulties with distribution shifts, trends and biases spanning rows. Their study uses Python-equipped cleaning agents and downstream performance feedback; it does not establish this study’s duplicate-row or shuffled-target mechanism. Here, some successful mixed-unit findings explicitly compare rows. “These two fault types were missed” is supported; a general cross-row incapacity is not.

8. **Spend reproduces; fail-closed budget enforcement does not.**

   Ledger totals are **$13.03308925 cross + $10.89826875 self + $6.600555 void + $0.080755 pilot = $30.612668**, correctly reported as **$30.61**. All 2,240 planned retained readings exist and are `ok`.

   There are 1,126 cross and 1,125 self ledger events, so retained readings are not identical to call counts. The records establish completion of all planned slots, not the broader assertion that no attempted reading was lost.

   Separately, the runner eagerly submits the draw through `ThreadPoolExecutor.map`; returning on a budget check waits for queued work rather than cancelling it. It also tolerates some unpriced events if any event is priced. That is not a fail-closed halt, although **no cap was breached in this study**.

**Not quotable — the single most important reason is that the report presents unrelated documentation flags as additional detections of scientific-data faults.**
