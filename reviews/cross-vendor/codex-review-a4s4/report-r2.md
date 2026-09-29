Reviewed `2b4855e` without modifying files. The arithmetic reproduces. The repairs substantially improve disclosure, but several semantic claims remain inaccurate.

1. **Major — the “stricter reading” remains a lexical filter, and its description overstates what it verifies.**  
   [RESULTS-DIAG.md:87](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:87) says counted findings must “state the fault itself.” Two concrete counterexamples contradict that description:

   - **Wrong exclusion:** `cross`’s `ccpp.F5.1` finding explicitly places ambient-pressure values under AT and temperature values under AP. Another reading calls this a “reversal.” `self` likewise correctly describes the reordered columns. These diagnose the manifest’s AT/AP swap, but the regex excludes them because it lacks those formulations. See [cross.d2.jsonl:197](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d2.jsonl:197), [self.d1.jsonl:197](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d1.jsonl:197), and [diag_posthoc.json:7](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_posthoc.json:7). Therefore the report’s statement that all three excluded power-plant swaps merely describe out-of-range values is false.
   - **Wrong admission at finding level:** the Kelvin token `"k "` matches the end of **“task ”**. Consequently, the second BLOCKER in [self.d1.jsonl:179](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d1.jsonl:179) passes despite containing no injected number, unit explanation or scaling diagnosis. The same happens in [self.d3.jsonl:177](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d3.jsonl:177). The cause is [posthoc_diag.py:46](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/posthoc_diag.py:46), used by the substring check at line 82.

   Executable probes also admit affirmative or negated statements such as “Water is complete and correct; document its unit” and “No duplicate rows.” These are probes, not additional observed outcomes.

   **Effect:** restoring `ccpp.F5.1` would increase the post hoc counts from 53/32 to 54/33. It is already validator-covered, so the union and strict contrast would not change. Removing the accidental Kelvin matches also leaves item counts unchanged because those items have other qualifying findings.

2. **Major qualification — several union-only verdicts do not accurately characterize the injected transformation.**  
   The problematic verdicts are at [diag_supplement.py:40](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/diag_supplement.py:40) and [diag_supplement.json:271](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_supplement.json:271).

   `concrete.F1.1`, `.F1.2` and `.F1.3` all convert selected strength values from MPa to psi using **145.038×**, as the manifest and CSVs confirm. The findings identify anomalous strength values, but:
   
   - `.F1.1` does not identify psi or establish the verdict’s “thousands of times” characterization.
   - `.F1.2` calls the values “decimal-shifted”; that is not an accurate account of the injected conversion.
   - `.F1.3` includes an explicit **100×** reconstruction that is wrong. For example, `4792.5105477174 / 145.038 = 33.0431373`, not the claimed `47.925105477174`. Its fourth reading does correctly identify values in another unit without claiming a factor.

   Thus “fourteen with the right columns” is defensible as **fault-relevant localization**, but not as fourteen fully correct explanations of the injected transformations. The post hoc numerical result survives that narrower interpretation.

3. **Reporting qualification — the renamed endpoint still claims more than column matching.**  
   [RESULTS-DIAG.md:1](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:1) and [RESULTS-DIAG.md:25](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:25) call the endpoint “naming the injected fault.” A schema listing mentioning `critical_temp` still counts without naming shuffling; a documentation request still counts without naming negation.

   The tables and caveats now describe this correctly. The title and defined endpoint should likewise say **meeting the registered lexical rule** or **naming the injected column**, with the duplication exception stated. The underlying records remain [self.d2.jsonl:262](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d2.jsonl:262) and [cross.d4.jsonl:114](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d4.jsonl:114).

4. **Minor — one counterexample is described incorrectly.**  
   [RESULTS-DIAG.md:76](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:76) groups `self`’s `supercond.F4.2` with row-count/card complaints. Its matching second-draw finding actually alleges duplicate or near-duplicate records with differing target values; its fourth-draw finding affirms the documentation. See [self.d2.jsonl:263](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d2.jsonl:263). Neither identifies the injected target shuffle, so its exclusion remains justified. This corrects an imprecision also present in round 1.

**Disposition of every round-1 finding**

| Round-1 finding | Status | Assessment |
|---|---|---|
| Lexical matches presented as correct diagnosis; unclear self aggregation | **Partly fixed** | Tables, caveats and “four flags, one matching reading” disclosure are fixed. “Names the injected fault” still overstates the endpoint. |
| Unsupported conservatism/lower-bound claim; wrong permutation; missing relevant findings; unreproducible sample | **Partly fixed** | Lower-bound claim withdrawn; wrong permutation and relevant misses disclosed. Sample reconstruction now reproduces. New verdict inaccuracies and scorer limitations remain. |
| Missing by-fault intervals and validator clean interval | **Fixed** | All 28 by-fault intervals reproduce; validator’s degenerate clean interval is disclosed. |
| Spend versus API valuation; halt versus hard cap | **Fixed** | Ledger valuation, extra events and periodic halt checking are accurately described. |

The seed-7 reconstruction selects exactly the recorded ten findings from **179 eligible reading-level texts**. All ten are fault-relevant. This establishes reproducibility of the reconstruction, not contemporaneous proof that these were the originally inspected ten.

**My assessment of all fifteen union-only verdicts**

Each row refers to the corresponding verdict in [diag_supplement.json:264](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_supplement.json:264). I checked the findings against the manifest, CSV and card.

| Item | Agreement with recorded verdict | Supporting reading |
|---|---|---|
| `airfoil.F1.0` | **Agree.** Correct chord column and 1000× scaling. | [cross.d3:106](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d3.jsonl:106) |
| `airfoil.F1.3` | **Agree.** Correct thickness column and 1000× scaling. | [cross.d1:109](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:109) |
| `airfoil.F5.1` | **Agree.** Correct frequency/pressure swap. | [cross.d1:127](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:127) |
| `airfoil.F5.2` | **Agree.** Correct frequency/chord swap. | [cross.d1:128](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:128) |
| `airfoil.F5.4` | **Agree.** Correct attack-angle/pressure swap. | [cross.d2:130](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d2.jsonl:130) |
| `concrete.F1.0` | **Agree.** Correct water column and approximately 1000× scaling. | [cross.d1:36](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:36) |
| `concrete.F1.1` | **Partly agree.** Correct column and scale anomaly; verdict overstates factor/unit identification. | [cross.d1:37](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:37) |
| `concrete.F1.2` | **Partly agree.** “Decimal-shifted” accurately quotes the finding, but does not correctly explain the 145.038× injection. | [cross.d2:38](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d2.jsonl:38) |
| `concrete.F1.3` | **Partly agree.** Correct localization; inaccurate scaling claims. Draw 4 supplies a valid mixed-unit explanation. | [cross.d4:39](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d4.jsonl:39) |
| `concrete.F1.4` | **Agree.** Correct cement column and 1000× scaling. | [cross.d2:40](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d2.jsonl:40) |
| `concrete.F5.0` | **Agree with “PARTLY WRONG.”** Finding invents a three-column reassignment; the injection swaps only superplasticizer/fine aggregate. Exclusion is justified. | [cross.d1:56](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:56) |
| `concrete.F5.3` | **Agree.** Correct coarse-aggregate/strength swap. | [cross.d1:59](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:59) |
| `concrete.F5.4` | **Agree.** Correct water/strength swap. | [cross.d1:60](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:60) |
| `supercond.F1.3` | **Agree.** Correct radius column, impossible mean/range relationship and 100-fold scale discrepancy. | [cross.d4:249](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d4.jsonl:249) |
| `supercond.F5.1` | **Agree.** Correct ionization-energy/valence reversal; quoted single-element row exists. | [cross.d3:267](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d3.jsonl:267) |

The other disclosed relevant exclusions, `cross`’s `supercond.F5.0/.F5.3` and `self`’s `ccpp.F5.2`, identify consequences in one swapped column. They remain excluded by the explicit both-column requirement. They do not establish the complete swap and do not alter the strict contrast as defined.

**Independent numerical checks**

I recomputed the bootstrap statistics without importing the analysis or supplement implementation, and separately reimplemented the post hoc filter.

| Quantity | Recomputed result |
|---|---|
| Registered validator / cross / self / union | **90 / 57 / 40 / 105** |
| Clean flags, same order | **0 / 9 / 14 / 9** |
| Registered H1 | **+10.7143 points [5.9603, 15.9420]**, 15:0, p = **0.00006103515625** |
| Registered H2 | **+12.1429 points [4.1379, 20.3008]**, 27:10, p = **0.007632078603** |
| Post hoc executable filter | **53 cross / 32 self; union 105** |
| Post hoc exclusion of `concrete.F5.0` | **14 added; union 104; +10.0 points [5.3691, 15.1079]**, p = **0.0001220703125** |

All reported by-fault intervals reproduce. All **560 mirrored files** match their originals; all CSV hashes, cards and validator outputs match the manifest. The 2,240 archived readings match their originals. Ledger totals reproduce **$13.57609225 + $10.83371550 = $24.40980775**, across 2,244 events.

Registered and post hoc quantities are clearly separated in the revised report and new records. The remaining problem is semantic validity, not concealed post hoc status or arithmetic.

**Not quotable as written.** The single most important reason is that the revised “fault-specific” interpretation still exceeds what its lexical scoring and recorded verdicts establish.

Reader statement: “On 280 new samples from four previously used tables, adding cross-model audit findings increased coverage under a preregistered lexical rule from 90 to 105 of 140 faulty items, with 9 of 140 clean items flagged; these counts do not establish correct diagnosis.”
