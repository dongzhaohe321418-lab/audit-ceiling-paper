The arithmetic and recorded chronology check out. The blocking issue is interpretation: the executable rule demonstrably credits findings that do not diagnose the injected fault. No files were modified.

1. **Major, blocking for quotation as “correct diagnosis.” The reported endpoint includes unrelated findings.**  
   [RESULTS-DIAG.md:33](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:33), [RESULTS-DIAG.md:47](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:47), and [diag_match.py:72](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/diag_match.py:72).

   Concrete counterexamples from executing the frozen rule and reading the credited observations:

   | Family / item | Credited finding | Record |
   |---|---|---|
   | `cross`, `airfoil.F2.3` | Requests column definitions; mentions frequency and displacement thickness. Does not identify the injected negative values. Other three readings have no BLOCKER. | [cross.d4.jsonl:114](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d4.jsonl:114) |
   | `self`, `supercond.F4.0` | Complains about insufficient rows; mentions `critical_temp` while acknowledging the schema. Does not diagnose target shuffling. | [self.d4.jsonl:261](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d4.jsonl:261) |
   | `self`, `supercond.F4.1` | Another sample-size complaint, credited because it names `critical_temp`. | [self.d2.jsonl:262](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d2.jsonl:262) |
   | `self`, `concrete.F7.4` | Complains about row count while listing columns. No rounding diagnosis. | [self.d1.jsonl:70](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d1.jsonl:70) |
   | `self`, `supercond.F7.3` | Lists columns and explicitly says the structure requirement is satisfied. Nevertheless labelled BLOCKER and credited as rounding diagnosis. | [self.d4.jsonl:279](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d4.jsonl:279) |
   | `self`, `concrete.F5.2` | Complains about missing ranges/schema and lists both swapped columns. Does not identify their swap. | [self.d3.jsonl:58](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d3.jsonl:58) |

   The third credited `self` shuffle item, `supercond.F4.2`, has a near-duplicate complaint and a separate affirmative statement about documentation, rather than an identified target permutation ([self.d2.jsonl:263](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d2.jsonl:263), [self.d4.jsonl:263](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d4.jsonl:263)). Thus the claim that `self` diagnosed three shuffled targets is unsupported as a semantic diagnosis claim.

   The implementation also requires **four flags but only one matching reading** for `self`, not four agreeing diagnoses ([analyze_diag.py:106](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/analyze_diag.py:106)). This deserves explicit disclosure.

2. **Major qualification. The rule is neither uniformly conservative nor a validated lower bound; one H1 gain gives an incorrect permutation.**  
   [RESULTS-DIAG.md:58](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:58), [RESULTS-DIAG.md:75](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:75).

   `concrete.F5.0`, one of H1’s 15 added items, swaps **Superplasticizer and Fine Aggregate**, leaving Coarse Aggregate unchanged ([manifest:1166](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/data_items_ho.json:1166)). Its sole matching reading instead describes a three-column reassignment involving Coarse Aggregate ([cross.d1.jsonl:56](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:56)). It identifies a real misassignment but does not correctly describe the injected permutation.

   Conversely, the rule excludes relevant findings: `cross` identifies impossible values in `supercond.F5.0` and `supercond.F5.3`, and `self` identifies out-of-range AT values in `ccpp.F5.2`, but each names only one swapped column ([cross.d1.jsonl:266](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:266), [cross.d1.jsonl:269](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/cross.d1.jsonl:269), [self.d1.jsonl:198](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_readings/self.d1.jsonl:198)).

   Executable probes also accept “No duplicate rows” for F3 and “PE is complete and correct” for F4. The rule is liberal about meaning and restrictive about wording.

   **Effect on H1:** the unrelated `cross` documentation finding is already covered by the validator, so removing it leaves H1 unchanged. As a post hoc sensitivity check, excluding `concrete.F5.0` leaves **14 added items, +10.0 points [5.37, 15.11], exact p = 0.0001221**, with the same 9 clean flags. H1 still passes. These findings undermine the endpoint’s interpretation, not the reproduced registered decision.

   The claimed seed-7 inspection is not reproducible from the supplied records: no ten selected finding identifiers, sampling population/order, or inspection script is supplied. I cannot verify that particular sample’s characterization.

3. **Minor reporting deviation. Preregistered fault-specific intervals are missing.**  
   [PREREGISTRATION-DIAG.md:89](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/PREREGISTRATION-DIAG.md:89) promises counts and shares with intervals by fault type. [RESULTS-DIAG.md:43](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:43) supplies only counts; the `by_fault` records likewise contain no intervals ([diag_results.json:40](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/code/records/ai4s/diag_results.json:40)). The validator’s clean interval is also omitted from the report; its registered empirical bootstrap yields the degenerate interval [0, 0], which should not be interpreted as certainty of zero population risk.

4. **Minor qualification. “Spend” is ledger API valuation, and the halt is not a hard spending cap.**  
   [RESULTS-DIAG.md:6](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/RESULTS-DIAG.md:6), [data_audit_run_ho.py:99](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/data_audit_run_ho.py:99).

   The ledgers sum to **$24.40980775**: cross **$13.57609225**, self **$10.83371550**. This verifies $24.41 of `api_value_usd`, not an invoiced cash expenditure; the self route uses Claude Code. The records contain **2,244 completion events**, including four extra self events, for **2,240 retained readings**.

   The runner submits a draw through `ThreadPoolExecutor.map` and checks cost after every 25 returned results ([data_audit_run_ho.py:208](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-diag/benchmarks/ai4s/data_audit_run_ho.py:208)); pending work can continue after a threshold check. No actual budget overrun occurred here.

I independently recomputed the analysis without importing or running `analyze_diag.py`, using the raw records and executing the frozen diagnosis matcher. Every displayed numerical result reproduces:

| Tier | Diagnosed / 140 | Diagnosis % [95% interval] | Clean flags / 140 | Clean % [95% interval] |
|---|---:|---:|---:|---:|
| Validator | 90 | 64.3 [56.4, 72.1] | 0 | 0.0 [0.0, 0.0] |
| Cross | 57 | 40.7 [32.6, 48.9] | 9 | 6.4 [2.8, 10.5] |
| Self | 40 | 28.6 [21.7, 35.9] | 14 | 10.0 [5.6, 14.8] |
| Validator or cross | 105 | 75.0 [67.6, 81.9] | 9 | 6.4 [2.8, 10.5] |

Development clean counts at thresholds 1–4 are cross **4, 0, 0, 0** and self **67, 49, 26, 10**, reproducing the registered percentages and operating points. Development calibration reproduces **60 cross, 65 self, 91 validator**; the development union adds **18/140 = 12.9 points**.

Held-out F1–F7 counts reproduce:

| Tier | F1 | F2 | F3 | F4 | F5 | F6 | F7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Validator | 5 | 20 | 20 | 0 | 5 | 20 | 20 |
| Cross | 13 | 14 | 0 | 0 | 12 | 18 | 0 |
| Self | 11 | 12 | 0 | 3 | 5 | 7 | 2 |
| Union | 13 | 20 | 20 | 0 | 12 | 20 | 20 |

H1 reproduces **+10.7143 [5.9603, 15.9420] points**, discordants **15:0**, exact McNemar **p = 0.00006103515625**. H2 reproduces **+12.1429 [4.1379, 20.3008]**, discordants **27:10**, **p = 0.0076320786**. Faulty flags are **63/46**, and S1 is **6/6**. All nine cross clean flags are airfoil documentation objections, as reported. H1 passes its registered **empirical-rate** criterion; the union interval extending above 10% means this is not confidence-level assurance that its population rate is below budget.

Recorded provenance supports registration before construction and calls:

- `a6c04af` registration: **September 24, 17:42:10 +08:00**.
- All 560 held-out CSV/card files have creation and modification times within **17:42:27.126–17:42:27.621**.
- Manifest committed at `5affaed`: **17:42:37**.
- Earliest ledger-derived call starts are approximately **17:42:37.433 cross** and **17:42:53.461 self**, both after registration.
- Every retained reading maps to a ledger run ID. Both families have exactly four successful readings for every item. Archived readings are byte-identical to the original run files.
- All CSV hashes, task hashes, cards, injected parameters, and validator results check out. An in-memory rebuild reproduces all 280 items. No held-out CSV hash occurs in development.
- Builder/runner differences are limited to registered changes, and all five study scripts remain unchanged from registration.

These are consistent local provenance records, not independent timestamp attestation proving the absence of unrecorded earlier activity. I found **no execution departure requiring an amendment**. The missing intervals are a reporting omission; changing the diagnosis rule now would be a post hoc analysis, not a retroactive preregistered repair.

**Not quotable as written.** The most important reason is that lexical matches are presented as correctly diagnosed faults despite concrete counterexamples.

Reader statement: “On 280 new samples from four previously used tables, adding cross-model audit findings to the validator increased coverage under a preregistered lexical matching rule from 90 to 105 of 140 faulty items, with 9 of 140 clean items flagged; the rule does not establish correct diagnosis.”
