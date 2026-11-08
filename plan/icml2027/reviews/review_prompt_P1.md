You are a senior ICML area chair and a hostile but fair methods reviewer. The authors want an ICML 2027 main-track
paper titled "What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data".
Read audit-ceiling-paper/plan/icml2027/CEILING_PROGRAM.md (the reorganised research programme), the current draft
audit-ceiling-paper/tex/paper.tex, and as needed crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E1.md,
crossaudit-harness/benchmarks/code/icml/e1.py and crossaudit-harness/benchmarks/code/records/icml/taxonomy_v3.jsonl
(the taxonomy reasons). You may run read-only Python. Do not review prose.

Answer, concretely:
1. Is the definition of the ceiling (reach = share of items with p>0, at a fixed clean-flag budget; Chao2 lower
   bound; plateau test) sound and identifiable? What would a referee attack, and what is the better estimator?
2. Is the thesis "reach is bounded by information; capacity levers move rate, information levers move reach"
   a strong, non-trivial, falsifiable ICML idea? Is it circular given that the taxonomy itself is a model
   judgement of whether the text determines the answer? How should the taxonomy be validated (human sample,
   execution-based definition, inter-rater agreement) to break the circularity?
3. E5 design: populations, configurations, margins (5 and 10 points), equivalence-style hypotheses with ~98
   OPEN/AT_ODDS items, multiple comparisons, the execution route, cost. What must change? What is missing
   (e.g. a configuration that adds partial information, a dose-response, other benchmarks)?
4. AT_ODDS items (task text contradicts the hidden suite) are 47/150. How should they enter the reach
   estimand and the paper's claims (benchmark label noise vs audit failure)?
5. Does the evidence map across general code, results, data and scientific code hold together as one paper,
   or should anything be cut or moved to the appendix for an 8-page ICML version?
6. The single most important change that would raise the chance of acceptance.

Output: (a) must-fix before preregistering E5; (b) recommended changes; (c) a one-paragraph verdict on whether this
programme can carry an ICML main-track paper.
