# Discussion

## What a union-recall number means

We report the shipped auditor's union recall over eight independent readings as 30.0% on one
substrate and 71.0% on another, and both figures are contingent on the rate they cost. On the
second substrate the same auditor flags 55.3% of correct work where it flagged 16.0% on the first,
and it buys less recall per unit of false-positive cost at every reading count. A single reading on
the second substrate already costs more false positives than eight readings on the first: 31.8%
[24.9, 39.0] against 16.0% [10.1, 22.3], intervals that do not meet. For the cross-vendor auditor,
then, no reading count gives a matched false-positive rate across the two substrates. That holds
for the cross-vendor auditor, which is the one the headline uses. Pooling the families breaks it,
because substrate 1's same-vendor auditor reaches 24.0% [17.2, 31.2], which overlaps substrate 2's
range. An earlier draft asserted the unrestricted version on point estimates alone, and a review of
the figures caught it.

An auditor's recall is a property of where it stands on its own trade-off, and the trade-off moves
with the material, so the two substrates measure one auditor at two operating points. Comparisons
of reviewers and critics that report recall, F1 or win rates without the corresponding rate on
correct work are comparing operating points that need not be the same.

## Repeated reading buys coverage only where the decision is marginal

Union-of-K is the instrument this paper uses to find a ceiling, and on the second substrate the
same-vendor auditor shows what it measures when it measures nothing. That auditor's block decision
is identical across all eight independent readings on every one of 250 instances, while its reply
text, cost and latency vary. Its union curve is flat, and the registered efficiency ratio, which
divides by the gain in false positives over one reading, is undefined rather than large.

The explanation is the operating point. On the second substrate that auditor flags 88% of
defective and 77% of correct increments, so almost nothing sits near its decision boundary and
resampling has little left to flip. The cross-vendor auditor on the same substrate splits its
verdict across draws on 103 of 250 instances and the same-vendor auditor on none; the flat arm is
also the arm sampled at temperature 0, and the two explanations are not separable without a
temperature-matched replication that was not run. The cross-vendor auditor, at 71% and 55%, splits on 103
of 250.

Best-of-K, union-of-K and panel aggregation over critics therefore buy coverage in proportion to
how much of the population sits near the critic's boundary. An auditor tuned loud enough is
invariant under resampling, and its union over K readings can rise only as far as its marginal
cases allow.

## What the ceiling is made of

Three measured contributions account for most of it, and repetition is the smallest. Eight
readings of one auditor buy 19.3 points of recall, and twenty readings across three families leave
51.8% of the defect population untouched. Changing which model reads moves the same quantity by
26.4 points, and changing one sentence of the rulebook moves flags by 26.8. The largest
contribution belongs to the benchmark rather than to the auditor: under a rule that asks whether
the specification's prose determines the hidden suite's expected value, 44 of the 57 never-flagged
defects fail that test, and a constructed population where the prose does determine the answer is
audited at 90 of 92 by the same auditor reading once.

The constructed population carries a limitation we measured rather than assumed. Its defects are
detectably artificial: a frontier model separates them from natural ones at 96.7%. What the
construction licenses is a bound, that the measured ceiling lies above what an auditor can do on
defects the specification settles, and it leaves open how often natural defects of that kind are
caught.

## Flagging is not naming

An audit that blocks an increment for the wrong reason has still blocked it, and a recall number
counts that as a catch. With the finding texts kept for one reading of the shipped auditor and
adjudicated blind by two raters, the auditor returned a finding on 9 of 110 defective instances
and asserted the actual failing behaviour on 5 to 7 of them, depending on how the two raters are
combined. The raters agreed at κ = 0.391, which we report beside the rate it produces, because a
moderate agreement is part of what the rate is worth.

## Limits

Both substrates are short, self-contained Python functions with executable hidden tests, so
nothing here measures auditing a change to a large program with no oracle. The generator is a
single model on both substrates. The residual rubric's raters were the author and a model; one
external label set agrees with them across eleven overlapping tasks. The injected population's
defects are distinguishable from natural ones. Each of these is recorded in the study that carries
it, together with the number it would change.

## What we would do next

Adjudicating more than one reading of the shipped auditor would let a naming rate be compared with
a union flag rate at the same K. A population of natural defects independently known to be
specification-determined would separate the injected population's artificiality from the property
it was built to isolate. And a substrate whose ground truth is not a hidden test suite would test
the assumption every ceiling here rests on, which is that a test suite asked the right question.
