# The claims ledger

Every sentence the paper is allowed to assert, the evidence for it, and the label it must
carry. A claim enters this file only when its report has passed an independent cross-vendor
review that ended "quotable" and has been merged. Nothing here may be restated without its
interval; nothing labelled post hoc or exploratory may be restated without that word.

The interval convention throughout: a rate carries the 95% problem-cluster percentile
bootstrap as its primary interval, with the Wilson interval beside it where the report gives
one; Wilson ignores the clustering that arises because most problems contribute two instances.

## Admitted claims

**C1 — Returns to repeated independent reading diminish well short of complete.** The shipped
cross-vendor auditor's union recall on the defect population rises from 10.7% at one reading
to **30.0%** [20.0, 40.7] at eight, at **16.0%** [10.1, 22.3] on correct code. The last-step
gain is **1.93 points, cluster [1.14, 2.78], against the preregistered flattening bar of 1.0**,
so **the bar was not met**: the constrained fit's 31.5% asymptote is an extrapolation, the raw
union at K = 8 is the number to quote, and **the word "saturates" may not be used of this
curve**. What is licensed is diminishing returns at the budget reached. The bar is also a
function of where a family was stopped, so a curve meeting it at K_max = 4 makes a weaker
statement than one meeting it at K_max = 8, and that must be said wherever families run to
different K are compared. Pooling twenty draws across all three auditor families reaches
**48.2%** [36.7, 60.0]. Evidence: ceiling 1 (`RESULTS-CEILING.md`, quotable at review round 21).

**C2 — Which auditor model reads moves union recall more than how many times it reads, at a
severity threshold and a sampling configuration that are not matched across families.**
Replacing the auditor with a stronger same-vendor model moves union recall at K = 8 by
**−26.4 points**, cluster [−37.3, −15.6] (4 of 110 against 33 of 110; 3 instances flagged by the
new family only, 32 by the shipped auditor only; exact McNemar p = 4.2 × 10⁻⁷, cluster sign-flip
p = 2.0 × 10⁻⁵). This is a preregistered primary, and **it may not be restated as "a stronger
model is a worse auditor"**. Three qualifications travel with it and none may be dropped:

* **Unmatched operating point.** The stronger model flags correct code at **3.3%** [0.7, 6.7]
  against the shipped auditor's **16.0%** [10.1, 22.3]. The recall figure may never appear
  without it.
* **The sign reverses under a weaker severity rule.** Under the any-finding rule (EXPLORATORY,
  not preregistered) the stronger model reaches **59.1%** [47.3, 70.6] on P at **34.0%**
  [26.5, 41.7] on C, against the shipped auditor's **34.5%** [23.6, 45.5] at **19.3%**
  [12.8, 26.3]; the ratio of those rates is 1.74 against 1.79, a derived point ratio
  carrying no interval and therefore supporting no claim that the families differ on it. The
  contrast is evidence about **severity calibration**, not auditing ability.
* **The routes are not sampled alike.** The cross-vendor route sends no sampling parameter; the
  same-vendor routes send temperature 0 and are near-deterministic. Over K = 1 to 8 the first
  gains 19.3 points of union and the second gains 3.0. **At K = 1 the gap is −10.1, not −26.4.**
  Every cross-family union-of-K contrast in this programme inherits this confound and must
  disclose it.

A counterexample must be reported beside C2: `astra` (gpt-6-astra, high reasoning) reaches
**32.7%** [20.7, 45.0] union recall at K = 4 at **10.7%** [5.9, 16.1] false positives,
dominating the shipped auditor on both axes at half the readings. Evidence: study 18
(`RESULTS-CEILING3.md`, quotable at round 7, merged), Tables 1, 2 and 4.

**C3 — What the auditor is told to look for moves what it writes down, on a small arm, at a
cost, and without a measured effect on outcomes.** One added rule — find what the visible tests
do not cover — moved flags on the defect population from **10 of 56 to 25 of 56**: **+26.8
points**, cluster [13.6, 40.4], exact McNemar p = 0.0003, cluster sign-flip p = 0.0009. With the
pooled P + C flag contrast it is one of only two comparisons clearing the Bonferroni threshold of
0.00313 over the sixteen computed, and the two are the same effect seen twice.

**Exploratory**: the preregistration named outcome contrasts, not flag contrasts, and the label
travels with the number wherever it appears. Three further restrictions travel with it:

* **The estimand is not the one C1 and C2 use.** It is **56 instances from 41 problems**, not the
  110-instance defect population; it counts **flags**, not union recall against the hidden suite;
  and it is **one reading**, because every loop arm revises once, not a union over eight.
  **+26.8 may therefore not be compared in magnitude with −26.4 or +19.3**, and the phrase "the
  largest effect we measure" is withdrawn.
* **It has a false-positive cost.** The same rule moved flags on correct code by **+12.50 points**
  [5.17, 21.82]. The recall-side figure may not appear without it.
* **It did not measurably move outcomes.** On the contrast that isolates the rule —
  referent-loop against cross-loop on hidden-suite pass after one revision — the effect is
  **+5.36 points, cluster [−0.89, +12.07], p = 0.146**, which does not exclude zero. Since this
  programme's own position is that a flag is not a catch, this sentence must accompany C3.

Evidence: ceiling 2 (`RESULTS-CEILING.md`).

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
  author. Study 22 was built to test it prospectively and **failed to**: its construction never
  enforced specification-determinedness (Amendment 7), so no prospective test exists. The split
  may be described only as a post-hoc observation, with its label, until one does.
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

**Study 22 (injection).** On defects constructed so the specification determines them, admitted
by six mechanical filters and then put to two models that are not the auditor, the same auditor at
the same eight readings reaches **84.2% [73.8, 93.1]** stratified over all 281 filter-accepted
instances, against 33 of 110 on the natural residual. **The headline is the stratified figure, not
the 90 of 92 on the gate-accepted population.** Amendment 6 preregistered an audit of 40 of the
189 filter-accepted instances the gate refused and found them audited at **77.5% [62.2, 90.5]**,
materially below the accepted population's 97.8%; under the amendment's stated reading rule that
makes the gate part of the effect, so 97.8% is a property of the gate-accepted population and may
not be quoted as a figure for specification-determined defects at large. The gate inflates the
contrast by about 14 points and does not create it. Two limitations stand: the construction still
conditions on the six filters, and the injected defects are detectably artificial (a preregistered
probe separates them from natural ones at 96.7% [92.5, 98.6], chance excluded), so the gap cannot
be attributed wholly to specification-determinedness. Amendment 6 also **withdraws Amendment 5's
claim** that the paired twin contrast isolates the injected defect "and nothing else": it isolates
the **edit**, which carries both the specification violation and the salience the probe measures.
If this survives review, **C4 gains its prospective test**.

**Study 20 (the referent rule at K = 8, with texts).** The rule raises union recall from 33 of
110 to 67 of 110 (+30.9 points [19.1, 43.1]) — it moves the ceiling, not just one reading — but
false positives go from 16.0% to 36.7% and a single draw sits at 23.6% against the product's
6.7% bar, so it is not shippable as it stands. Its adjudication bears on **C1**: the shipped
auditor's flag rate is not a defect-naming rate. On one reading with texts kept it returned a
finding on 9 of 110 defect instances and asserted the actual defect on 5 to 7, depending on how
two raters who agreed only at κ = 0.391 are combined.

**Study 23, re-run complete 2026-09-17.** The voided run's defect — visible-test text that
did not parse, shown to both the auditor and the generator on all 300 tasks — was corrected and
the study re-run in full. **Correcting that one input reversed six of the voided run's
conclusions, every one in the direction of that run having overstated**: the two cross-vendor
false-positive intervals go from disjoint by 2.6 points to **overlapping by 3.5**, so
"no reading count gives a matched rate across the substrates" is withdrawn; the same-vendor arm
goes from splitting on 0 of 250 draws to **12 of 249**, so "identical verdict everywhere" is
withdrawn; the registered gain ratio goes from 1.16 → 0.91 to **1.35 → 1.23**, staying above 1
throughout; the flattening bar goes from met at 0.62 points to **missed at 1.52**, so the one
curve in this programme that appeared to saturate does not; H23d goes from +17.0 [2.0, 32.0] to
**+4.0 [−10.1, 18.2]**, which spans zero, so the claimed sign reversal against substrate 1 is
withdrawn; and the same-vendor gain ratio goes from **undefined** — the voided arm never split,
so the denominator was exactly zero and an absence of data was reported as a property of the
auditor — to computable at 0.32 → 0.25.

The two runs are reported side by side as descriptive and post hoc under Amendment 2: one run
against one run, no interval and no p value on any difference between them, not an estimate of
what unparseable tests do to an auditor, and **not used to validate the voided run**, whose
defect was independent of where the numbers landed. Spend $37.16 of a $45 halt.
**None of this enters the paper until the study passes cross-vendor review.**

**Study 23's same-vendor arm, added after the first analysis.** At eight readings the same-vendor
auditor beats the cross-vendor one on the second substrate by +17.0 points [2.0, 32.0] of recall —
**the opposite sign to substrate 1's −12.7 [−25.0, −0.9]** — while costing +22.0 points [11.2,
32.7] of false positives, that is 1.29 points of false positive per point of recall. Its verdict
is identical across all eight readings on every one of 250 instances (verified independently:
costs vary on 100, wall times on all 250, so the readings are distinct), so its union curve is
flat and the registered efficiency ratio is undefined rather than large. The cross-vendor arm on the same substrate splits on 103 of 250 and the
same-vendor arm on none; an operating-point explanation and a temperature-0 explanation are not
separable without a temperature-matched replication, which was not run. (An earlier version of
this entry cited "9 of 260 verdicts on substrate 1" as evidence against determinism. That figure
traces to no record and has been removed.) Two
consequences for the ledger: **C5's direction is substrate-dependent and must be stated as a
measurement on substrate 1, not as a general property**, and the paper gains a claim it did not
have — repeated reading buys coverage only in proportion to how much of the population sits near
the auditor's decision boundary.

## First cross-vendor reviews, 2026-09-15: all five studies came back NOT QUOTABLE

Studies 22, 23, 20, 19 and 17 were all reviewed on the day the allowance returned. **None was
approved.** Two of the five were refused for a defect introduced by a previous round's *repair*
— study 19's rename was left half done, and study 17's replacement wording claimed the tests
establish a reconstruction they never perform — which is worth recording as a pattern: a fix
written to satisfy a reviewer is itself an unreviewed claim.

Study 17 is fixed (round 9's findings applied and its recommendation to stop hardening the
rendered Markdown accepted). Study 19 is fixed (Amendment 4). Study 20 is fixed (Amendment 2),
including a **permanent provenance loss** recorded rather than repaired: its L2 adjudication
artefacts lived only in the session scratchpad and were destroyed between the review that flagged
them and the fix. Study 22 is **withdrawn** (Amendment 7). Study 23 needs a re-run (Amendment 1)
and its budget is costed at `codex-review-queue/SUBSTRATE2-RERUN-BUDGET.md`, awaiting a decision.

**No admitted claim (C1 to C5) depends on any of these five studies**, which is why five
refusals in one day force no retraction. The paper's Results sections on repeated reading, the
auditor, the rulebook and the residual rest on ceiling 1, study 18 and study 21, all of which
passed review before they entered. Study 19's defect was a half-finished rename and is fixed (Amendment 4). Study 23's
run is void and must be re-run (Amendment 1). Studies 22 and 20 need their headline claims
restated, and study 22 has no usable headline figure at present.

**Study 20, corrected (Amendment 2, 2026-09-16).** The review refuses the headline for turning
higher eight-reading *flag coverage* into an established higher *ceiling*. H20a establishes higher union BLOCKER coverage at K = 8;
H20b establishes a positive difference between fitted asymptotes conditional on that model.
Neither resolves the true saturation difference, since the cross arm has not flattened and
heterogeneous low-probability detection can imitate a ceiling over eight readings. It also shows
the kill fires for a more basic reason than rater disagreement: only nine P instances received any
finding at all, so the largest possible defect-asserting count is nine, already below the floor of
twenty. The paper's statement of this result was corrected on 2026-09-12 and is consistent with the
review; the study report is not yet.



Both were reviewed twice (a dispatcher bug re-ran each; the second reviews are independent and
were kept). All four reports refuse quotation.

**Study 23.** Confirmed independently by re-running the extraction: the visible-test files shown to
the auditor are sliced out of their enclosing class without the `class` header, so **all 300 of 300
fail to parse**, while scoring executes the intact class. The auditor was shown syntactically
invalid Python on every task of this substrate, which can raise both recall and false positives and
therefore confounds H23a and H23c together. Separately, no arm in these records separates the
temperature-0 explanation of the flat curve from the operating-point one, so "operating point" may
describe the observed recall/false-positive pair but may not be offered as an explanation.

**Study 22, withdrawn entirely (Amendment 7, 2026-09-16).** The reviews reject the
post-Amendment-6 headline because stratifying over all filter-accepted instances **removes the only
semantic gate**, so 84.2%'s denominator is not "defects the specification determines". Checking
that, we found the deeper fault: **F6 was implemented as `bool(obj.get("witness_input"))`** while
this study registered it as recovering each edit's first failing hidden input by study 21's witness
path. No filter connects the quoted text, the named class, the witness and the actual failure, so
**no filter establishes specification entailment**, and the population is "small injected edits
that survive a sparse visible suite and fail a hidden one". Seven archived instances even carry a
comment naming the bug — one reads `DEFECT: should be +` and both gates accepted it — though only
one reached population I and removing it leaves 89 of 91, still 97.8%, so self-announcement does
not explain the effect; it shows nothing was looking for conspicuousness, which the 96.7% probe
then measured. **C4 does not gain a prospective test from this work**, and the residual
classification stays post hoc. Every injection number is out of the paper and Figure 3 is
withdrawn with its files deleted.

**Consequence for the manuscript, carried out 2026-09-15.** Every substrate-2 number is removed
from the paper. Its results subsection now reports the defect instead of the numbers; both
cautions in the discussion are restated without it, the first as a methodological point and the
second on the sampling asymmetry our own records do establish; Figure 1 is regenerated without its
substrate-2 series; and **Figure 2, which was entirely the two substrates' operating-point
comparison, is withdrawn and its files deleted** so nothing can plot void data. The injection
numbers stay in the *in review* section pending the re-analysis its reviews require. The hard
blocker below stands.

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

**This rule was broken, and the record says so rather than being amended to fit.** A peer review
of the manuscript on 2026-09-12 found that studies 17, 20, 22 and 23 were quoted throughout the
introduction, discussion and both figures, while the Results section stated in its own opening
paragraph that no numbers from studies in review appeared, and the abstract stated that every
report had been cross-vendor reviewed. Both statements were false. The introduction and discussion
had been written before the gate was enforced and the disclaimer was never reconciled with them.

The repair is not to weaken the rule. It is:

1. Every number from a study still in review is confined to one clearly labelled section of the
   manuscript, carries the words *in review* at each occurrence, and is load-bearing for no
   admitted claim.
2. The two false sentences are replaced by an accurate statement of what has and has not been
   reviewed: three studies completed, four in review.
3. **The manuscript does not go to a preprint server or a venue until each of those four reviews
   has ended in approval or its numbers have been removed from the manuscript.** This is a hard
   blocker, recorded here so that shipping the paper requires either the reviews or the deletions,
   and not a judgement call at submission time.

The rule as stated above remains the rule for admitted claims.
