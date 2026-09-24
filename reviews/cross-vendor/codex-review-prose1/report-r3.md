Reviewed `932d7de..25744b9` against both round-1 reports, round 2, `manuscript/CLAIMS.md` including its must-not-appear list, the study reports and records. No files modified. All five round-2 points are fixed; I found no new error introduced by the repairs.

1. **Clarification successes’ oracle agreement — fixed.**  
   [tex/appendix/discussion_full.tex:75](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:75) now correctly separates six consistent additions, one broadened precondition and two partly contradictory additions, with no diagnosis gain among the 23 wholly contradictory additions. It explicitly says the classification followed observation of the outcomes and retains the selected-population limitation.

   Records involved: `records/code/clarify/clarification_classification.json`, `h3.json`, and `reports/RESULTS-CLARIFY.md:55`. The two partial cases are indeed `b1:Mbpp/559` and `b2:Mbpp/559`. The accompanying changes to “did not wholly contradict” at [ceiling.tex:83](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:83) and [results_full.tex:412](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:412) are accurate. They no longer imply complete consistency and do not establish underdetermination as the cause of the original misses, which C13 prohibits.

2. **Fabrication adjudication’s post-hoc qualification — fixed.**  
   [tex/paper.tex:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:54) now attaches “on post hoc inspection” directly to the two wrong calculations.

   Record involved: `records/ai4s/results_posthoc.json`, `fabrication`. It records 23 flagged fabrications, 21 with sound rationale, and two unsound cases, `32.1.s3` and `70.5.s1`. The wording matches C18 and preserves the distinction between flagging and correctly identifying a fault.

3. **Reports-a-failure intervals — fixed.**  
   [tex/appendix/results_full.tex:292](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:292) now reports **3/110, 2.7% [0.0, 7.3]**, and **27/110, 24.5% [14.4, 35.7]**.

   Records involved: `reports/RESULTS-CEILING3B.md:82` and the study worktree’s `records/ceiling3b/numbers.json`, `H19d.strict_reports_a_failure_POST_HOC.by_arm.{S,R}.reports_failure_rate_over_all_P`. I checked both intervals against that record. Attribution to the referent rule, the post-hoc label and the prohibition on interpreting this as defect recognition all remain.

4. **Opening terminology and the twenty-reading reference — fixed and verified.**  
   [tex/sections/introduction.tex:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:2) replaces the unexplained family/route terminology with a true statement. For `b1:Mbpp/102`, I checked **all twenty readings**: eight cross, eight self and four astra. Every reading has zero model findings.

   Records involved: inherited `study1/arm-{cross,cross-replicate,self}.jsonl:63`, `study2/arm-holistic-{cross,self}.jsonl:7`, and the remaining `ceiling/records/cache/holistic__*` rows. `manifest_ceiling1.json` identifies three distinct models: `gpt-5.6-terra`, `claude-haiku-4-5-20251001` and `gpt-6-astra`.

   **“Those twenty readings” at [introduction.tex:34](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:34) correctly identifies the residual’s reading schedule.** Reconstructing that pool across all 110 defective instances gives 53 flagged and **57 never flagged**. This is C4’s residual, not the eight-reading shipped-route residual or the later forty-reading residual. `rerate/numbers.json` supplies the retained 44/57 and interval; both rating sheets label the opening instance, `Q038`, `ambiguous-oracle`.

5. **Contribution sentence’s causal ambiguity — fixed.**  
   [tex/sections/introduction.tex:55](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:55) now separates controlled and route contrasts from the specification association, explicitly calling the latter “not a tested cause.” This agrees with C4/C13 and the prohibited-claims list. The preceding text retains the model/sampling confound.

Nothing from rounds 1 or 2 remains open within this prose-review scope. The earlier fixes retain the scientific-code intervention bundle and no-tests condition, qualified route comparisons, flag-versus-recognition distinction, two-tier study scope, unresolved revision outcome, and conditional interpretation of clean-item flags. Relocated numerical results remain in the cited body sections with the previously requested intervals and qualifications. The appendix’s comparator and validation-threshold references remain explicit, and the earlier readability repairs have not regressed.

**accept revision** — the principal remaining factual error is repaired: the nine clarification successes are now accurately described as including two partly contradictory additions.
