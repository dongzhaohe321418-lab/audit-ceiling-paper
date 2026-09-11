# Title and abstract

## Title

**What sets the ceiling on automated code audit: the auditor, its rulebook, or the specification?**

## Abstract

An automated auditor reads code it did not write and decides whether to block it. We ask how much
such an auditor can catch and what sets the limit, on ground truth no model supplies: hidden test
suites executed by an interpreter. Holding the auditor, its instructions and its ground truth
fixed and varying one thing at a time, we find that the limit is not a property of the auditor
alone.

Repeated independent reading saturates far below complete: eight readings of the shipped
cross-vendor auditor reach 30.0% union recall on defective increments (95% problem-cluster
interval 20.0–40.7), the eighth reading adding 1.9 points, and pooling twenty readings across
three auditor families reaches 48.2% (36.7–60.0). What moves that figure is not more sampling.
Replacing the auditor with a stronger same-vendor model moves union recall by −26.4 points
(−37.3 to −15.6), a preregistered primary: a stronger model is not a better auditor. Adding one
sentence to the auditor's rulebook — find what the visible tests do not cover — moves flags by
+26.8 points (13.6–40.4), the largest effect we measure.

Most of what the auditor missed turns out not to be a property of the auditor at all. Under a
rubric that asks whether the specification's prose determines the hidden suite's expected value,
two raters agree that 44 of the 57 never-flagged defects are cases where it does not, reversing
the same instances' earlier classification and withdrawing a claim this work previously made;
where an outside party had independently flagged one of these specifications as defective, our
raters agree on 9 of the 11 tasks that overlap.

We draw two cautions for the literature that reports critic and reviewer recall. A union-recall
figure quoted without the corresponding rate on correct work is not portable: on a second
substrate with three times longer specifications the same auditor reaches more than twice the
recall while flagging more than three times as much correct code, and no reading count places the
two at a matched false-positive rate. And repeated reading buys coverage only in proportion to how
much of the population sits near the auditor's decision boundary — one auditor we measure returns
an identical verdict on all 250 instances across eight independent readings while its replies,
costs and latencies vary, so its union over K readings is flat by construction.

Every study was preregistered before its first model call, with hypotheses, intervals, kill
conditions and stopping rules fixed in advance; four preregistered hypotheses were killed by their
own rules. Every report was reviewed by a model from a different vendor with access to the raw
records, and the reviews are archived verbatim beside the results they judge.

## Positioning

The contribution is a measurement method and two negative results, not a better auditor. The
closest neighbours improve critics and report aggregate gains; we hold the critic fixed and ask
what its score is made of. The claims we are willing to defend are exactly those in `CLAIMS.md`,
each with the interval and the label its source report gives it.
