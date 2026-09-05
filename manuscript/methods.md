# Methods

## Two substrates

The **code substrate** scores outcomes by executing a hidden test suite, so
strata, recall denominators, the false-positive population and the loop's
accuracy change are decided by a Python interpreter and no model judges any
outcome. The **prose substrate** scores outcomes with CLEAR and inherits a
model-judged ground truth. Detection recall, false positives on correct work,
the architecture comparisons and both ceilings rest on the code substrate;
single-verdict reproducibility, revision gating and the audit-stage noise floor
rest on the prose substrate, and say so wherever they appear.

## Task and ground truth: code

The corpus is EvalPlus, whose structure is the object of study: the base suites
are the tests a developer can see, the plus suites the ground truth those tests
miss. HumanEval (MIT), HumanEval+ (Apache-2.0) and MBPP+ (Apache-2.0) are pinned
by revision, row count, byte count, sha256 and licence in every manifest
(`records/code/study1/manifest.json`, `data.datasets`). Two of 542 problems
(`HumanEval/32`, `Mbpp/590`) were excluded by name before generation, because
their own reference solutions fail their own hidden suites here; the other 540
pass both, which is the harness's model-free self-validation, and are the study
population. Solutions came from `anthropic:claude-haiku-4-5-20251001`, one call
per problem, no rubric and no audit rules; a small generator was fixed in
advance because a frontier generator leaves too few solutions in the population
of interest (`records/code/PREREGISTRATION.md`).

Execution alone assigns each solution to one stratum: **P** passes every visible
test and does not pass the hidden suite ("looks right, is wrong"), **C** passes
both, **F** fails a visible test. Batch 1 gave P 56, C 455, F 29; batch 2, a
second pass of the frozen generator over the same problems, gave P 54, C 455,
F 31; the preregistered rule (pool batches until P reaches 100, at most three)
stopped at two, pooling to P 110, C 910, F 60
(`records/code/study2/manifest.json`, `population`). An **instance** is a
`(batch, problem_id)` pair, and 68 problems contribute two instances each, which
is the clustering treated below. The **audit set** was drawn once from a fixed
seed before any arm ran and shared by every arm, so no arm can influence which
instances it sees: 235 instances in study 1 (P 56, C 150, F 29, seed
`20260904`), 290 in study 2 (P 110, C 150, F 30, seed `20260905`), frozen and
digest-pinned (`records/code/explore/manifest.json`, `data.audit_set_sha256`).
Every later study, the ceiling study included, reuses study 2's set and
solutions byte-identically; nothing is regenerated per arm. **Flagged** means
the arm raised at least one BLOCKER finding on that instance, from the model
rung or the deterministic rung; ADVISORY never gates in the product and is not
counted. The definition is identical in studies 1, 2, 7 and the ceiling study.

## Task and ground truth: prose

The prose task is `T03MaterialSEG` from ExpertLongBench: justify the key
decisions in a solid-state synthesis recipe against a six-item expert-designed
rubric, over a 50-row corpus pinned by sha256 in every manifest
(`records/prose/study6/noise-rep1.manifest.json`, `dataset`). CLEAR maps an
output onto that rubric and judges each mapped item against the checklist-mapped
human reference in both containment directions, giving a per-sample harmonic F1
over the full checklist length. **The authors released no evaluation code, so
this scorer is a reimplementation from the paper and has never been diffed
against theirs**; the item-by-item transcription is in
`benchmarks/expertlongbench/NOTES.md` in the product repository, and its only
external check is that it places frontier models in the band the paper reports
for this task. Two silent normalisation behaviours were found later, by the
cross-vendor review below, and fixed: a judge reply containing both verdicts was
resolved by taking the first token and now raises, so the item is recorded
unscorable and counted; and a rubric key the mapper never emitted was coerced to
`"N/A"` indistinguishably from a key answered `"N/A"`, and the omitted-key count
is now returned to the caller. Their effect on earlier runs cannot be recovered,
because raw replies were not retained; they are retained from the fix onward.

The corpus is treated as CC BY-NC-SA 4.0: no dataset row, input, reference
value, model output, mapped checklist or judge transcript is committed, only
ids, digests, counts and scores. The one dataset-derived string class committed
is the rubric item labels, at most 78 characters, treated here as identifiers;
`analysis/corpus_scan.py` lists every string field over 60 characters in the
prose records and exits non-zero if a free-text field appears
(`records/PROVENANCE.md`).

## The audited system

The system under measurement is the shipped product, entered at its own
`crossaudit.auditor.run.run_audit`. One round is: the generator writes an
increment; the increment is committed; a deterministic check layer runs over the
committed bytes, its findings CONFIRMED on being raised; a cross-vendor model
auditor reads the same bytes under a written constitution, its findings ALLEGED;
a verdict ladder returns PASS, BLOCKED, ESCALATE or DCL_ONLY, and the evidence
records are bound into one digest. `authority.lone_model_blocker` stayed at its
shipped conservative setting in every arm. The product refuses a same-vendor
generator/auditor pair: `run_audit` raises `ConfigDenial` when the vendors
overlap. That guard is asserted from configuration, so it fires only when the
generator's vendor is declared, and every self-audit arm is obtained inside the
harness by leaving `generator:` unset, so the guard has nothing to compare. This
is a deliberate bypass of a product guarantee, for measurement only; it is
confined to the harness, `src/` is unmodified by any study, and the
configuration is one no customer can run.

Models by role, from the manifests. Code: generator
`anthropic:claude-haiku-4-5-20251001`, cross-vendor auditor
`openai:gpt-5.6-terra`, self auditor the generator's own model, cheap tier
`openai:gpt-5.6-luna`, and **judge: none**, stated in those terms in every code
manifest. Prose: generator `anthropic:claude-sonnet-4-6`, with auditor, CLEAR
mapper, CLEAR judge and adjudicator all `openai:gpt-5.6-terra`, so instrument
and audited party share a vendor, recorded as a limitation. Sampling settings
are not free parameters: the provider layer exposes no seed, and temperature
comes from each model's capability card. The auditor model's card carries
`temperature=False`, because reasoning models of this generation accept only
their own default, so no temperature is sent
(`records/code/checks/manifest.json`, `models.auditor.temperature`:
"provider-default (not settable through the product's provider layer; the
auditor model's capability card carries temperature=False)"). Where a card
permits temperature, as on the self route, the broker sends 0; reasoning effort
is provider-default. No run reproduces byte-identically, and the replicate arms
quantify what that costs.

## Architectures compared

Each architecture is a detector specification `{detectors, aggregate}` scored on
the frozen audit set, so all judge identical bytes and every contrast is paired
on instances. **Holistic cross-vendor**, the reference, is one audit call by
`gpt-5.6-terra` over the solution and the visible test source under the shipped
constitution; **holistic self** issues the same call to the generator's own
model. **Decomposed** enumerates properties from the problem specification alone
and checks each separately, the decomposer seeing only `problem.spec` and the
per-property checker seeing the specification, the candidate, the visible test
source and one property, with any VIOLATED property a BLOCKER; the hidden suite
is unreachable by construction, because prompt builders take plain strings and
never the object carrying it, and three tests pin that. **Union, majority and
unanimous** aggregates were computed over repeated draws of one route and over
draws of different architectures, ten of the fifteen preregistered
specifications being set operations over records that already existed.
**Cheap-tier repeats** are one and three unioned draws of `gpt-5.6-luna`. The
**executable-check proposal** asked the auditor for runnable assertions rather
than an opinion, executed each against the candidate and against the EvalPlus
canonical reference in a subprocess sandbox, and classified it discriminating,
vacuous, inverted or firing on both; its preregistered kill condition was fewer
than one third of the 56 stratum-P instances yielding a runnable discriminating
check, and a primary arm and a preregistered replicate each ran all 56
(`records/code/checks/manifest.json`, `kill_condition`). Held fixed throughout:
the audit set, the solutions, the constitution, the increment, the flag
definition, the entry point and `max_rounds: 1`. What varies is who reads and
how the readings are combined; no specification asks a model for a truth value.
Selection among the fifteen was preregistered as split-half (seed `20260906`,
stratified on stratum and batch), claims taken only from the confirm half (P 55,
C 74, F 15) under a rule fixed before scoring: highest P-recall among
specifications whose false-positive rate on correct code is at most 6.7%, that
bound being the reference architecture's own upper 95% Wilson limit from study 1
(4 of 150 correct solutions flagged, 95% CI [1.0%, 6.7%])
(`records/code/PREREGISTRATION-explore.md`).

## The ceiling study

Preregistered in `benchmarks/code/ceiling/PREREGISTRATION.md` on branch
`study/ceiling`, with amendments 1 to 3 committed before the first model call
including the credential probe.

**Ceiling 1, seeing.** For a family of detectors and K independent draws over
the same instances, union recall at K is the fraction of stratum-P instances
flagged by at least one draw, averaged over all C(K_max, K) subsets exactly
rather than by sampling. Expected union recall is the mean over instances of
1 − (1 − p_i)^K, so its limit is the fraction of the population with non-zero
per-draw flag probability, which is the quantity called the ceiling. The
preregistered fit is A(1 − e^{−K/τ}) by unweighted least squares over the
K = 1 … K_max points, **A constrained to [0, 1] inside the objective**; the
single-exponential form was chosen in advance because under heterogeneity it
underestimates A, so the reported ceiling errs low. Reported beside every
asymptote, never instead of it: the raw union at K_max, a zero-inflated
beta-binomial estimate as a secondary and expected-unstable check, fit quality,
and a flatness diagnostic whose preregistered bar is a last-step gain of at most
1.0 percentage point, a curve failing it having its asymptote labelled an
extrapolation wherever quoted. Intervals are percentile bootstraps over whole
problem clusters, refitting the curve inside each resample. Families are `cross`
and `self` at K = 8 and, by dated amendment, `astra` (`gpt-6-astra` at high
reasoning) at K = 4. `astra` is issued through the Codex CLI from an empty
read-only scratch directory, using the shipped auditor prompt byte for byte
(checked against study 2's committed `prompt_sha256` values, 40 of 40 agreeing)
but bypassing the provider broker, the metered ledger and the heterogeneity
guard, so it is labelled a measurement of a model and not of the product path
wherever it appears. Results: `[PENDING: ceiling r4]`.

**Ceiling 2, correcting.** One `frozen solution → run_audit → revise once if
BLOCKED → hidden suite` cycle per instance, over a frozen paired sample of 112
instances (56 P, 56 C, 28 from each stratum-batch cell, seed `20260907`, 96
distinct problems). Generation is not repeated, so no arm difference can be
generation variance, and the revision prompt is the product's own. The primary
outcome is the net change in hidden-test pass rate over the whole sample,
**unconditional on whether a revision occurred**: instances the audit did not
block are carried at a delta of exactly zero, not dropped, because the
programme's largest retraction (`CORRECTIONS.md` item 9) is the opposite choice,
conditioning on a consequence of the treatment. The conditional figure is
computed and labelled exploratory at every occurrence. Arms are `self-loop`; its
identical replicate `self-loop-rep`, the loop's own noise floor, without which
no sentence may say "inside the noise floor" about a loop result; `cross-loop`;
and `referent-loop`, which adds exactly one BLOCKER constitution rule and
changes nothing else, telling the auditor that the visible suite shown to it is
neither a specification nor complete and that it should judge the behaviour
those tests never exercise. That arm exists because the referent is the only
lever in this programme's history measured to move recall by more than a few
points. **Kill condition, registered:** if `self-loop`'s net change is at most
zero, or its 95% interval contains zero, or its magnitude is inside the
replicate spread, then on this evidence self-audit does not raise accuracy and
the report's first sentence says so. Results: `[PENDING: ceiling r4]`.

**The residual** is every stratum-P instance flagged by no draw of any family,
classified by hand from the hidden-test failure record, the visible tests, the
candidate and the canonical solution. Categories and their precedence order were
fixed in the preregistration and the first residual instance was not opened
until that file was committed: `timeout`, `unexercised-edge`, `spec-misreading`,
`wrong-algorithm`, `ambiguous-oracle`, `other`, each instance taking the first
that applies. Two categories were never assigned, the ordering absorbing
disputable-oracle cases into `unexercised-edge`; the rule was applied as written
and the consequence stated at the table. Counts and shares:
`[PENDING: ceiling r4]`.

## Statistical analysis

**Unit of analysis.** The independent unit is the instance; the resampling and
permutation unit is the problem, because problems recur across batches (the
ceiling loop's 112 instances come from 96 problems, stratum P's 110 from 56). K
draws over the same instances are repeated measures, never K × n observations.
In the ceiling study every interval is a percentile bootstrap over whole problem
clusters (10,000 resamples, seed `20260908`) and every exact McNemar p carries a
cluster-level sign-flip permutation p beside it, Wilson intervals being printed
alongside and marked too narrow. The prose replicate study bootstraps instances
(20,000 resamples, seed `20260930`) and tests paired per-instance differences by
exact two-sided Wilcoxon signed-rank enumeration, ties dropped. Studies 1, 2 and
7 use Wilson intervals with exact McNemar and a seeded paired instance
bootstrap; that these treat instances as independent is a stated limitation.

**The paired-difference interval, and its history.** The ceiling study first
published a Clopper–Pearson interval for the direction probability *conditional*
on the discordant pairs, rescaled by the *observed* discordance fraction, which
is not a valid interval for the unconditional risk difference because that
fraction is itself estimated and its uncertainty discarded; enumerating
D ~ Binomial(112, 0.1) with every discordance beneficial gives it coverage 0.416
where 0.95 was claimed. An independent cross-vendor reviewer found it, it was
reproduced to ten digits before anything changed, and it survives in
`numbers.json` as `withdrawn_conditional_ci95` with a test pinning it. Its
replacement is the problem-cluster bootstrap as primary, checked by Tango's
unconditional score interval and a Berger–Boos-restricted, grid-approximated
exact unconditional interval; a second review found both checks bounded the
nuisance parameter by (1 − |δ|)/2 where the feasible bound is (1 − δ)/2, so the
exact grid interval covered 0.075 in the detrimental direction, and that too was
reproduced before acceptance and fixed, with a sign-symmetry test and a
two-directional coverage enumeration added. Measured at n = 112 by exact
enumeration in two scenarios (beneficial, D ~ Binomial(112, 0.1) at δ = +0.10;
detrimental, C ~ Binomial(112, 0.5) at δ = −0.50), coverage is 0.924 and 0.953
for the idealised cluster bootstrap, 0.960 and 0.953 for Tango, 0.997 and 0.984
for the exact unconditional. **Those are coverages of two estimands under
independent instances, and coverage of the primary interval under the clustered
design actually used is unvalidated**; an earlier blanket claim that every
interval is 2 to 5 points optimistic is withdrawn as unsupported. One caveat
travels with the bootstrap (`CORRECTIONS.md` item 4): where every discordant
pair points one way it cannot draw a resample of the opposite sign, so a bound
at zero is an artefact, and those rows are quoted from the unconditional
intervals instead. No point estimate changed under any of these changes.

**Multiplicity.** The two ceiling primaries, each declared singly before any
model call, are not corrected. Twelve comparisons were planned and sixteen
computed, so the correction family is every contrast reported with a p value,
size 16, Bonferroni threshold 0.05/16 = 0.00313, stated once and applied
everywhere, with the planned, performed and exploratory inventory
machine-readable in `numbers.json`. Five planned comparisons, the mixed-family
and `astra` asymptote contrasts, were not delivered as specified and are
recorded as unmeasured; every flag contrast is exploratory, because the plan
named outcome contrasts. Nine studies over two tasks by one author on one
harness is itself part of the multiple-comparison picture
(`EXPERIMENT_RECORD.md` §4).

**Noise floors, each tied to the estimand it bounds.** No difference is called
"inside the noise floor" without a replicate arm for the same estimand. On code,
three full draws of the shipped architecture over all 290 frozen instances give
16, 12 and 9 flags of 110 stratum-P instances, **a widest pair of 6.4 percentage
points at n = 110**, and 11, 7 and 6 of 55 on the confirm half, a widest pair of
9.1 points at n = 55; the stratum-C column is stable at 5, 5 and 4 of 74. The
1.8-point figure preregistered as the floor
(`records/code/PREREGISTRATION-explore.md`) is the narrowest available pairwise
comparison on one batch, and is superseded (`CORRECTIONS.md` item 12). On prose,
four replicates over 20 byte-fixed drafts give pooled recalls of 23.5, 19.4,
25.5 and 25.5 percent, **SD 2.89 percentage points (95% bootstrap CI
[1.26, 7.75]), range 6.12 points**, which bounds audit-stage variation on fixed
drafts and nothing else. Where generation changes, the governing floor is the
generation-inclusive replicate: three draws giving draft F1 of 9.72, 10.42 and
6.94, **SD 1.84 F1 at n = 8**. `AUTHOR_INPUT_NEEDED: a committed record path
for that generation-inclusive replicate; it is quoted in `CORRECTIONS.md`
item 10, but no study-5 records are mirrored into this repository.` Neither
detection floor bounds the ceiling loop's estimand; the loop's own replicate arm
does.

**Power.** For the ceiling loop, the two-sided exact McNemar test had power
**0.32 against a true improvement of +5 percentage points, 0.60 against +7.5 and
0.81 against +10**, under a model stated because a power figure without its
model is meaningless: 112 **independent** multinomial pairs, worsening
probability fixed at its observed value (`[PENDING: ceiling r4]`) and
improvement probability that value plus δ, so total discordance varies with δ.
It is instance-independent, and is not a power calculation for the clustered
procedure actually reported.

**Quotation rules.** `EXPERIMENT_RECORD.md` §9 and §10 bind every later use of a
result, not only its computation. A rate quoted without its interval is a
defect; a count small enough that its interval reaches an absurd bound is quoted
as the count; a claim inherits the narrowest scope of its evidence. "Inside the
noise floor" may be written only where a replicate exists for the same estimand,
and it names the measured spread; otherwise the honest form is that run-to-run
variation is unmeasured for that contrast. An interval names its method and the
quantity it covers in the same sentence, "exact" being an algorithm and not a
guarantee, and any interval built by transforming or conditioning has its
coverage simulated at the study's n and that simulation committed as a test. A
point estimate may be quoted with its p value before its interval is repaired;
an interval may not.

**Software and deviations.** Python 3.13.5 on macOS 26.6.2 arm64 throughout;
the code studies' test executor is Python 3.13.5 with numpy 2.4.0 and a
30-second per-suite timeout (`records/code/study1/manifest.json`,
`environment`). The ceiling study's inferential code uses no SciPy and no NumPy:
the regularised incomplete beta, the Clopper–Pearson inversion, the exact
McNemar tail, Tango's score interval, the exact unconditional inversion, the
cluster bootstrap, the sign-flip test, the saturation fit and the beta-binomial
likelihood are standard-library implementations in `report_ceiling.py`, and 15
tests in `tests/test_ceiling_stats.py` check each against brute force or its
defining property, including coverage enumerations for every interval method.
`AUTHOR_INPUT_NEEDED: package versions for studies 1, 2 and 7, whose manifests
record Python, the OS and the executor's numpy version but no package
inventory.` Every study lists its departures from plan, numbered, each with the
direction of its bias or an explicit statement that the direction is
undetermined. The classes recorded are: provider failures and resumed runs,
whose affected instances are selected by when the network faulted and not by
content; duplicate rows resolved by a keep-first rule fixed before the rows were
inspected; arms that bypass the same-vendor guard; a study-supplied
deterministic check outside the product's source digest; part-reconstructed cost
attributions, marked at every occurrence; prompt-cache-warm repeat draws that
understate what K independent draws would cost; post-run edits to display-only
code; discarded pilots, and one arm set discarded and re-run in full;
outcome-informed protocol adaptation on instances also in the analysed sample,
direction undetermined; planned comparisons not delivered; a post-hoc
interval-method replacement; and provenance completed after the runs. Two
earlier "bias: none" statements were themselves corrected to "undetermined" by
independent review.

## Reproducibility and independent review

Every number in the committed reports regenerates from the committed records
with no API key and no network, by running each study's own report script over
its records directory. Records are one JSONL row per (arm, draw, instance),
carrying the stratum, the flag, verdicts, rule ids, finding and property hashes,
the components a score is built from rather than the aggregate alone, tokens,
cost, wall time, and prompt and response digests. They are corpus-free: no
dataset text, no model finding prose, no generated prose output and no prompt
embedding any of these; EvalPlus is redistributable, so candidate and revised
code solutions may be committed, while ExpertLongBench derivatives may not.
Every study is preregistered before spend, with its hypothesis in falsifiable
form, one named primary outcome, its named secondaries, its arms and what is
held fixed, its intended n, its stopping rule, and where applicable a kill
condition that can end the line of work; two have fired and are reported as the
result rather than replaced by a second objective, the executable-check
proposal's and the ceiling loop's (`[PENDING: ceiling r4]`). Full run
directories, which carry corpus-derived material, are archived outside any
repository at `~/Documents/Crossaudit/study-data/` with per-file and
directory-level sha256 manifests whose digests are committed
(`ARCHIVE_MANIFEST.json`).

The measurement code itself was reviewed across vendors, and that is part of the
method rather than an afterword. Under the rule recorded as D153, no measurement
is published, quoted or used to move a product default until a model from a
different vendor has reviewed the harness, the scorer and the statistics; the
review is dispatched read-only, and anything it reports is reproduced from the
archived run data before it is accepted, because a cross-vendor reviewer reduces
correlated error and is not an oracle. The first such review
(`reviews/2026-09-05-cross-vendor.md`) returned five publication-blocking
findings, among them a primary outcome conditioned on a post-treatment variable
that had been written into the preregistration itself and so was inherited by
every same-vendor review that checked the analysis against the plan; it also
corrected an error in `CORRECTIONS.md`'s own first version. It returned explicit
negative findings on the two questions that most threatened the results: CLEAR's
denominator, containment directions, per-sample F1 and aggregation match the
published procedure with no chain-of-thought reaching the extractor or
comparator, and no hidden-test leakage was found in the code study through
prompts, imports, fixtures, caches or filesystem behaviour, the population
reproducing exactly. Three further reviews have read the ceiling study: the
first two refused quotation approval and each found a defect in its interval
method, the third approved subject to reporting corrections, and a fourth is in
progress, which is why no ceiling result is quoted here. In each round the
author's own checks had not found the defect, and a reader who did not share the
author's assumptions did.
