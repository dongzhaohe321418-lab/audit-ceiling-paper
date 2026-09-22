# P1 — WITHDRAWN. This was not a registration, and the document said otherwise.

**Withdrawn 2026-09-22, the same day it was written, on the first cross-vendor review.**

## What it claimed

The original text conceded one weakness — that the 121 ratings already existed when it was
written — and then rested its whole value on a second claim:

> What is true, and is the reason to write this now: **no analysis script exists and no contrast
> has been computed.** … I have not seen either arm's rate, and every rule below is fixed before
> I do.

## Why that is false

The contrast had been computed and committed **an hour earlier, by me, in this same session.**
Paper commit `b0719cd`, 2026-09-22 16:32:20, records it as P3's Amendment 1 second outcome:

> missed 43/68 = 63.2%, caught 23/53 = 43.4%, difference +19.8 points, cluster [+1.2, +38.1],
> seed 20260921

The registration was committed at 17:31:09. The reviewer found this in the repository's own
history. Both rating CSVs were byte-identical to versions committed before it.

A registration's entire worth is its claim about what its author had not yet seen. This one made
that claim, the claim was false, and no part of the document survives it. **The `cannot-tell`
rule, the interval method and the instrument caveat were not fixed in advance of the result;
they were written down after it.** They may still be the right rules — that is a separate
question, to be argued on their merits and not on a chronology that did not happen.

## What actually happened, as far as the record shows

The rating and its first analysis were run before this session's context was compacted. The
document was then written afterwards without checking the repository history, which is an
explanation and not a defence: the history was one command away, and the sentence asserted
something about my own prior work that I had not checked.

## What stands in its place

Nothing registers this analysis. `benchmarks/code/RESULTS-RATE3.md` reports it as **a
re-analysis of a contrast already computed and committed**, and states the `cannot-tell` rule,
the disjoint-population reading and the instrument caveat as choices made with the result in
view. The `analysis.json` record and the arithmetic are unaffected by this withdrawal; the
reviewer reproduced every figure independently.

**See also**: this is the seventh overstatement in this programme's repairs, and the second in
which a document claimed more discipline than the process had. The first was a gate said to be
proved that had never been seen to fail.
