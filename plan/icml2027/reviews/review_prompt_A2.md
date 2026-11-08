Review, adversarially and read-only, the design and code of a new preregistered experiment for the paper in
audit/audit-ceiling-paper (you reviewed the paper in round A1; your review is audit/review_gpt_A1.md):
audit/crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E1.md and icml/e1.py (it reuses the harness's
corpus.py, execute.py, generate.py, audit.py and ceiling.py). The author follows their own direction for the
paper (what moves the ceiling on automated audit, general code to science); E1 is the causal specification
test you ranked first, adapted to the available CLIs.

Find anything that would make H1-H4 invalid or uninterpretable, or that an ICML reviewer would attack:
leakage of the hidden suite or failing input into the clause or the audit prompt; the clause validation
(could a check be trivially separating, or test something other than the requirement it states?); placebo
design; whether "verified diagnosis" can be gamed (e.g. witnesses on invalid inputs, inputs outside the
specification's domain, exceptions); selection effects from admission; arm order and caching; the dev/test
split; statistics (paired unions, clustering, the H3 contrast); CLI confounds; and plain bugs in e1.py. Give
concrete fixes, ranked by importance. Be concise.
