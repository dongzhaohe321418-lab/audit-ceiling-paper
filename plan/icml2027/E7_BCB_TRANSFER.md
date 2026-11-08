# E7: randomised-contract transfer to library-heavy data-science code (BigCodeBench) — feasibility, 2026-11-08

**Why (meaningfulness check).** The largest open risk for the main track is scope: E6 uses HumanEval+/MBPP+ short
functions only. A replication of the same design on data-science code (pandas/numpy/scipy/sklearn) tests whether
the information limit and the effect of stating the contract carry over, and is the paper's direct evidence for
"from general code to scientific code". Further polishing of E6's protocol would not change a conclusion.

**Corpus.** BigCodeBench (1,140 tasks; local copy from the earlier substrate2 study,
`iCloud/Documents/Crossaudit/crossaudit_ceiling/benchmarks/code/data/bigcodebench.jsonl`). Deterministic tasks with
comparable outputs (libraries within numpy/pandas/scipy/sklearn/stdlib, no plotting, randomness, files, network or
mocks in tests or reference): **172**, of which 126 use numpy/pandas/scipy/sklearn/statistics.

**Expected size.** E6's open yield is 41 / 542 (7.6%); expected 13-20 registered units. Enough to test E6-1 (dev
effect +87.5 points) and E6-5; E6-2 (about 14 points) would be underpowered and is reported descriptively.

**Engineering (no GPT needed; code outside benchmarks/code so the E1/E6 freeze is untouched).**
1. Adapter: task text = BigCodeBench instruct prompt; visible tests = first test method(s) (reuse substrate2's
   AST-faithful extraction); hidden suite = remaining test methods, executed as the benchmark's own unittest
   class against the shown program.
2. Inputs for admission: there are no input lists, so the interface comes from the proposer's class and other inputs
   plus probe inputs; stress and red-team inputs as in E6, inside that interface.
3. Comparator: DataFrame/Series equality with check_dtype and a float tolerance, numpy allclose, exact otherwise;
   validated by running the reference against itself and against a perturbed copy.

**Cost.** Construction about 172 x 9 calls (half GPT); audits about 18 x 80 readings (half GPT): about 1,500 GPT
calls. Run only after E6's held-out audits have finished (GPT quota is the binding constraint).

**Go / no-go.** Go if, after admission and red team, at least 12 units pass the judges; otherwise report the funnel
as a finding (data-science tasks rarely leave a behaviour open in a way two vendors implement consistently) and
stop. Preregister before any audit; review by GPT before the held-out run, as for E6.
