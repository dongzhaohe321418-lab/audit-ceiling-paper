Reviewed `18fe530`, the full manuscript, `365c8f2..18fe530`, the archived reviews and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, residual classifications, clarification adjudication and review effectiveness are conflicted. This is a cross-vendor review relative to the generator, **not independent-family validation** of those claims.

The pooled operating point checks out. The principal remaining problem is incomplete propagation of the statistical qualifications.

1. **R6-1 — Moderate, residual R5-2. The manuscript still assigns undercoverage to intervals whose coverage was not measured.**

   [methods.tex:119](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:119) says intervals on rates below roughly .10 “should be read as narrower than they claim.” [paper.tex:87](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:87) repeats the categorical conclusion that “small-rate intervals are narrower than they claim.”

   **Contradicting record.** [coverage_simulation.py:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py:36) tests 600-resample, integer-index intervals under an assumed correlation model, at specified **true** rates. It neither measures coverage conditional on an observed small estimate nor validates the production implementation. [C15:309](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:309) correctly preserves these restrictions.

   All fourteen simulation cells reproduce. They justify **potential undercoverage suggested by analogous simulations**. The repaired Results introduction now says precisely that; Methods and Limitations must follow it. This remains the unresolved component of **R4-2, R3-2, R2-2 and R1-8**. No new simulation is necessary to retain the scoped warning.

2. **R6-2 — Moderate, new. The paper overstates what archived findings cannot support at a matched operating point.**

   [discussion.tex:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:18) attributes the inability to match operating points to re-grading rather than re-asking. [discussion.tex:125](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:125) says **only** re-asking can place families at a common false-positive rate.

   **Contradicting record and calculation.** The archived `self-strong` endpoints are **5/150** false positives under BLOCKER and **51/150** under any-finding grading. [RESULTS-SWEEP.md:57](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:57) A randomized policy choosing the latter rule with probability
   \[
   (24-5)/(51-5)=19/46
   \]
   has an expected empirical false-positive rate of **24/150**, matching the shipped route, without another model call.

   This would be a **new post-hoc randomized policy**, requiring uncertainty analysis and independent validation before a population-level comparison. It does not establish a ranking or justify interpolating the existing figure as a measured deterministic curve. But it disproves the methodological impossibility asserted here. Limit the claim to the deterministic rules evaluated. Re-asking is a useful additional experiment, not the only possible route.

3. **R6-3 — Minor, introduced by the population repair. The newly quoted product-population rates lose their denominators and substantial uncertainty.**

   [results.tex:334](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:334) and [CLAIMS.md:200](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:200) add **18.2% and 23.3%**, labelled post hoc, but omit their intervals.

   **Contradicting reporting record.** [RESULTS-TESTGEN-VAL.md:164](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:164) gives:

   | Rule | Visible-passing candidates only | Problem-cluster interval |
   |---|---:|---:|
   | A | 6/33 = 18.2% | [0.0%, 44.8%] |
   | B | 10/43 = 23.3% | [6.8%, 47.1%] |

   “Imprecise” does not communicate that A’s interval includes both zero and the 2% threshold. The ledger’s [reporting rule:5](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:5) also requires the intervals. Preserve the registered mixed-population failure; do not let these exploratory point estimates imply a separately established failure on the product population.

4. **R6-4 — Minor, introduced by the pooled-cost repair. Section 3 gives the retained recall interval the wrong provenance.**

   [RESULTS-DERIVED.md:71](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:71) attributes **[36.7, 60.0]** to study 21 at seed `20260924`.

   **Contradicting implementation and record.** Study 21 imports ceiling 1’s residual interval and complements it; it does not recompute this interval at that seed. [report_rerate.py:161](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/report_rerate.py:161) Ceiling 1 uses `BOOT_SEED + 4`, namely **20260912**. [report_ceiling.py:930](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:930)

   Independently bootstrapping the residual at that seed gives **[0.400000, 0.6330275]**; its complement is **[36.6972%, 60.0000%]**. The source report explicitly documents this canonical seed. [RESULTS-CEILING.md:840](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING.md:840)

   Correct the attribution. Neither the retained recall interval nor the new false-positive calculation needs withdrawal.

5. **R6-5 — Minor, introduced by the recurrence repair. The literature statement now has an unrestricted universal quantifier.**

   [related.tex:61](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:61) says self-consistent errors are something “every detection method struggles with.”

   **Contradicting source scope.** Tan et al. evaluate four representative detector types and report degradation on their evaluated tasks and models; they also introduce an improved cross-model probe. They do not establish a universal result about every detection method. Restore “the methods evaluated by Tan et al.” [Tan et al., §§3–4](https://arxiv.org/html/2505.17656v2#S3)

   The substantive R5-4 repair otherwise works: recurrence is now a compatible explanation, and the manuscript explicitly acknowledges that semantic identity of the errors was not established.

The disposition of every round-5 finding is:

| Finding | Ruling at `18fe530` |
|---|---|
| **R5-1**, pooled recall without its cost | **Fixed quantitatively and in the headline passages.** The new computation is quotable; its provenance sentence needs R6-4’s correction. |
| **R5-2**, coverage transferred to observed intervals | **Partly fixed.** R6-1 remains. |
| **R5-3**, generated-test population misrepresented | **Fixed substantively.** The mixed population is disclosed, and the registered failure is preserved. The added exploratory rates need R6-3’s uncertainty. |
| **R5-4**, recurrence promoted into a mechanism | **Fixed substantively.** The repair introduces the smaller literature-scope error R6-5. |
| **R5-5**, paid rules “do not beat” the comparator | **Fixed**, including C7. This closes the remaining **R4-4** issue without denying the observed advantage. |
| **R5-6**, reversed depth qualification in C1 | **Fixed.** Independently recovered increments are **2.892857** points at step four and **1.931818** at step eight. |

I found no regression in the previously accepted sampling-confound, Luna-role, paired-p-value or aggregation-operation repairs. **C14 and C15 retain their scoped admission**; neither establishes population stability or validates the production intervals.

**Explicit ruling on `RESULTS-DERIVED.md`, section 3: QUOTABLE for the pooled operating point, with the provenance correction identified above.**

I independently reconstructed all twenty complete readings from the archived arm/cache records, then separately used the harness loader. Both recover:

| Stratum | Pooled union | Problem-cluster interval |
|---|---:|---:|
| Defective | **53/110 = 48.2%** | **[36.4%, 59.8%]**, new computation |
| Correct | **54/150 = 36.0%** | **[28.2%, 44.2%]** |

The harness computation matches the new JSON record exactly. Retaining the previously reviewed recall interval **[36.7%, 60.0%]** is reasonable once its actual provenance is stated. **Both pooled recall and its price may remain.** This admission supports a descriptive operating point, not superiority at matched cost.

Additional verification recovered the generated-test totals **107 applications, 58 on F candidates**, all three rules’ mixed and P/C-only counts, and A’s four additional correct applications over C′, all on F candidates. Clarification reproduces **0/32, 9/32, 0/32**, interval **[7.6852, 51.4286]**, 27 zero bootstrap resamples, exact cluster **p=.0625**, and adjudicator agreement **84/91, κ=.85203**. These calculations do not independently validate my family’s adjudication judgments.

Table 1 regenerates byte-identically in memory, all three figure copies match, and the manuscript checker passes. I did not run the file-writing reproduction script.

The paper retains a useful descriptive contribution about audit operating points and the distinction between flags and diagnosis. The remaining concerns require accurate scope and reporting, not an entirely new experimental programme.

**not submittable — most importantly, the manuscript still turns limited coverage simulations into categorical claims about the uncertainty of its reported intervals.**
