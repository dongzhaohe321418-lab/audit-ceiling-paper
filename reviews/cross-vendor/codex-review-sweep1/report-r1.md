The no-new-model-call claim checks out, and the submitted arithmetic reproduces. The report nevertheless has three blocking problems.

Reviewed `fd4bba5` on `fusion/evidence-authority`. No files modified.

1. **R1-M1 · Major, blocking — the loader changes both the readings and the population.**  
   [The loader](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/sweep/threshold_sweep.py:9) reads one cache directory and renumbers its files. Consequently:

   - `cross` uses draws **4–8**, omitting archived draws 1–3.
   - `self` omits draw 1 and the inherited portion of draw 2. Population selection from its first loaded file then excludes **56 P and 32 C instances**, even though later draws contain them. Its denominators are **54 P and 118 C**, versus **110 P and 150 C** elsewhere.

   The inherited records are committed and their locations are explicitly handled by the [existing report loader](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/report_ceiling3.py:54). Complete archived K values are **8, 8, 4, 8, 4**. The statement “because that is what the archive holds” is false.

   Restoring those records gives the following shipped-rule results. Intervals are my independent 95% problem-cluster percentile recomputation, 10,000 resamples, seed 20260915.

   | Family | K | P flags | C flags |
   |---|---:|---|---|
   | `cross` | 8 | 33/110 = **30.0% [20.0, 40.7]** | 24/150 = **16.0% [10.2, 22.3]** |
   | `self` | 8 | 19/110 = **17.3% [8.1, 27.3]** | 36/150 = **24.0% [17.2, 31.3]** |

   Different K values are acceptable for explicitly descriptive comparisons of the observed configurations. They cannot isolate auditor identity. For the report’s stronger cross-family interpretation, require a **common-K sensitivity table**, preferably K = 4 averaged over all available four-draw subsets, alongside complete-ladder results. The sampling asymmetry already required by [C2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:43) must also travel with that comparison.

2. **R1-M2 · Major, blocking — finding occurrence becomes defect recognition without evidence.**  
   [Lines 39–46](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:39) say, “The model was never blind to these defects. It wrote them down.”

   The computation establishes that **65 of 110 P instances received some finding**, versus four receiving a BLOCKER. It does not establish that those findings identified the hidden failure. The sweep neither reads nor adjudicates their content. The [source report expressly disallows that interpretation](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CEILING3.md:161).

   The increase is a real, reproducible change in **flag coverage under re-grading**. Calling it recovered defect recognition, or claiming that “most” of the cross-family gap is severity calibration rather than detection, exceeds the evidence. Changing the counting rule mechanically changes the result; it does not identify the cause of the families’ original differences.

3. **R1-M3 · Major, blocking — the matched comparison does not establish the claimed surviving direction.**  
   [The table and conclusion](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:48) call the operating points matched or near-constant while comparing `self-strong` at **3.3% FP** with `cross` at **12.7% FP**. Choosing the nearest available point is a descriptive selection rule, not evidence of performance at a matched rate.

   The statement that `self-strong`’s comparison is “bracketed, not measured” is locally honest. It contradicts the subsequent claim that its direction has been established. Its two endpoints do not resolve the ranking between them. `self-frontier`’s displayed point is empirically dominated by the displayed `cross` point, but that does not settle `self-strong`.

   **Neither half of “direction survives, magnitude does not” works as written.** C2’s original, explicitly conditional contrast remains **−26.4 points [−37.3, −15.6]**. I recovered its exact discordances, three strong-only versus 32 cross-only. Under the any-finding rule, the complete archives instead give 65 P flags for `self-strong` versus 38 for `cross`, reversing the observed ordering while increasing false positives. Matched-FP ordering remains unresolved. The [current C2 already records this rule-dependent reversal](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:26).

Two further qualifications matter:

- **`astra`’s observed dominance survives archive restoration.** It should remain as a descriptive counterexample, qualified by substrate, K, reasoning and sampling configuration. It is not established superiority on both population rates. My paired cluster bootstrap against complete `cross` gives a recall difference of **+2.7 points [−6.5, 13.0]** and an FP difference of **−5.3 points [−10.3, −0.7]**. Thus lower FP has supporting contrast evidence here; higher recall remains uncertain. Overlapping marginal intervals alone would not justify either conclusion.
- **Minor reporting corrections.** The fourth rule is `any finding >= 2`, present in the code and JSON but unnamed in the report’s table. Four rules are a chosen analysis set, not the archive’s absolute limit: observed counts also permit cutoffs at three. The `self-strong` gap is accurately described **within the four selected rules**. The post-hoc designation and different-prompt limitation are appropriate; no curve or preregistration is claimed. Explicitly label the intervals 95% and keep intervals with repeated rates as §9 requires.

Verification was substantive: all **20 JSON rows and all 120 rate/interval values reproduced exactly**, both through the submitted calculation with its file-writing statement omitted in memory and through an independent implementation. All four predicates use the same rows within each family; there is no rule-dependent population substitution. The population error is **between families**. No sweep figure required generation or auditing.

The five source-report tests passed. Statistical tests returned 19 passes and three 30-second timeouts in exact-grid coverage calculations, not numerical assertion failures. The full application suite was not run.

**Not quotable — the loader silently changes the readings and population underlying the central cross-family comparison.**
