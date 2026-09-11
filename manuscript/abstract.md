# Title and abstract

## Title

What sets the ceiling on automated code audit: the auditor, its rulebook, or the specification?

## Abstract

An automated auditor reads code it did not write and decides whether to block it. We ask how much
such an auditor catches and what decides the limit, against ground truth no model supplies: hidden
test suites executed by an interpreter. Holding the auditor, its instructions and its ground truth
fixed, and varying one thing at a time, we find the limit is set jointly by which model reads,
what its rulebook tells it to look for, and whether the benchmark's hidden suite asks a question
the specification answers.

Repeated independent reading saturates far below complete. Eight readings of the shipped
cross-vendor auditor reach 30.0% union recall on defective increments [20.0, 40.7], the eighth
reading adding 1.9 points; twenty readings pooled across three auditor families reach 48.2%
[36.7, 60.0]. Replacing the auditor with a stronger same-vendor model moves union recall by −26.4
points [−37.3, −15.6], a preregistered primary, so a stronger model is a worse auditor here.
Adding one sentence to the auditor's rulebook, telling it to look for what the visible tests do
not cover, moves flags by +26.8 points [13.6, 40.4], the largest effect we measure.

Much of what the auditor misses turns out to be failure the specification never determined. Under
a rule that asks whether the prose settles the hidden suite's expected value, two raters agree
that 44 of the 57 never-flagged defects are cases where it does not, reversing the same instances'
earlier classification and withdrawing a claim this work previously made. Where an outside party
had independently flagged one of these specifications as defective, our raters agree on 9 of the
11 tasks that overlap.

Two cautions follow for work that reports critic and reviewer recall. First, a union-recall figure
is contingent on the matching rate on correct work. On a second substrate with three times longer
specifications the same auditor reaches more than twice the recall while flagging more than three
times as much correct code. For that auditor the two substrates' false-positive intervals never
meet, so no reading count offers a matched comparison. Second, repeated reading buys coverage in
proportion to how much of the population sits near the auditor's decision boundary. One auditor we
measure returns an identical verdict on all 250 instances across eight independent readings while
its replies, costs and latencies vary, so its union over K readings is flat by construction.

Every study was preregistered before its first model call, with hypotheses, intervals, kill
conditions and stopping rules fixed in advance; four preregistered hypotheses were killed by their
own rules. Every report was reviewed by a model from a different vendor with access to the raw
records, and the reviews are archived verbatim beside the results they judge.

## Positioning

The contribution is a measurement method and two negative results. The nearest neighbours improve
critics and report the aggregate gain; we hold the critic fixed and ask what its score is made of.
The claims we will defend are the ones in `CLAIMS.md`, each carrying the interval and the label its
source report gives it.
