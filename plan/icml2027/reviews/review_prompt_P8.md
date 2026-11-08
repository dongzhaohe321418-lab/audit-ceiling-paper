You are the same senior ICML area chair and methods reviewer. Your review review_gpt_P7.md released E1 (its held-out
audits have since run) and refused E6 for one blocker: the interface scope was not enforced consistently across
admission separation, red-teaming and witness credit. The authors responded at crossaudit-harness, branch
study/icml-e1, the current HEAD (git log -1) (code in benchmarks/code/icml). Read-only Python allowed (audit/.venv/bin/python with
PYTHONPATH=crossaudit-harness/src; executor audit/.exec/bin/python via CROSSAUDIT_BENCH_EXECUTOR). Do not review
prose. FREEZE_test.json has been rewritten at HEAD; no E6 held-out audit exists. Decide whether E6 may now run.
1. Scope consistency (PREREGISTRATION-E6.md section 3 item 5 (v)): agreement_violations with in-scope flags in
   stage_validate4 (separation counts only interface inputs), red-team requiring >= 1 interface input (units()),
   witness_flags requiring in_interface for every credit. Replay your P7 cases (open Mbpp/141, open2 Mbpp/573,
   control Mbpp/614, pancake_sort(['apple', 'Banana'])) and try to break the scope elsewhere.
2. Rescoring of earlier witness records (stage_rescope): the authors found that some earlier development witness
   records came from an older witness stage without the executable valid/in_class/oracle-difference checks; rescope
   adds those checks by execution and the interface flag, without model calls, and archives the previous files
   (*_witnesses_v4_prescope.jsonl). Check correctness, the completeness guard against unscoped witness records, and
   whether any held-out credit could still come from an unscoped or older-stage record.
3. The __main__ aliasing fix (e6.py: sys.modules["e6"]) so that analyse_e6 sees the selected kind; check
   registered_units, schedule and freeze for each kind.
4. Populations and schedule: dev 16 open / 30 controls, test 41 open (34 + 7) / 78 controls, 4,528 held-out readings;
   freeze verify passes. Any registration vs code mismatch (sections 1, 3, 10)?
5. E1 Amendment 5 (PREREGISTRATION-E1.md), written during the E1 held-out run after a provider quota incident and an
   operator error: failed calls without recorded model usage that exit (quota, HTTP 403) do not consume attempts
   (e1.reached_model, also used by e6.counts_as_attempt); the persisted E1 schedule is filtered by auditors; freeze
   binds only development rows of bridge_v4.jsonl. Is the amendment acceptable for E1's held-out run (333 GPT
   readings retried after the quota reset), and is the same rule acceptable for E6?
6. An independent pre-review (section 3 item 5 (vii)) found that hidden-suite inputs (argument lists) had been
   treated as outside the interface in v4.3 admission; conforms() now accepts argument lists and admission was rerun.
   It also led to: witness interface failures recorded as infrastructure; the credit rule's source bound into witness
   keys (all development witnesses rescored by execution); freeze verification at the held-out witness stage;
   interface-scoped predicate checks; worst-case missing-data bounds for E6-1b and E6-3; per-unit behaviour output;
   red-team inputs stored pickled. Check these, and the populations after the rerun.
7. New small study E8 (crossaudit-harness/benchmarks/e8/PREREGISTRATION-E8.md, pilot_discover.py): requirement
   discovery on the registered held-out E6 units with Claude routes only, after a development pilot. Is the
   registration adequate (estimands, hypotheses, judge), and may it run on held-out units?
8. Any other genuine blocker.
Output: (a) remaining blockers (only genuine ones; say explicitly if none); (b) disclosures; (c) verdict for E6:
release yes/no, whether E1 Amendment 5 stands, and whether E8 may run.
