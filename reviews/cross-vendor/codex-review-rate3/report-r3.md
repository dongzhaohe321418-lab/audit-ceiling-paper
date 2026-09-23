The arithmetic passes. The report still contains material errors in what that arithmetic licenses. I reviewed `eac2842` without modifying files or making model calls.

1. **The repeat disagreement does not quantify how much of the sheet contrast is instability.** [Lines 99–102](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:99) end with “which is how much of this movement plain instability can account for.” That inference is unsupported. Six discordant pairs cannot apportion the **34.38-point** change between presentation, sampling, and batch context.

   The 5/11 observation itself is correct: I verified identical specification, visible tests, and witness display for every pair. But its scope needs precision:
   
   - These 11 instance pairs cover **six problems**, not 11 independent problems.
   - For the primary binary outcome—`undetermined` versus everything else—**7/11 pairs agree**. Two categorical disagreements are `determined` versus `cannot-tell`, which contribute identically to the primary.
   - They are not all the sheet’s repeated questions. The 121 item bodies contain **56 distinct texts**; 54 repeat, and 38 of those groups have unanimous labels. Across all identical-text pairs, 55/81 agree. Those pairs are dependent and are not an alternative reliability estimate.

   Keep the prominent 5/11 disclosure, but restrict “more than half of its own repeats” to **those 11 instance pairs**. The bootstrap conditions on the collected labels; it does not measure uncertainty from another model-rating run.

2. **The gate is still overstated as a publication prohibition.** [Lines 90–95](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:90) say no reading of the broken result could have been quoted without setting aside the registered rule. The actual [rule](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:160) makes the outcome **inconclusive and keeps the decision waiting for P1**. It does not prohibit descriptive publication of an inconclusive result.

   The defensible statement is that the broken result could not authorize proceeding under the registered positive-result branch. “Could not have been published” is another overcorrection toward modesty.

3. **The blanket interval and consistency qualifications are false in scope.** [Line 110](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:110) says every interval’s lower endpoint is within five points of zero. The broken-sheet contrast intervals start at **+38.5**, and the Wilson intervals also contradict that sentence. It is true of the **four rebuilt-sheet contrast intervals**.

   Likewise, [lines 63–65](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:63) apply the L3 consistency warning to the whole table, including the different six-category instrument. I independently checked that comparator’s records: **L1 and L2 each agree on all 11 repeated instances**. That does not establish independence or validity, but L3’s 5/11 cannot describe their consistency.

4. **The abstention-excluded secondary also needs a post-hoc designation.** The [provenance section](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:29) correctly recovers the registered primary method, but identifies only the disjoint analysis and broken-sheet comparison as later additions. Amendment 1 contains no abstention-excluded secondary. That secondary appears in the subsequently withdrawn P1 registration, after the primary contrast was already committed. Label the overlapping secondary accordingly; retaining it is useful.

5. **The builder still supplies an unsupported justification for withholding expected values.** [Lines 16–19](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/rebuild_sheet.py:16) claim that showing an expected value hands the rater the answer and tends to make them judge it entailed. Showing a proposed value does not answer whether the prose entails it. Any anchoring effect is unmeasured here. Withholding expected values defines a different question; it is not demonstrated to eliminate that bias.

I independently reconstructed the following from the two CSVs and `_items.json`, using **10,000 problem-cluster resamples, seed 20260921**, without invoking `analyse.py`:

| Reading | First group | Caught group | Difference, points | 95% interval | Problems |
|---|---:|---:|---:|---:|---:|
| Rebuilt, overlapping | 43/68 = 63.2% | 23/53 = 43.4% | +19.8 | [1.2, 38.1] | 56 |
| Rebuilt, disjoint | 38/57 = 66.7% | 23/53 = 43.4% | +23.3 | [2.0, 43.6] | 56 |
| Rebuilt, overlapping, abstentions excluded | 43/61 = 70.5% | 23/48 = 47.9% | +22.6 | [2.4, 42.7] | 53 |
| Rebuilt, disjoint, abstentions excluded | 38/51 = 74.5% | 23/48 = 47.9% | +26.6 | [4.8, 48.4] | 52 |
| Broken, overlapping | 42/68 = 61.8% | 4/53 = 7.5% | +54.2 | [38.5, 69.5] | 56 |
| Broken, disjoint | 37/57 = 64.9% | 4/53 = 7.5% | +57.4 | [38.5, 74.6] | 56 |

All corresponding rates, Wilson intervals, cluster counts and bootstrap endpoints in `analysis.json` match. All resamples were usable. The primary Wilson intervals reproduce as **[51.4, 73.7]** and **[31.0, 56.7]**. I also reproduced the earlier prompt’s three intervals at seed **20260922**.

Other checks passed:

- **Clustering:** problem is the appropriate unit for the repeated specifications and batch instances. Jointly resampling problems preserves both arms’ within-problem dependence, including their overlap.
- **Abstentions:** the all-entry denominator is defensible for the stated estimand, the proportion *labelled* `undetermined`. It neither calls abstentions determined nor estimates their underlying determinacy. It was registered before the result; its smaller contrast is not evidence of opportunistic selection. Exclusion moves the contrast **+2.736 points overlapping, +3.323 disjoint**.
- **Other arithmetic:** removing overlap moves the rebuilt contrast **+3.431 points**, the broken contrast **+3.148**; the ratios are **2.733×** and **2.465×**. Labels change on **67 items: 21 missed, 46 caught**. The broken caught arm’s **42/53 = 79.2%** triggers the gate; neither rebuilt arm does.
- **Sheet symmetry:** all 121 specifications and visible-test blocks match the key. The same witness-selection rule applies to both arms. There are concrete inputs for **61/68** and **49/53** entries; no displayed input reaches the truncation limit. The only witness-display discrepancies are the disclosed H003/H117 newline conversions. The repair is procedurally symmetric, with unequal remaining missingness and those two caught-arm rendering defects.
- **Comparator and independence:** the six-category counts reproduce as **46/68 versus 24/53, +22.4 points**. These are different instruments, and the report does not subsequently use proximity to +22.6 as corroboration. Its explicit refusal to deliver the outside-human requirement holds. The broken-sheet comparison appropriately remains descriptive, except for the unsupported instability attribution above.

The corrected registration chronology is substantially supported: `d5919b9` contains the earlier method, and `b0719cd` precedes the withdrawn P1 registration. Two small synchronization issues remain: “a day before the ratings” should specify the **rebuilt** ratings—the broken outcome was already committed September 21—and [CLAIMS.md’s pending row](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:450) still carries the old disjoint interval **[2.4, 44.0]**.

**not quotable — the report converts observed duplicate disagreement into an unsupported explanation of how much the between-sheet contrast moved.**
