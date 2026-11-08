You are the same senior ICML area chair and methods reviewer. Your review review_gpt_P4.md refused test release for
E6 and E1. The authors responded with protocol e6-v4.1 and a wired E1 Amendment 4 (commit 677c78b in
crossaudit-harness). Decide whether both may now be frozen and run on test. Read-only Python allowed
(crossaudit-harness/.venv/bin/python; executor crossaudit-harness/.exec/bin/python via CROSSAUDIT_BENCH_EXECUTOR).
Do not review prose. Test construction for E6 is being rerun under v4.1 (records with split "test" may be partial);
no test audit exists for E6 or E1.

For each P4 blocker state fixed / not fixed with file:line:
1. Executable validity: stress_inputs in e6.py and admission v4.1; rerun your P4 counterexamples (HumanEval/125
   "a\v,b" and "è", HumanEval/20 [-1e308, 1e308], positive-control Mbpp/557, Mbpp/130 and Mbpp/8 domain) against
   records/icml/e6_units4.jsonl and e6det_units4.jsonl (dev); try new failures on 10 admitted open units and 5
   controls. Is the "narrower experimental domain" treatment of `valid` (section 6 of PREREGISTRATION-E6.md, with
   the reference-domain sensitivity) acceptable?
2. Provenance and missing data: completeness (prompt-hash rebuild, conflicting scores, pre-model infra attempts,
   superseded readings), witness_key (comparator bound), analyse_e6 missing bounds, judge prompt-hash check, e1.call
   refresh retry. Try to break them again.
3. Inference: betting_upper / betting_interval in analyse_e6.py (check validity of the implementation against
   Waudby-Smith & Ramdas, predictability of bets, ordering), the alpha_FPR = 10% budget, E6-3 margin +/-10 by
   betting interval placed last. Is anything still miscalibrated?
4. E1 Amendment 4: admitted_constructions (retention), completeness with superseded readings, analyse_e1 H6 on
   taxonomy v4, boundary sensitivity, bridge fixes. May the E1 test run now?
5. Remaining registration/implementation mismatches (PREREGISTRATION-E6.md v4.1 vs code), and the exact freeze
   bundle contents still missing.
Output: (a) remaining blockers (only genuine ones; say explicitly if none); (b) disclosures; (c) verdict for E6 and
E1: release yes/no.
