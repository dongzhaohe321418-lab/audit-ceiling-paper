# P0′ survey — the tool-use / executable-evidence axis

Started 2026-09-22 while P3's audit readings were being bought. **Incomplete**: this covers one
of the plan's five uncovered axes and three search queries. Nothing here may be cited until the
line says it was read from primary text.

## What was actually searched

Three queries, September 2026, via web search:

1. `LLM code review agent tool use execution versus read-only static inspection defect detection benchmark 2025 2026`
2. `ablation "with execution" versus "without execution" LLM bug detection agent recall improvement arxiv`
3. `code review LLM "read-only" versus agentic execution matched false positive rate ceiling recall audit comparison`

**No result answered the axis as the plan frames it** — a read-only auditor against a
tool-assisted one, on the same material, compared at a matched false-positive rate. That is
three queries, not a survey, and **the absence must not be reported as an absence in the
literature.** It is the state of this search.

## One paper read from primary text, and it matters

**Jin, H. and Chen, H., "Are LLMs Reliable Code Reviewers? Systematic Overcorrection in
Requirement Conformance Judgement."** Research Square preprint rs-8993044 v1, posted
2026-03-18; version of record in *Automated Software Engineering*, 2026-06-26,
doi:10.1007/s10515-026-00638-5. Read from the preprint PDF, pages 1–3 and 9–12.

**What it does.** Paired canonical/buggy implementations on **HumanEval, MBPP and QuixBugs**;
five models (three closed, two open); three prompting modes — `Direct` (verdict only),
`Direct+Explain` (verdict plus rationale), `Full` (verdict, rationale, and a proposed fix). The
question put to the model is "does the code satisfy the requirement?", answered YES/NO.

**Its headline, in its own terms.** Models frequently reject correct implementations, and
**richer prompts make it worse**: requiring an explanation and a proposed repair raises the
misjudgment rate rather than lowering it.

**⚠ The sign convention is INVERTED from ours, and mixing them up would be a serious error.**
In their confusion matrix `y = 1` is a *correct* implementation, so:

| theirs | means | our equivalent |
|---|---|---|
| **FN** (false rejection) | rejecting correct code — their "over-correction" | our **false positive on stratum C** |
| **FP** (false acceptance) | passing buggy code | our **miss on stratum P** |

**Its FN taxonomy is the mirror of our C4.** Table 1 names, among eleven categories,
*Added Requirement* — "the model introduces constraints not stated in the requirement and
rejects the code for violating these hallucinated requirements" — and *Overthink Edge*, where
the model overemphasises edge cases "despite the requirement not mandating such handling". Our
residual claim is that what the auditor *misses* concentrates where the specification does not
determine behaviour. Theirs is that what the auditor *falsely rejects* concentrates where the
model invents a requirement the specification does not state. **Same seam, opposite side.**

**Its evaluators are models**, as ours are: GPT-4o is used as an external evaluator for rationale
self-consistency (A1) and fault-awareness (A2).

## Two consequences for our own work

1. **The executable-evidence axis is not uncovered.** Their *Fix-guided Verification Filter*
   treats the model's proposed fix as **executable counterfactual evidence**, validating the
   original and the revised implementation against benchmark tests and spec-constrained
   augmented tests. The plan's P0′ table lists "tool use (executable code)" as an uncovered
   axis; that is true of *our* fifteen architectures and **is not true of the literature**. The
   plan's own instruction was to check each axis for existing work before spending, and this is
   what checking found.
2. **It belongs in related work, and near C12.** Their result — that asking for explanations and
   fixes increases false rejection — sits beside our finding that a rulebook sentence raises
   recall *and* false positives on correct code. The two are not the same experiment and must
   not be presented as replications of one another.

## Table 2, read from primary text (pp. 13–14), and what it costs us

Their Table 2 gives FPR and FNR per model, benchmark and prompting mode. Selected cells, in
**their** convention (FNR = rejecting correct code = our false positive on stratum C):

| model | benchmark | `Direct` FPR / FNR | `Full` FPR / FNR |
|---|---|---|---|
| GPT-4o | HumanEval | 2.44 / 26.2 | **0.00 / 73.2** |
| GPT-4o | MBPP | 3.70 / 35.9 | **0.20 / 87.9** |
| Claude-4-5-sonnet | HumanEval | 2.44 / 26.2 | 0.61 / 36.0 |
| Claude-4-5-sonnet | QuixBugs | 5.00 / 40.0 | 2.50 / 50.0 |
| Gemini-2.0-flash | HumanEval | 8.54 / 25.6 | 5.49 / 34.1 |

No intervals are given with these rates.

**Their §5.2 names the mechanism, and it is the one our rulebook study measured.** Enriching the
prompt does not improve judgement uniformly; it *redistributes* error between the two kinds,
buying fewer false acceptances at the price of more false rejections. Every model above moves
that way: FPR down, FNR up.

**This changes what our rulebook result may claim as new.** Our study 17/20 finding — a rulebook
sentence raises union BLOCKER recall by +20.9 points [+10.8, +31.8] at +8.0 points [+3.4, +12.7]
of false positives on correct code — is an instance of a **documented** tradeoff, not a
discovery of one. What is ours is the measurement: a defect population, a matched-rate
comparison, union at a stated depth, and intervals. **The paper must not present the tradeoff
itself as a finding**, and any sentence that reads that way is to be narrowed to the
measurement.

Their answer to RQ1 is also a prior statement adjacent to our residual claim: judging
conformance from the specification alone, without executing tests, is error-prone and
model-dependent. Ours is narrower and about misses rather than false rejections, and it should
be positioned against this rather than beside it.

## Not yet done
* The remaining four axes: sequential/adaptive, property-directed, debate/adversarial, and
  retrieval-augmented.
