**Updated recommendation: weak reject, with substantially improved evidential transparency.** At `c7e3e8e`, I assess **9 round-1 findings as fixed, 4 as partly fixed, and 1 as open**. The central science adjudications are now inspectable and supported. The remaining major objection concerns the empirical contribution, rather than incorrect headline arithmetic.

I reviewed the diff against the claims ledger, reports, registrations and mirrored records. No files were modified.

1. **R1-2 — Open. Major. The paper still measures configuration-dependent operating points without establishing a ceiling or comparative diagnostic ability.**

   The title still promises a ceiling at [tex/paper.tex:27](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:27), and the contribution still promises measurement of an auditor’s “limit” at [tex/sections/introduction.tex:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:50). The manuscript correctly admits that no matched-false-positive comparison exists at [tex/sections/discussion.tex:37](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:37).

   **Records involved:** `records/code/ceiling/numbers.json`, `records/code/threshold_sweep.json`, `reports/RESULTS-SWEEP.md`, and `manuscript/CLAIMS.md` C1–C2/C9. Nothing in the repairs resolves the distinction between any BLOCKER and a correct diagnosis, or the model/sampling/false-positive confounding. This remains the main reason for weak reject.

2. **R1-14 — Partly fixed. The new study map helps navigation but introduces factual errors.**

   Three cells need correction:

   - [tex/appendix/results_full.tex:51](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:51) gives **both stronger models \(K=8\)**. `self-strong` had eight readings; `self-frontier` had **four**. The primary \(K=8\) contrast concerns `self-strong`, not both models. **Records:** `plan/studies/ceiling3-PREREGISTRATION.md:30`, `reports/RESULTS-CEILING3.md:46`, `records/code/ceiling3/numbers.json`.
   - [tex/appendix/results_full.tex:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:53) lists only **56 defective instances**, while the revision experiment also includes **56 correct instances**. Its overall pass-rate outcome uses **112 instances**; the 56-instance population applies to the defective-stratum flag contrast. **Records:** `plan/studies/ceiling-PREREGISTRATION.md:230`, `records/code/ceiling/numbers.json`, and Table 1.
   - [tex/appendix/results_full.tex:59](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:59) calls the endpoint “share of wrong tests retained.” The registered endpoint is the **fraction of retained failing test applications that are wrong**. These reverse the conditioning. Rule A is **11/90**, not the wrong-application retention fraction **11/18**. **Records:** `plan/studies/testgen-PREREGISTRATION-VAL.md:126`, `records/code/testgen-val/tables.md:6`.

   The provenance narrative also remains largely unchanged, so the original writing concern is only partially addressed.

   I checked all population, intervention, endpoint and status cells. The complete row assessment is:

   | Study-map row | Assessment of its cells | Controlling records |
   |---|---|---|
   | Repeated reading, line 50 | Consistent for the selected cross/self comparison. | `code/ceiling/numbers.json`; ceiling registration; C1/C5 |
   | Stronger routes, line 51 | Population correct; reading budget wrong; primary endpoint needs restriction to `self-strong`. | `code/ceiling3/numbers.json`; ceiling3 registration; C2 |
   | Decision-rule sweep, line 52 | Consistent, including no calls and unregistered status. | `code/threshold_sweep.json`; `RESULTS-SWEEP.md`; C11 |
   | Rulebook revision, line 53 | Population incomplete; registered outcomes versus exploratory flags correctly distinguished. | `code/ceiling/numbers.json`; ceiling registration; C3 |
   | Referent rule, second family, line 54 | Consistent. Registration includes both referent and grading interventions. | `code/ceiling3b/numbers.json`; ceiling3b registration; C8 |
   | Referent rule at \(K=8\), line 55 | Consistent. | `code/ceiling4/numbers.json`; ceiling4 registration; C9 |
   | Residual rating, line 56 | Consistent for the primary 57-instance residual. | `code/rerate/`; rerate registration; C4 |
   | Outside rater, line 57 | Consistent as a study-level summary. “Entries” correctly avoids implying 121 unique instances. The method’s earlier specification remains a qualification. | `code/rate3/analysis.json`; P3 Amendment 1; C12 |
   | Specification edit, line 58 | Consistent for the final 32 selected instances; “same-length” means the registered ±15% band. | `code/clarify/`; P3 registration; C13 |
   | Test validation, line 59 | Endpoint denominator wrong. Population should explicitly include visible-test-failing candidates; intervention and failure status otherwise correct. | `code/testgen-val/`; testgen validation registration; C7 |
   | Injected defects, line 60 | Consistent, particularly “descriptive only.” | `code/inject/`; injection Amendment 7; C10 |
   | Flags on correct code, line 61 | Broadly consistent; specify that the endpoint is the share **among flagged instances** with an extracted reference disagreement. | `code/fpadj/adjudication.json`; fpadj registration §Outcome; C16 |
   | Second substrate, line 62 | Consistent with closure and no admitted quantitative result. | `RESULTS-SUBSTRATE2.md`; substrate2 registration Amendment 8 |

   Record paths in this table are under `records/`; registrations are under `plan/studies/` except P3.

3. **R1-4 — Partly fixed. The sensitivity is correctly added, but the conclusion overcorrects.**

   [tex/sections/ai4s.tex:82](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:82) accurately reports **70/70 versus 68/70**, with **0/70 versus 12/70** clean flags after excluding the four tolerance cases. However, “where the code can be run, running it is the stronger check,” also promoted into [tex/paper.tex:60](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:60), exceeds that conditional result.

   **Records involved:** `records/ai4s/results_posthoc.json`, `reports/RESULTS-AI4S-RESULTS.md:58` and `:123`. On the registered population, the flag counts are **70/74 for re-execution versus 72/74 for the model**, with four versus two discordant catches and \(p=0.6875\). Moreover, eight model flags on nominally clean items identify real construction defects.

   State that re-execution performs better **on this sensitivity subset for the injected numerical faults**, rather than asserting general superiority whenever execution is possible.

4. **R1-5 — Partly fixed. Semantic verification is substantially repaired; self-contained reproduction is not.**

   The claim at [tex/appendix/reproducibility.tex:16](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/reproducibility.tex:16) is now substantially justified for the science BLOCKER adjudications. The audited artefacts and BLOCKER texts permit independent checking of the central counts.

   Two limitations remain:

   - The mirrored `runs/analysis/pending/posthoc_results.py` is an older script with external paths and a missing `report_ceiling` import location. Its output construction at [posthoc_results.py:98](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/runs/analysis/pending/posthoc_results.py:98) does not produce the final fabrication-adjudication or sign-flip blocks. The adjacent pending JSON likewise lacks them.
   - The reports’ final `posthoc_data.py`, `clean_flag_exemplars.py`, and other science analysis scripts are not mirrored here. Also, “every reading’s findings” is too broad: rows preserve BLOCKER texts but can record additional findings without their text, for example [data_audit/cross.d4.jsonl:139](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/runs/data_audit/cross.d4.jsonl:139).

   **Records involved:** `records/ai4s/results_posthoc.json`, `records/ai4s/runs/analysis/pending/`, and the analysis provenance at the start of all three science reports. Distinguish the final records from historical snapshots, and describe the archive as retaining BLOCKER observation texts.

5. **R1-6 — Partly fixed. SciCode selection is now disclosed, but the qualitative sample still loses one consequential restriction.**

   The new exclusion count, earlier-chain failure counts and clean-chain sampling description at [tex/sections/ai4s.tex:33](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:33) and [:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:54) agree with the records.

   Neither this paragraph nor its appendix counterpart says that **four of the twenty sampled findings concern earlier functions explicitly excluded from the deliverable**. Also specify “the first BLOCKER of the first flagged reading.”

   **Records involved:** `reports/RESULTS-AI4S-CODE.md:111`, especially `:118`; `records/ai4s/code_posthoc_b.json`; `plan/studies/ai4s/PREREGISTRATION-CODE-B.md`. Passing earlier tests does not make those functions part of the requested deliverable.

6. **New, minor archive issue — the mirror is not free of personal identifying information.**

   [records/ai4s/runs/execution.jsonl:193](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/runs/execution.jsonl:193) and eleven other error records contain **17 occurrences of a local home-directory path identifying the username**. These are traceback paths, not scientific observations.

   I scanned the 2,018 files in the newly mirrored directories for common credential formats, credential assignments, bearer tokens, authenticated URLs, email addresses and personal-path indicators. **I found no credentials or email addresses.** I cannot certify absence of every possible secret, and the personal-path finding means “contains no personal data” would be false. Redact those path prefixes in a distribution copy.

The other nine round-1 findings are fixed:

| Round-1 finding | Status and verification | Manuscript location and controlling record |
|---|---|---|
| **1. Residual label** | **Fixed.** Operational non-entailment, contradiction and first failing input are now distinguished. | [sections/ceiling.tex:65](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:65); `plan/studies/rerate-PREREGISTRATION.md:32`, `records/code/rerate/{L1,L2}.csv`, C4 |
| **3. Deterministic zero clean flags** | **Fixed.** The construction qualification now accompanies the headline and discussion. | [sections/discussion.tex:19](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:19); `PREREGISTRATION-RESULTS.md:51`, `RESULTS-AI4S-DATA.md:25` |
| **7. Cross-row generalization** | **Fixed.** Restricted to duplicated rows and shuffled targets in these runs; 28 is correctly identified as a subset of 48 misses. | [sections/discussion.tex:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:18); `records/ai4s/data_posthoc.json`, `RESULTS-AI4S-DATA.md:88` |
| **8. Amendment chronology** | **Fixed.** The 30 pre-amendment draw-2 readings are explicitly disclosed. | [appendix/method_full.tex:165](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/method_full.tex:165); ceiling3 registration Amendment 2, `RESULTS-CEILING3.md:3` |
| **9. Scientific residual reliability** | **Fixed.** Both cluster counts, intervals and κ values match the records; the appendix adds sheet limitations and three changed repeat labels. | [appendix/ai4s_full.tex:63](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:63); `residual_results.json`, `residual_b_results.json`, `RESULTS-AI4S-CODE.md:147` |
| **10. Surviving-label condition** | **Fixed.** It now accompanies the discussion’s adjudication figures. | [appendix/discussion_full.tex:97](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:97); `RESULTS-CEILING4.md:262`, C9 |
| **11. Scope-failure attribution** | **Fixed.** Workflow discovery is separated from correct model findings. | [sections/discussion.tex:31](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:31); data registration Amendment 2 |
| **12. Coverage, families, Figure 1** | **Fixed.** Coverage 0.87 at 0.05 is correct for P; six configurations use five models; Figure 1 now reads the canonical endpoint intervals. | [appendix/discussion_full.tex:146](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:146), [figures/src/make_figures.py:48](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/figures/src/make_figures.py:48); `coverage_simulation.json`, `RESULTS-DERIVED.md:14`, `code/ceiling/numbers.json` |
| **13. Rulebook narrative** | **Fixed.** The \(K=8\), 110-instance contrast leads, includes its false-positive cost, and is separated from the exploratory revision-study flags. | [sections/ceiling.tex:57](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:57); `code/ceiling4/numbers.json`, `code/ceiling/numbers.json`, C3/C9 |

The science archive supports the specific post hoc claims as follows:

- **21 sound fabrication catches:** I inspected the 23 flagged fabrication cases and checked the underlying numerical calculations against the archived programs and inputs. The two exclusions are supported by the raw findings at [cross.d2.jsonl:48](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/runs/results_audit/cross.d2.jsonl:48) and [:114](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/runs/results_audit/cross.d2.jsonl:114). Their actual outputs are approximately \(-1.35921\times10^{-6}\) and \(-1.61598\times10^{-7}\), contradicting the auditors’ arithmetic. The other 21 have fault-specific support.
- **18 fault-relevant data catches:** All 18 IDs in [data_posthoc.json:38](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/data_posthoc.json:38) have archived findings identifying the corrupted quantity or its invalid values, consistent with the injection manifests: **nine mixed-unit and nine swapped-column items**, all missed by the validator. “Fault-relevant” is supported; these texts do not uniformly recover the exact injection mechanism.
- **Clean-item adjudications:** The results archive supports the eight construction-defect versus four erroneous-flag classification. All **48** data refutation exemplars match their raw BLOCKER text, and their claimed file facts check against the CSVs. The separate 12 delivery disputes remain appropriately excluded from that count.

I also verified complete, nonduplicated production-reading grids, all 280 data-file hashes and row counts, and the principal science flag totals. Table 1 regenerated byte-for-byte in memory, and the manuscript’s mechanical checks passed. I did not run the writing `reproduce.sh` pipeline.

**The single change that would most improve the paper remains a held-out scientific-audit experiment measuring correctly diagnosed faults at a prespecified, matched false-positive budget, with independent human or executable adjudication.** That would add the comparative evidence the current descriptive measurements and improved disclosures still cannot supply.
