Reviewed `932d7de`, including repairs `84ad0de` and `1eb87d0`, against both round-1 reports, `manuscript/CLAIMS.md`, the study reports and records. No files changed. The principal main-body repairs work, but the appendix qualification repair remains factually too strong.

Three issues remain, most severe first.

1. **The nine successful specification edits were not all non-contradictory.**  
   [tex/appendix/discussion_full.tex:76](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:76)

   “In each of the nine instances whose diagnosis changed, the added rule did not contradict the hidden suite” fixes the antecedent but preserves an inaccurate qualification. The nine comprise six fully consistent additions, one broadened precondition, and **two additions that partly contradict the oracle**.

   The two partial cases are `b1:Mbpp/559` and `b2:Mbpp/559`. For example, the first addition requires a maximum sum of 5 on its fifth archived input, whereas the oracle expects 0. This is explicit in `records/code/clarify/clarification_classification.json`, C13 and `reports/RESULTS-CLARIFY.md`. The manuscript itself correctly acknowledges the two partial contradictions at `tex/appendix/results_full.tex:439`.

   **Appendix round-1 finding 3 is only partially fixed.** The round-1 suggested repair was itself insufficient. Say that diagnosis increased on six consistent additions, one precondition-broadening addition and two partly contradictory additions, versus none of the 23 classified as contradictory. Preserve that this classification was post hoc. The same overstatement survives at `tex/sections/ceiling.tex:83`.

2. **The abstract drops the post-hoc qualification when compressing the fabrication result.**  
   [tex/paper.tex:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:54)

   “Twice on a wrong calculation” restates the adjudication behind the former “21 for the right reason, post hoc,” but removes its label. The earlier “post hoc rating” at line 51 concerns specification determinacy and cannot qualify this separate result.

   Record involved: `records/ai4s/results_posthoc.json`, `fabrication`, which records 23 flagged, 21 with sound rationale and two unsound cases. C18 and the ledger’s opening rule require the qualification.

   Add “on post hoc inspection,” or remove this detail from the abstract and retain the correctly qualified body account.

3. **The repaired reports-a-failure sentence still omits available intervals.**  
   [tex/appendix/results_full.tex:292](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:292)

   Attribution is now correct, but `3/110` and `27/110` remain interval-free despite the ledger’s reporting rule. These are **2.7% [0.0, 7.3]** and **24.5% [14.4, 35.7]**, respectively, using the primary problem-cluster intervals.

   Records involved: `reports/RESULTS-CEILING3B.md`, Table 5b; the study worktree’s `records/ceiling3b/numbers.json`, `H19d.strict_reports_a_failure_POST_HOC.by_arm.{S,R}.reports_failure_rate_over_all_P`.

   This omission is inherited, not introduced by the repair. Keep the existing post-hoc label and explicit prohibition on interpreting these counts as defect recognition.

The disposition of every numbered round-1 finding is below. “Fixed” refers to the original finding; the additional issues above are separate.

| Round-1 finding | Disposition at `932d7de` | Current location and evidence |
|---|---|---|
| Main 1 — attributing scientific-code change to naming alone; missing “no tests shown” | **Fixed.** The introduction names the bundle; the body retains sequential execution and registration after A’s outcomes. | `introduction.tex:45`; `ai4s.tex:35,48`. C19; `code_results_b.json`; `RESULTS-AI4S-CODE.md`. |
| Main 2 — stronger-model interval and exploratory label | **Fixed by relocation.** Both survive in the cited body section. | `ceiling.tex:46–52`. C2/C11; `records/code/ceiling3/numbers.json`. |
| Main 3 — “catch” conflating flags with identified defects | **Fixed at the cited locations.** The abstract and introduction define the union through flags; scientific code reports union recall. | `paper.tex:46`; `introduction.tex:29`; `ai4s.tex:50`. C11/C19; sweep and scientific-code records. |
| Main 4 — opening example exceeds evidence | **Fixed.** The conclusion is now attributed to two model raters and the hidden-test definition. | `introduction.tex:8`. C4; rerating key `Q038`, both label files, clarification record. |
| Main 5 — implying all three science studies compare tiers | **Fixed.** The introduction identifies results and data as the paired-tier studies. | `paper.tex:51`; `introduction.tex:38`. C17–C19; the three science reports. |
| Main 6a — unresolved outcome improvement presented as no change | **Fixed.** “Not established” accurately accompanies +5.4 [−0.9, +12.1]. | `ceiling.tex:61`. C3; `ceiling/numbers.json`, `referent-loop__vs__cross-loop`. |
| Main 6b — false-positive rate necessarily “measures the evaluator” | **Fixed.** “Can include valid findings” preserves the distinction between construction defects and wrong findings. | `introduction.tex:63`. `results_posthoc.json`, eight correct and four wrong clean-item flags. |
| Main 7 — interval-free science headline figures | **Fixed at the cited abstract/introduction locations by relocation.** | `ai4s.tex:43,102`. C17/C19; `code_results{,_b}.json`, `data_results.json`. |
| Appendix 1 — referent result attached ambiguously to grading intervention | **Attribution fixed.** Both passages explicitly name the referent rule. Interval omission remains as finding 3 above. | `results_full.tex:292,299`. C8/C9; Ceiling 3b Table 5b and Ceiling 4 records. |
| Appendix 2 — unspecified eight-reading comparator | **Fixed.** Both arms, the counting rule and eight-reading depth are explicit. | `results_full.tex:300`. C9; `ceiling4/numbers.json`, `primary_H20a_crossR_minus_cross_P`. |
| Appendix 3 — unclear antecedent for nine successes | **Partially fixed.** The antecedent is clear; the qualification is false for two successes. | `discussion_full.tex:76`. C13; clarification classification record. |
| Appendix 4 — unclear validation-threshold reference | **Fixed.** “That validation criterion” retains the application-level unit and frozen population. | `related_full.tex:55–58`. C7; `RESULTS-TESTGEN-VAL.md`; study record `rules.A/B.primary`. |

The numerical relocation did not discard results:

- **Stronger model and rulebook**, [ceiling.tex:46](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:46): −26.4 [−37.3, −15.6], 3.3% [0.7, 6.7], exploratory any-finding reversal, and sampling qualifications remain. The rulebook’s +26.8 [13.6, 40.4], correct-code cost +12.5 [−3.6, +26.8], one-reading/56-instance scope and unresolved revision outcome remain at line 57.
- **Scientific code**, [ai4s.tex:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:43): all four removed rates remain with intervals: 87.7% [72.7, 98.6], 68.7% [56.6, 79.7], 72.8% [59.3, 87.3] and 36.0% [26.4, 45.6]. The bundled intervention and sequential-arm qualifications remain.
- **Scientific results**, [ai4s.tex:79](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:79): the 49/25/23/21 accounting survives, with the sound-finding count labelled post hoc and the combined-workflow limitation stated.
- **Scientific data**, [ai4s.tex:102](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:102): 92/140, 65/140 and 112/140 retain their intervals, including 80.0% [73.6, 86.4] for the union and 2.9% [0.7, 5.7] on clean items. The within-dataset uncertainty limitation and post-hoc 61/110 fault-relevant accounting remain. The latter counts have no intervals supplied in `data_posthoc.json` or its report.

On the fresh ICML reading, the numerical overload is substantially improved. The opening’s actual-versus-expected output is clear; I confirmed the selected `b1:Mbpp/102` instance has zero findings across all 20 readings and both raters label it undetermined. The vendor/control distinction, data paragraph and shortened review history also address their round-1 readability findings.

Two places still interrupt the argument:

- **The opening defines “family” using another unexplained term, “route.”** At [introduction.tex:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:2), “In one audited instance, none of twenty readings across three model configurations flagged the program” would introduce the observation directly. The ceiling cache and inherited study-1/study-2 readings support it.
- **The contribution sentence blurs intervention and association again.** At [introduction.tex:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:54), “each of these moves the rate” includes the immediately preceding post-hoc specification association. That makes the reader reconsider line 27’s explicit denial of a tested cause. C4/C13 and the must-not-appear list support separating the claims: the controlled contrasts change flag rates; the residual analysis describes an association with specification determinacy.

**revise** — the most important reason is that the appendix repair explicitly says all nine successful specification edits avoided contradicting the hidden suite, whereas the records identify two partly contradictory successes.
