# The ceiling programme (ICML 2027), version 2

2026-11-07. Version 1 (asymptotic reach, E5 capacity grid) was reviewed by GPT (`review_gpt_P1.md`) and
withdrawn: reach is not identified at finite k, the clean-flag budget was not imposed, the taxonomy is a model
judgement on the first failing input only, AT_ODDS was mixed with underspecification, and the "capacity does
not help" hypotheses were underpowered non-equivalence claims. Version 2 replaces E5 with a controlled
information-release experiment (E6) whose ceiling is a theorem, not an extrapolation.

## 1. The ceiling is a property of the evidence

An audit case is a program X, the evidence E the auditor sees (task text, visible tests, any added text,
tool outputs that are functions of these), and a hidden contract H that defines the ground truth. D = 1 if X
violates H. An auditor, of any capacity, is a randomised map from E to a finding.

**Proposition 1 (evidence ceiling).** For every auditor, TPR - FPR <= TV(P_{E|D=1}, P_{E|D=0}); at a false-flag
rate alpha the attainable TPR is at most the Neyman-Pearson ROC of E at alpha.

**Corollary (indistinguishable component).** On any component of cases where E has the same distribution for
defective and correct programs, every auditor's TPR equals its FPR. If a share pi of the defects lies in such a
component, recall at component false-flag rate alpha is at most (1 - pi) + pi * alpha.

Consequences, which organise the paper: (i) capacity (sampling, model, reasoning, execution of supplied code) can
at most approach the ROC of the evidence; (ii) only changing E (information) moves that ROC; (iii) on a natural
benchmark, where the hidden contract is fixed to the benchmark's convention, flags on indistinguishable cases can
look like detection while being convention-guessing that would be false flags under the other convention. The
empirical questions are therefore how large pi is in natural populations, how much measured audit recall lies on
it, how far real auditors sit below the ceiling once information is released, and whether capacity matters more
after release.

## 2. Estimands (finite budget, common constraint)

- **Coverage at budget k**: exact subset-averaged union U(k) = mean_i [1 - C(m - s_i, k) / C(m, k)] over m readings,
  for verified diagnosis on defective programs and for flags on correct programs (F(k), which accumulates too).
- **Constrained comparison**: configurations are compared at a common cumulative clean-flag budget alpha, set on
  development controls (aggregation threshold: number of the k readings that must flag), frozen, and checked on
  held-out controls with uncertainty; a configuration exceeding alpha fails the constrained comparison.
- **Youden J = TPR - FPR** at fixed k as a budget-free summary; by Proposition 1, J <= TV.
- No asymptotic reach is estimated. Chao2 appears only as a sensitivity analysis, labelled a lower bound.

## 3. E6: contract-randomised information release (new, primary)

**Unit.** A discrepancy unit: a task, an input class, and two behaviours on it, A (the defective generation's) and
B (the benchmark reference's), both compatible with the task text and the visible tests.

**Construction (candidate-blind where possible, verified by execution).**
1. Source: E1's 150 hidden-test failures (HumanEval+/MBPP+), plus new failures from additional generators to
   enlarge the pool; development problems for piloting only.
2. Minimal pair: a model rewrites the reference into C_A that adopts A on the input class. Admitted only if C_A
   passes the visible tests, differs from the reference on at least one hidden input, and on every differing
   hidden input returns the defective program's output (same discrepancy, no new defect).
3. Contracts: suite_B = the original hidden suite; suite_A = the same inputs with C_A's outputs.
4. Validation of compatibility (breaking the circularity): two independent human programmers, blind to which
   behaviour is the benchmark's (order randomised) and to all auditor outcomes, judge for each unit whether A and
   B are each compatible with the task text and visible tests; third-person adjudication. Model raters (three
   vendors) run in parallel and are compared with the humans, not substituted for them. Classes: COMPATIBLE-BOTH
   (the indistinguishable component), DETERMINED (only B compatible: positive controls), AT_ODDS (only A
   compatible: benchmark error), UNCLEAR-DOMAIN, each with its written evidence. Report pre-adjudication
   agreement, confusion matrix and class-specific agreement.

**Arms** (texts appended to the task; constructed blind to auditor outcomes; length-matched where applicable):
- `none`; `pointer` (names the input class); `menu` (states that the hidden contract fixes the behaviour on this
  class and lists both behaviours, order randomised; maximal attention and both options, no resolution);
- `resolve-A`, `resolve-B` (a requirement stating one behaviour); E1's checks for leaks and for consistency with
  the task.

**Programs.** Each unit is audited with C_A and with the reference R (both suite-passing under one contract).

**Configurations (capacity).** Two vendors x two reasoning budgets within the same model (low, high); an execution
route (OS-isolated shell, same visible evidence, no hidden tests) as a prespecified secondary factor. Four
readings per unit x program x arm x configuration.

**Scoring.** Under contract H, a program is defective iff it differs from H's implementation; verified diagnosis
requires a witness on which the program and H's implementation differ, with the expected value equal to H's
output (judge-v3.1). In `none`, `pointer` and `menu` the evidence does not depend on H, so the same readings are
scored under both contracts (symmetric scoring); `resolve-H` reveals H.

**Registered contrasts (test units; problem-cluster bootstrap; hierarchical order).**
- E6-1 (information moves the ceiling): symmetric J, `resolve` minus `menu`, on COMPATIBLE-BOTH units, pooled over
  configurations. Supported if the lower bound exceeds 0.
- E6-2 (convention-guessing inflates natural recall): on COMPATIBLE-BOTH units in `none`, natural recall (contract
  fixed to B: verified diagnosis on C_A) minus symmetric recall. Supported if the lower bound exceeds 0. Reported
  with the auditors' preference for B (flag C_A minus flag R).
- E6-3 (information changes the return to computation): (high - low reasoning) in `resolve` minus the same in
  `menu`, symmetric J. Two-sided; either sign is a result.
- Descriptive: constrained coverage at the frozen alpha by arm and configuration; gained and lost units, not only
  net change; DETERMINED units as positive controls (J > 0 expected in `none`); AT_ODDS units analysed as
  benchmark-error cases (does the auditor identify the specification-reference conflict).
- Power: simulated before registration from the real cluster sizes, observed discordance in the pilot and
  reading dependence; sample size set so that E6-1 and E6-2 have at least 80% power at effects of 10 points.

## 4. Natural population: how much of the miss mass is information-limited

On the 150 E1 failures (and new generations), the human-validated classes give pi for HumanEval+/MBPP+ failures
and hence the ceiling for that population: recall at budget alpha <= (1 - pi) + pi * alpha. Observed auditors
(E1 original-text readings) are placed against it: the gap on DETERMINED units is a capacity gap; misses on
COMPATIBLE-BOTH units are information-limited by Proposition 1.

## 5. Transfer to scientific code

The same E6 construction on scientific functions with hidden numerical tests, where the classic underspecified
points are conventions (units, normalisation, sign and boundary conventions). Prediction: pi is larger than for
general code, so the same auditors have a lower ceiling without the convention, and resolving it moves coverage
more. Source: a scientific-coding benchmark with gold solutions and executable tests (to be selected; SciCode if
its test data can be obtained and run offline).

## 6. Roles of the existing studies

| Study | Role |
|---|---|
| E1 (registered) | natural-text clause intervention; pointer as attention control; taxonomy H6, read against the human labels |
| E6 (new) | primary identification experiment |
| natural decomposition (Section 4) | measurement foundation |
| E3 (registered) | data transfer, reported at its registered operating point; not claimed as a ceiling result |
| scientific results, SciCode reframing, earlier route and rulebook studies | appendix or compact illustration |
