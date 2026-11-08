You are a hostile but fair methods reviewer for an ICML submission. You reviewed the E1 design before (your
fixes were implemented). Now the development split of E1 has been run end to end. Your job: find anything in
the pipeline, records or registered analysis that would make the TEST results wrong, biased or unreportable,
BEFORE the test audits are run. Do not review prose. You may read any file; you may run read-only Python.

Repository root (current directory): crossaudit-harness, branch study/icml-e1.

Read:
- benchmarks/code/icml/PREREGISTRATION-E1.md (including Amendment 1)
- benchmarks/code/icml/e1.py (all stages) and benchmarks/code/icml/analyse_e1.py (registered analysis)
- records in benchmarks/code/records/icml/: items.json, split.json, constructions.jsonl, adjudications.jsonl,
  audits.jsonl, audits_raw.jsonl, witnesses.jsonl, schedule_dev.json, e1_results_dev.json, select.log

Check specifically:
1. Item admission: are any admitted items malformed (defective solution actually passes hidden tests, control
   actually fails, clause cases that do not separate defective from reference, placebo that changes
   behaviour)? Spot-check at least 8 dev items by reading the clause, placebo, cases and both solutions.
2. Leakage: does the clause or placebo give away the failing input or the defect beyond stating the missing
   requirement? Does anything in the audit prompt identify the arm, the kind (defective/correct) or the item?
3. Audit records: reply validity rates by auditor and arm; whether invalid/failed readings are missing at
   random across arms (differential missingness would bias H1-H4); tool use; retries.
4. Witness verification: read several witnesses and judge_witness results. Is "verified diagnosis" being
   credited when it should not be (e.g. expected value equals reference by accident, outside-domain inputs,
   float tolerance, mutable arguments, exceptions)? Is it denied when it should be credited (parse failures on
   reasonable witnesses)? Report the unparseable rate.
5. Registered analysis: does analyse_e1.py compute exactly what the preregistration says (unions, O2 subset
   averaging, auditor averaging, problem-cluster bootstrap, verdict thresholds, the Amendment-1 sensitivity)?
   Any item silently dropped? Any off-by-one in the bootstrap quantiles?
6. Anything else that would make a referee distrust the test result.

Output, in this order: (a) BLOCKERS that must be fixed before test audits, each with file:line or record id
and a concrete fix; (b) things to disclose; (c) a one-paragraph judgement of whether the dev results look
like a working instrument. Do not suggest changing hypotheses or thresholds after seeing dev outcomes unless
the change is required to fix a bug; say explicitly if a fix would touch registered quantities.

Dev headline (from e1_results_dev.json; dev only, 36 items): defective verified diagnosis orig2 11.1, orig4
12.5, placebo2 15.3, clause2 100.0 (both auditors, every item); correct-program flags orig4 33.3, placebo2
33.3, clause2 12.5. The clause arm sits at the ceiling. Judge in particular whether the clauses are
legitimate "missing requirements" or are hints that point at the defect (e.g. naming the edge case the
candidate mishandles in a way a specification author would not), and if so what a referee-proof
construction or additional control would be before the test split is run. Read at least 12 clauses with
the specification and the defective solution side by side.
