# E13 design: a shape control for the convention finding (draft, 2026-11-15)

## Decision on E12
E12 (unused library tasks) is dropped: on-disk BigCodeBench projects about 5 units (E12_DESIGN.md), and DS-1000 would
need a download, a new task interface (code completion in context rather than functions) and weeks of construction,
for another set of constructed tasks. The code-shape finding below matters more to the paper's main claim.

## Why
An unanchored review (reviews/review_claude_fresh_F1.md) asked whether auditors flag program A more because its code
looks special rather than because it departs from a convention the models share. The exploratory split
(benchmarks/exploratory/e6_code_shape.py) supports the worry: with the task alone, the flag preference is +38.8
[20.0, 58.8] on the 20 held-out units whose A program has more conditionals than B and +9.5 [-7.1, 26.2] on the other
21; the convention advantage is +18.1 and +5.4. A split cannot separate the explanations, because departing from the
convention often needs extra code. A manipulation can.

## Design
For every registered E6 open unit, the vendor that wrote the audited programs edits program B into B': the inputs of
the unit's class are handled by an explicit branch that reproduces B's behaviour exactly; nothing else changes.
Execution check (no model): B' equals B (E6's comparator) on every registered input of the unit (hidden suite,
proposer, probes, stress, red team); B' must also add at least one conditional. Units whose B' fails get one second
edit, then drop out (reported).
Auditors read one program per call, so A's readings, and B's, are E6's frozen readings. Only B' is audited: E6's
task-alone arm, its four configurations, two readings per cell (8 per unit), E6's frozen prompt, rulebook, witness
scoring and cell policy, with the program text the only change.

## Hypotheses (held out: E6's 41 units)
- E13-1 (primary): change in flagging of the benchmark-conforming program, flag(B') - flag(B), task alone. The
  code-shape explanation predicts a positive change; the convention explanation predicts none. Reported with its
  95% problem-level interval; claimed positive if the lower limit is above 0, and "no shape effect detected" only if
  the interval lies within +/-10 points (equivalence margin fixed now).
- E13-2: flag preference with the shape matched, flag(A) - flag(B'), and the convention advantage with B' in place of
  B: lower limit above 0 means the preference survives shape matching.
- Descriptive: both, split by the code-shape strata above; conditionals added; edit sizes.
Development: E6's 16 development units first (pilot of the edit prompt and the checks), then freeze.

## Caveats
B' is a third program, written later by the same vendor; its added branch may itself look unusual. A's code is
unchanged, so E13 tests whether adding shape to B raises its flag rate, not whether removing shape from A lowers it.
E6's held-out results are known; E13's readings of B' are new. Units are reused and this is disclosed.

## Cost
About 41 + 16 edits, 57 x 8 = 456 readings plus witnesses; no download.
