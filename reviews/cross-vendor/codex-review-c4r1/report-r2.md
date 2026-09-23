The original ceiling overclaim is repaired, and the numerical results reproduce. **I would not clear c638b49 for quotation yet:** the repair introduces an incorrect provenance conclusion and leaves one withdrawal incomplete.

1. **The draw-5 gap is recoverable.** The [new run-history text](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:415) overlooks the archived usage ledger. Its [rows 165–166](/Users/ericdong/Documents/Crossaudit/study-data/wt-ceiling4-runs/projects/project-holistic__cross-R__d5/.crossaudit/usage.jsonl:165) record completions at **2026-09-10 15:31:49.682Z** and **2026-09-11 04:11:59.066Z**, exactly **12:40:09.384 apart**. These are also the latest completion before interruption and earliest after resumption. The committed cache lacks timestamps; the supplied archive does not. This is not a permanent provenance loss. The manifest difference, **12:47:51**, is correct, but measures the separation of two end-of-invocation records, not the interruption itself.

2. **“No text was adjudicated” survives regeneration.** It remains in the [generator](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/report_ceiling4.py:592) and `numbers.json:1783`, under a secondary that includes `cross-T`. Furthermore, “No text from these eight-reading unions was adjudicated” remains literally incorrect for `cross-R`: its adjudicated draw 1 contributes to that union. The supported replacement is: **“Neither complete eight-reading union was adjudicated; cross-R draw 1 and the separate cross-T reading were.”** Byte-identical regeneration preserved this stale claim.

3. **Two smaller new assertions need correction.** The 7,000 failed-attempt rows comprise **96 reporting HTTP 429, 6,903 circuit-breaker refusals, and one TLS failure**, not 7,000 HTTP 429 responses. The newly printed long π decimals also differ from the stored values: `cross` is **0.9999999999989448**, and `cross-R` **0.9999999999896982**. “Approximately 1.0 in both families” is accurate.

The permanent **L2 artifact loss is different**. The surviving sheet, key and label-file hashes verify, but I cannot reparse an unavailable raw reply or audit the prompt, launcher and execution. Recording that loss permits qualified use of the surviving label-based calculations; it does not restore provenance. That caveat belongs beside the adjudicated results in §3, rather than only in [Amendment 2](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/ceiling4/PREREGISTRATION.md:137). It does not invalidate H20a’s independently reproducible flag counts. Thus, these limitations need not permanently prevent quotation, but the present account of **two permanent gaps** is incorrect.

I reran `report_ceiling4.py`, intercepting its writes in memory. **Both output files reproduce byte for byte; all 16 results blocks match.** `numbers.json` equals its parent version, and only `KILL-A` changed in generated `tables.md`.

Independent calculations from the records reproduced:

| Outcome | Verified result |
|---|---|
| H20a | 67 versus 33 of 110; **+30.9 points**, problem-cluster 95% **[19.1, 43.1]**; discordance 38 versus 4 |
| H20b | Fitted A: **58.6% [46.8, 70.2]** versus **31.5% [21.5, 46.0]**; paired difference **+27.1 points [10.9, 39.0]** |
| H20c | 55 versus 24 of 150; **+20.7 points [12.8, 28.8]**; single-draw FP **23.6% [17.1, 30.3]**, with 0 of 8 draws meeting the bar |
| H20d | Residual **56 → 32**; 24 leave: 23 unexercised-edge and one spec-misreading |

This included independently implemented saturation fitting and **10,000 paired problem-cluster refits**, plus independent McNemar, sign-flip, Tango and grid-unconditional calculations. The reported values match. The ZIBB fits and bootstraps reproduce through the report. The new illustration is correct: **0.98⁸ = 0.850763**. Neither estimator establishes a difference in true ceilings.

The split conservative-estimator sentence is now correct. The repaired kill block and §3 appropriately distinguish the eight-reading flag union from the single-reading adjudicated rate. **The kill is arithmetic:** nine P instances returned findings, so even perfect adjudication could yield at most **9 < 20**.

All nine draws contain **260 distinct in-scope readings**. Draw 5 comprises 165 before interruption and 95 afterward. Failed attempts contributed no successful readings or additional ledger charges. The ledgers contain **2,340 auditor completions costing $19.83767825**. Amendment 1’s commit falls during draw 1, after **93 completions**; the assertion that nobody had read those results cannot be established from these records.

The sheet contains no explicit arm, severity, stratum or instance metadata. All **80 items** map correctly to the key, specifications, solutions and archived findings. I independently reproduced **57/80 agreement, κ = 0.390728**, and all sixteen rates and their intervals:

| Route / question | Consensus | L1 | L2 | Either |
|---|---:|---:|---:|---:|
| cross-T naming | 5 | 5 | 7 | 7 |
| cross-T defect-asserting | 5 | 5 | 7 | 7 |
| cross-R naming | 26 | 29 | 36 | 39 |
| cross-R defect-asserting | 26 | 29 | 32 | 35 |

Counts are over 110 P instances. Recognition κ is correctly **undefined**: on the 39 consensus naming-positive items, observed and expected agreement both equal one, giving **0/0**, not κ = 1.

I rated the first fifteen shuffled items **before reading either rater’s item labels**. Every “yes” below also receives recognition = “defect.”

| Item | Mine | L1 | L2 |
|---|---|---|---|
| K0001 | Yes | Yes | Yes |
| K0002 | No | No | No |
| K0003 | No | No | No |
| K0004 | Yes | Yes | Yes |
| K0005 | No | No | No |
| K0006 | No | Yes | No |
| K0007 | Cannot tell | Yes | No |
| K0008 | Yes | Yes | Yes |
| K0009 | No | Yes | No |
| K0010 | No | No | No |
| K0011 | Yes | Yes | Yes |
| K0012 | No | No | Yes |
| K0013 | Yes | Yes | Yes |
| K0014 | No | No | Yes |
| K0015 | Yes | Yes | Yes |

For the registered **yes/non-yes counting decision**, I marginally side with **L2**, the more inclusive rater overall: 13 agreements versus L1’s 12. Exact three-label agreement is **12 each**, so neither earns a general endorsement. L2 is right to reject K0006/K0009’s mismatch with the demonstrated failure; L1 is right to reject K0012/K0014’s overflow claim as a match for the shown rounding failure. K0007 supplies only a timeout witness, insufficient to establish the asserted overflow match. The softened attribution to both item ambiguity and rater judgment is warranted.

**Validation:** 38 focused report/statistics tests passed with `--timeout=0`; the initial three failures were 30-second timeouts. The full application suite was not run under this read-only review. No files were modified; the worktree remains clean. The study changes neither `src/` nor kernel or frozen-comparator files, and commits no corpus or finding text.

**not quotable — the repair incorrectly treats surviving, timestamped ledger evidence as an unrecoverable provenance gap.**
