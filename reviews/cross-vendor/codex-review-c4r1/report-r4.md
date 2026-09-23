**The three principal repairs pass. I would permit qualified quotation of the measured results.** Some overbroad sentences remain, including one introduced by this repair.

The withdrawal now reaches Amendment 2: the second provenance gap is explicitly withdrawn, the π values match storage, and the correction acknowledges that adjudicated `cross-R` draw 1 contributes to its union. Ledger rows 165–166 independently give **12:40:09.384**; **12:47:51** is correctly identified as manifest separation.

The failed-attempt recount is finally correct:

| Recorded category | Rows | HTTP 429 occurrences |
|---|---:|---:|
| One 429 occurrence | 88 | 88 |
| Two | 6 | 12 |
| Three | 2 | 6 |
| Breaker refusals | 6,903 | 0 |
| TLS failure | 1 | 0 |
| **Total** | **7,000** | **106** |

The retry implementation supports multiple recorded 429s within one attempt. “No accepted reading and no recorded usage charge” is appropriately bounded; actual zero provider expenditure is not established.

Four remaining sentences need narrowing, although they do not invalidate qualified quotation:

- **The new caveat overstates dependence on labels.** [Results, line 265](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:265) makes *every figure* in §3 conditional on surviving labels. The archived nine flagged instances and the kill’s upper bound are independently verifiable without labels. Use **“Every adjudication-derived figure.”** This is another repair making the evidence sound weaker than it is.
- **A downstream sentence still conflates failures with rate limits.** [Line 457](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:457) says “the denials counted above are HTTP 429 rate-limiting.” Only 96 rows contain that evidence. Refer specifically to those rows.
- **Complete compliance is not established.** [Line 467](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:467), “Nothing else in the preregistration is unmet,” conflicts with Amendment 2’s acknowledged manifest deficiencies and §3’s provenance caveat. “All registered outcomes are reported” would fit the evidence.
- **“No ceiling at all” remains too strong.** [Line 121](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:121) should describe the ZIBB boundary estimate near 100%, without suggesting it establishes universal eventual detectability.

Reproduction succeeded:

| Outcome | Independently reproduced |
|---|---|
| H20a | 67 versus 33; +30.9 points [19.1, 43.1]; discordance 38/4; McNemar, sign-flip, Tango and grid intervals |
| H20b | Fits 58.6225% versus 31.5002%; paired difference +27.1223 [10.9321, 39.0358], refitting both within 10,000 resamples |
| H20c | 55 versus 24; +20.7 points [12.8, 28.8]; single-draw FP 23.5833%; no draw meets the bar |
| H20d | 56 → 32; 23 unexercised-edge and one spec-misreading instance leave |

`numbers.json` and `tables.md` regenerate **byte for byte**, with writes intercepted in memory; all 16 spliced blocks match. All **16 report tests pass**. The earlier Amendment 2 regeneration preserved `numbers.json`; the subsequent round-2 commit changed its explanatory label, not numerical results.

All nine draws contain 260 unique accepted readings. All 2,340 archived readings agree with cache finding counts, BLOCKER hashes, prompt digests and frozen solution digests. Ledger cost is **$19.83767825**. Amendment 1 was committed during draw 1, after 93 recorded completions; whether the author had read results is not independently observable. The interruption is adequately disclosed.

The sheet, key and both CSV hashes verify. Archived findings independently recreate the shuffled key. All sixteen adjudication counts and both interval types reproduce. Naming κ is **0.3907284768**. Recognition κ is correctly **undefined**: observed and expected agreement both equal one. Raw-reply-to-CSV verification remains impossible because L2’s source artefacts are missing.

For my independent reading, I used the first fifteen shuffled items before consulting their labels:

| My naming judgment | Items |
|---|---|
| Yes; defect asserted | K0001, K0004, K0008, K0011, K0013, K0015 |
| No | K0002, K0003, K0005, K0006, K0009, K0010, K0012, K0014 |
| Cannot tell | K0007 |

I favor the **stricter interpretation**, but neither rater consistently applies it: I match each on 12/15. K0012/K0014 describe overflow rather than the recorded rounding failure; K0006/K0009 describe a different name-filtering discrepancy. K0007’s timeout provides insufficient evidence to connect it to overflow. This supports reporting asymmetry descriptively and leaving its cause unresolved.

The L2 loss permits quotation **conditional on surviving labels**, not certification of independently auditable adjudication. The kill remains independent of that loss: **9 < 20**, even under perfect adjudication. The 5-of-110 result cannot be compared directly with the eight-reading 30.0% union.

No files were modified. `src/` and kernel directories are unchanged across the study; no corpus or finding text was added in its committed records. I ran the report tests, not the full application suite.

**Quotable, with qualification — the measured coverage improvement reproduces without establishing a higher true ceiling.**

Reader sentence: “On this frozen benchmark, the referent-rule arm increased eight-reading BLOCKER coverage by 30.9 points (95% problem-cluster interval 19.1–43.1), with 20.7 points more union false positives (12.8–28.8); no higher true ceiling is established, and the separate single-reading result of five defect-asserting instances out of 110 remains conditional on surviving labels whose L2 production cannot be audited.”
