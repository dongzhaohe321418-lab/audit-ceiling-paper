# Results

Every figure in this section comes from a report that passed an independent cross-vendor review
ending in approval, and carries the interval and the label that report gives it. The governing
list is `CLAIMS.md`; three further studies have reported and are in review, and none of their
numbers appear here. Rates carry the 95% problem-cluster percentile bootstrap as the primary
interval, with the Wilson interval beside it where the source report gives one; problems recur
across generation batches, so an interval that treats instances as independent is too narrow.

## 1. Reading again saturates below complete

The shipped cross-vendor auditor reads an increment holistically and returns findings; an
increment is blocked if any finding is graded BLOCKER. Over eight independent readings of the
same 110 defective instances, union recall rises from 10.7% at one reading to **30.0%** [20.0,
40.7] at eight, and the eighth reading adds 1.9 points. The constrained fit puts the asymptote at
31.5%, but the preregistered flattening bar was not met, so **that asymptote is an extrapolation
and the raw union at eight readings is the number to quote**. Pooling twenty readings across three
auditor families reaches **48.2%** [36.7, 60.0].

The price is measured on the same footing. Union false positives on 150 correct increments reach
**16.0%** [10.1, 22.3] at eight readings, and the recall bought per point of false positive falls
monotonically as readings accumulate.

## 2. The auditor and its instructions move the ceiling; repetition does not

Two interventions were compared against that baseline on the same frozen instances.

Replacing the auditor with a stronger model of the generator's own vendor moved union recall at
eight readings by **−26.4 points**, cluster [−37.3, −15.6] — three instances flagged only by the
new family, thirty-two only by the shipped auditor, exact McNemar p = 4.2 × 10⁻⁷. This was a
preregistered primary, and its direction is the one worth stating plainly: a stronger model is not
a better auditor.

Adding a single rule to the auditor's constitution — *find what the visible tests do not cover* —
moved flags on the defect population by **+26.8 points**, cluster [13.6, 40.4], McNemar p =
0.0003. This is the largest effect measured anywhere in the programme, and it is **exploratory**:
the preregistration named outcome contrasts, not this one, and the label travels with the number.

A same-vendor auditor was worse than the cross-vendor one on these instances by **12.7 points**
[25.0, 0.9] of union recall at eight readings. A later study on a second substrate reverses that
sign, so this is reported as a measurement on this substrate rather than as a property of
same-vendor auditing.

## 3. Most of what the auditor missed is failure the specification never determined

Fifty-seven of the 110 defective instances were flagged by no reading of any family. The first
classification of that residual, made under a rule that asked whether the visible tests exercised
the failing input before asking anything else, called 46 of 57 unexercised edges, and the paper's
earlier draft rested a claim on that.

Re-rating the same instances under a rule that asks first whether the specification's prose
determines the hidden suite's expected value reverses it: two raters agree that **44 of 57**
(77.2%, cluster [62.1, 91.1]) are cases where the prose does not settle the value, and **2 of 57**
are cases where it does and the visible tests merely never built the input. The preregistered
condition for withdrawing "the residual is mostly unexercised edge" fires on both of its clauses,
and the claim is withdrawn.

A classification that reverses when the order of its questions changes is not, by itself, a fact
about the auditor, and we do not present it as one. Two things support the second reading. It was
fixed before any label was written, and its labels were committed before we looked for outside
evidence. And where an outside party had independently recorded that one of these specifications
is defective — twelve MBPP tasks named in a paper written for another purpose — our raters agree
on **9 of the 11** that fall inside our defect population, with both disagreements on the boundary
that paper's own "incomplete" category draws. That check is one-sided by construction: it can
support agreement where an outsider looked, and can bound nothing about the rate.

## 4. What follows for a recall number

Taken together, the results above say that an audit recall figure is not a property of an auditor
alone. It moves with which model reads, with what the rulebook tells it to look for, and with
whether the benchmark's hidden suite asks a question the specification answers. The studies now in
review test the last of these prospectively, measure the ceiling on a second substrate, and
adjudicate whether a flag is a naming; where they bear on the claims above, `CLAIMS.md` records
what they would change.
