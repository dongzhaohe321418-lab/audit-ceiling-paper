# The review instrument is subject to the ceiling this paper measures

Raised by the owner, 2026-09-23: *using a model to review model-written work has the same
limitation the product does.* It does. This note records what can be measured about it rather
than arguing the point.

## The measurement

Rounds needed to clear review, from the archived reports:

| study | rounds to clear |
|---|---:|
| 20, ceiling 4 | 4 |
| P1, third rating | 6 |
| P2, severity sweep | 7 |
| 22, injection | 9 |
| 19, ceiling 3b | 10 |
| 17, testgen validation | 11 |

**In every one of them the round before the last still returned substantive findings** — sweep
round 6, rate3 round 5, injection round 8, ceiling 4 round 3, each checked in the archive. A
single pass with high recall clears a report in one round or two. These did not.

So **"quotable at round N" means a report survived N passes.** It is a filter whose per-pass
recall is low and unmeasured, not a verification.

## The split that makes it useful anyway

Across every round of every study, **no measurement ever moved.** Reviewers reproduced rates,
intervals, exact subset enumerations, seeds and bootstrap endpoints independently, executed the
analyses with writes intercepted, and found no arithmetic error in any of them. Every refusal
concerned what the prose claimed about arithmetic the reviewer had already confirmed.

**On recomputation the instrument is strong; on interpretation it is weak.** Those are two
different assurances and quoting them as one would be the exact error this programme keeps
making in other places.

Two further reasons it is not worthless, stated without inflating them:

* **Its findings are checkable, and every one acted on was checked first.** The 21-of-31
  contamination, the reversed sentence scoring 1.00, the three "hidden" assertions printed in
  the specification — each was reproduced locally before anything changed. The reviewer is a
  pointer, not an authority.
* **It refuses, including repairs.** Most later-round refusals rejected a fix written to satisfy
  the previous round. A relay endorses; this does not.

## The class of defect it leaves open, with an instance

The defect neither the gates nor a reviewer found: P3 audited the wrong program for **384
readings**, because `canonical_solution` is per problem and an instance is per (batch, problem).
Every automated gate passed — each checked that the code was *identical across conditions*, and
it was, identically wrong. It was found by hand, reading an adjudication sheet and noticing that
a displayed program returned exactly what its hidden suite was said to reject.

That is the shape of what this instrument cannot be relied on for: **a defect that looks right to
a language model**, because the reviewer is one. We do not know what else of that kind remains,
and the paper now says so in its methods rather than only here.

## What is being done about it, as opposed to conceded

1. **Stated in the paper.** The methods section carries the round counts, the
   recomputation/interpretation split, and the 384-reading instance.
2. **One channel is being tested.** Every review prompt states the claimed result before the
   reviewer begins — the "conclusion field" that arXiv 2609.07680 recommends withholding at the
   audit boundary. A prompt that withholds every figure and every prior verdict is written
   (`codex-review-blind1/prompt.md`) and will be dispatched against an already-settled report.
   If it finds the same things, the prompts' conclusions are not doing the work; if it finds
   something the others missed, this programme has been reading its own reports through a
   channel it did not know was open.
3. **What would actually fix it is not available here.** A human reviewer outside the project.
   P1 has been owed one since it was designed, and a third *model* rating did not discharge it.
