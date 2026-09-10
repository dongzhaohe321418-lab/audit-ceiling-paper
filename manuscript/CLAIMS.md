# The claims ledger

Every sentence the paper is allowed to assert, the evidence for it, and the label it must
carry. A claim enters this file only when its report has passed an independent cross-vendor
review that ended "quotable" and has been merged. Nothing here may be restated without its
interval; nothing labelled post hoc or exploratory may be restated without that word.

The interval convention throughout: a rate carries the 95% problem-cluster percentile
bootstrap as its primary interval, with the Wilson interval beside it where the report gives
one; Wilson ignores the clustering that arises because most problems contribute two instances.

## Admitted claims

**C1 — Repeated independent reading saturates well below complete.** The shipped
cross-vendor auditor's union recall on the defect population rises from 10.7% at one reading
to **30.0%** [20.0, 40.7] at eight, with a last-step gain of 1.9 points; the constrained fit
puts the asymptote at 31.5% but the preregistered flattening bar was not met, so **the fitted
asymptote is an extrapolation and the raw union at K = 8 is the number to quote**. Pooling
twenty draws across all three auditor families reaches **48.2%** [36.7, 60.0]. Evidence:
ceiling 1 (`RESULTS-CEILING.md`, quotable at review round 21).

**C2 — Which auditor model reads matters more than how many times it reads.** Replacing the
auditor with a stronger same-vendor model moves union recall at K = 8 by **−26.4 points**,
cluster [−37.3, −15.6] (3 instances flagged by the new family only, 32 by the shipped auditor
only; exact McNemar p = 4.2 × 10⁻⁷). This is a preregistered primary. Evidence: study 18
(`RESULTS-CEILING3.md`, quotable at round 7, merged).

**C3 — What the auditor is told to look for is the largest single lever measured.** One added
rule — find what the visible tests do not cover — moved flags on the defect population by
**+26.8 points**, cluster [13.6, 40.4], McNemar p = 0.0003. **Exploratory**: the
preregistration named outcome contrasts, not this one, and the label travels with the number
wherever it appears. Evidence: ceiling 2 (`RESULTS-CEILING.md`).

**C4 — The residual is dominated by failures the specification does not determine, and the
earlier characterisation of it does not survive a change of rubric.** Under a rubric that asks
whether the prose entails the hidden suite's expected value *before* asking whether the visible
tests exercised the input, two raters agree that **44 of 57** residual instances (77.2%,
cluster [62.1, 91.1]; Wilson [64.8, 86.2]) are oracle-defined and **2 of 57** are
specification-determined but unexercised — reversing the same instances' earlier
classification, which called 46 of 57 unexercised edges. The preregistered kill for "the
residual is mostly unexercised edge" fires on both of its conditions. What survives both
rubrics is only the size of the residual and the fact that under the second rubric most of it
fails the entailment test. Evidence: study 21 (`RESULTS-RERATE.md`, quotable at round 3,
merged).

**C5 — A same-vendor auditor is worse than a cross-vendor one on the same instances.** Raw
union difference at K = 8 on the defect population: **−12.7 points** [−25.0, −0.9]. Evidence:
ceiling 1.

**C6 — The false-positive price of reading eight times.** Union false positives on the clean
population rise to **16.0%** [10.1, 22.3] at K = 8 for the cross-vendor auditor; the recall
bought per false-positive point is 1.68. Evidence: ceiling 1.

## Claims the evidence does not support, and which must not appear

* *"The ceiling is set by unexercised edges."* Withdrawn by C4. The paper's earlier claim (2)
  is retracted in the text, not silently dropped.
* *"The ceiling is set by oracle-defined failures."* Not yet. The split behind it — the union
  of twenty draws catching 23 of 25 specification-determined defects and 24 of 68
  oracle-defined ones — is **post hoc**, on one substrate, from two raters one of whom is the
  author. Study 22 tests it prospectively on a constructed population; until that reports, the
  split may be described only as a post-hoc observation with its label.
* *"CrossAudit finds most defects."* No configuration measured here exceeds 48.2% union recall,
  and that figure pools twenty readings across three families.
* *"The auditor cannot see these defects."* The naming and recognition adjudications measure
  what a finding says, not what a model could see; the distinction is stated wherever those
  rates appear.
* Any asymptote quoted without the word extrapolation where the flattening bar was not met.

## Pending — reported here only when their reviews end quotable

| study | claim it would license | state |
|---|---|---|
| 19 (ceiling 3b) | a changed rulebook moves a second vendor's family as it moved the shipped auditor | review round 4 in flight |
| 17 (testgen validation) | corroboration across independent generations does not reach the preregistered threshold for validating generated tests | review round 3 in flight |
| 20 (ceiling 4) | the rulebook effect and the auditor axis at K = 8 with texts archived | run halted: the OpenAI account has no credit |
| 22 (injection) | the prospective test of C4's post-hoc split | population constructed; audit held on the same credit |

## Rule

A number that has not been through an independent review that ended quotable does not enter
the manuscript, even as a placeholder with a caveat. The pending table is the only place such
a result may be named, and only by what it would license.
