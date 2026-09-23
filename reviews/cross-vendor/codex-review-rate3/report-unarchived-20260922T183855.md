The arithmetic passes. The prose still needs correction. I reviewed `5c87e4c` without modifying files or making model calls.

Five findings remain:

1. **The consistency qualification does not fit the abstention-excluded analyses.** [Lines 19–26](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:19) say `determined` and `cannot-tell` “count identically in every table below.” They do in the primary binary outcome; they do **not** in the secondaries, where `determined` remains in the denominator and `cannot-tell` disappears. The 7/11 agreement therefore cannot qualify every contrast identically. After excluding pairs containing an abstention, seven complete pairs remain, five agreeing—another conditional description, not a replacement reliability estimate.

2. **The withdrawn publication-ban claim remains the Table 2 heading.** [Line 91](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:91) still says “why it could not have been published.” Lines 113–117 correctly explain why that claim is false. A heading is part of the report’s claims; the correction below does not cancel it. The supported restriction concerns proceeding under the positive branch, not publication.

3. **The repaired docstring introduces another false distinction.** [Lines 16–20](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/rebuild_sheet.py:16) assert that showing an expected value makes the question one of *consistency*, rather than determination. Showing a value does not dictate that weaker criterion. The comparator expressly asks whether the prose **entails** that value and excludes the candidate’s. The supportable distinction is between judging determinacy without a supplied target and judging entailment of a supplied target. The anchoring effect remains unmeasured.

4. **“The Wilson intervals are wider still” is numerically false.** [Lines 135–137](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:135) describe intervals whose widths are 22.34 and 25.78 points; the broken-sheet contrast intervals span 31.01 and 36.10 points. Moreover, these are intervals for different quantities. This is another erroneous qualification toward alarm.

5. **The promised change in emphasis was not implemented throughout.** The opening quotation still leads with **5/11**, immediately followed by the assertion that it was stated second. The title and [limits bullet](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:132) also foreground full-label disagreement. Additionally, “No figure in this report” at line 39 conflicts with the comparator exemption at lines 82–83. The numbers are correct; their stated scope and ordering are not.

My independent implementation reproduced every stored contrast, Wilson interval, cluster count and successful-resample count. At the **registered seed `20260921`**, with 10,000 resamples:

| Reading | Numerators/denominators | Difference | Cluster 95% interval |
|---|---|---:|---|
| Rebuilt, overlapping | 43/68 versus 23/53 | +19.8 | [+1.2, +38.1] |
| Rebuilt, disjoint | 38/57 versus 23/53 | +23.3 | [+2.0, +43.6] |
| Overlapping, abstentions excluded | 43/61 versus 23/48 | +22.6 | [+2.4, +42.7] |
| Disjoint, abstentions excluded | 38/51 versus 23/48 | +26.6 | [+4.8, +48.4] |
| Broken, overlapping | 42/68 versus 4/53 | +54.2 | [+38.5, +69.5] |
| Broken, disjoint | 37/57 versus 4/53 | +57.4 | [+38.5, +74.6] |

The opening brief’s `20260922` intervals also reproduce, but they are not the registered-seed results. The committed harness identifies L3 as **`gpt-5.6-luna`**, not `gpt-6-astra`.

The other requested checks pass with these boundaries:

- **Registration:** the original P1 registration falsely claimed the contrast had not been computed. The withdrawal correctly acknowledges this: the result was committed at 16:32:20, before the registration at 17:31:09. Amendment 1 had already specified the all-item denominator, clustering, resample count, seed and gate. The later additions are correctly labelled post hoc.
- **Denominator:** retaining abstentions is defensible for the expressly stated *share labelled undetermined*. Its being smaller is not the justification; the estimand and earlier specification are. Exclusion changes the overlapping contrast by 2.736 points and the disjoint contrast by 3.323.
- **Clustering:** resampling problems jointly across arms preserves the relevant shared-problem dependence. There are 56 primary clusters; the conditional analyses retain 53 and 52.
- **Instruments and independence:** the report correctly distinguishes the instruments and does not subsequently use +22.4’s proximity to +22.6 as corroboration. Its substantive body does not reclaim the outside-human independence that remains absent.
- **Sheet repair:** both arms use the same mechanical display rule. I verified 61/68 versus 49/53 concrete witnesses, the disclosed missing-input categories, and only the two disclosed newline discrepancies. All 11 duplicate-instance displays match. The 7/11, 5/11, six-problem, 55/81 and comparator 11/11 counts reproduce.
- **Broken-sheet interpretation:** the body appropriately limits this to an association between changed presentation and a fresh rating, without identifying their separate effects or establishing anything changed in the specifications.

**not quotable — the report still claims that abstentions and determined labels count identically across analyses, although its secondary analyses explicitly treat them differently.**
