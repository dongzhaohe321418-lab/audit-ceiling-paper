Reviewed `3a94625`, the full manuscript, `fbeaf9f..3a94625`, prior findings, and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, residual labels, clarification adjudication, and previous reviews are conflicted. This review checks the author’s account independently, but **does not provide independent-family validation**.

Both round-10 findings are fixed. I found these remaining issues, most severe first.

1. **R11-1 — Moderate. The discussion still ranks contributions that the paper expressly says cannot be compared.**

   [discussion.tex:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:50) says “Repetition is the smallest of the contributions we could measure.” C2’s [heading:29](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:29) similarly generalises that changing the auditor moves recall more than changing reading depth.

   **Contradicting records.** The rulebook contrast is on **56 instances at K=1**, rather than **110 at K=8**, as [RESULTS-CEILING.md:477](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING.md:477) records. [C3:74](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:74) explicitly prohibits comparing its magnitude with 19.3 or 26.4. Moreover, the measured same-size auditor substitution is **−12.7 points**, smaller in magnitude than the repetition gain, in [RESULTS-CEILING.md:380](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING.md:380).

   The specific observation **26.4 > 19.3** is valid. It does not establish a general ordering of auditor, repetition, rulebook and specification contributions. The subsequent qualifications do not reconcile the opening superlative. Remove that ranking or restrict it explicitly to the two named observed contrasts.

2. **R11-2 — Moderate. P4’s new table row loses a material qualification of its admitted result.**

   [table1.tex:28](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:28) reports “reference disagrees,” **10.0% [0.0, 26.3]**, among 20 flagged instances, without saying that **nine yielded no valid input** or restricting disagreement to the extracted inputs.

   **Contradicting admission scope.** The [round-3 reader sentence:30](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-fpadj1/report-r3.md:30) carries both qualifications. The [registered interpretation:74](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/fpadj-PREREGISTRATION.md:74) requires stating N’s share because these cases can be neither confirmed nor refuted.

   The numerical row is correct, but it does not distinguish **nine observed agreements from nine unresolved cases**. Add “on extracted inputs,” **2/20**, and **9/20 no valid input**, in the row or caption. Preserve the registered interpretation without turning the unresolved cases into negative adjudications.

3. **R11-3 — Minor. C16 reinstates the complete-spending claim P4’s third review specifically corrected.**

   [CLAIMS.md:331](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:331) says “total spend $4.28.”

   **Contradicting record.** [RESULTS-FPADJ.md:8](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-FPADJ.md:8) states that extraction costs cover recorded replies only; failed attempts and the initial halted call are unaccounted for. The [third review:7](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-fpadj1/report-r3.md:7) expressly accepted the withdrawal of a complete-total claim.

   **$4.19887425 + $0.076526 = $4.27540025**, rounding to $4.28, is the accounted subtotal. Label it accordingly or omit it. Merely acknowledging imperfect spend guards does not qualify “total.”

4. **R11-4 — Minor. P4’s opening attributes hidden-suite incompleteness to the wrong result.**

   [results.tex:463](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:463) says the residual result shows that hidden suites leave behaviour unexercised.

   **Contradicting scope.** The residual consists of candidates that **fail the hidden suite**, by [Methods:20](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:20). Its classification concerns whether the prose determines the tested expected behaviour. That does not itself establish missing hidden-test coverage.

   P4 supplies the relevant evidence directly: its two witnesses are absent from their hidden suites, as [RESULTS-FPADJ.md:52](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-FPADJ.md:52) documents. Attribute that observation to P4, or introduce suite incompleteness as a possibility.

The requested dispositions are:

| Finding | Ruling at `3a94625` |
|---|---|
| **R10-1 / remaining R9-1**, third-rater reliability | **Fixed.** The generated caption and compiled table carry **7/11 on six problems**. Independent reconstruction reproduces that count and both contrasts. |
| **R10-2**, probe completion bounds | **Fixed.** The summary distinguishes answered-only accuracy from extreme completion of unanswered items. |
| **R9-2**, rulebook recall | **Remains fixed.** Raw loop records reproduce **10/56 versus 25/56**; the K=1 recall interpretation retains its population and exploratory limits. |
| **R8-1–3** | **Remain fixed.** Rerun confounding, simultaneous classification-protocol changes, and tracker corrections remain disclosed. |
| **R7-1 / inherited R6-3** | **Remains fixed.** A’s inconclusive interval does not erase B’s exploratory evidence above 2%. |
| Other inherited repairs | No regression identified in the previously corrected passages. R11-1 concerns a remaining broader ranking statement. |

**`RESULTS-DERIVED.md` §3 remains QUOTABLE.** Its [scope:61](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:61) accurately preserves the earlier ruling. Reconstruction gives **53/110 = 48.2% [36.4, 59.8]** and **54/150 = 36.0% [28.2, 44.2]** at seed 20260908. Complementing the residual interval at seed 20260912 reproduces the retained recall interval **[36.7, 60.0]**. This licenses the descriptive operating point, not superiority at matched cost.

**P4’s substantive results reproduce.** I recovered **D/A/N = 2/9/9**, per-finding **3/47/20**, the disagreement interval **[0.0, 26.3158]**, and union **20/150 [7.9470, 19.2053]**. Apart from the opening attribution above, §3.5 follows the reader sentence without erasing the two observed disagreements or calling them specification violations. C16 preserves the outcome’s scope, except for its spending statement.

The updated counts are correct: **eight admitted studies**, with **3 + 3 + 4 + 6 + 7 + 9 + 10 + 11 = 53 rounds**. This excludes the separately described closed second-substrate study and the headline ceiling study’s 21 rounds.

Table 1 regenerates byte-identically in memory, the manuscript checker passes, and the compiled table and figures were inspected. The remaining issues concern interpretation and transfer of qualifications, not the reconstructed arithmetic.

**not submittable — most importantly, the discussion still presents a general ranking of contributions that its differently scoped contrasts do not establish.**
