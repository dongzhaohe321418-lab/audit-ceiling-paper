# ICML 2027 plan

Target: ICML 2027 main track (deadline expected late January 2027; to be confirmed on icml.cc). Fallback: an
ICLR 2027 or ICML 2027 workshop, then NeurIPS 2027.

## The paper's direction (kept)

The question stays the author's: **what moves the ceiling on automated audit, from general code to scientific
code, results and data.** The answer the paper will defend, in one sentence:

> An automated auditor's ceiling is set less by which model reads than by what the reader is given: what the
> specification determines, how a finding is counted, and, in science, whether an executable check can verify
> what the model claims.

Two halves carry it:

1. **General code: information and operating point.** Recall is an operating point (readings, rulebook,
   decision rule), so auditors must be compared on operating-characteristic curves, not single numbers; and
   the defects no reading flags are mostly ones the specification does not determine. The new causal
   experiment (E1) tests the second part directly.
2. **Science: evidence tiers.** Deterministic verification and model reading fail in different places on
   scientific code, reported results and data. The extended science study (E3) tests this on unseen datasets,
   larger artefacts and a stronger deterministic baseline.

## What the first review (GPT, round A1, 4/10) found, and the response

| Objection | Response in this plan |
|---|---|
| "Ceiling" is not identified; union curves flatten by construction | Define the ceiling operationally (finite-budget union recall at its false-positive rate) in the first page; report operating-characteristic curves (E2); keep "diminishing returns, no plateau". |
| Model and sampling confounded across routes | E1 and E2 compare auditors only within route, at matched observable budgets, and report K=1 separately; route contrasts are labelled configuration comparisons. |
| Small N, one generator, tiny functions | E1/E2 use two generators (GPT and Claude), fresh candidates, ~300 tasks, and a newer substrate. |
| Flag is not diagnosis | New primary endpoint: **verified diagnosis**, an auditor-supplied input whose expected output disagrees with the candidate's and agrees with the reference, checked by execution. |
| Specification account is post hoc | E1: randomised within-item intervention (original / plus a validated missing requirement / plus a length-matched irrelevant sentence), clauses validated by executable predicates before any audit call. |
| Science complementarity easy by construction | E3: more datasets, held-out sources, three sizes, a deliberately strong validator, model auditing measured without seeing validator output. |
| Study 23 numbers withheld after a failed hypothesis | Recover the technically valid run, validate it, report it as a failed replication. |
| Too many studies, lab-notebook prose | Reorganise by question; main text carries E1, E2, the repeated-reading/rulebook results and the science results; the rest moves to the appendix; governance vocabulary removed. |

## Experiments

All model calls go through the shipped prompt builder; GPT auditors through the Codex CLI path the harness
already uses (`astra`-style, same prompt bytes), Claude auditors through a new Claude Code CLI path that sends
the same bytes. Every experiment is preregistered in `plan/icml2027/` before its first audit call, with
development/test splits by problem.

- **E1, causal specification intervention (core).** Fresh candidates from two generators on HumanEval+/MBPP+
  and a newer substrate; items = visible-pass/hidden-fail defects with a correct candidate for the same task.
  For each item, a minimal missing requirement (prose + executable predicate) and a length-matched irrelevant
  sentence are drafted by a model and admitted only if the reference passes the predicate, the defective
  candidate fails it, and the irrelevant sentence's predicate is satisfied by both. Arms: original, +clause,
  +placebo, at fixed code. Auditors: one GPT, one Claude. Endpoints: flag and verified diagnosis on defective
  items; flag on correct items; paired contrasts, task-cluster bootstrap.
- **E2, operating characteristics across auditors and generators.** Same item pool, K=4 readings per auditor,
  a fixed severity/confidence score; curves of union recall against false-positive rate, ranking reversals
  across operating points, verified-diagnosis curves.
- **E3, science at scale.** Data: more UCI/OpenML datasets, held-out sources, three table sizes, strong
  validator; results: more SciCode-derived and numerical workflows with independent re-computation.
- **E4, study 23 recovery.** Validate and report the BigCodeBench run.

## Schedule (weeks from 9 Nov 2026)

1–2 E1/E2 construction, preregistration, pilots · 3–5 E1/E2 runs · 5–7 E3 · 7 E4 · 8–10 rewrite, GPT audit and
humanize rounds, reproducibility · 11 buffer, submission.
