# The ceiling programme (ICML 2027), version 3

2026-11-07. v1 (asymptotic reach) and v2 (minimal pairs from failures) were reviewed by GPT (`review_gpt_P1.md`,
`review_gpt_P2.md`; P2 verdict: borderline, lean accept if executed with the corrections below). E1's development
pipeline was reviewed in `review_gpt_A4.md` (test stays closed until B1-B7 are resolved).

**One-sentence contribution (P2).** A human-validated, contract-randomised audit benchmark separates
benchmark-convention agreement from reliable defect diagnosis, and measures how clarification and computation
change verified detection at a fixed false-flag budget.

## 1. Framing (what is theory, construction, observation, transport)

- *Classical limit.* For any flagging policy phi(E) on the complete observation E (program, task, visible tests,
  added text, anything computable from them), TPR - FPR <= TV(P1, P0); the constrained envelope is the
  Neyman-Pearson power beta_E(alpha). Presented as a textbook testing bound specialised to auditing, with proof and
  assumptions; not claimed as new. The component bound TPR <= 1 - pi + pi*alpha needs the component FPR constraint;
  under an overall constraint only 1 - pi + pi*min(1, alpha/q).
- *Construction guarantee.* Under contract randomisation with symmetric presentation, unrevealed flag J = 0 exactly.
  This is a baseline built by design, not a finding.
- *Observation.* What auditors do once the contract is revealed, how close verified diagnosis comes to the
  flag constraint, what computation adds, and how strongly auditors side with the benchmark's convention.
- *Transport.* Natural-failure analyses (E1, taxonomy, human ambiguity prevalence) are descriptive: logical
  ambiguity is not distributional indistinguishability, an OPEN miss is not automatically an information miss, and
  nothing here says computation cannot help on natural programs.

## 2. Outcomes

1. *Flag discrimination* of one deployable policy: TPR, FPR, J.
2. *Actionable audit performance*: verified-diagnosis coverage of the same deployable policy's findings, under a
   cumulative clean-flag constraint alpha (numerical alpha, primary k and the aggregation threshold set on
   development units, frozen; held-out compliance = upper bound below alpha; >= 59 independent clean cases).
   Verified diagnosis scores the policy's own findings; no aggregation uses hidden verification.
3. Secondary: contract-conditioned (conditional) findings, clarification requests, cost (tokens, time).

## 3. E6 construction (contracts first)

1. *Proposal.* For every HumanEval+/MBPP+ problem (542; frozen problem-level split 136 dev / 406 test), a proposer
   names one input class the task text and visible tests leave open and states RULE_B (the reference's behaviour)
   and RULE_A (an equally compatible alternative), equally specific, plus 4-8 class inputs and 3-5 other inputs, or
   skips.
2. *Independent implementations.* Each rule is implemented from the task plus the rule alone by two vendors with
   the same prompt (no reference shown). Audited programs: one A and one B implementation from the same vendor,
   vendor counterbalanced across units, so the pair shares provenance and style (no untouched reference beside an
   edited copy).
3. *Admission (execution).* All four implementations pass the visible tests; both B implementations pass the full
   hidden suite; the two A implementations agree on every validation input; A and B differ on >= 2 class inputs and
   agree on every other input; class and other inputs are valid for the reference.
4. *Validation without human raters (the author declined to rate; no second rater).* (i) A blind two-vendor judge
   panel (Claude Opus, GPT-6.1-sol; neither proposes rules nor audits) rates RULE_A and RULE_B separately as
   compatible / incompatible / unresolved, order randomised, provenance hidden; the primary population is the
   execution-admitted units both judges rate compatible on both rules. (ii) Behavioural evidence: the twelve task-only
   E1 generations per problem that pass the visible tests are run on the class inputs and classified as following A,
   B or neither. On the 55 dev units 94.5% of classified solutions follow B: the rules are logically open but
   conventionally dominated, so behaviour measures convention strength (or memorisation), not admissibility. It is
   reported per unit, and units where both rules are followed by at least one solution form a registered
   sensitivity subset. The lack of human validation is a stated limitation.
5. *Positive controls (distinguishable).* Units whose alternative rule is incompatible with the task (human-judged),
   evaluated under the uniquely valid contract with the B implementation as correct control: unrevealed J > 0
   expected.

**Arms.** `none`; `menu` (both rules, order randomised independently of the contract, identical bytes under both
contracts, no labels such as standard or alternative); `resolve-A`, `resolve-B` (the same menu plus one selection
sentence of equal specificity; no witness, patch or guidance). All four resolved program-contract cells are kept.

**Configurations.** Two vendors x two reasoning budgets of the same model; execution route (OS-isolated shell) on a
prespecified subset. Two readings per cell.

**Size.** Target >= 200 admitted held-out problems (P2 planning: 197 problems for 80% power at 10 points if the
problem-level SD is 0.5); outcome-blind enlargement rule fixed after the dev power simulation. Grid: 2 programs x 4
arms x 4 configurations x 2 readings = 64 readings per unit, about 12,800 for 200 units.

**Registered contrasts (hierarchical).**
- E6-1: actionable coverage at alpha, resolve minus menu, with an absolute criterion on resolve set on dev.
- E6-2 *benchmark-convention advantage*: in `none`, (r_B - r_A)/2, with symmetric provenance; plus flag preference.
- E6-3: reasoning-budget effect after resolution (the menu-arm term is zero by construction; not an interaction).
- Power simulated on dev covariance (pairing, readings, configurations, clusters, missingness, aggregation);
  joint power if both E6-1 and E6-2 are required.

## 4. Bridge to natural programs (E1)

Classify E1's successful witnesses by the discrepancy they diagnose; rescore convention-dependent witnesses against
validated alternative contracts; report programme-level successes supported only by convention-dependent witnesses
separately from those with an independently valid witness. Framed as benchmark-conformance recall versus
contract-robust diagnosis.

## 5. E1 (registered; Amendment 4 before test)

Fix A4 B1-B7: semantic reconciliation of the 38 admitted items (human-rated: both behaviours permissible), neutral
placebos and pointers rechecked, H5 framed as benefit beyond the specified pointer, H6 as a programme-level
observational association with first-failure labels, judge-v3.2 (done), completeness from the required key
universe (done), full H6 matrix (done), boundary-sensitive intervals for H2/H4 as a sensitivity rule, checksummed
pre-test bundle.

## 6. Transfer

Only if it tests the same mechanism: E6 on a prespecified deterministic NumPy/SciPy subset of DS-1000 (~50
problems), modest claims. No claim that scientific code has larger ambiguity prevalence. Position against
SciCode-Verified (specification repair) as randomised-contract auditing.

## 7. Roles

E6: core. Bridge and E1: natural evidence. E3: data study at its registered operating point (appendix or short
section). Earlier studies: appendix.
