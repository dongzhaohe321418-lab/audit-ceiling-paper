**All three round-2 findings are fixed at `e3baa55`.** The whole-report reread found no further substantive overclaim. No files were modified.

1. **Re-execution conclusion: fixed.** [The closing sentence](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-results/benchmarks/ai4s/RESULTS-RESULTS.md:141) now correctly distinguishes four registered flags from three supported findings. The raw readings support the report/log contradictions on `11.10.s1` and `23.2.s3`, and the numerical finding on `66.3.s1`. For `70.5.s1`, all six nonzero tensor contributions are negative; they do not cancel. The registered union remains **74 of 74**, while the union requiring sound LLM findings covers **73 of 74**, explicitly post hoc.

2. **Unit inventory: fixed.** [The revised account](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-results/benchmarks/ai4s/RESULTS-RESULTS.md:103), `UNIT_DOCUMENTED`, and its JSON output agree with the source documentation and readings. Checking all 74 selected functions’ output documentation confirms the four explicitly documented physical-unit cases. Two received correct unit findings; `77.8.s2` received no flag; `61.2.s1` received only an incorrect arithmetic finding. Execution confirms detector offsets of **49.015 and −70.362**, supporting that last distinction. The eight supported versus four unsupported clean-item classifications remain unchanged.

3. **Clustered sensitivity: fixed for both quoted comparisons.** [The added qualification](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-results/benchmarks/ai4s/RESULTS-RESULTS.md:58) accurately labels the problem-level tests as post hoc. Independent enumeration reproduces **p = 0.000003814697265625** against the profile, with 19 nonzero problem clusters, and **p = 0.6875** against re-execution.

Both analysis JSON outputs reproduce exactly with writes intercepted in memory. All 36 table intervals match at displayed precision; all 148 item hashes match the 592 successful production readings. Ledger spend totals **$7.69932325**, including the pilot.

The report now consistently separates registered BLOCKER counts from post hoc rationale adjudication, identifies reporting-fault performance as assisted by deterministic findings, and confines the interpretation to small executable examples and two synthetic fabrication types.

**quotable — the interpretation now distinguishes a registered flag from a sound detection throughout, including the conclusion.**

Reader sentence: On these small SciCode examples, the deterministic profile flagged all 49 reporting faults and none of 25 consistently fabricated outputs, while the model flagged 23 of those 25 at four readings, with sound fault-specific findings supported for 21 in post hoc review.
