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

## Under review, and already changing the claims above

These three have reported and are in independent review. None may enter the manuscript until a
review ends quotable, but two of them bear directly on claims C1 and C4 and are recorded here so
the ledger is not read as settled.

**Study 22 (injection).** On defects constructed so the specification determines them, the same
auditor at the same eight readings catches 90 of 92, against 33 of 110 on the natural residual;
against each instance's own unmodified twin, 90 of 92 against 11 of 92. One reading catches
94.4%. If this survives review, **C4 gains its prospective test** and the paper may say the
measured ceiling is not a limit on detecting specification-determined defects. Its own limitation
is that the injected defects are detectably artificial (a preregistered probe separates them from
natural ones at 96.7%, chance excluded), so the gap cannot be attributed wholly to
specification-determinedness.

**Study 20 (the referent rule at K = 8, with texts).** The rule raises union recall from 33 of
110 to 67 of 110 (+30.9 points [19.1, 43.1]) — it moves the ceiling, not just one reading — but
false positives go from 16.0% to 36.7% and a single draw sits at 23.6% against the product's
6.7% bar, so it is not shippable as it stands. Its adjudication bears on **C1**: the shipped
auditor's flag rate is not a defect-naming rate. On one reading with texts kept it returned a
finding on 9 of 110 defect instances and asserted the actual defect on 5 to 7, depending on how
two raters who agreed only at κ = 0.391 are combined.

**Study 23 (a second substrate).** On BigCodeBench's standard-library half — median specification
118 words against 41, median solution 41 lines against 6 — the same auditor reaches 71 of 100 at
eight readings, against 30.0% on substrate 1. **This obliges a change to C1 whatever the review
says about the details: 30.0% is not a general figure.** But the auditor is not better there. Its
recall per false-positive point is lower at every K (1.55 down to 1.28, against 2.37 down to
1.88), and its single-reading false-positive rate on substrate 2, 31.8%, already exceeds its
eight-reading rate on substrate 1, 16.0% — so the two substrates cannot be compared at a matched
false-positive rate anywhere in the measured range. The claim the paper can carry is that **the
measured ceiling is an operating point, not a constant, and a union-recall figure quoted without
its false-positive rate is not portable.**

**Study 23's same-vendor arm, added after the first analysis.** At eight readings the same-vendor
auditor beats the cross-vendor one on the second substrate by +17.0 points [2.0, 32.0] of recall —
**the opposite sign to substrate 1's −12.7 [−25.0, −0.9]** — while costing +22.0 points [11.2,
32.7] of false positives, that is 1.29 points of false positive per point of recall. Its verdict
is identical across all eight readings on every one of 250 instances (verified independently:
costs vary on 100, wall times on all 250, so the readings are distinct), so its union curve is
flat and the registered efficiency ratio is undefined rather than large. The same model splits on
9 of 260 verdicts on substrate 1, so this is an operating-point effect, not determinism. Two
consequences for the ledger: **C5's direction is substrate-dependent and must be stated as a
measurement on substrate 1, not as a general property**, and the paper gains a claim it did not
have — repeated reading buys coverage only in proportion to how much of the population sits near
the auditor's decision boundary.

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
