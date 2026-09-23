# The paper as a four-act study, and the AI4S programme that completes it

Written 2026-09-23 at the owner's direction: the paper is to (1) introduce CrossAudit, (2) show its
limit, (3) study what sets and moves an audit limit, and (4) test whether these audit setups work
in AI for Science (AI4S): auditing scientific code, validating scientific results, and auditing
scientific data. Acts 1–3 exist as measurements (C1–C16). Act 4 does not exist yet; this document
designs it. Every study below is preregistered before its first model call, reviewed cross-vendor,
and enters the paper only through `manuscript/CLAIMS.md`.

## The story, and why it is novel

**Act 1 — the system.** CrossAudit separates the model that builds from a different vendor's model
that audits, adds a deterministic check layer (profiles `general`, `science`, `research`), blocks
on BLOCKER findings, and records every call in a tamper-evident ledger with signed receipts. The
`science` profile already encodes the design rule the AI4S act tests: *the model names evidence,
code verifies it* (units, convergence, provenance, number→source).

**Act 2 — its limit.** On HumanEval+/MBPP+ against hidden suites: 30.0% union recall at eight
readings at 16.0% false positives; pooling three families reaches 48.2% at 36.0%; flags on correct
code are mostly unconfirmable (C16).

**Act 3 — what sets and moves a limit.** Repetition (diminishing, singleton-driven), which model
reads (confounded with sampling), the rulebook, the decision rule, specification determinacy
(C4/C14), and the clarification intervention (C13).

**Act 4 — AI4S.** Three studies, one per job a scientist would hand an auditor.

**Novelty, from the survey (`notes/ai4s-survey.md`).** No prior work measures an LLM auditor's
recall *and* false-positive rate against an *executed* ground truth on scientific code, results or
data, across vendors and repeated readings. Nearest: Luo et al. 2025 (100 constructed AI-scientist
items, one model, accuracy/FPR), SPOT (papers, recall ≤21.1%, unstable across runs), SciCoQA
(paper–code discrepancies, 46.7% recall, annotated not executed), scicode-lint (partly LLM-judged).
What this paper adds: the same instrument across general and scientific code, the
spec-determinacy decomposition of misses carried into science, and a head-to-head of an LLM
auditor against deterministic verification for results and data, inside one shipped system.

## A4S-1 — auditing scientific code (SciCode)

*Question.* Does the audit limit measured on toy Python hold, fall or rise on research code, and
are scientific misses even more often failures the specification never determined (tolerances,
units, conventions, numerical method)?

*Substrate.* SciCode (Tian et al. 2024; Apache-2.0): 80 main problems, 338 steps, scientists'
tests with numeric targets. Gate done (`notes/ai4s-scicode-gate.md`): gold code on the dev split
passes 48 of 50 steps in our environment; the two failures are a wall-clock-dependent gold solution
and one unexplained numeric mismatch.

*Design.* The frozen generator of Acts 2–3 (`claude-haiku-4-5-20251001`) writes each step in
SciCode's own protocol (with background, earlier steps from its own code), three samples per step.
A step candidate that passes the scientists' tests is *correct*; one that fails is *defective*;
steps no candidate passes are excluded as unproven-passable in this environment. SciCode has no
visible/hidden split and **we do not invent one** (substrate 2 died of exactly that): the auditor
sees the step's prose, background, header and the candidate, and no tests. Samples: up to 150
defective and 150 correct instances, problem-clustered, drawn by seed. Auditor: the shipped
cross-vendor route at K = 8; the same-vendor route at K = 8 as the second family.

*Outcomes.* Union recall and false positives at K; the flattening statistic; the same-vendor
contrast; and, on the residual, the spec-determinacy classification under the Act-3 rubric,
compared with EvalPlus's 44 of 57.

*Hypotheses fixed in advance.* H1: union recall at K = 8 is lower on SciCode than 30.0% (reported
as two estimates on two substrates, not as a test). H2: the undetermined share of the SciCode
residual exceeds the EvalPlus share (77.2%) — registered as a directional expectation with its
interval, killed if the SciCode share's lower bound falls below 50%.

*Budget.* Generation ~1,000 step samples, auditing ~4,800 readings: halt at $90.

## A4S-2 — validating scientific results

*Question.* Given code and a report of the numbers it produced, can an auditor tell whether the
reported results follow? This is the reproducibility question in its smallest executable form.

*Construction.* From A4S-1's correct candidates, run each on its test inputs to obtain true outputs.
Build a short results report (prose plus `results.json`) per instance. Clean reports state the true
outputs; faulty ones carry exactly one registered fault: a unit or scale slip (×10³, eV↔J,
degrees↔radians), a sign flip, a value from a different input, a misreported tolerance (a number
that differs beyond the test's own tolerance), or a transposed-digit transcription. Ground truth is
execution.

*Three auditors, one population.* (a) the LLM auditor, read-only, K readings; (b) CrossAudit's
deterministic `science` checks as shipped; (c) a re-execution check (run the cited code on the
cited input and compare within tolerance), which is the "model names, code verifies" design.
Outcomes: recall by fault type and false positives on clean reports, per auditor and for (a)+(b)
and (a)+(c).

*Expectation stated in advance.* (c) near-perfect where the input is cited, (a) weak on numeric
faults, (b) catches provenance breaks only. The value of the study is the size of those gaps and
which faults only a reader catches (e.g. a physically implausible value with a valid provenance).

## A4S-3 — auditing scientific data

*Question.* Can the same auditor find the faults that corrupt scientific datasets, and how does it
compare with deterministic data checks?

*Substrate.* Physical-science tabular datasets from the UCI repository under CC BY 4.0 (to be
fixed in the registration, e.g. concrete strength, superconductivity, airfoil self-noise, combined
cycle power plant, protein tertiary structure), each with a short data card.

*Faults, injected with known ground truth, one per corrupted copy:* mixed units within a column,
physically impossible values, train/test leakage by duplicated rows, a subset of shuffled targets,
swapped columns under unchanged headers, an unflagged missing-value sentinel, and a silently
truncated precision. Clean copies are the false-positive stratum.

*Auditors.* LLM auditor with K readings; a deterministic profile (schema, ranges, duplicates, unit
consistency) as the "code verifies" comparator; the combination. Outcomes: recall by fault type,
false positives on clean copies.

## Order, cost, gates

1. A4S-1 generation and execution (no auditing yet) — establishes the strata; cheap.
2. A4S-1 preregistration committed; auditing; spec-determinacy rating; review.
3. A4S-2 built on A4S-1's correct candidates; preregistered; run; review.
4. A4S-3 preregistered; run; review.
5. Paper restructured into the four acts; whole-manuscript review until submittable.

Total model budget ~$150–200 across the three studies, each with its own halt. Every new substrate
passes a parse-and-execute gate before its first model call. Nothing enters the paper before its
report ends quotable.
