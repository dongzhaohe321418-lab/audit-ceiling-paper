# Introduction

An automated auditor reads code it did not write and says whether to block it. The question this
paper asks is how much such an auditor can catch, and what sets the limit.

The question is not the same as asking how good a reviewer model is. A reviewer's score on a
benchmark mixes at least four things: whether the model can see a defect, whether it decides the
defect is worth blocking on, whether the benchmark's hidden tests define the behaviour it would
have to see, and how many times it is allowed to look. Published work on code-review and critic
models improves the first two and reports aggregate gains. We hold the auditor, its instructions
and its ground truth fixed and vary the other three, one at a time, on a truth no model supplies:
a hidden test suite executed by an interpreter.

Three results follow, and the third is the one that changes how the first two should be read.

**Reading again saturates.** Eight independent readings of the same increment by the shipped
cross-vendor auditor reach union recall far below complete, and the last reading adds little.
Pooling twenty readings across three auditor families does not close the gap either. Whatever the
ceiling is, it is not something more sampling removes.

**What sets the operating point is the auditor and its instructions, not the number of readings.**
Changing which model reads moves union recall by more than reading eight times does. Adding one
sentence to the auditor's rulebook — look for what the visible tests do not cover — moves it
further still, and at a false-positive cost that puts it outside the product's own constraint.

**And a large part of what the auditor "misses" is failure the specification never determined.**
Re-rating the residual under a rubric that asks whether the prose settles the expected value,
before asking whether the visible tests exercised the input, reverses its earlier
characterisation. Two outside sources that labelled these same benchmark tasks for their own
reasons agree with the re-rating where they overlap. Constructing a population where
specification-determinedness holds by construction, and auditing it with the same auditor and the
same eight readings, raises recall from roughly a third to nearly all — and one reading is almost
as good as eight.

That last result is easy to overstate, so we state it narrowly. It shows the measured ceiling is
not a limit on detecting defects the specification settles. It does not show that the auditor
catches specification-determined defects in general, because the constructed defects are
detectably artificial: a frontier model separates them from natural ones well above chance.

Finally, the headline number is not portable. On a second substrate whose specifications are
three times longer and whose solutions are seven times longer, the same auditor reaches more than
twice the recall — while flagging more than three times as much correct work, at a worse rate of
recall bought per false positive at every reading count, and with a single reading already
producing more false positives than eight readings on the first substrate. There is no reading
count at which the two substrates can be compared at a matched false-positive rate. **A union
recall figure quoted without its false-positive rate is not a portable number, and the ceiling we
measure is an operating point rather than a constant.**

## What this paper is careful about

Every study here was preregistered before its first model call, with its hypotheses, intervals,
kill conditions and stopping rule fixed in advance; every departure is a numbered amendment that
records what was known at the time. Four preregistered hypotheses were killed by their own rules,
including two of our own conjectures. Every report passed an independent review by a model from a
different vendor with access to the raw records, and no report entered this manuscript until such
a review ended in approval; several needed many rounds, and the reviews are archived verbatim
beside the results they judge. We record this as method, not as contribution, but it is the reason
the negative results here can be read as results rather than as failures to find an effect.
