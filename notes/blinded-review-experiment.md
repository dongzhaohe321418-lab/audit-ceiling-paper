# Does telling the reviewer our conclusion change what it finds?

> **WITHDRAWN AS AN EXPERIMENT, 2026-09-23, by a mock referee who checked the prompt.**
> The prompt's own text withheld every figure. **Its binding-artefact list then named
> `plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md`, both of which state those
> figures**, the second being the ledger entry for the result under review. The blinding was
> never enforced. The agreement result below establishes nothing and is withdrawn; the six
> disagreement findings stand as findings about the report, not as evidence about blinding.
> The design was also not preregistered and has no matched briefed control, so it is n = 1,
> uncontrolled, exploratory.

**Original text follows, uncorrected, because a withdrawal that hides what it withdraws is
worse than the error.** One dispatch, 2026-09-23.

## The design

`RESULTS-RATE3.md` had been declared **quotable at round 6** after five refusals, and the file
was byte-identical since the commit at which that verdict was given. It was reviewed once more
under a prompt that gave the binding artefacts, the question and the verification list but
**withheld every claimed figure, every population description and every prior verdict**, and
asked the reviewer to compute its own numbers *before* reading the report.

This tests the channel arXiv 2609.07680 recommends closing: the conclusion field exposed to the
component whose independence it compromises. Every other review prompt in this programme states
the claimed result in its second paragraph.

## What agreed

The verdict: **quotable**, the same as round 6. All six contrasts reproduced, at a *different*
seed (23891) and resample count (30,000) chosen by the reviewer before it read ours — +19.84
points [+1.56, +38.01] against our +19.8 [+1.2, +38.1]. The repeat-agreement counts, the
registration chronology and the abstention gate all checked out.

**So the headline was not an artefact of being told.** That is worth as much as the rest.

## What only the blinded prompt found

Six things, after six conclusion-bearing rounds on the same file.

1. **The two groups are not one population with duplicates — they use different definitions of
   "caught".** The 68-entry group is what `cross` and `self` missed over 16 draws; the 53-entry
   group is what a larger three-family collection flagged. Eleven instances are missed under the
   first definition and caught under the second. Six rounds treated this as "11 instances sit in
   both arms" and never asked why.
2. **The sheet shows at most three failing inputs, and 81 of 121 entries have more than three
   recorded.** Eleven have none. So the labels cannot certify entailment across an instance's
   hidden failures — only across the ones displayed. **This is the same defect class as the
   `cases[:3]` truncation found in P3's classification the same day**, in a different artefact,
   and no conclusion-bearing round found either.
3. **The comparator is a different category, not a different format.** Its `ambiguous-oracle`
   includes cases where the prose *does* determine the answer and the oracle contradicts it —
   which need not be `undetermined` under the three-option question. Printing it under a heading
   about undetermined labels is misleading even with the caveat we attached.
4. **P3's registration says 71 labels changed. The CSVs say 67** (46 caught, 21 missed).
   Verified: 67.
5. **The "about six-tenths the size" comparison juxtaposes a 57-vs-53 contrast with a 68-vs-53
   contrast** while the instrument also changed, so it cannot isolate the effect of removing the
   author.
6. **There is no archived request/response trail binding each label to its prompt.** The
   registration describes six per-item retries; the committed runner does batch retries.

And one correction in the other direction: our "re-test rather than an independent review for
each" **overstates** the limitation. Prior author involvement does not make a fresh rater's
judgement non-independent; what it prevents is `L1` validating `L1`.

## What follows

**The conclusion-bearing prompts were doing work.** Telling a reviewer what we claim appears to
narrow what it examines: the blinded pass re-derived the population from the records and
immediately asked a question about its construction that six briefed passes did not.

Changes made:

* **Round 1 of every future review is dispatched conclusion-suppressed.** Later rounds may state
  what changed, because a reviewer checking a repair needs to know what was repaired.
* The six findings above are being verified and fixed individually; 2 and 4 are confirmed
  numerically already.
* The paper's methods section records this, because a programme that measures an auditing
  ceiling and then audits itself through a channel it had not tested owes the reader that.
