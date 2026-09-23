You are an INDEPENDENT REVIEWER from a different vendor. Review `study/substrate2` at 338b62b (the worktree you are in). Do not modify any file.

**Read `benchmarks/code/substrate2/PREREGISTRATION.md` Amendments 1-4 FIRST.** This study was voided and re-run, and the re-run is the interesting object. Your job is not only to check the new numbers; it is to judge whether the correction and the way it is reported are honest.

**What happened.** Study 23 measures the shipped cross-vendor auditor on a second substrate (BigCodeBench stdlib half) against ceiling 1's frozen 30.0% on substrate 1. The first run was VOIDED: `Task.visible_tests_text()` sliced the selected test methods out of their enclosing class without the class header, so the text shown to the auditor AND to the generator began at an indented `def` and **failed `ast.parse` on 300 of 300 tasks**, while scoring executed the intact class. The extraction is fixed, a digest gate (`verify_frame.py`) now refuses to spend if the visible text does not reproduce a frozen hash, and the study was re-run in full.

**The re-run reversed six of the voided run's conclusions**, every one in the direction of the voided run having overstated:

| | voided | re-run |
|---|---|---|
| cross-vendor FP intervals across substrates | disjoint by 2.6 pts | **overlap by 3.5** |
| same-vendor draw splits | 0 of 250 | **12 of 249** |
| cross registered gain ratio | 1.16 -> 0.91 | **1.35 -> 1.23** |
| flattening bar on P | 0.62 pts, MET | **1.52 pts, NOT met** |
| H23d (self - cross, P) | +17.0 [2.0, 32.0] | **+4.0 [-10.1, 18.2]**, spans zero |
| self registered gain ratio | UNDEFINED (denominator exactly 0) | **computable, 0.32 -> 0.25** |

Claimed now: H23a union recall at K=8 is **76 of 99 = 76.8% [65.7, 87.0]** against ceiling 1's frozen 33 of 110; H23c false positives **68 of 150 = 45.3% [36.4, 54.4]**; scope 249 instances (99 P, 150 C) re-frozen from the new generation. Spend $37.16 of a $45 registered halt, including $22.25 a first re-run attempt wasted on a stale scope.

**Verify, at least:**

1. **Re-run `report_substrate2.py --run <archive>` and `substrate2/splice_tables.py`; confirm `numbers.json` and `tables.md` reproduce and the splice matches.** Recompute H23a, H23c, H23d and both curves independently from the caches. The run archive is `~/Documents/Crossaudit/study-data/wt-sub2-rerun`.
2. **Attack the correction itself.** Is the new `visible_tests_text()` actually what a developer sees? It now emits the module prologue, the class header, the class's non-test members and the selected test methods. Does it leak any hidden test? Does the digest gate actually bind what it claims?
3. **Judge whether six reversals from one input defect is coherent.** Could some of these reversals have another cause -- the re-frozen scope (249 vs 250 ids, 99 P vs 100), the regenerated candidates, the 23 hours of HTTP 429 that split the cross arms across time? The report claims a denied call lands no reading and costs nothing; check that.
4. **The comparison discipline.** Amendment 2 fixed, before the re-run, that the two runs are reported side by side as descriptive and post hoc, with no interval or p value on any difference, not as an estimate of what unparseable tests do to an auditor, and never used to validate the voided run. Check every place the two runs are compared and say whether that rule is kept.
5. **Stale-artefact reuse.** Three artefacts were found being reused across generations because they live in committed `records/`: the readings cache, `audit_set.json`, and `cost.json` (which made an earlier regeneration report the VOIDED run's spend). Amendment 3 added a `generation_sha256` guard. **Is that guard sufficient, and are there others of the same class you can find?**
6. **Eight assertions that pinned the old findings.** Tests and the report generator both hardcoded outcomes -- `flattened_by_ceiling1_bar is True`, split count `== 0`, `intervals_overlap is False`, `P_excludes_zero is True`, `registered_gain_ratio_is_undefined is True` (in both places), "a curve that never rises", and a superseded test that wrapped unparseable text in `class T:` so it would parse. All now branch on the data. **Check that none of the rewrites weakened a test into vacuity**, and look for any remaining assertion that encodes a result rather than checking one.
7. `src/` and kernel dirs untouched; no corpus text, solution text or finding text committed (the row writer now redacts tracebacks to their last line plus a sha256).

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Note: three tests in `test_ceiling_stats.py` fail on a 30-second pytest timeout (study 8's Monte-Carlo coverage simulations); they are not assertion failures and are unrelated to this branch.

End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.
