**The arithmetic reproduces, but the report is not ready for quotation.** I reviewed `d57f404` read-only, using the CSVs, key, archived witnesses, comparator records and paper-repository history. No model calls or file changes were made.

1. **Blocking: the “missed” and “caught” groups overlap.** The key contains 121 entries but only **110 unique instances**: 11 instances appear in both arms. For example, `b2:Mbpp/300` is “missed” at H001 and “caught” at H096. This is the exact comparison the [claims ledger already rejects](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:97). The [comparator report](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RERATE.md:7) explains that the 68-item sheet comprises 57 residual instances plus 11 caught instances.

   Thus +19.8 measures the difference between two overlapping sheet groups, not the stated missed-versus-caught populations. As a **post-hoc diagnostic only**, removing the 11 caught instances’ “missed” copies gives **38/57 versus 23/53, +23.27 points [2.45, 44.04]**. The error understates that contrast; modesty does not make the population claim correct.

2. **Blocking: the claimed registration chronology is contradicted by committed results.** The [registration](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P1-ANALYSIS-REGISTRATION.md:5) candidly acknowledges that ratings existed, but then claims no contrast had been computed and neither arm’s rate had been seen.

   Paper commit **`b0719cd`, September 22 at 16:32:20**, already records **43/68, 23/53, +19.8**, and a bootstrap interval using seed 20260921. The P1 registration, **`28994e3`**, was committed at **17:31:09**. Both CSVs are byte-identical to their versions committed at `d81d4b0`, before that registration. The [earlier outcome remains visible](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:214).

   This establishes prior computation, although it cannot establish what a particular later session remembered. The registration describes its weakness incompletely: this was also **after the primary result had been recorded**, not merely after label collection.

3. **Blocking: rater identity and timing conflict with the provenance records.** [RESULTS-RATE3](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:5) attributes L3 to `gpt-6-astra` and places both readings on September 22. However, the [launcher](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/third_rater.py:32) specifies `gpt-5.6-luna`; P3’s outcomes attribute both readings to that model and date the broken-sheet reading September 21. Its outcome was already committed that evening.

   The CSVs establish the labels, not which model produced them. These contradictions require reconciliation from existing execution evidence; another model call would not repair historical provenance.

The independent arithmetic check used Python’s seeded generator, 10,000 problem-cluster resamples, and linearly interpolated percentiles, without calling `analyse.py`’s analysis functions:

| Reading | Missed-labelled entries | Caught-labelled entries | Difference, points | 95% interval | Clusters |
|---|---:|---:|---:|---:|---:|
| Primary | 43/68 = 63.2353% | 23/53 = 43.3962% | 19.8391 | [1.5053, 38.1792] | 56 |
| Excluding `cannot-tell` | 43/61 = 70.4918% | 23/48 = 47.9167% | 22.5751 | [2.1113, 42.6256] | 53 |
| Broken sheet | 42/68 = 61.7647% | 4/53 = 7.5472% | 54.2175 | [38.7566, 69.7562] | 56 |

All 10,000 resamples were usable for each analysis. The comparator’s **46/68 versus 24/53 = +22.3640** also reproduces from its rating CSVs. Problem-level clustering correctly keeps batches and overlapping entries together; it cannot correct erroneous arm membership.

4. **The `cannot-tell` rule is defensible for the registered label-frequency estimand.** Counting it in the denominator estimates the proportion **labelled `undetermined`**, without claiming abstentions are determinate. Exclusion answers a different, conditional question. Both are reported, and their difference is **2.7361 points**. The smaller headline is neither evidence of manipulation nor proof of conservatism for an underlying specification property.

   The numerical analyses follow these registered rules. One explicit reporting commitment is missing: [the registration promises Wilson intervals alongside](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P1-ANALYSIS-REGISTRATION.md:37), but neither the report nor `analysis.json` supplies them. The primary arm intervals would be [51.4, 73.7] and [31.0, 56.7], ignoring clustering.

5. **The instruments differ substantively, and I found no later appeal to numerical closeness.** The comparator uses two-rater consensus, a six-category hierarchy and expected/actual witness values. L3 uses one rater, three options and inputs without hidden expected values. Consequently, it does not directly check whether the **particular hidden expected value** follows from the prose. The difference goes beyond option count. Also, the registration incorrectly lists `disputed` among the selectable categories: it is a consensus outcome.

   The report appropriately refuses to treat +22.4 and +22.6 as replication. Its broad heading “undetermined specifications” should nevertheless remain explicitly tied to operational labels.

6. **The repair is symmetric in procedure, but its description and implementation have defects.** Both arms receive the same witness-display function; all specification and visible-test text matches the key. I found no arm-specific repair rule or active 300-character truncation. Concrete inputs appear for **61/68** and **49/53** entries.

   However, [the claim that every remaining entry is a timeout](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/rebuild_sheet.py:9) is false: the missed-labelled remainder contains **five timeouts and two unrecovered-input cases**, H083/H089. Also, regex replacement interprets escaped `\n` as an actual newline in H003/H117, altering two caught entries’ displayed input representations. These are real repair defects, although I have not attributed any label changes to them.

7. **The exploratory interpretation overclaims causality, despite correctly limiting its subject to sheets.** The ratio **2.7329**, **67 changed labels**, and the exact correspondence between 42 empty caught input classes and 42 broken-sheet abstentions all check out.

   But [“the mechanism is entirely in the caught arm”](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:44) is false: **21 missed-arm labels and 46 caught-arm labels changed**. The missed `undetermined` rate rose 1.47 points; the caught rate rose 35.85 points. Both presentations changed and the model was rerun. This supports a descriptive association with the sheet repair, not exclusive causal attribution or the general assertion that unanswerable controls necessarily produce hypothesis-favouring numbers. I found no sentence explicitly turning this exploratory comparison back into specification evidence.

Finally, the refusal to satisfy P1’s outside-human requirement is explicit. But [the L1 limitation](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:62) is inaccurate in both directions: L1’s records cover **all 110 unique instances**, not just 57, while previous author ratings do **not themselves prevent another rater from reviewing independently**. That is precisely what P1 proposes.

**not quotable — the headline calls overlapping groups “missed against caught,” although 11 caught instances are also counted as missed.**
