You are the same hostile but fair methods reviewer. Your previous review (records/icml/v2/review_gpt_A3.md)
found seven blockers in E1's development pipeline. They have been addressed in Amendments 2 and 3 of
benchmarks/code/icml/PREREGISTRATION-E1.md (protocol e1-v3; code in benchmarks/code/icml/e1.py and
analyse_e1.py). The development split has been rerun end to end under e1-v3. No test-split audit has been
made. Your job: decide whether the test split may now be run, and if not, what exactly must change first.
You may read any file and run read-only Python (the executor interpreter is ../../../.exec/bin/python
relative to benchmarks/code if you need numpy; set CROSSAUDIT_BENCH_EXECUTOR to it).

Records (benchmarks/code/records/icml/): items_v3.json, oracles_v3.json, executions_v3.jsonl,
constructions_v3.jsonl, adjudications_v3.jsonl, taxonomy_v3.jsonl, schedule_v3_dev.json,
schedule_v3_orig_dev.json, audits_v3.jsonl, audits_raw_v3.jsonl, witnesses_v3.jsonl, e1_results_dev.json,
e1_taxonomy_dev.json. The archived e1-v2 records are in records/icml/v2/.

Check:
1. For each of your seven A3 blockers: is it fixed as described in Amendment 2? Cite code lines.
2. The candidate-blind constructor and dual adjudication: read every admitted clause, pointer and placebo
   (38 items, both splits; you may read test-split construction materials, which are frozen inputs, but no
   test audits exist). Flag any clause that still contradicts the task, codifies a quirk or is determined by
   the task's words; any pointer that implies the correct output; any placebo that is related. Give item ids.
3. The pointer arm as a control: does the pointer-versus-clause contrast (H5) identify "behavioural
   information beyond attention to the input class"? What would a referee object to?
4. The taxonomy (Amendment 3): are the class definitions and the blinding sound? Read at least 20
   classifications with their reasons and the task; report errors. Is H6 well defined?
5. The judge (judge_call / JUDGE runner): try to break it (mutable arguments, numpy outputs, None, nested
   tuples, generators, very large outputs, exceptions inside the suite's assertion helper).
6. Analysis: missing-data rule, completeness refusal, witness cache keys, quantiles, H5/H6 code.
7. Sample size: H1-H5 rest on 29 test items (problem-clustered). Is that defensible for the paper's claims,
   and should anything be added BEFORE test audits (it cannot be added after)?

Output: (a) BLOCKERS before test audits, with file:line or item id and a concrete fix; (b) disclosures;
(c) a short verdict: run the test split now, yes or no.
