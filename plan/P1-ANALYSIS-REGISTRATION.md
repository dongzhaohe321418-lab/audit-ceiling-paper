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
that claim, the claim was false, and no part of *this document* survives it.

**The first version of this withdrawal then overcorrected, and the second review caught that
too.** It said the `cannot-tell` rule and the interval method "were not fixed in advance of the
result". They were. P3's Amendment 1 (`d5919b9`, 2026-09-21 20:24:05, a day before the ratings)
registered the three-option rubric, the share over **all** entries in each group, the
problem-cluster percentile bootstrap over the union of their problems, 10,000 resamples, seed
`20260921`, Wilson beside it, and an inconclusiveness gate at one-third `cannot-tell`.

So the record is: **a method registered in advance, then a redundant registration that described
its own chronology falsely, then later additions that were never registered at all** — the
disjoint-population diagnostic and the broken-sheet comparison. Each of the three deserves its
own name, and flattening them into "nothing was registered" was the easier, and wrong, summary.

## What actually happened, as far as the record shows

The rating and its first analysis were run before this session's context was compacted. The
document was then written afterwards without checking the repository history, which is an
explanation and not a defence: the history was one command away, and the sentence asserted
something about my own prior work that I had not checked.

## What stands in its place

Nothing registers this analysis. `benchmarks/code/RESULTS-RATE3.md` reports it as **a
re-analysis of a contrast already computed and committed**, and separates what Amendment 1
registered in advance from what was added afterwards with the result in view. The `analysis.json` record and the arithmetic are unaffected by this withdrawal; the
reviewer reproduced every figure independently.

**See also**: this is the seventh overstatement in this programme's repairs, and the second in
which a document claimed more discipline than the process had. The first was a gate said to be
proved that had never been seen to fail.
