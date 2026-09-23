You are an INDEPENDENT REVIEWER from a different vendor. SIXTH cross-vendor review of `study/injection` at 53927c1 (the worktree you are in). Do not modify any file.

**Round 5's three findings are fixed at `53927c1`, the only commit since. Start with the
binding, because it has now failed twice and you broke it both times.**

You were right about why round 4's binding failed, including the part I would not have found:
two of its six assertions were written as `"...".capitalize()[:31]` and `[:44]`, truncations
added so the strings would match, which cut off exactly "nothing" and "entailment". Three more
of your attacks reversed a conclusion while leaving its opening intact, and the fifth left the
required sentence in an HTML comment and displayed its reversal beside it.

Now: complete passages, no truncation; the check reads a **visible** document with HTML comments
stripped; and section 2's binding extends to the subordinate clause your fourth attack reversed.
All five of your attacks are kept in the file as regression cases and were run against the live
suite before committing — five red, the comment attack included. **Attack it a third time.** The
test states its own limit, which is your sentence: this protects these passages, it does not
establish that contradictory prose cannot be written elsewhere.

The probe is now stated the same way in all four places. §3's "shows those cues are there" and
Amendment 6's "shows that salience is detectable" are gone; the probe separates two sets by
something it does not identify. §3's "neither the auditor nor a gate" is now marked as what the
preregistration ASKED for, with the implemented departure stated.

The cross-tab: 8.55% and 0.087 are labelled a uniform-placement calculation, not a probability
from any model of the auditor following the probe's signal, and the report now says the two
misses are `inj:b1:Mbpp/404` and `inj:b2:Mbpp/404` — **the two instances of one problem**,
verified from the record — so the calculation is not cluster-aware. Fisher's p = 1.0 supports
only that this table does not distinguish the explanations.

**What this round should settle.** Whether the binding holds under a third attack; whether the
probe, filter and cross-tab accounts are now accurate and mutually consistent; whether the cost
figure and its provenance qualification are right; and whether anything still claims more, or
less, than the records support. If the answer is that the descriptive content is sound and only
the C4 denominator is missing — which has been your verdict for three rounds — say what, if
anything, would still need to change for this report to be final in that form.

**Round 4 read "quotable descriptively / not quotable for C4" and listed eight things still
wrong. All eight are fixed at `e3ba0a3`, the only commit since, and every figure you gave was
recomputed here before it was accepted.**

**Start with the one that matters most, because it was a check of mine that did not check.** You
replaced section 2's conclusion with an explicit endorsement of C4 and every test passed. That
was reproduced here — swapping "What this licenses about C4 is nothing" for "exactly what C4
needs, and the study confirms it prospectively" left 26 of 26 green. The round-3 binding named
one sentence of a withdrawal that lives in six, so it protected none of it. Every load-bearing
withdrawal sentence is bound now, and two mutations were run against the new binding before
committing; both are red. **Attack it again, with sentences I did not think of.**

Three things round 3's repair got wrong, all yours and all fixed: "selects on detectability
rather than on the specification" was reported as narrowed and had been narrowed in one place of
two, so §1 and the deviations both still said it and now both say association; "the gate-rejected
sample carries no duplication at all: 40 distinct programmes" contradicted the table generated in
the same commit and now says 35 with the five byte-identical pairs named; and Amendment 5's
round-3 notice claimed the probe "measures conspicuousness at 96.7%", which it cannot — that
notice and `probe.py`'s docstring, which still said "not a gate", now carry the three limits.

Two arithmetic corrections, recomputed rather than taken: the cross-tab is **8.55%** and
**0.087** over 92 — 1 − C(88,2)/C(92,2) — with the note that the old 11% and 0.12 use 69, the
injected items the probe answered. And the cost section omitted Amendment 6's arm entirely: 320
cached readings at **$1.8965**, taking $16.47 to **$18.37**. Check that derivation; it is summed
from the cache's per-reading `cost_usd` over the registered 40-instance sample, and your $18.3687
differs from it only by my adding to a rounded $16.47.

Two withdrawals that went too far are pulled back: the weighted figure has a population (the 281
filter-accepted edits) and lacks the **semantic** denominator C4 needs, and "what this licenses
is nothing" now says nothing **about C4**. `CORRECTIONS.md` no longer conflates the twins with
the natural residual.

**What this round should settle.** Whether the withdrawal is complete and whether its bindings
now hold under attack; whether the probe and filter accounts are accurate; whether the cost and
cross-tab arithmetic is right; and whether anything still claims more, or less, than the records
support. Four repairs in this programme have now erred toward modesty and been wrong for it,
three of them in this study.

**Round 3 read "quotable only descriptively; not quotable for C4" -- which is this study's own
position -- and refused on two grounds: the withdrawal had not reached six named places, and the
repair asserted things that are false. Both are fixed at `2050044`, the only commit since, and
every one of your factual corrections was verified here before it was accepted.**

The six places: section 1 no longer declares H22a positive on a denominator of "defects the
specification determines", and says the kill's verdict is withdrawn with it because it is
computed on the same denominator; sections 1 and 2 no longer conclude that the measured ceiling
is not the auditor's ability to see specification-settled defects -- that sentence is withdrawn
as the study's reason for existing, and the study is now stated to contradict nothing, leaving
C4 exactly where study 21 left it; the generated primary table's ROW names the population what
it is; the CLI output leads with a withdrawal notice; `test_inject_report.py` no longer DEMANDS
the prose say "the kill does not fire" and instead binds both the computed value and the fact
that it licenses nothing; and Amendment 7 carries an in-place correction.

**Your four factual corrections, each reproduced before acceptance.** The intervals are
reproducible: seed 20260916 is `BOOT_SEED` and is named in the registration, the published
[62.2, 90.5] reproduces exactly at it, and the `+ 70` offset that moved it was the author's --
the generator is back on the registered seed and the "cannot be reproduced" claim is withdrawn
in both the tables and the results. The prober is `anthropic:claude-opus-4-8`, one of the two
`GATE_SPECS`; four places said "not a gate" and now say it is not independent of the gate, with
your other two limits stated beside it (the arms share no problem; it sees the specification).
The self-announcing count is 19, not seven, with only `b2:Mbpp/643` in I. The rejected sample is
40 readings over 35 distinct programmes.

Two of your qualifications are taken as narrowings: "selects on detectability rather than on the
specification" no longer claims specification judgements played no role, and "nothing in the
construction was looking for conspicuousness" is replaced by what is true -- the injector prompt
prohibits markers and comments, and **no acceptance check enforced it**, which is F6's shape.
And your third is taken against the author: "nothing remains quotable" withdrew too much, so
`CORRECTIONS.md` and the results now state what survives, in the narrow scope you gave it.

**What this round should settle.** Whether the withdrawal is complete this time -- read anything
a reader or a script meets without the results banner, including the CLI output and the
standalone records. Whether the account of the six filters and of the probe is now accurate.
Whether what the study is said to license matches what it can. And whether any sentence still
claims more, or **less**, than the records support: two repairs in this programme have now gone
the modest way and been wrong for it, and one of them was in this study.

**Round 2 agreed the withdrawal is justified and refused quotation because it had not reached
every place the claim lives, and because the repair introduced factual errors of its own. Both
are right and both are fixed.** Four tests had been red since Amendment 6 -- the ladder test, the
"no table outside a generated block" test, the block-order test and the cross-tab test -- and
that was reproduced here, by stashing, before anything was edited: the failing set was identical
with and without the fix.

**The withdrawal now travels with the record.** `numbers.json` carries a `WITHDRAWN` block and
`tables.md` opens with a withdrawal notice, both emitted by the generator so a regeneration
cannot drop them. The splice registry's `xtab` anchor no longer demands "it points the other
way", the sentence 60babd8 replaced. Four preregistration passages -- §1's conservativeness
argument, Amendment 1's "can only lower recall", Amendment 3's conservative gate, Amendment 5's
"the injected defect and nothing else" -- carry in-place supersession notices and are otherwise
untouched. `benchmarks/CORRECTIONS.md` gains the study-22 entry it lacked. Section 5 is new and
sets out what each of the six filters checks, using your counterexamples.

**Your three corrections to the withdrawal are taken.** F6 is described as a truthiness check,
with 179 of 281 witnesses strings and 102 lists; F6 *as registered* is said not to have
established entailment either; and F2 to F5's gaps are stated rather than left to F6.

**Amendment 6's gate-rejected arm is in the record for the first time.** Its eight draws had
been in the archive and in `inject.LADDER` since that amendment while its numbers were
hand-written into the results. It is generated now: 31 of 40 = 77.5%, Wilson [62.5, 87.7], 35
problems, reproducing the hand-computed counts exactly. **The cluster interval is [62.5, 90.7]
against the hand-written [62.2, 90.5], and the difference is stated rather than reconciled,
because that figure's bootstrap seed was never recorded.** Check that reasoning. The 84.2% is
restated nowhere; it was never in `numbers.json`, which is why its interval could not be
reproduced either.

**What this round should settle.** First, whether the withdrawal is now complete -- look
especially at anything a reader or a script meets without the results banner. Second, whether
the account of the six filters is accurate and whether any other filter is described as doing
something it does not. Third, your question from round 2, which the author has answered "nothing"
and will act on: does anything in this study remain quotable at all, and if so, exactly what
claim does it license? Fourth, whether the proposed successor -- a population whose
specification-determinedness is established by someone other than the injector -- would give C4
its prospective test or inherit the same problem.

**Read this before anything else: the study's headline figures are both WITHDRAWN, and this review is not about whether they are right.** The first cross-vendor review refused quotation twice, most recently because "the 84.2% headline removes the only semantic gate, so its denominator is not shown to be 'defects the specification determines'; it is a post hoc, non-reproducibly reported estimate over hidden-suite-selected artificial edits." The author's response at `d3f8334` accepts both refusals in full and goes further than either asked.

**What the author now says against their own study.** F6 was registered as recording the witness AND recovering the first failing hidden input by study 21's witness path. It is implemented as `bool(obj.get('witness_input'))` — a non-empty string check that never recovers, never executes, and never connects the quote, the named class, the witness and the actual failure. Amendment 6 caught half of this and still called the six filters mechanical guarantees of specification entailment; the author now says they are not, and that **no filter in this study establishes specification entailment at all**. So neither figure survives: 97.8% conditions on a gate whose own measurement showed it selects for detectability, and 84.2% removes the gate but leaves a denominator that is "small injected edits that survived a sparse visible suite and failed a hidden one", which is not "defects the specification determines". The reviewer's alternative account — that the retry loop concentrates the pool into conspicuous edits — is accepted as surviving the paired twin arm too, because removing the edit removes the cues. **C4 does not gain its prospective test from this work**, and the author states what would: a population whose specification-determinedness is established by someone other than the injector.

**One thing the author found while checking, and reports against interest.** Seven archived instances carry a comment naming the bug, one reading literally `DEFECT: should be +`, and both gates accepted it. Only one reached population I; it was flagged 8 of 8, and removing it gives 89 of 91, still 97.8%. So self-announcement does not explain the effect — but nothing in the construction was looking for conspicuousness, which is what the 96.7% probe then measured. Verify that count and that recomputation.

**What this review is for.** Four questions, in this order.

1. **Is the withdrawal complete?** Find any sentence, table, figure, docstring, JSON key, commit-message-derived note or amendment that still presents either figure, or any filter, as establishing specification entailment. A withdrawal that does not reach every place the withdrawn claim lives is the exact failure two other studies in this programme were refused for on 2026-09-15.
2. **Is the account of F6 accurate and complete?** Read the implementation and the registration yourself. Say whether `bool(obj.get('witness_input'))` is the whole of it, and whether any OTHER filter is also described as doing something it does not do — the author claims F6 was the only one that was audited this way.
3. **Does anything in this study remain quotable at all?** The author's position is that nothing does. If you agree, say so plainly and say what the study is then evidence of, if anything. If you find something that does survive — a negative result, a measurement of the gate's selectivity, the conspicuousness probe — name it and say exactly what claim it licenses.
4. **Is the proposed successor the right one?** "A population whose specification-determinedness is established by someone other than the injector." Say whether that would in fact give C4 a prospective test, or whether it inherits the same problem in a new costume.

**One standing hazard, stated so you can look for it.** A fix written to satisfy a reviewer is itself an unreviewed claim, and in this programme two of five studies were refused for a defect introduced by a previous repair. This repair is unusually large — it withdraws the study's entire result — so check the opposite failure too: has anything been withdrawn that the evidence actually supported, and is the record still able to show what was believed and when?

The study tests prospectively a claim an earlier study of ours reached POST HOC: that the measured audit ceiling is mostly a property of the benchmark's oracle rather than of the auditor. It builds a population where "the specification determines this defect" holds by construction, and audits it with the shipped auditor, the shipped constitution and the same K = 8 that produced the frozen 30.0% comparator.

Claimed. **Population**: 910 stratum-C instances (solutions that pass BOTH suites) walked in one seeded order; one defect injected per instance by the generator's own model; six MECHANICAL filters (the injector's quote must be a literal substring of the specification and at least six words; the modified code must pass every visible test; must fail the hidden suite without timing out; at most four changed lines and no new import; must run; a witness recorded); then a gate of two models, neither the auditor, which must BOTH agree the specification entails the modified code is wrong on the named class. **281 passed the filters; 92 passed both gates; 189 were refused by a gate.**

**The headline is the STRATIFIED figure over all 281 filter-accepted instances: 84.2% [73.8, 93.1], against ceiling 1's frozen 33 of 110 = 30.0% [20.0, 40.7].** On the 92 the gate accepted, union recall at K = 8 is 90 of 92 = 97.8%; on a preregistered random sample of 40 of the 189 the gate REFUSED, it is 31 of 40 = 77.5% [62.2, 90.5]. **H22b (paired, Amendment 4)**: every instance of the 92 audited again with the injection REMOVED — 90 of 92 against 11 of 92, +85.9 [+77.3, +93.3], 79 discordant pairs one way and none the other. **§4.1 detectability probe**: a frontier model that is neither the auditor nor a gate separates injected from natural solutions at 96.7% on the 152 of 184 items it answered, chance excluded, and between 79.9% and 97.3% if the 32 it would not classify are counted all wrong or all right. Cost about $18.4 of a $35 cap.

**Read Amendment 6 first, because it withdraws two things the earlier draft of this study asserted, and your review should test whether the withdrawal went far enough.**

1. §1 used to argue that the filters and the gate can only err by ADMITTING instances they should have refused, so no failure mode could manufacture the effect. **That argument is false and is withdrawn.** The gate asks whether the specification settles behaviour on an `input_class` the injector itself names, and no filter ever checked that the named class is the one the edit actually breaks. So the gate refuses plainly determined boundary edits — `b1:Mbpp/223` changes `count > n/2` to `count >= n/2` against a specification saying "occurs more than n/2 times", and both gate models voted no. Amendment 6 replaced the argument with the measurement above, and 77.5% against 97.8% says **the gate does select for detectability**, which is why the headline is now the stratified figure and 90 of 92 is labelled a property of the gate-accepted population.
2. Amendment 5 used to claim the paired twin contrast isolates "the injected defect and nothing else". **Withdrawn.** It isolates the EDIT, which carries both the specification violation and the surface salience the probe measures at 96.7%.

Binding: `benchmarks/code/inject/PREREGISTRATION.md` and its **SIX** amendments — read each and judge it for outcome-dependence. Two disclose construction pilots; one changes a gate model after an OpenAI credit failure; one adds the paired twin arm; one fixes in advance which contrast carries which confound; **Amendment 6 was written after an internal hostile review and before the arm it governs was run — check that ordering in the git history yourself.** Also ceiling 1's preregistration and `RESULTS-CEILING.md` (the frozen comparator, the strata, the interval conventions), study 21's `RESULTS-RERATE.md` (the post-hoc split this study tests), `EXPERIMENT_RECORD.md` §9-§10.

Verify, at least:

1. Re-run `report_inject.py`; confirm `numbers.json` and `tables.md` reproduce and the splice matches; recompute the gate-accepted rate, the paired contrast and the curve independently from the caches. **Then recompute the stratified 84.2% and its interval yourself** — it weights the two strata by population (92 and 189 of 281) and bootstraps problem clusters within each. Say whether that estimator is the right one and whether its interval is honest about estimating the second stratum from 40 of 189.
2. **The construction is still the thing to attack.** Read `inject.py`'s filters and gate yourself and say whether "the specification determines this defect" is really what they enforce; sample fifteen accepted injections from the archive (`~/Documents/Crossaudit/study-data/wt-inject-runs/injected/injections.json`, base solutions in `study2-inputs/`) and say for each whether you would have admitted it; then sample ten the filters REJECTED and say whether they threw away anything they should have kept.
3. **Now that the conservativeness argument is gone, find what replaces it or say nothing does.** Is 84.2% a defensible estimate for "defects the specification determines", or does conditioning on the six filters carry its own selection that the rejected-arm measurement does not reach? Construct a failure mode that manufactures the remaining effect if you can. The contrast against 30.0% is what the paper leans on — attack that, not the 97.8%.
4. **Duplication.** |I| is 92 instances over 54 problems but only **59 distinct `modified_sha256`** — 33 byte-identical groups covering 66 instances. The study claims no duplicate group spans more than one `problem_id` and therefore that the problem-cluster bootstrap absorbs the duplication. Check that claim directly, and say whether the Wilson figures printed beside it are flagged clearly enough.
5. **The probe and the empty cross-tab.** The probe says the defects are detectably artificial, which the results present as the study's main limitation — judge whether the results give it enough weight. The post-hoc cross-tab that appears to cut the other way is now reported as carrying **no information** (2 misses over 92, 4 instances in the natural cell, Fisher p = 1.0). Verify that arithmetic and say whether any sentence still leans on it.
6. Every sentence of §1 to §3 against the records; in particular whether anything claims the auditor NAMES the defect, which the adjudication of §5 has not been run to support. And `src/` and the kernel dirs untouched; no corpus, solution or finding text committed.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Archive: `~/Documents/Crossaudit/study-data/wt-inject-runs/` (injections, gate verdicts, per-draw findings with text, probe replies, ledgers). End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.
