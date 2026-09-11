# Discussion

## What a union-recall number means

The most portable thing this paper has to say is a warning about its own headline. We report that
the shipped auditor's union recall over eight independent readings is 30.0% on one substrate and
71.0% on another. Neither number travels. On the second substrate the same auditor flags 55.3% of
correct work against 16.0% on the first, and its recall per unit of false-positive cost is lower
at every reading count. A single reading on the second substrate already produces more false
positives than eight readings on the first: 31.8% [24.9, 39.0] against 16.0% [10.1, 22.3], and
those intervals do not meet, so for this auditor no number of readings gives a matched
false-positive rate across the two substrates. That statement holds for the cross-vendor auditor,
which is the one the headline uses. It does not hold if the auditor families are pooled, because
substrate 1's same-vendor auditor reaches 24.0% [17.2, 31.2] and overlaps substrate 2's range. An
earlier draft of this section made the claim without that restriction, on point estimates alone;
a review of the figures caught it.

The consequence is not that one substrate is wrong. It is that an auditor's recall is a property
of where it is standing on its own trade-off, and that the trade-off moves with the material.
Published comparisons of reviewers and critics that report recall, F1 or win rates without the
corresponding rate on correct work are comparing operating points that need not be the same.

## Repeated reading buys coverage only where the decision is marginal

Union-of-K is the instrument this paper uses to find a ceiling, so it is worth saying when the
instrument does nothing at all. On the second substrate the same-vendor auditor's block decision
is identical across all eight independent readings on every one of 250 instances, while its reply
text, cost and latency vary — the readings happened, the verdict did not move. Its union curve is
therefore flat, and the registered efficiency ratio, which divides by the gain in false positives
over one reading, is undefined rather than large.

This is not a discovery about determinism. The same model, on the first substrate, splits its
verdict on 9 of 260 instances. What changed is the operating point: on the second substrate it
flags 88% of defective and 77% of correct increments, so almost nothing is near its decision
boundary and sampling noise has nothing to flip. The cross-vendor auditor, flagging 71% and 55%,
splits on 103 of 250.

The lesson generalises past this paper. Best-of-K, union-of-K and panel aggregation over critics
buy coverage in proportion to how much of the population sits near the critic's boundary. An
auditor tuned loud enough is invariant under resampling, and reporting its union over K readings
as though repetition contributed something would be an artefact of the reporting, not a property
of the system.

## What the ceiling is made of

Having measured a ceiling, we spent most of this work asking what it consists of, because the
answer determines whether it is a fact about auditors at all.

It is not a limit on repetition: the curve flattens, and pooling twenty readings across three
auditor families does not close the gap. It is not a fixed property of the auditor either: which
model reads, and what its rulebook tells it to look for, both move it by more than repetition
does. And a large part of it is not a property of the auditor at all. Under a rubric that asks
whether the specification's prose determines the hidden suite's expected value, most of the
residual fails that test, and a constructed population where the specification does determine the
answer is audited at close to ceiling by the same auditor reading once.

We are deliberately narrow about the last point. The constructed defects are detectably
artificial, and we measured that rather than assuming otherwise. What the construction licenses
is a negative claim — the measured ceiling is not a limit on detecting defects the specification
settles — not the positive claim that such defects are generally caught.

## Flagging is not naming

An audit that blocks an increment for the wrong reason has still blocked it, and a recall number
counts that as a catch. With the finding texts kept for one reading of the shipped auditor and
adjudicated blind by two raters, the auditor returned a finding on 9 of 110 defective instances
and asserted the actual failing behaviour on 5 to 7 of them, depending on how the two raters are
combined. The raters agreed only moderately, and we report that agreement rather than only the
rate it produces. Flag rates and naming rates are different quantities and should not be quoted
as though one licensed the other.

## Limits

Both substrates are short, self-contained Python functions with executable hidden tests; nothing
here measures auditing a change to a large program with no oracle. The generator is a single
model on both substrates. The residual rubric's raters were the author and a model; one external
label set agrees with them where it overlaps, and that overlap is eleven tasks. The injected
population's defects are distinguishable from natural ones. The same-vendor comparison on the
second substrate is incomplete because the provider refused most of its readings. Each of these is
recorded in the study that carries it, with the number it would change.

## What we would do next

Three things, in order. Adjudicate more than one reading of the shipped auditor, so the naming
rate can be compared with the union flag rate at the same K rather than across different K. Build
a population of *natural* defects independently known to be specification-determined, which is the
only way to separate the injected population's artificiality from the property it was built to
isolate. And measure one substrate where the ground truth is not a hidden test suite at all, since
every ceiling in this paper is, in the end, a statement about what a test suite was able to ask.
