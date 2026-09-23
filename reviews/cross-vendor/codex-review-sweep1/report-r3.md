The numerical repairs pass. **The report is not yet final: two substantive wording errors remain, plus one incorrect methods sentence.** No files were modified.

1. **R3-M1 — “Equal cost” remains asserted.** [RESULTS-SWEEP.md:129](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:129) still says “The one comparison that is matched” and “essentially the same cost.” That contradicts the withdrawal at line 150. The false-positive contrast, −0.3 points [−3.8, +3.4], supports similar observed rates with an unresolved difference; it establishes neither equality nor a matched false-positive operating point. Replace the opening with “At equal reading depth, the observed false-positive rates are similar.” The interpretation at lines 148–153 is otherwise correctly scoped.

2. **R3-M2 — The preregistration limitation is larger than the truth.** [Line 114](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:114) says “a grading rule that no preregistration fixed.” But [ceiling’s preregistration:35](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/ceiling/PREREGISTRATION.md:35) explicitly fixes the flag as ≥1 BLOCKER, and study 18 inherits that definition. The **alternative rules and this sweep** are exploratory; C2’s original grading rule was specified. Say: “C2’s magnitude is specific to its preregistered BLOCKER rule; exploratory re-grading changes its magnitude and reverses its sign.” Similarly, clarify line 161 as “This four-rule sweep was not preregistered.”

3. **R3-m1 — Both sides do not have 70 subsets.** [Line 141](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:141) says “both sides averaged over all 70 four-draw subsets.” `cross` has 70; `astra` has **one**, C(4,4). The implementation and table are correct. Change this to “each side averaged over all its available four-draw subsets: 70 for `cross`, one for `astra`.”

What passes:

- **Loader and provenance:** independently reconstructed all 8,320 selected readings from 35 committed source files. Every draw covers the same 110 P and 150 C instances; depths are **8, 8, 4, 8, 4**. Every applicable row has both integer counts. No ungradeable rows, conflicting overwrites, or incomplete draws; shipped flags agree with BLOCKER counts throughout.
- **Reproduction:** ran the script with its output write intercepted in memory and network/process calls prohibited. The regenerated JSON equals the committed record exactly.
- **Independent arithmetic:** explicitly enumerated four-draw subsets and independently bootstrapped problem clusters, using 10,000 resamples and seed 20260915. **All 80 table rates, all 160 interval endpoints, and all six paired-contrast intervals reproduce.** Every displayed table cell matches.
- **Interpretation:** all three contrasts are legitimate and worth retaining with their distinct estimands. The nearest-point discussion honestly leaves `self-strong` unresolved. Recognition and causal attribution are explicitly disclaimed. The revised post-hoc paragraph correctly permits exploratory inference; it does not require further weakening.

These findings require prose corrections, not new measurements or model calls. I did not run the application-wide suite; validation here was the read-only reproduction and independent statistical audit.

**not quotable — the report still asserts the equal-cost interpretation it says it withdrew.**
