Reviewed `590abaf`, the full manuscript, `87c8db7..590abaf`, the archived reviews and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, residual classifications, clarification adjudication and previous reviews are conflicted. This review independently checks the author’s account, but **does not provide independent-family validation** of those judgments.

The round-7 repairs hold. Two remaining passages give comparisons between changed measurement procedures more explanatory authority than their records support.

1. **R8-1 — Moderate. Figure 3 attributes the larger contrast to the broken control arm without preserving the rerun confound.**

   [results.tex:267](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:267) says the unanswerable control arm “did not produce noise, it produced a larger contrast pointing the way the hypothesis points.” The accompanying discussion at [results.tex:418](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:418) calls this evidence about sheets without stating what else changed.

   **Contradicting record.** [RESULTS-RATE3.md:143](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-RATE3.md:143) explicitly limits the comparison to a descriptive association between **sheet repair and a fresh model run**. It says presentation, sampling and batch context cannot be separated. The observed contrasts, **+54.2 points before repair and +19.8 afterward**, therefore do not distinguish a presentation effect from model-run variation.

   Preserve those observations, including the exact correspondence between missing evidence and abstention. Replace the categorical distinction from noise with the report’s stated limitation. The registered gate still correctly classified the broken result as inconclusive; that procedural success does not identify what caused the contrast to change.

2. **R8-2 — Minor. The residual reclassification is described too specifically as a consequence of changing question order.**

   [results.tex:233](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:233) describes “a classification that reverses when the order of its questions changes.” Together with the preceding account, this foregrounds ordering as the operative difference.

   **Contradicting record.** [RESULTS-RERATE.md:201](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-RERATE.md:201) specifies that **ordering, category definitions and raters/consensus procedure changed together**, and expressly says the study cannot isolate their contributions.

   Describe the reversal between the two classification protocols and name these simultaneous changes. The supported conclusion remains sensitivity to the classification procedure, with **44/57 failing the second rubric’s entailment test**. Neither that count nor its descriptive value needs withdrawal.

3. **R8-3 — Minor, review-record accuracy. The tracker understates round 7’s finding and overstates its closure of round 6.**

   [MASTER-TRACKER.md:153](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/presubmission/MASTER-TRACKER.md:153) calls round 7 “three minor findings” and says all round-6 findings were ruled fixed.

   **Contradicting archive.** [report-r7.md:7](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-paper1/report-r7.md:7) classified R7-1 as **Moderate**. Its [disposition table:46](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-paper1/report-r7.md:46) described R6-3 as “Numbers fixed; interpretation overcorrected.” That remaining interpretation is fixed **now**, rather than having been accepted in round 7.

The disposition of the requested earlier findings is:

| Finding | Ruling at `590abaf` |
|---|---|
| **R7-1 / remaining R6-3**, generated-test uncertainty | **Fixed.** [Results:334](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:334) and C7 distinguish A’s unresolved interval from B’s exploratory evidence above 2%, while preserving the registered mixed-population point-estimate decision. |
| **R7-2**, grading-rule absence of effect | **Fixed.** [C8:120](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:120) now says no demonstrated BLOCKER-recall improvement, consistent with **+0.9 [−1.8, +4.5]**. |
| **R7-3**, self-preference literature | **Fixed substantively.** [Related work:31](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:31) now preserves the distinction between legitimate preference and harmful preference on incorrect responses. This agrees with [Chen et al., §§3–4](https://arxiv.org/html/2504.03846v1). |
| **R6-1 and the inherited coverage chain through R1-8** | **Remain closed.** The manuscript distinguishes analogous single-rate simulations from measured coverage of its production intervals. |
| **Other previously accepted repairs** | No regression found in pooled cost, sampling confounding, operating-point matching, recurrence, paid-comparator interpretation, Luna’s role, paired-test reporting or the clarification mechanism. |

**`RESULTS-DERIVED.md` §3 remains QUOTABLE.** Its [provenance and admission:61](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:61) faithfully preserve the earlier ruling, without extending it.

I independently reconstructed the twenty-reading pool through the harness loader:

| Stratum | Union | Recomputed cluster interval |
|---|---:|---:|
| Defective | **53/110 = 48.2%** | **[36.4%, 59.8%]** |
| Correct | **54/150 = 36.0%** | **[28.2%, 44.2%]** |

Both match the committed record exactly. Complementing the residual interval at seed **20260912** also recovers the retained recall interval **[36.7%, 60.0%]**. These quantities support the descriptive pooled operating point, without establishing superiority at matched cost.

The generated-test calculations independently reproduce **6/33 [0.0%, 44.8%]** and **10/43 [6.8%, 47.1%]**. Table 1 regenerates byte-identically in memory, all three figure copies match their manuscript copies, and the manuscript checker passes. I did not execute file-writing reproduction commands.

The descriptive contribution remains useful. The remaining corrections require narrower explanations of existing observations, not withdrawal of the numerical results or a new experimental programme.

**not submittable — most importantly, Figure 3 still presents an uncontrolled sheet-repair-and-rerun comparison as distinguishing the control defect’s effect from noise.**
