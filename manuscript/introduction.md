# Introduction

An automated auditor reads code it did not write and says whether to block it. We ask how much
such an auditor catches, and what decides the limit.

That is a different question from how good a reviewer model is. A reviewer's score on a benchmark
mixes at least four things together: whether the model can see a defect, whether it judges the
defect worth blocking on, whether the benchmark's hidden tests define the behaviour it would have
to see, and how many times it is allowed to look. Work on code-review and critic models improves
the first two and reports the aggregate gain. We hold the auditor, its instructions and its ground
truth fixed, and vary the other three one at a time, against a truth no model supplies: a hidden
test suite executed by an interpreter.

Reading again saturates. Eight independent readings of the same increment by the shipped
cross-vendor auditor reach 30.0% union recall on defective increments, with a 95% problem-cluster
interval of 20.0 to 40.7, and the eighth reading adds 1.9 points. Twenty readings pooled across
three auditor families reach 48.2%. More sampling does not remove whatever sets that limit.

What does move it is the auditor and its instructions. Swapping in a stronger model of the
generator's own vendor changes union recall by −26.4 points [−37.3, −15.6], a preregistered
primary: a stronger model is a worse auditor here. Adding one sentence to the auditor's rulebook,
telling it to look for what the visible tests do not cover, moves flags by +26.8 points
[13.6, 40.4], which is the largest effect we measure, and it costs enough false positives to put
the rule outside the product's own constraint.

Much of what the auditor "misses" turns out to be failure the specification never determined. We
re-rated the never-flagged residual under a rule that asks whether the prose settles the hidden
suite's expected value before it asks whether the visible tests exercised the input. Two raters
agree that 44 of 57 residual instances are cases where the prose does not settle it, reversing the
same instances' earlier classification. Where an outside party had already flagged one of these
specifications as defective, for their own purposes and before we looked, our raters agree on 9 of
the 11 tasks that overlap.

We then built a population where specification-determinedness holds by construction and audited it
with the same auditor and the same eight readings. Recall goes from roughly a third to 90 of 92,
and one reading is worth almost as much as eight. This is easy to overstate. It shows the measured
ceiling is not a limit on detecting defects the specification settles. It does not show that such
defects are generally caught, because the constructed defects are detectably artificial: a
frontier model separates them from natural ones at 96.7%, well above chance, and we measured that
rather than assuming it away.

The headline number does not travel either. On a second substrate whose specifications run three
times longer and whose solutions run seven times longer, the same auditor reaches more than twice
the recall while flagging more than three times as much correct work, and buys less recall per
false positive at every reading count. For the cross-vendor auditor the two substrates' false
positive intervals do not meet at any reading count, so there is no matched operating point at
which to compare them. A union recall figure quoted without its false-positive rate is not a
portable number, and the ceiling we measure is an operating point rather than a constant.

## What this paper is careful about

Every study was preregistered before its first model call, with hypotheses, intervals, kill
conditions and stopping rules fixed in advance, and every departure recorded as a numbered
amendment that says what was known at the time. Four preregistered hypotheses were killed by their
own rules, two of them our own conjectures. Every report was reviewed by a model from a different
vendor with access to the raw records, and no report entered this manuscript until such a review
approved it; several needed many rounds, and the reviews are archived verbatim beside the results
they judge. We record this as method rather than contribution. It is why the negative results here
can be read as results instead of as failures to find an effect.
