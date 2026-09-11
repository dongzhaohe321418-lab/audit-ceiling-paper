# Two manuscript reviews, 2026-09-12, and what was done with each

Two independent reviews of the manuscript arrived on the same day. Both read the paper as a
whole rather than a single study. This file records every finding and its disposition, including
the findings deliberately not acted on, so that the deferrals are a decision on the record rather
than an omission.

## Review A — Claude, peer-review framing, verdict "reject (3), confidence 4"

Read the built PDF at the state before `6e97963`.

**Acted on.** Two false statements about the paper's own review gate; "saturates" against a failed
flattening bar; the `-26.4` auditor contrast restated with its unmatched operating point, its sign
reversal under the any-finding rule, and the temperature-0 sampling asymmetry; `astra` reported as
the counterexample; "the largest effect we measure" withdrawn and C3's estimand restated with its
false-positive cost and its null on hidden-suite pass rate; study 20's fired kill stated;
multiplicity and the cluster sign-flip p; unvalidated bootstrap coverage; models, versions and the
repository URL; rater non-blindness; the missing coverage@k and self-correction literatures.

**Rejected, with reason.** Its recommendation to compute precision at the observed prevalence
rested on a correct-code population of 910. The record says 150. The strata are built at a
designed ratio chosen for the power of the contrasts, so a precision computed from them would
describe our design and not a repository; the paper now says that instead. Its transcription of
the last-step-gain interval, `[1.13, 2.82]`, is also wrong: the record says `[1.14, 2.78]`.

## Review B — OpenAI, read at `fcbc92b`, before Review A's repairs were applied

Most of its list was already closed by those repairs. Five items were not.

**Acted on.** The CriticGPT characterisation, which claimed that work is "evaluated largely on
inserted defects" when it reports critiques on naturally occurring model errors (preferred over
human critiques in 63% of cases) and reports critic hallucination — both of which this paper had
been positioning as its own ground. The conflict between calling hidden-suite-passing code
"correct" and arguing that specifications do not determine what the hidden suite asks. The defect
population as the residue that survived the visible tests rather than a sample of model-written
code. That twenty readings missing an instance does not establish that it is undetectable. The
"independent unit is the instance" wording, and what the problem bootstrap does and does not
cover.

**Deferred, with reason.**

| finding | why not now |
|---|---|
| Equal-false-positive comparison of rules, models and reading counts (its P1-A) | Needs a severity-threshold sweep. Already the first item in the paper's own limitations and future work; the two threshold points we have are reported. |
| Independent human annotation of findings and of the residual rubric (P1-B) | Needs a person who is not on this project. Named in the limitations. |
| Specification-clarification experiment holding code and visible tests fixed (P1-C) | **The best new idea in either review.** Adopted into future work verbatim as a design, with the length-matched placebo arm. Not run: it needs new model calls. |
| Tool-assisted auditing arm (P2-A) | The conservative path was taken instead: the paper scopes itself to reading-based review and does not extrapolate to agentic auditors. |
| Two-dimensional residual labelling, separating "does the specification determine it" from "do the visible tests cover it", instead of an ordered mutually exclusive rubric | A genuine improvement over the current rubric. Requires re-labelling 57 instances and re-running the agreement analysis; recorded for the next revision. |
| Restructure Results by scientific question rather than by study, and a four-figure narrative | Invasive, and cosmetic relative to the claims. Recorded. |
| Retitle away from "ceiling" | The current title is a question, not an assertion of a proved bound, and the text no longer claims a universal limit. Left as is. |
| A frozen validation set never used for rule design or model selection | The right answer to the accumulated researcher degrees of freedom across eight studies. Out of scope for this revision; recorded as the strongest available answer to that concern. |

**Not accepted.** Its earlier framing of an "audit ceiling ≤ specification ceiling" inequality,
which it retracts itself in the same review, was never in the manuscript.

## The standing rule these reviews do not change

Four studies remain in independent cross-vendor review. Their numbers stay confined to one
labelled section, load-bearing for no admitted claim, and this manuscript does not go to a
preprint server or a venue until those reviews approve or the numbers are removed.
