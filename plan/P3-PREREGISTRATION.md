# P3 — the specification-clarification experiment

**Status: registered, not started. No model call has been made under it.** This file is the
authoritative text; it is copied into the harness beside the code that implements it before the
first call, and the copy's hash is recorded there. Written 2026-09-21.

## 1. What this tests, and why the other two designs cannot

Claim C4 says the residual — the defects no auditor flagged — is dominated by failures the
specification's prose never determined. Two studies have approached it and neither can make it
causal:

* **Study 21 (re-rating)** is post hoc. It re-read the residual under a rubric that asks the
  oracle question first, and two raters agreed that 44 of 57 residual instances are
  oracle-defined. That **conditions on** specification-determinedness; it does not manipulate it.
* **Study 22 (injection)** built a population where the property was to hold by construction, and
  review established that no filter in it enforces the property. Its own report is final in a
  descriptive form and licenses nothing about C4.

This design **manipulates the specification and changes nothing else**. That is the whole of its
contribution, and if it fails to move the outcome, C4 is a correlation between two properties of
hard instances rather than a causal account.

## 2. The manipulation

For each instance, the candidate code and the visible tests are **byte-identical across all three
conditions**. Only the specification prose differs.

| condition | code | visible tests | specification |
|---|---|---|---|
| original | unchanged | unchanged | as the dataset ships it |
| **clarified** | unchanged | unchanged | plus the behavioural rule the prose never settled |
| **placebo** | unchanged | unchanged | plus text of comparable length that settles nothing |

**What a clarification may add**: the rule the hidden suite tests and the prose leaves open — how
ties break, what an empty input returns, whether the result is sorted, what happens at a boundary.

**What it may not add**: the failing case, the expected value at the failing input, any hint that
a defect exists, or any wording that names the location of the change. A clarification that
describes the failure rather than the rule is a leak, not a clarification, and the check in §5
exists to catch it.

**The placebo** must match the clarification in added word count within ±15%, be written by the
same model under a prompt that forbids resolving any ambiguity, and be about the same function.
It is the control for "more words about this problem" and for "the specification was edited at
all".

## 3. The outcome, fixed now because this is where the last three studies went wrong

The outcome is **correct diagnosis**, not flagging, and not naming. Three times in this programme
a flag rate has been read as a naming rate or a naming rate as recognition — study 19's Table 5b,
study 22's probe, and the P2 sweep's first version. So the measure is defined before the data:

An instance counts as **correctly diagnosed** in a condition when the auditor's finding text, read
by two raters blind to condition and to instance identity, **states the behaviour the hidden suite
expects at an input the hidden suite exercises**, and does so in a way that would let a reader fix
the code without seeing the test. Disagreement counts as not diagnosed. The rubric, the sheet
format and the shuffle seed are fixed in §5 before any reading is bought.

Flag rate and naming rate are recorded beside it as secondaries, **explicitly labelled as not the
outcome**, precisely because they are the quantities that have been mistaken for it before.

## 4. Hypothesis, and what would falsify it

**H3.** Correct diagnosis is higher under `clarified` than under `original`, and the difference
under `placebo` is smaller than under `clarified`.

Both halves are required. A rise under both conditions means the auditor responds to the
specification having been *edited*, not to what the edit *settles*, and that is not evidence for
C4.

**Kill, registered before any call.** If the clarified-minus-original difference does not exclude
zero on the problem-cluster percentile bootstrap, **H3 fails and the report says C4 remains a
correlation.** The result is reported as found either way, and this sentence exists because every
correction in this programme so far has moved a number in the direction that made the work look
better, and because three of them then moved one in the direction that made it look worse.

## 5. Population, procedure, and the checks that must pass before spending

**Population.** The stratum-P instances of ceiling 1's frozen audit set that **no draw of any
family flagged** — the residual C4 is about — intersected with those study 21's two raters marked
consensus `ambiguous-oracle`. That intersection is 44 instances on the current records, and the
exact list is frozen to `records/clarify/population.json` with its generation digest before the
first call.

**Three gates, each proved able to fail by a planted violation, before anything is spent:**

1. **Code identity.** Every candidate and visible suite is byte-identical across the three
   conditions, checked by digest per instance per condition. A single differing byte halts.
2. **No leak.** The clarified text is checked against the hidden suite: it may not contain the
   expected value at the failing input, the failing input itself, or a quotation from the hidden
   test. Checked mechanically, and the check is run against a deliberately leaky clarification
   to prove it fires.
3. **Placebo length.** Added word counts within ±15% between the two edited conditions, per
   instance.

**Adjudication.** Two raters, one the author and one a model from a third vendor that is neither
the auditor nor the clarifier. Sheets carry no condition label, no instance id and no arm marker;
the shuffle seed is `20260921`. Round 1 of study 19's review found an identity leak in exactly
this kind of sheet, so the sheet builder is the one study 19 fixed, reused unchanged.

**Analysis.** Problem-cluster percentile bootstrap, 10,000 resamples, seed `20260921`, as the
primary interval; Wilson beside it and marked too narrow. The three conditions are **paired on
the same instances**, so the contrast is paired: exact McNemar and a cluster sign-flip
permutation, both reported, with the sign-flip the one that respects clustering.

## 6. Budget and sequencing

**Estimated $40–60.** Three conditions x 44 instances x K readings, plus the clarification and
placebo generation. The cap is **$70** with a halt at **$60**. A fourth condition is not
authorised by this registration.

**Sequencing, from the project plan and not waived here.** P3 was registered to start after P1's
blinded human rating, because if the missed and caught groups turn out to have similar ambiguity
rates, **P3's premise fails and the question should change rather than be run as written**.

That precondition has now been checked on the model raters and it holds: residual 44 of 57
(77.2%) against flagged 24 of 53 (45.3%), a difference of **+31.9 points, cluster [9.6, 53.4]**,
which excludes zero. That contrast is itself post hoc and **has not been through review**, so it
is evidence that the premise is not obviously false — not confirmation that it holds.

**Therefore: this registration is complete and no reading is bought under it until either P1's
human rating confirms the premise, or the owner decides to proceed on the model raters alone.**
That decision is the owner's and is recorded here rather than made by inference.

---

## Amendment 1 — a third rater on the blinded sheet, registered 2026-09-21 before its first call

**Why.** §6 said nothing is bought until P1's human rating confirms the premise or the owner
decides to proceed. The owner delegated the decision. Before spending P3's \$40–60 on a premise,
the premise is checked where it is actually weak.

**Where it is weak.** The +31.9-point contrast rests on study 21's consensus of **L1, who is the
author of this study and of the paper**, and L2 (`gpt-6-astra`). Amendment 2 of that study found
its sheets were **not blind to instance identity** — the id sat inside the hidden-outcome block.
So the premise currently rests on the author's own labels, taken from a partially unblinded
sheet, plus one model. P1 exists to fix exactly that, and P1 is one person's time away.

**What is registered here.** The 121-item blinded sheet already built for P1
(`~/Desktop/CrossAudit-审计天花板/人类评分任务/评分册.md`, 68 missed + 53 caught, shuffled,
answer key isolated) is rated by a **third rater that is neither the author nor `gpt-6-astra`**,
under the booklet's own three-option rubric — `determined`, `undetermined`, `cannot-tell` —
with no other instruction. The sheet was checked before this amendment and carries no `arm`,
`instance`, `old_id` or `problem_id` in its body: the rater sees the specification and the
visible tests, and nothing else.

**The quantity.** The share of `undetermined` among the 68 missed items against the 53 caught
items, with a problem-cluster percentile bootstrap over the union of their problems, 10,000
resamples, seed `20260921`, and Wilson beside it.

**What each outcome does, fixed before the numbers exist.**

* If the difference **excludes zero in the same direction**, the premise stands on evidence
  independent of the author, and **P3 starts without waiting for P1**. P1 remains worth doing and
  is not cancelled by this.
* If it **includes zero**, the premise does not hold once the author's labels are removed, and
  **P3 does not run as written.** The plan's own rule then applies: change the question rather
  than run it. What P3 would become is not decided in advance here.
* If the third rater returns `cannot-tell` on more than a third of either group, the rating is
  **inconclusive** rather than negative, and the decision waits for P1 after all.

**This is a precondition check, not a replacement for P1.** One model rater does not make a human
rating unnecessary; it tests whether the premise survives removing the one rater who knew the
hypothesis. It is post hoc with respect to study 21 and is labelled so wherever it appears.

### Amendment 1, outcome — INCONCLUSIVE by its own registered rule, and the sheet is broken

Ran 2026-09-21 on `gpt-5.6-luna` through the harness's own route, not Codex, whose allowance is
exhausted until 2026-09-22. All 121 items were labelled.

| group | n | `undetermined` | `determined` | `cannot-tell` |
|---|---:|---:|---:|---:|
| missed | 68 | 42 (61.8%) | 21 | 5 (7.4%) |
| caught | 53 | 4 (7.5%) | 7 | **42 (79.2%)** |

**The registered rule fires: more than a third of one group is `cannot-tell`, so this is
inconclusive rather than negative, and the decision waits for P1.** That is applied as written.

**But the reason is a defect in the sheet, and the sheet is mine.** The 42 `cannot-tell` answers
in the caught arm are exactly the 42 items whose `failing_input_class` is **empty** — a one-to-one
correspondence, with no empty item receiving a judgement and no non-empty item in that arm
refusing one. The booklet asks whether the specification determines what should be returned *on
the failing input class*. For 42 of the 53 control items, no failing input class is shown. The
question cannot be answered, and `cannot-tell` is the correct answer to it.

**Why it is empty.** `failing_input_class` lives in `records/ceiling/residual_classification.json`,
which by construction covers only the residual — the instances no family flagged. The caught
instances were never classified, so the control arm was built from a source that structurally has
no data for it.

**This breaks P1 as well as this check.** A human rater meets the same 42 unanswerable items. The
sheet on the owner's desktop cannot compare the two groups in its current form, and that should
be known before anyone spends an evening on it.

**What the answerable items show, recorded but not relied on.** Excluding the 42, the missed arm
is 61.8% `undetermined` (n = 68) and the caught arm 36.4% (n = 11). The direction matches study
21's 77.2% against 45.3%. With n = 11 in the control it settles nothing, and it is reported here
only so that the inconclusive verdict is not mistaken for a null result.

**A third place where "the author" enters the chain.** `residual_dump.py` describes the
classification as "the one hand step in this study": `failing_input_class` is written by the
author from the dumped evidence. So the premise P3 rests on passes through the author at the
classification, at L1's labels, and at the sheet built from both.

**The repair, which is not a patch.** The same script already re-runs each failing hidden input
and recovers the expected and actual values mechanically. That evidence exists for any stratum-P
instance, caught or missed, and does not pass through a hand step. Rebuilding both arms on it
would make the sheet comparable, remove one author dependency, and make P1 answerable. That is
the next action; it costs no model calls.

### Amendment 1, second outcome — the premise holds without the author, at about six-tenths the size

The sheet was rebuilt on mechanical witness evidence for both arms (`rate3/rebuild_sheet.py`),
and `gpt-5.6-luna` rated it again. The control arm is answerable now: `cannot-tell` falls from
79.2% to 9.4%, and 71 of the 121 labels changed.

| group | n | `undetermined` | Wilson | `cannot-tell` |
|---|---:|---:|---|---:|
| missed | 68 | 43 (63.2%) | [51.4, 73.7] | 7 (10.3%) |
| caught | 53 | 23 (43.4%) | [31.0, 56.7] | 5 (9.4%) |

**Difference +19.8 points, problem-cluster percentile bootstrap [+1.2, +38.1]**, 10,000
resamples, seed 20260921. It excludes zero, and neither arm is near the one-third `cannot-tell`
threshold.

**So the first registered branch fires: the premise stands on evidence independent of the
author, and P3 starts without waiting for P1.** That is applied as registered.

**And the size should be read plainly.** Study 21's contrast, on L1 the author plus
`gpt-6-astra`, was +31.9 points [9.6, 53.4]. This is **+19.8 [+1.2, +38.1]** — about six-tenths
of it, with a lower bound close to zero. The premise survives removing the author; the effect it
survives at is smaller than the study that first reported it suggested. No stricter bar is
imposed here after the fact, because the rule was written before the number existed and inventing
one now is the failure this programme has made repeatedly.

**What this does not settle.** One model rater is not a human rating. P1 remains worth doing on
the rebuilt sheet and is not cancelled: it would say whether a human reading the same mechanical
evidence agrees, which is a different question from whether the premise survives a change of
rater. Six items needed a per-item retry after a batch returned nothing; one of those
(`H080`) took three attempts. Nothing else was re-asked.

## Amendment 2 — a registered secondary population, 2026-09-21, before the first P3 call

The population §5 registers is the residual intersected with study 21's consensus
`ambiguous-oracle`: **44 instances**, frozen to `records/clarify/population.json`.

Amendment 1's third rater, reading the rebuilt sheet, judges those same 44 as **30
`undetermined`, 13 `determined`, 1 `cannot-tell`**. So on an independent reading, **roughly
three in ten of the population are not specification-undetermined at all**.

That matters for the manipulation rather than for the premise. Clarifying a specification that
already settles the question is a no-op: those instances can only dilute the effect, and if H3
fails it will not be possible to tell a null result from a diluted one.

**Registered now, before any P3 reading is bought:**

* The **primary** stays the 44 instances §5 registers. The registration is not rewritten because
  a later rating disagreed with it.
* A **secondary** is added on the 30 instances that both study 21's consensus and the third
  rater call undetermined. It is reported beside the primary, always, whichever way each goes.
* **If the two disagree in direction, the primary is what the study reports** and the
  disagreement is the finding. If H3 holds on the 30 and fails on the 44, that is evidence the
  manipulation works where there is something to manipulate — a weaker claim than H3 and stated
  as one, not as H3 confirmed.

The 13 disputed instances are listed in the record rather than dropped, so a reader can see which
they are.

## Amendment 3 — who writes the clarification, 2026-09-22, before the first generation call

§2 says what a clarification may and may not add and does not name the model that writes it.
Registered now, before any call:

**The clarifier is `anthropic:claude-sonnet-4-6`. The auditor is the shipped cross-vendor
auditor, `openai:gpt-5.6-terra`, as in ceiling 1.** They are different vendors and different
models, and the first draft of the generator had the clarifier set to `gpt-5.6-terra` — the
auditor that missed these very instances, writing the clarifications it would then be asked to
read. That is caught here rather than in review.

**Why a strong model and not the study's frozen generator.** `claude-haiku-4-5` writes the
candidates in this programme and would be the conventional choice, but a clarification that
fails to state the missing rule turns H3's null into a fact about the writer. The manipulation
has to be real for its absence to mean anything. The trade is disclosed: the clarifier is
stronger than the generator, and that is a property of the manipulation, not of the auditor.

**The clarifier sees the witness; the auditor does not.** Only someone who knows which rule was
left open can write it down, so the clarifier is shown the failing inputs. The auditor is shown
the specification, the visible suite and the candidate — never the witness, the hidden suite, or
which condition it is reading. Gate 2 checks mechanically that the clarification did not carry
the failure across that boundary.
