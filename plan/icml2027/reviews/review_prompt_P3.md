You are the same senior ICML area chair and methods reviewer (your reviews: review_gpt_P1.md, review_gpt_P2.md,
crossaudit-harness/.../review_gpt_A4.md is ../review_gpt_A4.md). The authors implemented programme v3
(audit-ceiling-paper/plan/icml2027/CEILING_PROGRAM.md) and ran the E6 development pilot. Decide whether E6 may be
frozen and run on test. Read-only Python allowed (executor: crossaudit-harness/.exec... see e1.py EXEC; venv
.venv/bin/python). Do not review prose.

Read:
- crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E6.md (draft), e6.py, analyse_e6.py, e1.py (judge_witness
  with oracle, routes), isolate.py is not used by E6.
- Records in crossaudit-harness/benchmarks/code/records/icml/: e6_proposals.jsonl, e6_impls.jsonl, e6_units.jsonl,
  e6_judgements.jsonl, e6_behaviour.jsonl, e6_audits.jsonl (3,520 dev readings), e6_witnesses.jsonl,
  e6_results_dev.json; positive controls e6det_*.jsonl and e6det_results_dev.json. Test construction may be in
  progress (e6_* rows with split "test"); no test audit exists.
- Important change since P2: the author declined to rate and no second rater exists, so human validation was
  replaced by a blind two-vendor judge panel and behavioural evidence (94.5% of task-only solutions follow RULE_B).
  E1 amendment 4 was revised accordingly (PREREGISTRATION-E1.md).

Dev headline (50 open units in the registered population): none flags 13.4% on defective = correct; menu 1.6%;
resolve TPR 100%, FPR 0.9%, verified coverage 95%; convention advantage +10.5 [6.0, 15.5]; high-minus-low reasoning
after resolution +0.9 [-0.9, 2.7]. Positive controls (53 units, none arm): TPR 94.8%, FPR 1.4%, J 93.4 [87.3, 98.1],
verified 90.1%.

Check, concretely:
1. Read at least 15 open units (rules, class, both shown implementations, arm texts) and 10 positive controls. Are
   the open rules genuinely both admissible; are the positive-control misreadings genuinely ruled out by the words?
   Does any arm text leak the contract or bias toward one rule (menu wording "the task author has fixed which" and
   "The task does not say which")? Is the menu's near-zero flag rate an artefact of the wording telling auditors not
   to flag?
2. Scoring: oracle = other vendor's implementation; domain check via reference; verified diagnosis only among
   flagging readings; unrevealed scoring under both contracts; the population filter; missing-data handling.
   Try to find a bug in analyse_e6.py (cells, contract mapping, averaging, bootstrap).
3. Is the resolved 95% / positive-control 95% result trivially "auditors can read a requirement", and what is the
   paper's real empirical contribution now? What single additional arm or analysis, cheap enough to add before test,
   would most raise the contribution (e.g. a partially informative arm, natural-language reveal phrased as an
   ordinary task sentence instead of a menu selection, the execution route, the E1 bridge)?
4. Is the replacement of human validation acceptable for an ICML main-track paper, and how should it be framed?
5. Preregistration completeness: hypotheses, order, thresholds, alpha, policy, missing data, populations, what must
   be frozen in the bundle. List exact edits.
Output: (a) blockers before test; (b) recommended additions (ranked by contribution per cost); (c) verdict.
