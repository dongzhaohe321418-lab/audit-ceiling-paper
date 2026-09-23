You are an INDEPENDENT REVIEWER from a different vendor. FIRST review of study P4 on branch `study/fpadj` of the auditor harness at `24827b8` (the worktree you are in). Do not modify any file.

**What it is.** A preregistered study asking what an automated code auditor's flags on test-passing code point at. It re-audits 150 correct-stratum instances with the shipped cross-vendor route (K = 8), keeping the finding texts; a second model extracts the concrete inputs each finding names, blind to the reference; the candidate and the benchmark's reference solution are then executed on those inputs, and each flagged instance is classified by whether they disagree.

We deliberately do not tell you what the report concludes. Derive the result yourself first from the records, then read the report.

**Binding.** `benchmarks/code/fpadj/PREREGISTRATION.md` (registration `37ae487`, Amendment 1 `75131f6`); `benchmarks/code/fpadj/audit.py` and `adjudicate.py`; `benchmarks/code/records/fpadj/` (caches, `adjudication.json`, `extraction_audit.json`, `sensitivity_nonliteral.json`); `benchmarks/code/RESULTS-FPADJ.md`; the archive at `~/Documents/Crossaudit/study-data/wt-fpadj-runs/` (`blocker_texts.jsonl`, `extractions.jsonl`, `executions.jsonl`, `run.log`); ceiling 1's cache at `benchmarks/code/records/ceiling/cache/` for the identity check.

**Verify, at least:**
1. That the readings are ceiling 1's code path on ceiling 1's candidates, complete (1,200), and that the captured texts correspond to the cached rows.
2. The extraction: blindness to the reference as registered, the leak check, faithfulness of extracted inputs to the finding texts (check more than the author's twenty), and whether the parse and literal rules dropped anything that matters.
3. The execution and comparison: correctness of the harness, the invalid-input rule, the equality rule, and every D, A and N classification. Recompute the primary share, its problem-cluster interval at the registered seed, and the secondary union false-positive rate.
4. Whether the report's reading follows the registration's fixed reading, and whether any sentence claims more — or less — than the records support, including the post-hoc sensitivity and the closing description.
5. Process: whether the amendment, the halts and the rerun were handled as registered.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.
