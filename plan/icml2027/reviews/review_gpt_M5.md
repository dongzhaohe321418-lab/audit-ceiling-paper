**I retain 7/10, with stronger support than M4.** E14 is credible evidence that preference survives shared surrounding code. It does not establish independence from implementation form. No files changed.

**A. Verification and corrections**

I reproduced every E14 number in the specified paper passages from individual readings:

| Quantity | Verified result, percentage points |
|---|---:|
| Construction; valid scheduled readings | 38/41 units; 1,216/1,216 |
| Matched preference | +28.9 [14.5, 42.8] |
| Worst-case imputation across all 41 units | **+19.5 [2.4, 35.4]** |
| Fresh original preference | +26.3 [14.5, 38.2] |
| Matched minus original preference | +2.6 [−3.9, 9.2] |
| More-conditionals stratum, 20/20 units | +40.0 [23.8, 57.5] |
| Other stratum, 18/21 units | +16.7 [−4.2, 36.1] |

**No numerical mismatches.** Corrections concern scope and reporting. Paper paths below are relative to `audit-ceiling-paper/tex/`.

| Location | Finding and exact correction |
|---|---|
| `paper_v3.tex:63`; `sections/e6.tex:104` | **Identify the complete-case population.** Abstract: “and by 28.9 points among 38 of 41 units in a preregistered control sharing all code outside one branch body.” Main text: insert “among 38 of 41 units” after the E14 estimate. |
| `appendix/e6_protocol.tex:216` | **“Computes exactly what A and B compute” exceeds finite, tolerant execution checks.** Replace with “agrees with A and B, respectively, in execution status and returned value under E6’s comparator on every registered admission input”. |
| `appendix/e6_protocol.tex:221–223`; `:321` | **Distinguish the estimate displayed from the statistic supporting the verdict.** Report “Complete cases: +28.9 [14.5, 42.8], n=38; worst-case imputation: +19.5 [2.4, 35.4], n=41; supported.” The current verdict is correct; its table presentation hides the registered decision criterion. |
| `appendix/e6_protocol.tex:225` | **Registered body-size reporting is absent** (`PREREGISTRATION-E14.md:53–54`). Add: “Branch-body source-line spans had medians 1/1 and maxima 10/3 for M_A/M_B; M_A’s body was longer in 9 of 38 pairs.” This quantifies the residual mismatch. |

The appendix’s final interpretation is appropriately narrow. The +2.6 interaction interval establishes neither zero change nor equivalence.

One **M4 carry-over** remains at `sections/e6.tex:119`: replace the inference about auditors’ reading ability with “The controls show that these auditors can discriminate clear misreadings, although they are not matched to the open units in difficulty.”

**B. Integrity**

- **Freeze chronology is supported:** P15 redesign `fea555a` → P16 repairs `7be8b95` → construction/freeze `559abb1` at **05:25:19 UTC** → earliest timestamped held-out GPT thread **05:25:24.420** → results `23ed980`. At the freeze commit, audit files contain development rows only. Frozen source, corpus, construction and program hashes match; all **1,216 rebuilt prompt hashes** and completeness checks pass. The marker itself is untimestamped, so it is not independent timing evidence.
- **Third attempt is legitimate:** `Mbpp/576`, M_B, Claude-high, reading 0 had two malformed JSON replies followed by a valid reply. E6’s pre-existing registration permits three attempts. All three replies express BLOCKED; the companion reading already flags, so this retry does not change the cell’s flag outcome. Raw-parser replay matches every recorded decision.
- **Missing units are handled defensibly:** Mbpp/472, /740 and /558 each exhausted three parse-failed construction attempts. All enter the primary worst-case bootstrap as −1; its lower endpoint remains positive. All three belong to the other-conditionals stratum, whose reported interval is complete-case only.
- **Minor resilience gap:** raw audit rows still lack `split`, making that closure fallback ineffective without the marker or parsed rows. Neither safeguard is missing here.

**C. Scores and remaining priority**

| Soundness | Presentation | Significance | Originality | Overall | Confidence |
|---:|---:|---:|---:|---:|---:|
| 3/4 | 3/4 | 3/4 | 3/4 | **7/10** | 4/5 |

The control materially strengthens acceptance; residual body-form differences and model-dependent admissibility judgements prevent an upgrade.

**Single highest-value change:** complete the rule × presentation crossing **inside the differing branch body**. Give both rules ordinary and conspicuous implementations under symmetric constraints, execution-check and freeze them before fresh audits, then estimate the rule effect and interaction with missing-unit bounds. Existing tasks suffice; no human raters or downloads are needed. This directly addresses what E14 still leaves unresolved.