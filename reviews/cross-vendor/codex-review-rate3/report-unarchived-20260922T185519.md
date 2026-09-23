Two findings remain. The rates and intervals reproduce; the revised prose still contains a false scope claim.

1. **The abstention-free consistency statistic covers four problems, not six.** [RESULTS-RATE3.md:139](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:139) says all three consistency readings sit on six problems. The 11-pair binary and full-label readings do. The seven abstention-free pairs cover only `Mbpp/119`, `Mbpp/244`, `Mbpp/589`, and `Mbpp/739`; five agree. Removing abstention-containing pairs removes both `HumanEval/154` and `Mbpp/300` entirely. The correct scopes are **7/11 on six problems; 5/11 on six; 5/7 on four**. The [CLAIMS.md row](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:450) should distinguish these too. This overstates the problem-level support for the secondary’s consistency reading.

2. **The repaired instrument explanation has not reached the generated instructions.** The docstring now correctly distinguishes determinacy without a target from entailment of a supplied target. But [rebuild_sheet.py:103](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/rebuild_sheet.py:103), also present in the booklet, still says “期望值等于答案，给了就没法问这个问题了”—the expected value equals the answer, and supplying it makes the question impossible. Supplying an oracle value does not answer whether the prose entails it; the comparator explicitly asks that question. This is an overstatement toward methodological alarm. **It does not invalidate these L3 labels:** `third_rater.py` excludes the booklet header from its item prompts.

The independent recomputation, using 10,000 problem-cluster resamples and the checked-out report’s seed **20260921**, gives:

| Reading | Counts | Difference, points | 95% interval |
|---|---|---:|---|
| Rebuilt, overlapping | 43/68 versus 23/53 | +19.8 | [+1.2, +38.1] |
| Rebuilt, disjoint | 38/57 versus 23/53 | +23.3 | [+2.0, +43.6] |
| Overlapping, abstentions excluded | 43/61 versus 23/48 | +22.6 | [+2.4, +42.7] |
| Disjoint, abstentions excluded | 38/51 versus 23/48 | +26.6 | [+4.8, +48.4] |
| Broken, overlapping | 42/68 versus 4/53 | +54.2 | [+38.5, +69.5] |
| Broken, disjoint | 37/57 versus 4/53 | +57.4 | [+38.5, +74.6] |

All six match `analysis.json`, including its Wilson intervals. The opening brief’s three intervals reproduce at **20260922**; they are not the current report’s intervals. Problem-level resampling correctly retains dependence across instances and arms: 56 clusters for the complete-label analyses, 53 and 52 after abstention exclusion.

The remaining requested checks pass within these scopes:

- **Registration:** The original P1 registration’s chronology was false, not merely weak. The contrast was committed at 16:32:20, before the registration at 17:31:09. Its withdrawal acknowledges that. Amendment 1 genuinely fixed the primary denominator, bootstrap method, seed and gate beforehand. The secondary and other additions are correctly identified as post hoc.
- **Abstentions:** Keeping them in the denominator is defensible for the share *labelled undetermined*. It does not classify abstentions as genuinely determined. Exclusion answers a conditional question and raises the overlapping contrast by **2.736 points**, or **3.323** for disjoint instances. A smaller result alone would not justify the rule; its estimand and earlier registration do.
- **Comparator:** I reproduced 46/68 versus 24/53 and each comparator rater’s 11/11 repeated-instance agreement. These are different instruments. I found no later use of +22.4’s proximity to +22.6 as corroboration.
- **Broken sheet:** All 42 caught entries lacking an input class received `cannot-tell`; the registered gate fires. The report appropriately limits the comparison to the observed sheet-and-rerating association and disclaims isolating presentation effects.
- **Sheet symmetry:** Both arms use the same mechanical construction. I verified 61/68 and 49/53 concrete witnesses, the stated timeout/unrecovered counts, and the two disclosed newline defects. All 11 duplicate-instance displays are identical. The broader 55/81 agreement count also reproduces; those pairs have identical item bodies.
- **Independence:** The report and pending claims row retain the outside-human limitation. The recorded launcher names **`gpt-5.6-luna`**, not the brief’s `gpt-6-astra`.

No model calls were made and no files were modified.

**not quotable — the revised reliability limitation still assigns six problem clusters to a statistic calculated on four.**
