**Not quotable at `707c3f7`.** The numerical results reproduce, but the withdrawal still contradicts Amendment 2, and the denial-count repair introduces another factual error. No files were modified.

1. **The withdrawal did not reach Amendment 2.** [PREREGISTRATION.md:154](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/ceiling4/PREREGISTRATION.md:154) still says the within-draw interval could not be reproduced and calls it a second provenance gap. I independently recovered **12:40:09.384** from archived ledger rows 165–166. The results’ withdrawal is correct; this surviving assertion is not.

   Amendment 2 also retains two other superseded statements: “no text from the eight-reading unions” at line 132, although adjudicated `cross-R` draw 1 contributes to its union; and the inaccurate shortened π values at lines 110–111. This is precisely the incomplete-withdrawal failure the review was asked to detect.

2. **96 is a count of failed-attempt rows, not HTTP responses.** [RESULTS-CEILING4.md:419](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:419) says “96 HTTP 429 responses” and “Only 96 calls were refused by the provider.” The records contain:

   - 88 rows mentioning one HTTP 429;
   - 6 mentioning two;
   - 2 mentioning three;
   - 6,903 circuit-breaker refusals;
   - one TLS failure.

   Thus **96 rows contain 106 recorded HTTP 429 occurrences**. The provider retry code explains the repeated responses within a row. Say “96 failed-attempt rows containing HTTP 429 errors,” and distinguish those rows from responses. The subsequent sentence calling the denials collectively HTTP 429 rate limiting also remains inaccurate.

   Similarly, “a denial spends nothing” exceeds the evidence for the TLS failure. The supported statement is that these attempts produced no accepted reading and no recorded usage charge.

3. **The explanation of rater disagreement is still too definite.** [RESULTS-CEILING4.md:311](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:311) still says “not noise in both directions” and that a property of the findings “is part of the reason.” The observed 16-versus-7 split establishes descriptive asymmetry, not its cause. My item readings support ambiguity and inconsistent application by both raters. Present the proposed explanation as an interpretation.

Two smaller wording issues deserve correction: the L2 caveat currently sits in **§2**, before the mixed-results bullet, rather than within §3; and “the hidden suite reached no … model” should explicitly describe the auditor’s input boundary, since the adjudication sheet contains hidden-failure witnesses.

**The L2 loss alone does permit qualified quotation.** It prevents independently verifying how L2 produced the labels; it does not invalidate arithmetic reproducible from those labels, the archived flags, or the kill’s upper bound. It does not satisfy the original provenance standard, and disclosure cannot restore that compliance.

For quotation of the adjudicated result, use:

> On one shipped-constitution reading, the surviving human/model consensus labels classify 5 of 110 instances as having a defect-asserting finding (problem-cluster 95% interval 0.9–8.9%); naming agreement was κ = 0.391, and L2’s label production is unauditable because its raw reply, prompt, launcher and execution log were lost.

That is a result **conditional on surviving labels**, not a independently verified adjudication execution. It must not be compared directly with the eight-reading 30.0% union.

The verification completed as follows:

- **Regeneration:** ran the report with its writes intercepted in memory. Both output files reproduce **byte for byte**, and the results splice matches exactly. `numbers.json` was unchanged by `c638b49`; `707c3f7` changes only the secondary’s explanatory label, not numerical values.
- **Independent calculations:** directly loaded the records and separately implemented the cluster resampling and saturation fitting, including all **10,000 paired refits**.

| Outcome | Independently reproduced |
|---|---|
| H20a | 67 versus 33; +30.909 points, cluster [19.091, 43.119]; discordance 38/4; McNemar 5.653×10⁻⁸ |
| H20b | A(`cross`) 31.500%, cluster [21.524, 45.967]; A(`cross-R`) 58.622%, [46.838, 70.202]; difference +27.122 points, [10.932, 39.036] |
| Flattening gains | `cross` 1.9318 points; `cross-R` 0.5682 points |
| H20c | 55 versus 24; +20.667 points, cluster [12.752, 28.758]; single-draw FP 23.583%, zero qualifying draws |
| H20d | 56 → 32; 23 unexercised-edge and one spec-misreading leave; none enter |

The independently sampled sign-flip results also match. Report regeneration reproduces the Tango, grid-unconditional and ZIBB outputs. The ceiling withdrawal is substantively correct: these results establish higher observed coverage at K = 8, not higher true saturation. The family-specific raw-union correction is correct.

- **Run integrity:** all nine draws contain 260 distinct instances. All 2,340 archived finding records match the cache’s BLOCKER-text hashes, finding counts and prompt hashes. The usage ledgers total **$19.83767825**. The interruption and noncontemporaneous readings are adequately disclosed in the results once the contradictory amendment is corrected.
- **Timing:** preregistration and driver commits precede the earliest ledger-derived request start. Amendment 1 was committed during draw 1, with **93 ledger completions already recorded**. “Before any result was read” remains an author attestation; timestamps cannot verify it.
- **Adjudication integrity:** sheet, key and both CSV hashes verify; all 80 keyed findings and solutions match the archive. Explicit arm, severity, stratum and instance metadata are absent from the sheet. This verifies the sheet’s construction, not L2’s actual exposure. Its missing raw reply cannot be parsed against the CSV.
- **Agreement:** cells 39/7/16/18 give 57/80 agreement and **κ = 0.3907284768**. Recognition κ is correctly **undefined**: both raters assign “defect” to all 39 consensus-named items, making expected agreement one.
- **All sixteen rates and their Wilson/cluster intervals reproduce.** Counts below are over 110:

| Arm/question | Consensus | L1 | L2 | Either |
|---|---:|---:|---:|---:|
| T naming | 5 | 5 | 7 | 7 |
| T defect-asserting | 5 | 5 | 7 | 7 |
| R naming | 26 | 29 | 36 | 39 |
| R defect-asserting | 26 | 29 | 32 | 35 |

The kill explanation is correct independently of these labels: **only nine T instances have any finding, so even perfect adjudication cannot reach twenty**.

I rated the first fifteen shuffled sheet items before inspecting their corresponding CSV labels:

| Item | My naming judgment | Reason |
|---|---|---|
| K0001 | Yes; defect | Negative-bound exception matches. |
| K0002 | No | Test imports do not explain the timeout. |
| K0003 | No | Trailing newline differs from the recorded decimal failures. |
| K0004 | Yes; defect | Ignoring the supplied length matches. |
| K0005 | No | Test-module imports differ from unsorted-input failures. |
| K0006 | No | Rejected punctuation-leading names do not explain the recorded overcounts. |
| K0007 | Cannot tell | Timeout witness cannot establish the asserted overflow cause. |
| K0008 | Yes; defect | Unhashable elements match. |
| K0009 | No | Same mismatch as K0006. |
| K0010 | No | Missing leading digits differ from the recorded failures. |
| K0011 | Yes; defect | Unequal lengths and indexing failure match. |
| K0012 | No | Overflow at very large inputs differs from finite precision errors. |
| K0013 | Yes; defect | Floor division matches. |
| K0014 | No | Same overflow/precision distinction as K0012. |
| K0015 | Yes; defect | Duplicate multiplicity matches. |

**I favour the stricter interpretation, but not L1 categorically.** I side with L1 against L2 on K0012/K0014, and with L2 against L1 on K0006/K0009. Each agrees with me on 12/15; K0007 remains indeterminate. This small sample does not establish either rater’s overall accuracy.

The 16 report tests pass. The full application suite and frozen rebuild were not run in this read-only review. The study diff leaves `src/` and kernel directories untouched; the committed study records contain no corpus or finding text.

**Not quotable — the single most important reason is that Amendment 2 still asserts the provenance loss that this repair explicitly withdraws.**
