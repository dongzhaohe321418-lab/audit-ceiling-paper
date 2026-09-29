Reviewed `b8a0693` without modifying files. **The report’s substantive repairs hold.** Inaccurate descriptions remain in companion code, so the distinction is not consistent everywhere in the repository.

1. **Reporting inconsistency — round-2 finding 1 partly fixed; fixed in the report.**  
   [RESULTS-DIAG.md:82](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:82) now correctly calls the stricter procedure a keyword filter, discloses its false exclusion of `ccpp.F5.1`, and separates its counts from agent judgments. The records support this: `cross.d2.jsonl:197` describes pressure values under AT and temperature values under AP; `self.d1.jsonl:197` describes the reordered columns. Restoring that item gives **54 cross / 33 self**, with union coverage unchanged at **105**.

   The Kelvin-token repair removes **three** accidental finding-level matches: `self.d1.jsonl:177`, `self.d1.jsonl:179`, and `self.d3.jsonl:177`. Other qualifying findings preserve those items’ counts.

   However, [posthoc_diag.py:7](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/posthoc_diag.py:7) still says the filter requires a finding to “state the fault itself.” Executable probes still accept “Water is complete and correct; document its unit” for `concrete.F1.0` and “No duplicate rows” for `concrete.F3.0`. These are probes, not additional observed outcomes. This remaining documentation claim is false.

2. **Endpoint terminology — round-2 finding 3 partly fixed repository-wide; fixed in the report.**  
   [RESULTS-DIAG.md:23](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:23) now defines “meets the registered lexical rule”; the title says “naming the injected column,” and the duplication exception is explicit.

   But [diag_match.py:3](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/diag_match.py:3) still says “correctly diagnosed,” and [analyze_diag.py:2](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/analyze_diag.py:2) still calls the analysis “correct diagnosis.” The counterexamples remain `self.d2.jsonl:262` (`supercond.F4.1`, schema listing) and `cross.d4.jsonl:114` (`airfoil.F2.3`, documentation request). Those comments need correction; the frozen registration’s historical wording should remain identifiable as historical.

3. **Psi verdicts — round-2 finding 2 fixed.**  
   The revised verdicts at [diag_supplement.json:271](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_supplement.json:271) accurately distinguish localization from explaining the conversion:
   
   - `concrete.F1.1`: correct strength-column anomaly, no psi identification (`cross.d1:37`).
   - `concrete.F1.2`: “decimal-shifted” remains the finding’s description, not an endorsed explanation (`cross.d2:38`).
   - `concrete.F1.3`: the incorrect 100× reconstruction and the fourth reading’s mixed-unit explanation are both disclosed (`cross.d2:39`, `cross.d4:39`).

   All three injections are **145.038×**. Independently reversing their transformations recovers source-table rows; for example, `4792.5105477174 / 145.038 = 33.0431373`.

   I also checked the other twelve union-only items. The resulting distinction—**fourteen with fault-relevant localization, eleven with supporting explanations of the transformation**—is defensible as the explicitly post hoc item reading at [RESULTS-DIAG.md:84](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:84). It is not a registered diagnostic-accuracy estimate.

4. **Misdescribed counterexample — round-2 finding 4 fixed.**  
   [RESULTS-DIAG.md:74](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:74) now accurately describes `self`’s `supercond.F4.2`: the second reading alleges near-duplicate records with differing targets; the fourth affirms the card’s consistency (`self.d2.jsonl:263`, `self.d4.jsonl:263`). Neither identifies the injected target shuffle.

Independent calculations, without importing the analysis or supplement implementation, reproduce:

| Quantity | Recomputed result |
|---|---|
| Registered validator / cross / self / union | **90 / 57 / 40 / 105** |
| Clean flags, same order | **0 / 9 / 14 / 9** |
| Post hoc lexical cross / self | **53 / 32** |
| Fourteen-item agent selection | **+10.0000 points [5.3691, 15.1079]**; p = **0.0001220703125** |
| New eleven-item agent selection | **+7.8571 points [3.7037, 12.5000]** |
| Ledger valuation | **$13.57609225 + $10.83371550 = $24.40980775** |

The registered H1/H2 intervals and all 28 by-fault intervals reproduce. The seed-7 sample reproduces from 179 eligible texts. All 560 mirrored item files, eight reading files, and both ledgers match their originals; all 280 CSV hashes match the manifest.

**The three quantities are distinguished throughout the revised report, but not everywhere in its companion documentation.** No current report sentence presents the registered or post hoc lexical totals as correct diagnosis. Its eleven-item explanation claim is expressly attributed to the study agent’s unblinded reading.

**Quotable — for the registered lexical result.** The single most important reason is that the revised report now limits its central claim to what the scoring rule actually measures.

Reader statement: “On 280 new samples from four previously used tables, adding cross-model audit findings increased coverage under a preregistered lexical rule from 90 to 105 of 140 faulty items, while flagging 9 of 140 clean items; these counts do not establish correct diagnosis.”
