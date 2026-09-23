Reviewed `fafd1e4`, the full manuscript, `3a94625..fafd1e4`, the earlier findings and supporting records. **No files modified.**

I share the measured GPT-6/Astra family. My judgments about its comparative performance, residual classifications, clarification adjudication and previous reviews are conflicted. This is an independent checking pass, **not independent-family validation**.

All four round-11 repairs hold. I found two remaining issues, most severe first.

1. **R12-1 — Moderate. The manuscript still overstates prospective control of protocol departures.**

   [introduction.tex:65](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:65) says every departure was recorded as a numbered amendment. [methods.tex:158](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:158) further says those amendments were committed before the steps they governed.

   **Contradicting records.** P4’s accepted [report:78](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-FPADJ.md:78) documents a narrower leak check, audit spending guards applied per invocation, extraction accounting substituted for the registered ledger, and an unpriced reply allowed through. These differ from the [registered checks:83](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/fpadj-PREREGISTRATION.md:83). Its sole [amendment:97](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/fpadj-PREREGISTRATION.md:97) corrects the extractor’s history, not those departures. The [accepting review:12](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-fpadj1/report-r3.md:12) explicitly accepts disclosure without claiming implementation now satisfies registration.

   Registration, advance amendment and retrospective disclosure are different assurances. The paper currently turns the third into the second. Narrow the general account to distinguish planned amendments from deviations discovered and disclosed afterwards. **This does not invalidate P4’s reproduced outcome or require another experiment.**

2. **R12-2 — Minor. C9 attributes an observed residual count to the wrong estimator.**

   [CLAIMS.md:145](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:145) says, “Under the ZIBB secondary the residual falls 56 to 32,” followed by the 23-of-24 unexercised-edge classification.

   **Contradicting records.** The reduction is the observed **H20d union residual**, after adding `cross-R` to five previously measured routes, documented in [RESULTS-CEILING4.md:175](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING4.md:175) and its [Table 8:223](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING4.md:223). ZIBB instead estimates a latent detectable fraction, with boundary estimates near one and substantial uncertainty, as [lines 121–127](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING4.md:121) explain.

   Attribute **56 → 32** to the observed union. Identify **23/24** explicitly as the *original* classification, preceding the revised entailment rubric. Neither count needs withdrawal.

The requested dispositions are:

| Finding | Ruling at `fafd1e4` |
|---|---|
| **R11-1**, general ranking | **Fixed.** [Discussion:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:50) and C2 restrict the comparison to the named contrasts, retain the smaller same-size substitution and separate the rulebook population. |
| **R11-2**, P4 table qualifications | **Fixed.** [Table 1:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:2) supplies extracted-input scope, nine agreements and nine unresolved cases; the row supplies 2/20. |
| **R11-3**, complete spending | **Fixed.** [C16:333](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:333) now describes accounted spending and missing attempts. |
| **R11-4**, hidden-suite attribution | **Fixed.** [Results:462](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:462) introduces incompleteness as a possibility; P4 supplies the observed witnesses. |
| **R10-1 / remaining R9-1** | **Remains fixed.** The table preserves reliability; independent reconstruction gives **7/11 on six problems**. |
| **R10-2, R9-2, R8-1–3, R7-1 / inherited R6-3** | **Remain fixed.** Completion bounds, K=1 recall, simultaneous protocol changes and the two generated-test intervals retain their distinct interpretations. |

Round 11 left no additional earlier finding explicitly partly open. I found no regression in the other repaired passages.

**`RESULTS-DERIVED.md` §3 remains QUOTABLE.** Its [provenance and scope:61](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:61) preserve the earlier ruling. Independent reconstruction gives **53/110 = 48.2% [36.4, 59.8]** and **54/150 = 36.0% [28.2, 44.2]** at seed 20260908. Complementing the residual interval at seed 20260912 reproduces **[36.7, 60.0]**. Admission supports the descriptive operating point, without superiority at matched cost.

P4 reproduces **D/A/N = 2/9/9** and **[0.0, 26.3158]**. Its procedural null reading preserves the two observations and leaves the nine unresolved cases unresolved. Table 1 regenerates byte-identically in memory, figure copies match and manuscript checks pass. The repaired table also appears in the compiled manuscript, page 6. :codex-file-citation{path="/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.pdf" purpose="source"}

**not submittable — most importantly, the manuscript still presents retrospectively disclosed protocol deviations as universally controlled by advance amendments.**
