Reviewed `365c8f2`, the full manuscript, `77dbade..365c8f2`, all four earlier manuscript reviews, and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, residual classifications, clarification adjudication and previous reviews are conflicted. This is a cross-vendor review relative to the generator, but **not independent-family validation** of those results.

The principal calculations hold. Five round-4 findings are fixed; two remain partly fixed. The fresh reading identifies additional mismatches between the quantities measured and the conclusions presented.

1. **R5-1 — Major, new. The pooled recall headline omits its substantially higher false-positive cost.**

   [results.tex:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:53) reports **48.2%** recall from twenty readings across three routes. The following cost paragraph supplies **16.0%**, explicitly the eight-reading shipped route’s rate. The pooled result also appears without its own cost in [introduction.tex:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:18) and [table1.tex:12](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:12).

   **Contradicting record.** Independently OR-ing those same twenty readings on the correct stratum gives **54/150 = 36.0%**, not 16.0%. I recovered this both directly from the archived arm/cache rows and through the harness loader. The loading and union definitions are at [report_ceiling.py:449](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/ceiling/report_ceiling.py:449).

   This materially changes the operating point accompanying the pooled headline. It also violates the paper’s explicit reporting rule at [methods.tex:51](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:51). Report the pooled cost with the pooled recall. The residual characterization remains valid; pooling’s additional coverage must carry pooling’s additional cost.

2. **R5-2 — Moderate, residual R4-2. Coverage is still transferred from the simulation to observed intervals.**

   The revised Discussion and derived report are better scoped. However, [results.tex:12](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:12) still says “that bootstrap’s coverage under this clustered design is measured.” More explicitly, [methods.tex:115](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:115) says an interval “quoted around 3%” covers about .80. The repaired [results.tex:93](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:93) still concludes that the observed interval is “likely narrower than it claims.”

   **Contradicting implementation.** [coverage_simulation.py:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py:36) tests 600-resample, integer-index intervals under assumed correlation .5 and specified **true** rates. It does not measure coverage conditional on observing approximately 3%, or establish coverage of the production procedure. [C15:303](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:303) correctly states this distinction.

   All fourteen cells reproduce. They support a warning about **potential undercoverage suggested by analogous simulations**, not a measured coverage assignment to the reported intervals. No new simulation is necessary to retain that useful warning.

3. **R5-3 — Moderate, new. The generated-test result is presented as a user-facing false-alarm quantity without disclosing its different candidate population.**

   [related.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:56) describes the retained failing applications as “what reaches a user as a false alarm.” [results.tex:325](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:325) gives 12.2% and 14.9% without explaining that these include candidates already failing visible tests. Elsewhere, [methods.tex:22](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:22) describes such candidates as discarded.

   **Contradicting record.** [RESULTS-TESTGEN-VAL.md:213](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:213) specifies the mixed population. Of 107 failing applications, **58 are on visible-test-failing F candidates**. I independently recovered:

   | Rule | Registered mixed population | Visible-test-passing P/C population |
   |---|---:|---:|
   | A | 11/90 = 12.2% | 6/33 = 18.2% |
   | B | 15/101 = 14.9% | 10/43 = 23.3% |
   | C′ | 11/86 = 12.8% | 6/33 = 18.2% |

   The P/C-only analysis is explicitly post hoc and considerably less precise. [RESULTS-TESTGEN-VAL.md:158](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:158)

   Preserve the registered failure of the 2% criterion on its actual population. Identify that population and avoid presenting its rate as the product-population rate. Also replace “a frozen set of canonical-failing tests” at [related.tex:58](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:58): the denominator includes both canonical-passing and canonical-failing tests.

4. **R5-4 — Moderate, new. Problem-level error recurrence is promoted into a demonstrated self-consistent-error mechanism.**

   [related.tex:59](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:59) explains the failed threshold “because wrong tests recur by problem,” then calls this a concrete case of the cited self-consistent-error result.

   **Contradicting record.** [RESULTS-TESTGEN-VAL.md:117](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:117) expressly says recurrence does not distinguish the same misreading repeated from different errors on difficult or ambiguous problems. Its [post-hoc corroboration analysis:173](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:173) likewise does not identify the cause.

   The outside paper defines self-consistent errors through **semantically equivalent incorrect responses across samples**, a property this study did not establish. [Tan et al., §2.2](https://arxiv.org/html/2505.17656v2#S2.SS2)

   Report recurrence and failed validation as observations. Their relationship to repeated semantic errors is a compatible explanation, not an identified mechanism.

5. **R5-5 — Moderate, residual R4-4. The comparator repair did not reach the admitted claim.**

   [results.tex:326](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:326) now correctly preserves A’s small observed advantage while saying superiority was not established. But [CLAIMS.md:193](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:193) still asserts that the paid rules “do not beat” the free comparator.

   **Contradicting record.** A retains exactly C′’s applications plus four correct applications; their wrong-application counts are identical. The source explicitly declines a comparative conclusion. [RESULTS-TESTGEN-VAL.md:45](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:45)

   I independently recovered the four additions, all on F candidates. The manuscript repair is accurate; the ledger still denies a benefit the study cannot settle.

6. **R5-6 — Minor, earlier repair incomplete. C1 retains the reversed reading-depth qualification.**

   [CLAIMS.md:21](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:21) says meeting the flattening bar at \(K=4\) makes a weaker statement than meeting it at \(K=8\).

   **Contradicting calculation.** The corrected [results.tex:49](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:49) states the reverse difficulty correctly. I recovered marginal increments of **2.892857** points at step four and **1.931818** at step eight. For the subset-averaged curve, the fixed bar becomes easier to meet as depth increases.

   Round 2’s repair reached the manuscript but not C1. Neither depth’s criterion establishes an asymptotic ceiling.

The disposition of every round-4 finding is:

| Finding | Ruling at `365c8f2` |
|---|---|
| **R4-1**, consensus-validation literature | **Fixed as to the cited papers.** ConVerTest’s 84–91% retained-test precision and CANDOR’s .894–.930 oracle correctness support the rewritten attribution. The surrounding account of this manuscript’s own experiment has the separate problems R5-3 and R5-4. |
| **R4-2**, coverage scope | **Partly fixed.** The derived report and Discussion improve; R5-2 remains. |
| **R4-3**, sampling and marginality explanations | **Fixed.** The repaired passages distinguish observed verdict variation from unmeasured causes; the heading now states the arithmetic. |
| **R4-4**, paid versus free comparator | **Partly fixed.** Results repaired without overcorrection; admitted C7 remains wrong, R5-5. |
| **R4-5**, Luna’s audit role | **Fixed.** The heading and paragraph now acknowledge its earlier secondary audit role. |
| **R4-6**, paired p-value reporting | **Fixed.** Both added values match the record: .015625 on correct code and approximately \(1.0014\times10^{-5}\) for pooled cluster sign-flipping. |
| **R4-7**, SWR-Bench aggregation | **Fixed.** Additional-model synthesis is now distinguished from Boolean union. |

I checked the rewritten outside-paper claims directly against [ConVerTest’s metrics and Table II](https://arxiv.org/html/2602.10522v1#S5.SS2), [CANDOR’s oracle-correctness evaluation](https://arxiv.org/html/2506.02943v7#S5.SS2), and [SWR-Bench’s Multi-Review description](https://arxiv.org/html/2509.01494v2).

For the earlier findings round 4 left partial: **R3-2 / R2-2 / R1-8 remain partial** through R5-2; **R3-5 and R3-6 are now fixed**, as is the remaining causal-allocation component of **R2-1**. **C14 and C15 retain their scoped admission.** Neither licenses population stability or validation of the production intervals.

Independent verification recovered the three-family union counts, C14’s **25/32 and 43/68**, all fourteen coverage cells, clarification’s **0/32, 9/32, 0/32**, its **[7.6852, 51.4286]** interval and 27 zero resamples, exact cluster **\(p=.0625\)**, and adjudicator agreement **84/91, κ=.85203**. Table 1 regenerates byte-identically in memory; all three committed figure/compiled-copy pairs match. The manuscript checker passes. I did not run the file-writing reproduction script.

The paper retains a useful descriptive contribution. These findings require consistent denominators, operating points and inferential limits, rather than discarding the measurements or demanding an entirely new programme.

**not submittable — most importantly, the pooled 48.2% recall headline omits its 36.0% false-positive cost, despite the paper’s central requirement that recall be interpreted at its own operating point.**
