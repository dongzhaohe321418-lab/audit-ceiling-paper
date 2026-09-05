# Where is the ceiling of AI audit?

Private. A manuscript in preparation, with every number it states regenerable
from the records committed beside it.

## Question

As AI-generated output grows, can AI audit itself to raise accuracy, and where
is the limit? Two ceilings are measured separately: how much of what is wrong an
AI reviewer can ever *see* (a saturation curve over repeated and diverse draws),
and how much *correction* that seeing buys once the loop is closed (hidden-test
accuracy before and after self-audit-then-revise). Ground truth throughout is a
test that passes or fails; no model judges anything.

## Layout

    records/      one JSONL row per (arm, draw, instance); manifests; preregistrations
    analysis/     scripts that regenerate every number and figure from records/, no key, no network
    figures/      generated only by analysis/; never hand-edited
    manuscript/   the paper

## Standard

`EXPERIMENT_RECORD.md` here is the binding standard, copied from the product
repository at the commit named in `PROVENANCE.md`. Its section 9 is the one
this repository exists to honour: a number keeps its interval and its
estimand wherever it travels; a small count is quoted as the count; nothing is
"inside the noise floor" without a replicate arm for the same estimand; a
superseded number is withdrawn in writing.

Every study's raw run directories live outside any repository, in
`~/Documents/Crossaudit/study-data/`, because they carry model outputs derived
from a CC BY-NC-SA corpus. Only derived values are committed.
