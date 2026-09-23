Reviewed `93615fd` against `306bd8d`, the round-1 report, the claimed repairs, and the underlying records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, its residual labels, its clarification adjudication, and the effectiveness of its reviews are conflicted. This review does **not** supply independent-family validation of those claims.

The main calculations checked here reproduce. Several interpretations and repair claims still do not.

1. **Major — the manuscript still attributes effects that its design cannot separate.**

   [results.tex:108](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:108) attributes roughly two-thirds of the model contrast to how much each union “was permitted to grow.” The observed decomposition is arithmetic: the gap changes from approximately −10.1 to −26.4 points. It does not identify how much temperature caused that change.

   **Contradicting evidence:** [RESULTS-SWEEP.md:163](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:163) explicitly says the comparisons do not isolate model identity from sampling configuration; [discussion.tex:34](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:34) correctly says their contributions cannot be separated.

   The replacement at [related.tex:64](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:64) also calls the contribution a measurement of self-preference. A frozen generator compared across different auditors, operating points and sampling configurations does not identify self-preference. The cited [Chen et al. study](https://arxiv.org/abs/2504.03846) distinguishes preference from objectively better performance; this manuscript’s contrasts do not make that separation.

   Finally, [results.tex:461](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:461) says recall moves with whether the specification answers the oracle’s question. The residual analysis is observational, while P3 measures adjudicated **diagnosis** after specification edits.

   **Contradicting record:** [RESULTS-CLARIFY.md:91](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:91) identifies the oracle-agreement split as post hoc and potentially explained by problem difficulty. Keep the observed contrasts; remove the causal allocation.

2. **Major — the statistical assurances still exceed the procedures checked.**

   The repaired Table 1 caption correctly limits the coverage simulation. However, [results.tex:9](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:9) and [discussion.tex:98](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:98) still describe the primary intervals as having measured, near-nominal coverage.

   **Contradicting record:** [coverage_simulation.py:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py:53) simulates binary single-rate intervals under one correlation model. It does not validate the headline paired contrasts, conditional shares, or clarification interval.

   There is a separate, previously unreached problem. [results.tex:174](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:174) and Table 1 call the replacement interval “exact unconditional,” without its actual limitations.

   **Contradicting implementation:** [report_ceiling.py:234](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:234) says the nuisance supremum is grid-approximated, has no bound on the missed supremum, is not guaranteed exact, and ignores clustering. The source report already records this qualification at [RESULTS-CEILING.md:765](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING.md:765). The numerical interval can be reported with those limitations; it cannot serve as an unqualified exact solution to the clustered-inference problem.

3. **Major — repairs removed prohibited interpretations from the prose but retained them in the authoritative ledger.**

   [CLAIMS.md:42](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:42) still calls C2 evidence about “severity calibration.” [CLAIMS.md:51](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:51) still says `astra` dominates the shipped auditor on both axes.

   **Contradicting records:** [RESULTS-SWEEP.md:109](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:109) withdraws the causal interpretation; its paired comparisons at line 145 do not establish both advantages simultaneously. C11 and the ledger’s newly added prohibitions also contradict C2.

   The manuscript additionally retains “with no false-positive difference” at [results.tex:118](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:118). The estimate is **−0.3 points [−3.8, +3.4]**, an unresolved difference, not evidence of equality. This concern directly involves my own family’s ranking.

4. **Moderate — the new clarification warning overgeneralises a correct conditional calculation.**

   [results.tex:414](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:414) and [CLAIMS.md:275](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:275) say the criterion was nearly guaranteed by construction once discordance was one-signed.

   The calculation is correct **conditional on the observed five success-bearing clusters**. One-signed discordance alone is insufficient. With only one such cluster among 19, the probability of a zero bootstrap difference would be approximately **0.358**, and the percentile interval would include zero.

   **Relevant records:** `records/code/clarify/h3.json`, the archived adjudication keys and labels, and [P3-PREREGISTRATION.md:65](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:65). The registration also requires a smaller placebo contrast, which the bootstrap argument does not guarantee. The full ruling appears below.

5. **Moderate — the newly added secondary result identifies the wrong population.**

   [results.tex:413](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:413) calls the 23 instances those “both earlier raters called undetermined.” Both original raters already supplied the consensus defining the entire primary population.

   **Contradicting registration:** [P3-PREREGISTRATION.md:266](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:266) defines the secondary by agreement between **study 21’s consensus and the third rater, L3**. Thirty instances met that definition before generation gates; 23 entered this analysis. The **8/23**, **+34.8**, and interval reproduce. The repair introduced a population-description error.

6. **Moderate — round-1’s abstract qualification finding is only partly repaired.**

   [paper.tex:47](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:47) now supplies the flag-effect interval and its cost, but drops the cost interval **[−3.6, +26.8]**, including the fact that it contains zero. At line 51, clarification gains an appropriately nonsignificant cluster-test result but still lacks its **[+7.7, +51.4]** interval.

   **Binding evidence:** [CLAIMS.md:5](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:5), C3 and C13, together with `records/code/clarify/h3.json`. Table 1’s specific round-1 omissions were repaired.

7. **Moderate — the explanation of the flattening threshold reverses its dependence on depth.**

   [results.tex:47](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:47) says families stopped at \(K=4\) meet the last-step threshold more easily than families stopped at \(K=8\).

   **Contradicting estimator and record:** [report_ceiling.py:487](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:487) defines exact subset-averaged union coverage. Its marginal increments are non-increasing with depth on a fixed ladder. The committed cross-vendor curve has approximately **2.893 points** at step four and **1.932** at step eight. A fixed small-increment threshold becomes easier to meet later, not earlier. An early apparent plateau can still provide weak evidence about an asymptote, but that is a different argument.

8. **Minor — the reproduction repair checks the compiled copies but does not refresh them.**

   [paper.tex:120](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:120) promises refreshing the copies used by LaTeX.

   **Contradicting implementation:** [reproduce.sh:13](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reproduce.sh:13) compares files and exits on a difference; it contains no copy operation. Verification is a reasonable contract. Describe that contract accurately.

**Disposition of every round-1 finding**

“Fixed” below refers to the original finding, not approval of every nearby sentence.

| R1 | Ruling at `93615fd` |
|---|---|
| 1 | **Admission question resolved by the two scoped rulings below.** The ledger still needs its pending status reconciled with this review. |
| 2 | **Withdrawn substrate conclusion fixed.** The replacement’s self-preference claim introduces a different overstatement, finding 1 above. |
| 3 | **Fixed.** Selected-population conditioning, generator-versus-benchmark uncertainty, and model adjudication are now disclosed. |
| 4 | **Partly fixed.** Results and abstract use rule-dependence; C2 retains the stronger calibration interpretation. |
| 5 | **Fixed.** Measurement changes are acknowledged, and review-round counts no longer estimate single-pass recall. |
| 6 | **Partly fixed.** Introduction corrected; ledger dominance language remains. |
| 7 | **Partly fixed.** Table qualifications added; abstract uncertainty remains incomplete. |
| 8 | **Partly fixed.** P3’s exception and Table 1’s coverage limitation are stated; broader coverage assurances remain. |
| 9 | **Fixed.** Figure 2’s caption identifies every family’s reading depth. |
| 10 | **Fixed for the identified omissions.** All thirteen added review files match their source copies byte-for-byte. Harness assets are now explicitly located outside this repository. |
| 11 | **Fixed.** The third-rater marginal is post hoc and explicitly measures a different construct. |
| 12 | **Partly fixed.** Secondary numbers and naming-rate omission added; secondary population misdescribed. |
| 13 | **Fixed for the cited manuscript statements.** Seven-study status and the three-to-twenty-one-round range are corrected. |
| 14 | **Fixed.** Exploratory inference is permitted without being presented as confirmatory. |
| 15 | **Mostly fixed.** Temporary table stays inside the checkout, figure copies are checked, and deterministic reanalysis is acknowledged. “Refreshes” remains false. |

**Ruling on `reports/RESULTS-DERIVED.md`, section 1**

I independently joined both rating sheets through their instance keys. The 121 rating entries represent 110 distinct instances; duplicate-instance labels agree. I obtained:

- **68** consensus `ambiguous-oracle` instances.
- **25** within the six-route residual of **32**.
- **43 = 68 − 25** flagged by at least one route.
- **25/32 = 78.125%**, reported correctly as **78.1%**.
- **44/57 = 77.193%** in the earlier residual.
- The 32-instance residual is a subset of the 57-instance residual.

The six-route residual spans **20 problems**; 56 is the problem count of the full 110-instance defect population. Clarify that distinction in the report’s opening sentence.

These support a descriptive composition comparison and show that consensus-undetermined status does not imply remaining unflagged. They do not establish population stability or correct defect recognition. The report states those substantive limits appropriately. **quotable**

**Ruling on `reports/RESULTS-DERIVED.md`, section 2**

I ran all fourteen simulations with **400 datasets, 600 bootstrap resamples and seed 20260923**, calling the simulation functions without executing their file-writing wrapper. Runtime was approximately 64 seconds. Every cell matched `records/coverage_simulation.json` exactly.

| True rate | .03 | .05 | .10 | .16 | .30 | .48 | .60 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Defect, 56 clusters | .7975 | .8700 | .9325 | .9325 | .9525 | .9350 | .9275 |
| Correct, 143 clusters | .8875 | .9175 | .9375 | .9325 | .9425 | .9550 | .9650 |

The frozen population independently confirms the simulated cluster-size profiles: **54 pairs plus two singletons**, and **seven pairs plus 136 singletons**.

The report’s scope restriction is essential. These are coverage estimates for the simulated binary-rate procedure, with assumed within-problem correlation 0.5 and 600 resamples. They do not establish coverage for every manuscript interval or directly measure the 10,000-resample implementation.

One minor uncertainty correction is needed at [RESULTS-DERIVED.md:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:43): **0.011** is the Monte Carlo standard error near 95% coverage. It is approximately **0.020** at the observed .7975 cell. State cell-specific errors or approximately .01–.02. This does not invalidate the fourteen simulation estimates. Within the report’s restricted simulation scope, **quotable**

**The clarification criterion and the weight of the result**

Recomputing from the archived readings, adjudication keys and both label files gives **0/32, 9/32, 0/32**, with the nine successes distributed across five problems as **2, 2, 2, 2, 1**. The primary bootstrap interval reproduces as **[7.6852, 51.4286]** points; the secondary reproduces as **8/23**, **[10.0, 60.8696]**.

For a bootstrap drawing 19 problems with replacement,

\[
P(\text{zero difference})=(14/19)^{19}=0.003020746.
\]

The probability of a **negative** difference is zero. The author’s tracker incorrectly describes approximately .003 as the probability of falling below zero; it is the probability of being **exactly zero**. The registered seeded run contains **27 zero-valued resamples out of 10,000**, comfortably below the lower percentile cutoff.

Thus the warning about the percentile interval is justified. Its exclusion of zero supplies little additional reassurance once this observed support is fixed. But five one-way success clusters are themselves observed evidence, not something the construction guaranteed. Exact two-sided cluster enumeration gives **2/32 = .0625**. This is suggestive directional evidence, insufficient for a two-sided .05 declaration, and not evidence of no effect.

The appropriate weight is therefore **a descriptive specification-edit contrast on selected instances, with suggestive but limited cluster-level evidence**. The current paper mostly reaches that position. “Close to guaranteed by construction” needs the conditional qualification above and must refer to the interval criterion, not the entire registered hypothesis or the observed improvement.

**Reproduction and overall referee assessment**

I could **not** run `./reproduce.sh` on a copy: the sandbox permits no writes, including temporary copies. An attempted in-memory figure regeneration also stopped because Matplotlib required a writable cache directory. This is an execution limitation, not evidence that the script fails in an ordinary writable checkout.

I did verify Table 1 byte-for-byte in memory, all three committed figure/LaTeX-copy pairs, the added review archives, the residual join, the coverage simulations, clarification outcomes and intervals, and adjudicator agreement (**84/91; κ = .85203**). The manuscript checker passes despite the issues above.

The paper has a useful, narrowly scoped empirical contribution about operating points, repeated readings, and the distinction between flagging and diagnosis. Its principal remaining weakness is the translation from those measurements into claims about mechanisms and validated uncertainty.

**not submittable — the repaired manuscript still gives observational contrasts and limited statistical checks more inferential authority than their records support.**
