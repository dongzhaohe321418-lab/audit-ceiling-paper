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
* **It has a false-positive cost, and the cost's interval contains zero.** The same rule moved
  flags on correct code by **+12.50 points**. Every discordant pair points one way (7 against 0),
  so the percentile bootstrap's bound at zero is an artefact of the method; the admissible exact
  unconditional interval is **[−3.6, +26.8]**, and the exact McNemar p is 0.0156 against this
  study's Bonferroni threshold of 0.003125. **This entry previously quoted [5.17, 21.82]**, the
  interval the programme's own rule forbids for a one-signed discordance. The recall-side figure
  may not appear without the cost, and the cost may not be quoted as excluding zero.
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

*Added 2026-09-18, after that review and therefore NOT quotable:* study 21's record now also
carries the contrast C4's two shares invite — residual 44 of 57 (77.2%) against flagged 24 of 53
(45.3%), a difference of **+31.9 points** [9.6, 53.4] (`RESULTS-RERATE.md`, Table 6). Amendment 1
registered that both shares would be reported; it did not register their difference, so the
contrast is post hoc. Round 3 reviewed the study without it. It may not enter the manuscript, and
C4 above stands on the share it already quotes, not on the difference. Recorded here because a
new number in a merged study's record is exactly the path by which an unreviewed figure reaches
the paper. Note also that comparing the 68-instance sheet with the flagged sheet yields +22.4
points and is wrong: that sheet is 57 residual plus 11 flagged instances, so it contains part of
the group it is compared with.

**C5 — At K = 8 the same-vendor route's union recall is lower than the cross-vendor route's on
the same instances.** Raw union difference on the defect population: **−12.7 points**
[−25.0, −0.9]. *Retitled 2026-09-23: it said the same-vendor auditor "is worse", which is the
auditing-ability reading C2 forbids; the interval is unadjusted with its upper end 0.9 points
from zero (R2-M4), and the route is sent temperature 0, so this is a direction under that
sampling, not a ranking.* Evidence: ceiling 1.

**C8 — The referent rule moves a second vendor's family as it moved the shipped auditor, and
the grading rule does not.** On `self-strong` (Sonnet 4.6) at four readings, the referent rule
raises BLOCKER union recall by **+20.9 points**, problem-cluster [+10.8, +31.8], at a
false-positive cost on C of **+8.0 points** [+3.4, +12.7]. The grading rule shows **no
demonstrated recall improvement**: +0.9 points [−1.8, +4.5], and H19a fails its registered
criterion, which demonstrates neither equivalence nor that the grading rule did nothing.
This is C3's effect reproduced on a different vendor's model, at a different K, with its own
false-positive price. Evidence: study 19 (`RESULTS-CEILING3B.md`, quotable at review round 10,
2026-09-20).

**What C8 does not license.** The post-hoc Table 5b quantity — whether a finding **reports a
failure** on the named class — is broader than asserting a defect: its prompt admits a finding
even where it grades the class non-blocking or says the specification is silent, so findings that
disclaim the requirement are counted in. It is **3 of 110** under the shipped constitution and
**27 of 110** under the referent rule, and **may not be quoted as defect recognition**. Seven
review rounds passed over the opposite error — the report called the instrument *narrower* than
defect assertion, the flattering direction — before round 9 caught it.

**C9 — The referent rule raises union recall at K = 8; whether it raises the ceiling is
not established.** On the defect population the rule takes union recall from 33 of 110 to
**67 of 110**: **+30.9 points**, problem-cluster [19.1, 43.1], discordance 38 against 4. The
false-positive price is **+20.7 points** [12.8, 28.8], and its single-draw rate of 23.6%
[17.1, 30.3] fails the product bar on all eight draws. Under the ZIBB secondary the residual
falls 56 to 32, 23 of the 24 leaving being unexercised edges. Evidence: study 20
(`RESULTS-CEILING4.md`, quotable at review round 4, 2026-09-20).

**Three limits are part of the claim, not caveats on it.** H20b's fitted-asymptote difference of
+27.1 points [10.9, 39.0] does **not** establish a higher ceiling: the `cross` arm never
flattened, so one of its two terms is an extrapolation; heterogeneous low-probability detection
imitates a ceiling at this budget, since an instance found with probability 0.02 per reading
survives eight readings about 85% of the time; and this study's own ZIBB estimator finds no
never-detectable class in **either** arm, a boundary estimate that settles little given its
interval. **Its adjudication kill is arithmetic, not a labelling artefact**: only 9 of 110
instances drew any finding on `cross-T`, so the largest defect-asserting count available under
perfect adjudication was 9, below the floor of 20.

**Every adjudication-derived figure here is conditional on surviving labels.** L2's raw reply,
prompt, launcher and execution log lived only in a session scratchpad and were destroyed between
the review that flagged them and the repair. The labels survive and every number reproduces from
them; how L2 produced them cannot be audited. Round 4 permits qualified quotation on that basis
and forbids setting these figures directly against the eight-reading union of 30.0%.

**C10 — An injected-defect population does not give claim C4 a prospective test, and the
attempt says why.** Study 22 built a population where "specification-determined" was to be fixed
by construction, and **the construction does not deliver that property**: F6 was registered as
recovering the first failing hidden input and is a truthiness check on `witness_input`, and F2 to
F5 each accept cases their registered wording excludes. **No filter establishes specification
entailment, and no repair of F6 alone would have** — recovering the input and executing a witness
shows the edit changes behaviour on an exercised input, not that the specification entails the
value expected there. Both headline figures are withdrawn. **C4 keeps exactly the status study 21
gave it, post hoc and unreplicated.** Evidence: study 22 (`RESULTS-INJECT.md`, *final in its
descriptive form* at review round 9, 2026-09-21).

**What may be quoted from it is descriptive and nothing more.** At eight readings the auditor
blocked **90 of 92** filter-and-gate-accepted injected instances against **11 of their 92
unmodified twins** (79 discordant pairs one way, none the other) and against **33 of 110** on the
natural residual; the gate-rejected sample was blocked **31 of 40**, which is why the gate's
conservativeness argument is withdrawn — gate acceptance is associated with detectability. A
probe separates the injected set from the natural one at 96.7% on the items it answered, **by a
feature it does not identify**: its two arms share no problem, so task composition alone could
produce the result, and its model is one of the two gate models.

**A successor needs more than independence.** An independent party must validate the actual
violation **and** the specification-entailing expected behaviour, under a fixed, blinded
protocol. A second substrate alone does not do it and an independent rater alone does not do it,
because task composition and construction confounding survive both. That is a condition on a
future study, not unfinished work here: the naming adjudication and the deferred OpenAI gate are
**final omissions**.

**C7 — Corroboration across independent generations does not validate a generated test.**
A wrong generated test — one that fails on the dataset's canonical solution — is not reliably
recognised by asking whether further independent generation draws also fail on the same
candidate. On this frozen substrate neither paid rule reached the preregistered validation
threshold: the retained wrong-test rates are **12.2%** (Wilson 7.0–20.6; cluster 3.6–22.6) for
majority-over-draws and **14.9%** for any-draw, against a preregistered limit of **2%**, and
each retained 5 and 6 of the 7 validated-only P instances against a floor of 5 of 7. **H17 is
killed on the rate**, and the paid rules do not beat the free within-draw comparator, which
retains wrong tests at 12.8%. A 2.4% floor on the brief's original unique-test quantity holds
because 29 of the 45 wrong tests never fail on any candidate at all. Evidence: study 17
(`RESULTS-TESTGEN-VAL.md`, quotable at review round 11, 2026-09-20).

This claim is **negative and substrate-bound**: it says these rules do not validate generated
tests on this substrate, not that generated tests cannot be validated. Rounds 3 to 10 of its
review were about the reporting medium rather than the measurement, and every figure has
reproduced unchanged since round 1.

**C6 — The false-positive price of reading eight times.** Union false positives on the clean
population rise to **16.0%** [10.1, 22.3] at K = 8 for the cross-vendor auditor; the recall
bought per false-positive point is 1.68. Evidence: ceiling 1.

**C11 — Measured union recall is rule-dependent, and C2's magnitude belongs to C2's rule.**
The severity sweep re-grades findings already archived by ceiling 1 and study 18 under four
decision rules, with **no model calls**. C2's -26.4 points is specific to its **preregistered**
flag, "≥ 1 BLOCKER finding" — ceiling 1's registration fixes it and study 18 inherits it — and
**exploratory re-grading under any-finding grading reverses the sign.** That is a mechanical
consequence of changing the counting rule. **It does not identify why the families produced
different findings or different severities**, and it does not show that any auditor recognised
any defect. Evidence: P2 (`RESULTS-SWEEP.md`, *quotable* at review round 7, 2026-09-22).

**What may be quoted, at the stated depth and not otherwise.** At the common depth K = 4,
`astra` exceeds `cross` on union recall over stratum P by **+11.5 points** [+2.9, +21.3],
`cross` averaged over all C(8,4) = 70 four-draw subsets and `astra`, which has exactly four
readings, a single realisation (an earlier version said 70 on each side), paired over the same
instances and clustered by problem; the paired false-positive difference is **-0.3 points** [-3.8, +3.4]. On
`cross`'s complete eight-draw ladder the same contrast is **+2.7 points** [-6.5, +13.0] with a
false-positive difference of **-5.3 points** [-10.3, -0.7] — **the complete-ladder comparison
points toward lower false positives, not higher recall** — an unadjusted interval whose upper
end is 0.7 points from zero, so a direction and not an established finding (R2-M4). The observed false-positive rates at
K = 4 are similar (10.7% [5.9, 16.0] against 10.9% [6.9, 15.4]); **that is an observation about
two rates and not a matched operating point**, and the contrast leaves their difference
unresolved. `self-strong` has no point between 3.3% and 34.0% false positives — exactly where a
matched comparison would sit — so **that family is bracketed, not measured.**

**Three limits are part of the claim.** Re-grading is not re-asking: it shows where existing
findings fall under a different cut, not how an auditor would behave under different severity
instructions. Flag coverage is not naming: nothing here assesses finding content against the
hidden failure. And the sampling asymmetry travels with every cross-family row — the cross-vendor
route is sent no sampling parameter while the same-vendor routes are sent temperature 0.


**C12 — The missed-against-caught ambiguity gap survives a rater who is not the author, on a
control arm that can be answered — and the instrument that shows it disagrees with itself.**
P1's third rating had `gpt-5.6-luna` re-rate all 121 entries of the study 21 sheet after it was
rebuilt on mechanically recovered witnesses, because its control arm had been unanswerable: 42
of 53 caught entries carried no failing input class and all 42 drew `cannot-tell`. Evidence: P1
(`RESULTS-RATE3.md`, *quotable* at review round 6, 2026-09-22).

**What may be quoted, with its scope.** On the sheet's two groups — the reading the method
registered in P3's Amendment 1 — the share labelled `undetermined` is **43/68 = 63.2% against
23/53 = 43.4%, +19.8 points** [+1.2, +38.1]. **Those two groups are not two populations, and the overlap is definitional rather than clerical**: they use different definitions of "caught". The 68-entry group is ceiling 1's residual — 57 instances no family flagged, plus 11 flagged only by the third family — while the 53-entry group is what *some draw of any family* flagged, so those 11 are where the two definitions disagree. Removing their missed-group copies — **post hoc**, registered nowhere — gives **38/57 against 23/53, +23.3 points** [+2.0, +43.6]. The overlap *understated*
the contrast.

**Four limits are part of the claim, and the first is binding.** On the 11 instances carried in
both arms, with identical specification text and identical witness display, **the rater agreed
with itself on 7 of 11 on this binary outcome (6 problems), 5 of 11 on the full three-option
label (6 problems), and 5 of 7 among the abstention-free pairs (4 problems)** — where study 21's
two raters each agreed 11 of 11 on the same instances under a different instrument. Second,
every interval's lower end is within five points of zero. Third, **this is a model, not the human from outside the project that P1 exists to obtain**; `L1` — the author — rated all 121 entries, which prevents `L1` validating `L1` but does not make a fresh rater's judgement of the same material non-independent. Fourth, found by a conclusion-suppressed review after six briefed rounds had passed over it: **the sheet displays at most three failing inputs while 81 of the 121 entries have more recorded**, and eleven have none, so a label certifies what the prose determines *on the inputs shown* rather than across an instance's hidden failures.

**Not a claim, and recorded to stop it becoming one.** The same rater scored the *unrepaired*
sheet at +54.2 points [+38.5, +69.5], 2.7 times the repaired contrast and in the direction that
flatters C4, because its caught arm could not be answered. That comparison is **evidence about
sheets, not about specifications**, it does not isolate presentation from a fresh model run, and
the registered one-third `cannot-tell` gate fires on it — the broken arm was 79.2% — so it could
not have authorised proceeding under the positive branch.


**C13 — Adding a behavioural rule to the specification, with the code and visible tests held
fixed, raised jointly adjudicated diagnosis from none to nine of 32 selected instances; a
same-length placebo raised none. The additions that raised it were the ones the oracle agrees
with.** Evidence: P3 (`RESULTS-CLARIFY.md`, *quotable* at review round 3, 2026-09-23, reviewed at
`c63ac66`; residual corrections in harness `4fee74f`; κ regenerable from `records/clarify/agreement.json`).

**What may be quoted, with its scope** — the reviewer's reader sentence, not exceeded: on 32
selected instances across 19 problems, jointly adjudicated diagnosis rose from **0/32 to 9/32**
under the added specifications, versus **0/32** under placebo (**+28.1 points**, problem-cluster
bootstrap 95% interval **[+7.7, +51.4]**; cluster sign-flip **p = 0.0602**, exact enumeration
0.0625), **without establishing that specification underdetermination caused the original
misses.** The registered secondary (Amendment 2): **8/23 against 0/23, +34.8** [+10.0, +60.9].

**Five limits are part of the claim.** First, **the nine successes sit on five problems**; the
cluster test has five informative signs and is not significant at 0.05, though the registered
bootstrap criterion is met — both must be stated together. *Added 2026-09-23:* every discordant
pair points one way, so no bootstrap resample falls below zero and one misses all five
success-bearing problems with probability about 0.003; the criterion was close to guaranteed by
construction, and the exact cluster test (0.0625) is the informative figure. Second, **the clarifier saw failing
inputs without expected values, and its added rule contradicts the oracle entirely on 23 of 32
instances and partly on 2**; diagnosis was 6/6 where the addition agreed, 1/1 where it broadened
a precondition, 2/2 where it partly agreed, 0/23 where it contradicted. That split is
**measured, not assigned**, and it makes this a specification-edit contrast, not a manipulation
of ambiguity alone. Third, the manipulation check's clarified-against-placebo contrast is
**+18.8 [−9.4, +45.2] — unresolved here**, beside +28.1 [+2.6, +54.3] against the original.
Fourth, **`L1` is the author and `L2` is `gpt-6-astra`, the model that reviewed this study** — so the review checked labels its own model co-produced; κ = 0.85 on 84/91 measures agreement, not accuracy. Fifth, the
registered naming-rate secondary was never computed. **This does not license C4's causal reading
of "most" misses**, and the words "causes" or "explains" may not be used of it.

## Claims the evidence does not support, and which must not appear

* *"The ceiling is set by unexercised edges."* Withdrawn by C4. The paper's earlier claim (2)
  is retracted in the text, not silently dropped.
* *"The ceiling is set by oracle-defined failures."* Not yet. The split behind it — the union
  of twenty draws catching 23 of 25 specification-determined defects and 24 of 68
  oracle-defined ones — is **post hoc**, on one substrate, from two raters one of whom is the
  author. Study 22 was built to test it prospectively and **failed to**: its construction never
  enforced specification-determinedness (Amendment 7), so no prospective test exists. The split
  may be described only as a post-hoc observation, with its label, until one does.
* *"CrossAudit finds most defects."* The **shipped** configuration reaches 30.0% union recall at
  eight readings, and pooling twenty readings across three families reaches 48.2%. **This line
  previously said no configuration measured here exceeds 48.2%, and that was false.** Study 20
  measured `cross-R` — the same auditor under a constitution with one sentence added — at
  **67 of 110 = 60.9%** [48.6, 72.5] union BLOCKER recall at eight readings, on the same
  instances under the same rule, and its own report calls that column union recall. What it does
  not reach is a shippable operating point: it costs **36.7%** [28.5, 44.8] false positives on
  correct code against the shipped route's 16.0%. The honest statement is that no configuration
  measured here finds most defects **at a false-positive rate anyone would ship**, and the
  price, not the recall, is the reason.
* *"The auditor cannot see these defects."* The naming and recognition adjudications measure
  what a finding says, not what a model could see; the distinction is stated wherever those
  rates appear.
* Any asymptote quoted without the word extrapolation where the flattening bar was not met.
* *"The same-vendor contrast's direction is substrate-dependent."* Study 23 licenses nothing;
  its clean contrast was +6.9 [−4.9, +18.6]. (Review paper1 r1, finding 2.)
* *"`astra` beats both on recall and false positives."* It does not beat `self-strong` on false
  positives, and no paired contrast establishes both advantages over `cross` at once. (Finding 6.)
* *"No measurement moved on review."* The sweep's, P1's and P3's did. (Finding 5.)
* *"The stronger model writes down more of what is wrong"* or *"−26.4 is a fact about severity
  calibration."* The sweep shows rule-dependence, not cause or recognition. (Finding 4.)
* *"The clarification study is not conditioned on being missed."* Its population was selected
  for being missed. (Finding 3.)

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

**Study 23, third run complete 2026-09-19 — and it holds no quotable number.** Two runs were
voided for the same fault in different costumes: visible-test text shown to both the auditor and
the generator that did not parse on all 300 tasks, and then, from the repair for that, a hidden
method's decorators re-attached to the first visible method on 26 of 300. The third run passed
all three of Amendment 8's gates before a call was made, each proved able to fail first, and
both ladders are complete at 8 draws x 252 instances per family. Generation $1.907, audit
$27.659, total **$29.566** against a $45 cap; the study has now spent about **$82** across three
runs.

Amendment 8 fixed the criterion before the numbers existed: does a clean extraction reproduce
the six reversals the second run produced? **Five of the six did. One did not.**

| the reversal | run 1 (void) | run 2 (void) | run 3 | reproduced |
|---|---|---|---|---|
| the false-positive intervals | apart, gap 2.6 | overlap 3.5 | apart, gap 3.2 | **no** |
| the same-vendor arm splitting | 0 of 250 | 12 of 249 | 22 of 252 | yes |
| the gain ratio staying above 1 | 1.16 → 0.91 | 1.35 → 1.23 | 1.21 → 1.17 | yes |
| the flattening bar missed | 0.62, met | 1.52, missed | 1.47, missed | yes |
| H23d spanning zero | +17.0 [2.0, 32.0] | +4.0 [−10.1, 18.2] | +6.9 [−4.9, 18.6] | yes |
| the same-vendor gain ratio computable | undefined | 0.32 → 0.25 | 0.66 → 0.36 | yes |

Amendment 8 states its criterion over the set. Five of six is a case it did not anticipate, and
**the looser reading — judging each reversal on its own, which would license five findings — is
declined**: the five that reproduced are the ones favourable to this work, and adopting a reading
after seeing which way the numbers fell is the failure this study has already made three times.
The registered consequence therefore follows: **the study has consumed three runs and about $82
without a quotable number, and that is reported as found.** No fourth run is authorised and the
paper continues to carry no substrate-2 figure.

Run 3 is not void — its gates passed, its ladders are complete, its numbers are internally
consistent, and `RESULTS-SUBSTRATE2.md` reports them in full. What it lacks is the licence
Amendment 8 conditioned on reproducing the six, and the independent cross-vendor review every
number in this programme needs. Whether a 5-of-6 outcome should license the five is left to the
owner and to review, unresolved rather than settled in the direction that helps.

The item that did not reproduce is worth its own line, because it is the one the paper leaned on
hardest. The registered cross-vendor false-positive comparison has now been apart by 2.6 points,
overlapping by 3.5, and apart by 3.2 across three extractions of the same protocol. **It is
reported as unstable**, and "no reading count gives a matched rate across the substrates" is not
available in either direction.

**Study 23's same-vendor arm.** On the third run the same-vendor auditor's recall at eight
readings is 81.4% [71.0, 90.4] against the cross-vendor arm's 74.5% [63.8, 84.5] on the same 102
instances: **+6.9 points [−4.9, 18.6], which spans zero**, so no difference in recall is
established and **no sign reversal against substrate 1's −12.7 [−25.0, −0.9] is claimed**. Two
earlier entries claimed one, on +17.0 [2.0, 32.0] and then on +4.0 [−10.1, 18.2]; the first is
from a voided run and the second already spanned zero. On false positives the same-vendor arm
pays 66.0% [57.1, 74.5] against 53.3% [44.2, 62.3], **+12.7 points [1.4, 23.7]** — 1.85 points of
false positive per point of recall.

Its verdict is **not** identical across readings, which an earlier entry asserted: it splits on
22 of 252 instances against the cross-vendor arm's 102, so its union curve rises slightly and the
registered efficiency ratio is computable at 0.66 → 0.36 rather than undefined. An
operating-point explanation and a temperature-0 explanation are still not separable without a
temperature-matched replication, which was not run. (An earlier version of this entry cited
"9 of 260 verdicts on substrate 1" as evidence against determinism. That figure traces to no
record and has been removed.) **C5's direction is still to be stated as a measurement on
substrate 1 rather than a general property** — but on this substrate the contrast that would have
made it substrate-dependent includes zero, so the ledger gains nothing here, and the claim that
repeated reading buys coverage in proportion to how much of the population sits near the
auditor's decision boundary is not licensed by this study either.

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

## Second reviews, 2026-09-20: all four came back NOT QUOTABLE, three for the repair

Studies 17, 19, 20 and 22 were re-reviewed on the fixes made after 2026-09-15. **None was
approved, and in three of the four the reason was the repair rather than the measurement.** The
pattern this ledger recorded on 2026-09-15 — *a fix written to satisfy a reviewer is itself an
unreviewed claim* — held again, at a higher rate: it was two of five then, three of four now.

* **Study 19.** Amendment 4 finished the rename the previous round ordered and, regenerating,
  **deleted the whole `secondaries` block from numbers.json and Tables 6-7 from tables.md** while
  the report still spliced those tables. Its commit message said "regenerating numbers.json moves
  no value", which was true and not a description of the commit. The branch was pushed with three
  red tests. The rename had also missed its own binding test, which still read the withdrawn key
  — so the check that would have caught an incomplete rename was itself asking for the old name.
* **Study 17.** The §5 withdrawal was appended in one place while three other files kept
  promising what it withdrew, including two sentences the reviewer disproved by editing a figure
  in the prose and watching every test pass.
* **Study 22.** The withdrawal never reached the generator or the standalone records, so
  `numbers.json` and `tables.md` still carried the withdrawn population label; the splice
  registry still required a withdrawn sentence as an anchor; and four tests had been red since
  Amendment 6 added an arm without updating them. The self-indictment was also wrong in two
  ways, both of which made it cleaner than the truth: F6 is a truthiness check rather than a
  string check (102 of 281 witnesses are lists), and F6 *as registered* would not have
  established entailment either.
* **Study 20** is the exception, and it points the other way. Amendment 2 recorded a **permanent
  provenance loss that had not occurred**: it said the within-draw gap could not be recovered
  from the records, resting on cache rows with no clock time, while the archived usage ledger
  carries millisecond timestamps giving exactly the first review's 12:40:09. Every other
  correction in this programme has moved a number toward making the work look better. This one
  made it look worse. **A claim that evidence has been lost is a claim like any other.**

All four are fixed and pushed (036f2dc, fc5b002, 707c3f7, 8025ff4); none has been re-reviewed,
so none is quotable and the shipping blocker still stands on all four.

One operational note belongs here because it recurs. Two of the four branches were pushed with
failing tests that nobody ran, and in both cases the failures were exactly the checks that would
have caught what the reviewer found. The tests were not weak; they were not run.

## Pending — reported here only when their reviews end quotable

| study | claim it would license | state |
|---|---|---|
| 19 (ceiling 3b) | — | **QUOTABLE at round 10, 2026-09-20.** Moved to the admitted claims as C8 |
| 17 (testgen validation) | — | **QUOTABLE at round 11, 2026-09-20.** Moved to the admitted claims as C7 |
| 20 (ceiling 4) | — | **QUOTABLE (qualified) at round 4, 2026-09-20.** Moved to the admitted claims as C9 |
| 22 (injection) | — | **FINAL (descriptive) at round 9, 2026-09-21.** Moved to the admitted claims as C10 |
| 21 (rerate), added after review | the missed-against-caught ambiguity contrast, +31.9 points [9.6, 53.4] | post hoc; written to the record 2026-09-18, never reviewed |
| 23 (substrate 2) | nothing — Amendment 8's criterion was not met, so the study licenses no claim | third run complete 2026-09-19, 5 of 6 reversals reproduced; **closed without a quotable number**, no fourth run authorised |
| P2 (severity sweep) | — | **QUOTABLE at round 7, 2026-09-22.** Moved to the admitted claims as C11 |
| P1 (third rating) | — | **QUOTABLE at round 6, 2026-09-22.** Moved to the admitted claims as C12 |
| P3 (clarification) | — | **QUOTABLE at round 3, 2026-09-23.** Moved to the admitted claims as C13. Rounds 1 and 2 refused it (manipulation misdescribed; 3 of 32 classification rows wrong) |
| R1-M3 cross-tab (post hoc) | per-instance agreement of a non-participating rater with study 21's pair on the residual: L3 agrees on **30 of the 44** the pair called undetermined and calls 13 determined (`records/rate3/residual_crosstab.json`, harness `8119866`) | computed 2026-09-23, **never reviewed**; only L3's marginal 38/57, which RATE3's reviewed disjoint reading already carries, is in `tex/` |
| derived: six-family residual composition | 43 of 68 consensus-undetermined flagged by some family; 25 of 32 = 78.1% of the six-family residual undetermined (`reports/RESULTS-DERIVED.md` §1) | in `tex/` **before** admission — found by review paper1 r1; submitted to review round 2; removed if refused |
| derived: bootstrap coverage table | fourteen single-rate coverage cells (`reports/RESULTS-DERIVED.md` §2) | same status |

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

**Studies 17 and 19 discharge their halves of that blocker by the first route, 2026-09-20.**
Round 11 and round 10 both ended quotable; their claims are admitted as C7 and C8 and may enter
the manuscript body. Study 23 is closed without a quotable number, so nothing of it is there to
remove.

**The blocker is discharged, 2026-09-21.** All four studies it named are resolved, and the
record says by which route each went:

| study | route | outcome |
|---|---|---|
| 17 (testgen validation) | review | quotable at round 11 → **C7** |
| 19 (ceiling 3b) | review | quotable at round 10 → **C8** |
| 20 (ceiling 4) | review | qualified quotable at round 4 → **C9** |
| 22 (injection) | review | final descriptively at round 9 → **C10** |
| P2 (severity sweep) | review | quotable at round 7 → **C11** |
| P1 (third rating) | review | quotable at round 6 → **C12** |
| P3 (clarification) | review | quotable at round 3 → **C13** |
| 23 (substrate 2) | removal | closed without a quotable number; nothing of it was in `tex/` |

**The shipping condition in point 3 above is therefore met.** That does not mean the manuscript
is ready — it means this particular gate no longer holds it. C7 to C10 have to be written into
the paper before anything is submitted, and three of them are narrow or negative claims whose
limits are part of the claim: C8's post-hoc quantity may not be quoted as defect recognition,
C9's adjudication-derived figures are conditional on labels whose production cannot be audited,
and C10 licenses description only.

**What the five refusals of 2026-09-15 cost to clear: thirty-one further review rounds, and in
most of them the refusal was about a repair rather than a measurement.** No measurement moved in
any of the four studies. What moved was what the reports claimed about them.

**Study 23 discharges its half of that blocker by the second route, and the record says which.**
Its third run closed on 2026-09-19 without a quotable number, so there is no review to wait for.
Nothing of it remains to delete: the manuscript's only mention of substrate 2 is the Methods
sentence defining what it is, and `tex/` carries none of its figures or rates. The blocker now
stands on studies 17, 19, 20 and 22.

The rule as stated above remains the rule for admitted claims.
