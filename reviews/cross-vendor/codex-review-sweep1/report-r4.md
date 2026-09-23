All three round-3 findings are fixed. The numerical analysis passes, but **one factual correction remains**.

**R4-m1 — Incorrect adjudication provenance.** [RESULTS-SWEEP.md:175](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:175) credits “studies 18 and 19” with two-rater adjudication. Study 18 explicitly says its advisory texts were **neither archived nor adjudicated** ([RESULTS-CEILING3.md:161](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CEILING3.md:161)). This is a required factual correction, not a stylistic preference.

A sufficient replacement is:

> No figure here establishes what a finding identified; that requires assessing finding content against the hidden failure, which this sweep does not do.

Verification at `d81d4b0`:

- Independently reconstructed all **8,320 readings**, with true draw numbers and the frozen **110 P / 150 C** population. No missing counts, dropped readings, or partial draws.
- Independently reproduced **all 80 rates, 160 interval endpoints, and six paired contrasts**, using explicit subset enumeration and the stated bootstrap settings.
- Executed the actual sweep with its output redirected into memory and filesystem writes/network calls prohibited: **byte-identical JSON**.
- Confirmed all three contrasts are correctly scoped. Equal-depth recall improves; false-positive equality remains unresolved. The complete-ladder comparison establishes lower false positives, not higher recall.
- Found no remaining assertion of matched operating points, causal severity attribution, or defect recognition in the substantive conclusions. C2 remains valid for its registered rule; exploratory re-grading reverses the observed contrast without resolving matched-rate ranking.

No further readings or numerical analysis are needed. I modified no files.

**not quotable as written — the limits section still attributes adjudication to study 18 that its own report explicitly says was not performed.**
