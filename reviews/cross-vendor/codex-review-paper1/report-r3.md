Reviewed `fb400e3` against both earlier reviews, `93615fd..fb400e3`, the full LaTeX manuscript, the ledger and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its ranking, residual classifications, clarification adjudication and previous reviews are conflicted. This is independent of the author’s account, but **not independent-family validation** of those results.

The repaired calculations reproduce. Most round-2 corrections hold; two substantive problems remain partly repaired.

1. **R3-1 — Major, blocking. The clarification section still converts a post-hoc association into a mechanism.**

   [results.tex:433](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:433) says the observed split “means what moved diagnosis was specification text that agreed with the oracle, not the resolution of an ambiguity as such.”

   **Contradicting record:** [RESULTS-CLARIFY.md:76](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:76) explicitly limits this to an association. At [line 91](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:91), it states that classification followed observation of the outcome and that consistent instances might simply be easier. Oracle agreement was measured, not assigned.

   The revised closing paragraph correctly avoids causal attribution, but this earlier sentence still supplies it. The supported result remains **0/32 versus 9/32 versus 0/32**, with successes confined to the observed agreement categories. It does not identify which property of those edits produced the improvement.

   Preserve the intervention contrast and its suggestive cluster-level evidence. Remove the mechanistic discrimination unless supported by a design that separates the competing explanations.

2. **R3-2 — Major. Statistical qualifications still do not propagate throughout the manuscript and ledger.**

   The Results and Discussion repairs correctly distinguish single-rate simulations from paired contrasts and conditional shares. However, [paper.tex:82](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:82) still introduces the simulation as coverage evidence for “the primary intervals,” without that restriction.

   **Contradicting implementation and ruling:** [coverage_simulation.py:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py:36) simulates a binary single-rate procedure using 600 resamples. It also uses integer-index percentiles, whereas [report_ceiling.py:638](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:638) interpolates percentiles. The round-2 [ruling at line 117](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-paper1/report-r2.md:117) expressly withheld validation of the manuscript’s 10,000-resample implementation.

   **C15 also needs tighter scope.** [CLAIMS.md:302](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:302) correctly specifies single rates and assumed correlation, but drops the 600-resample qualification and says coverage is 0.93–0.97 “at true rates of 0.10 and above.” The record tests five rates from **0.10 through 0.60**, not that entire range. Upper-boundary rates cannot inherit this assurance. Under the simulation’s own model, at \(p=.999\), all-success samples alone occur with probability approximately .9203 and produce an interval excluding the true rate.

   Two smaller remnants belong to the same repair:
   
   - [CLAIMS.md:74](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:74) still calls C3’s replacement interval “exact unconditional,” although [the implementation at line 234](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:234) explicitly disclaims guaranteed exactness.
   - [methods.tex:99](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:99) and the final Limitations paragraph retain Monte Carlo SE ≈.011 throughout. It is approximately **.020** for the .7975 cell. The derived report and C15 corrected this; the manuscript did not.

   These simulations remain useful and quotable within their actual scope. They do not certify the other intervals.

3. **R3-3 — Moderate, newly identified. A pooled flag contrast cannot establish violation of a false-positive constraint.**

   [introduction.tex:29](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:29) says the pooled contrast, rather than the correct stratum, puts the rule outside the product’s constraint.

   **Contradicting definition:** the constraint is a rate **on correct code**, ≤6.7%, in [PREREGISTRATION-explore.md:130](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/PREREGISTRATION-explore.md:130). The pooled contrast includes defective instances, whose increased flagging is not a false-positive cost.

   The [correct-stratum record](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/ceiling/numbers.json:2129) gives **10/56** flags under the rule against **3/56** without it. Its observed absolute rate exceeds 6.7%. Whether an absolute rate exceeds a threshold and whether its difference from another rate excludes zero are different questions. The pooled significance result answers neither threshold question.

4. **R3-4 — Moderate, newly identified. The discussion discounts an association for a reason that does not make it definitional.**

   [discussion.tex:58](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:58) calls the association between being missed and being undetermined “partly definitional, because the residual is defined by conditioning on never being flagged.”

   Selecting the missed group defines that group; it does not determine its specification labels or force a difference from the caught group.

   **Relevant contrary evidence:** [RESULTS-RATE3.md:84](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-RATE3.md:84) reports the disjoint, post-hoc comparison **38/57 versus 23/53**, +23.3 points [2.0, 43.6]. That is an empirical association under the stated instrument, with substantial limitations. Selection and confounding prevent a causal interpretation; they do not make the observed association a definitional consequence.

   This is an overcorrection that gives the evidence less authority than it warrants.

5. **R3-5 — Moderate, newly identified. The general account of repeated sampling goes beyond the measured quantities.**

   [discussion.tex:39](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:39) concludes that best-of-K, union-of-K and panel aggregation buy coverage “in proportion to” the population near the critic’s boundary, and that a sufficiently loud auditor is invariant under resampling.

   **Contradicting measurement scope:** [report_ceiling.py:486](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:486) computes coverage from per-instance flag counts. There is no measured distance to a decision boundary, no fitted proportional relationship and no panel-aggregation experiment supporting this generalization.

   The same formula also makes subset-averaged marginal gains non-increasing by construction. The measured contribution is their **size**, the coverage reached and the failure of the flattening criterion; the diminishing shape itself is not independent empirical evidence of a ceiling. The revised depth explanation is correct, but this broader mechanism remains unsupported.

6. **R3-6 — Minor. The general statistical reporting policy still differs from the studies actually reported.**

   [methods.tex:93](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:93) says multiplicity is handled through a Bonferroni family per study over every computed comparison.

   **Contradicting record:** [RESULTS-CEILING3B.md:203](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING3B.md:203) inventories its comparisons and explicitly says no correction is applied to the other twenty quantities.

   Likewise, [results.tex:25](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:25) promises both McNemar and cluster sign-flip values wherever a p-value appears, but [line 189](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:189) supplies only .146. The [record](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/ceiling/numbers.json:2242) gives McNemar **.145996** and cluster sign-flip **.182617**. The conclusion remains nonsignificant; the stated reporting contract is inaccurate.

7. **R3-7 — Minor. C14’s admission has not reached Table 1.**

   [table1.tex:26](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:26) still labels the six-family residual quantity “post hoc, pending.”

   **Contradicting admission:** [CLAIMS.md:300](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:300) records its round-2 admission. The stale label originates in the table generator and reproduces faithfully.

**Disposition of every round-2 finding, including the remaining round-1 findings**

| R2 finding | Ruling at `fb400e3` |
|---|---|
| 1. Causal allocation, self-preference, specification interpretation | **Partly fixed.** The three cited passages were repaired. R1 #2’s withdrawn substrate conclusion and its self-preference replacement are now corrected. The clarification mechanism remains overstated elsewhere, R3-1. |
| 2. Coverage assurances and “exact unconditional” | **Partly fixed.** Results, Discussion, Methods’ interval description and Table 1 improved. Final Limitations and C3 retain errors; C15 needs narrower scope. R1 #8 remains partly fixed. |
| 3. Calibration, dominance and “no false-positive difference” | **Fixed.** C2 now states rule dependence and qualified comparisons; −0.3 [−3.8, +3.4] is unresolved. This resolves R1 #4 and #6. |
| 4. Bootstrap near-guarantee | **Fixed.** The statement is conditional on five observed success-bearing problems, concerns exactly zero, and preserves suggestive evidence. |
| 5. Secondary population | **Fixed.** It is agreement between study 21’s consensus and L3. I independently recovered 30 eligible before gates and 23 analysed. R1 #12 is resolved. |
| 6. Abstract intervals | **Fixed for the identified omissions.** Both the false-positive-cost interval and clarification interval are present. R1 #7 is resolved. |
| 7. Flattening threshold’s depth dependence | **Fixed.** Recomputed increments are 2.892857 points at step four and 1.931818 at step eight. |
| 8. “Refreshes” versus checks | **Fixed.** The manuscript now accurately describes comparison against the compiled copies. R1 #15’s remaining wording issue is resolved. |

**C14 and C15 admission rulings**

**C14 is faithful to the scoped round-2 ruling when read as a whole.** I independently recovered 68 consensus-undetermined instances, 25 in the 32-instance six-route residual, and therefore 43 flagged. The residual spans 20 problems. The entry explicitly limits the comparison to a post-hoc description and excludes a stability test. Its heading’s “keeps its composition” must retain that qualification; it does not establish population stability or correct diagnosis.

**C15 preserves much, but not all, of the ruling’s scope.** Its single-rate restriction, assumed correlation and corrected Monte Carlo uncertainty are appropriate. Admission covers the fourteen simulated cells, using 600 resamples, at the tested rates. It does not cover all rates above .10 or directly validate the production interval implementation. R1 #1’s admission issue is resolved for C14; C15 requires this scope correction.

**Verification and referee assessment**

All fourteen coverage cells reproduced exactly. Independent reconstruction also recovered clarification **0/32, 9/32, 0/32**, five informative clusters, the primary interval **[7.6852, 51.4286]**, **27** zero bootstrap resamples, exact cluster \(p=.0625\), secondary **8/23**, and adjudicator agreement **84/91, κ=.85203**.

Table 1 regenerated byte-identically in memory; all three figure copies match. The manuscript checker passes despite the findings above. I did not execute the file-writing `reproduce.sh` under this read-only environment.

The paper offers a useful descriptive study for evaluation researchers, particularly its separation of flagging from diagnosis and its documentation of failed checks. Its numerical evidence is substantially stronger than its remaining explanatory language. The current limitation is not that every result needs another experiment; several conclusions need to stay within the experiments already performed.

**not submittable — the manuscript still turns the post-hoc oracle-agreement split into an explanation of why diagnosis improved.**
