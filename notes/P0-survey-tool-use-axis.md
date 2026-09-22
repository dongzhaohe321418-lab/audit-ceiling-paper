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

## Not yet done

* The reported FPR/FNR tables (their §5.1, Table 2) were not read. **No number from this paper
  may enter our manuscript until they are.**
* The remaining four axes: sequential/adaptive, property-directed, debate/adversarial, and
  retrieval-augmented.
