You are the same senior ICML area chair and methods reviewer. Your previous review review_gpt_P3.md refused test release
for E6. The authors addressed it in protocol e6-v4. Decide whether E6 (and E1 under its Amendment 4) may now be frozen
and run on test. Read-only Python allowed (crossaudit-harness/.venv/bin/python; executor
crossaudit-harness/.exec/bin/python, set CROSSAUDIT_BENCH_EXECUTOR). Do not review prose.

Read: crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E6.md (v4 draft), e6.py (stage_probe,
stage_classpred, stage_validate4, judge v2, arm_text with sentence arms, units() oracles, witness_key, stage_witness,
completeness), analyse_e6.py (population, unit_value, fpr_compliant, verdicts), e1.py (judge-v3.2, sync_auth,
stage_bridge, taxonomy2, stage_controls), PREREGISTRATION-E1.md (Amendment 4 incl. items 3 and 8).
Records (crossaudit-harness/benchmarks/code/records/icml/): e6_probes.jsonl, e6_units4.jsonl,
e6_judgements2.jsonl, e6_behaviour4.jsonl, e6_audits_v4.jsonl, e6_witnesses_v4.jsonl, e6_results_v4_dev.json,
e6det_* equivalents and e6det_results_v4_dev.json, e6_units4_opuspred.jsonl (first v4 admission with an independent
class predicate, which rejected 45/55 because the predicate was too narrow; replaced by the proposer's predicate),
taxonomy_v4.jsonl, controls_v4.jsonl, bridge_v4.jsonl. Test construction may be in progress; no test audit exists.

Check:
1. Each P3 blocker: fixed or not, with file:line. In particular re-run your Mbpp/798 and Mbpp/557 probes and the
   Mbpp/762 domain case against the v4 pipeline; try to find new oracle or predicate failures on 10 admitted open
   units and 5 positive controls (run the shown programs, oracles and predicates on inputs you choose).
2. Is the proposer-written class predicate acceptable (independence vs fit), given `valid` and probes are independent?
3. The boundary FPR rule (section 7) was chosen after seeing dev data: acceptable as disclosed, or must it change?
4. Analysis: try to break completeness, missing-data, duplicate handling, witness keys; check that verified credit
   requires valid + in_class + oracle disagreement among blocking readings.
5. E1 Amendment 4 (taxonomy v4 retention: 13 of 38 admitted items remain, 9 test items over 7 problems; witness
   bridge; control rechecks): may E1 test run? What claims can 9 items support?
6. With the dev v4 results (27 open units: E6-1 +91.7, E6-2 +12.5, E6-3 0.0 [-3.7,3.7], sentence = resolve,
   routing GPT pass vs Claude escalate in menu; positive controls J 90.6) and the bridge pilot (natural verified
   diagnoses mostly on DETERMINED witnesses: 5 of 6 dev items), what is the strongest honest framing of the paper,
   and what is your current main-track assessment?
Output: (a) blockers before test; (b) disclosures; (c) verdict for E6 and for E1.
