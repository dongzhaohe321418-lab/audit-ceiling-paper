**I would not preregister E5 as written.** The programme has a potentially strong empirical contribution, but its present definition of reach, treatment of benchmark disagreement and proposed negative tests cannot establish the central thesis.

I read the programme, the draft’s included sections, E1’s registration and implementation, the taxonomy records, and E3’s registration. The counts below were recomputed from the frozen records.

**(a) Must-fix before preregistering E5**

**1. Replace asymptotic reach as the primary estimand.**

For a fixed configuration with stationary, conditionally independent readings,
\[
R_c=\frac1N\sum_i\mathbf1[p_{i,c}>0]
\]
is a mathematically well-defined limit. **Structural zeros are not distinguishable from sufficiently small positive probabilities in this experiment.** Sixteen unsuccessful readings do not establish that an item is unreachable.

There is also a substantive problem: logical entailment is unnecessary for \(p>0\). An auditor can guess a missing convention or reproduce a memorised benchmark answer. A stochastic model could therefore have positive probability of producing a valid witness for almost every item, despite lacking the information needed for reliable diagnosis.

The proposed plateau test does not solve this. If every item has \(p=0.001\), then:

- asymptotic reach is **100%**;
- coverage at 16 readings is approximately **1.59%**;
- the gain from readings 9–16 is approximately **0.79 percentage points**.

That passes the proposed 5-point plateau criterion while leaving almost the entire population undiscovered. Moreover, diminishing increments follow mathematically from the mixture-of-geometric model; they are not evidence of an informational boundary.

**Chao2 should remain a secondary sensitivity analysis.** It estimates a lower bound on richness under its sampling model, not an upper ceiling, and its realised estimate is not automatically a confidence bound. Heterogeneous rare-item probabilities can leave substantial undetected mass. Similar Chao2 estimates across configurations do not establish similar asymptotes. The original methodological account explicitly distinguishes lower-bound estimation from conditions giving approximately unbiased richness estimates. [Chao and Colwell, 2017](https://www.idescat.cat/sort/sort411/41.1.1.chao-colwell.pdf)

**Better primary estimator:** finite-budget verified-diagnosis coverage, with a frozen decision policy and a specified clean-flag constraint. For ordinary union coverage, use exact subset averaging:
\[
\widehat U_c(k)=\frac1N\sum_i
\left[1-\frac{\binom{m-s_{i,c}}k}{\binom mk}\right],
\]
where \(s_{i,c}\) counts successful readings among \(m\). Estimate paired differences and marginal gains over prespecified budgets. Call these finite-budget coverage and additional discovery, not estimates of an asymptote.

There is no assumption-free “better estimator” that rescues \(R_c\). A minimum positive detection probability or a parametric mixture model would make extrapolation possible, but the resulting ceiling would depend on that assumption.

**2. Actually impose the clean-flag budget.**

The [programme’s definition](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/plan/icml2027/CEILING_PROGRAM.md:13>) specifies a fixed budget; E5 merely reports clean flags as secondary outcomes. These are different designs.

For an OR aggregation, clean-item flags also accumulate:
\[
F_c(k)=\frac1{N_0}\sum_j[1-(1-q_{j,c})^k].
\]
A 1% per-reading flag probability becomes approximately 15% over 16 readings. Fixing the per-reading budget does not fix the cumulative budget.

Before registration:

- Specify a numerical **cumulative** budget \(\alpha\).
- Select thresholds or aggregation policies using development controls, then freeze them.
- Evaluate both coverage and budget compliance on held-out controls, with uncertainty.
- Treat configurations exceeding the budget as failing the constrained comparison.
- Give vendor unions their own calibration.

If thresholds change with \(k\), the policy changes with \(k\); the original fixed-\(c\) asymptotic formula no longer describes that sequence.

Also retain E1’s accurate terminology, **test-passing controls**. Of the 150 controls, **68 are reference implementations, 24 come from the other generator and only 58 from the same generator**. Passing the suite does not establish semantic correctness, particularly on AT_ODDS tasks.

**3. Validate the taxonomy and align it with the scored outcome.**

Freezing labels before E5 prevents outcome-driven relabelling. It does **not** establish that the labels measure information availability independently of model capability.

The taxonomy raters are also the proposed strong auditors. Their shared interpretation of the task can generate both a DETERMINED label and successful auditing. Thus E5-H1 is an association involving model judgement, task difficulty and benchmark composition, not a causal test of an information bound.

More seriously, [`stage_taxonomy`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:845>) labels the **first failing input**, whereas E5 counts **any verified witness against the programme**. An OPEN-labelled programme may contain another, fully specified defect. Finding that defect neither crosses nor disproves an information boundary.

Choose one aligned unit:

- a target behavioural discrepancy, with diagnosis required to address that discrepancy; or
- a programme whose relevant failure modes have been independently characterised.

A defensible validation protocol would have two independent human programmers rate all 150 items, followed by third-person adjudication. If resources require sampling, prespecify a stratified sample, for example 20 per existing class, and weight population summaries appropriately. Validate every item contributing to a definitive benchmark-error claim.

Require evidence for each classification:

- **DETERMINED:** a cited requirement and independently checked derivation of the expected behaviour.
- **OPEN:** two explicit, executable behavioural contracts that humans judge compatible with the supplied specification but that disagree on the target behaviour.
- **AT_ODDS:** an explicit contradiction between the specification and the reference, supported by independent computation.
- **Outside-domain/unclear-domain:** a separate designation, not silently absorbed into OPEN or AT_ODDS.

Initially hide which displayed output comes from the reference and randomise output order. Keep raters blind to auditor outcomes and model labels. Report pre-adjudication agreement, the confusion matrix, class-specific agreement and problem-cluster uncertainty, alongside Cohen’s \(\kappa\). **Agreement is evidence of reliability, not validity.**

The current model agreement is **84%, \(\kappa\approx0.754\)**. That is useful, but insufficient. Fifteen of the 24 disagreements are Claude AT_ODDS versus GPT OPEN. The rubric’s phrase “arbitrary artefact” is conflating unsupported conventions with genuine contradictions. For example, both raters label MBPP/278 AT_ODDS while their reasons explicitly say the task leaves the relevant behaviour undefined.

Execution validates behavioural differences; it cannot, by itself, prove what natural-language instructions entail.

**4. Separate AT_ODDS from the primary information-limitation population.**

The **47/150 figure is currently a model-labelled rate in a selected hidden-test-failure population**, not a verified benchmark-wide label-noise rate.

Use three separate scientific targets:

| Population | Appropriate interpretation |
|---|---|
| Independently validated DETERMINED defects | Failure to diagnose is an audit miss. |
| Validated OPEN discrepancies | Agreement with the hidden convention measures benchmark conformance; clarification or justified abstention may be appropriate audit behaviour. |
| Validated AT_ODDS discrepancies | Agreement with the suite may reward an incorrect diagnosis; disagreement may demonstrate correct auditing. |

Retain all items in a descriptive **suite-conformance** analysis, but exclude validated reference contradictions from the denominator of **semantic defect-detection recall**. Analyse them separately as benchmark-error cases, including whether the auditor identifies the specification–reference conflict.

The programme’s proposed interpretation, “the auditor sides with the suite against the task”, is justified only when its witness addresses the contradictory behaviour. A different, legitimate defect in the same programme does not support that interpretation.

Controls need the same treatment: a suite-passing implementation can deserve a flag when it implements the suite’s erroneous convention.

**5. Redesign the E5 hypotheses and power analysis.**

The actual population is smaller than “98 items” suggests:

| Class | All items | Held-out test items |
|---|---:|---:|
| DETERMINED | 28 | 22 |
| OPEN | 51 | 39 |
| AT_ODDS | 47 | 28 |
| DISPUTED | 24 | 18 |

The 150 items cover **97 problems**. OPEN/AT_ODDS together cover **64 problems**, or **44 problems among 67 held-out test items**. The 39 test OPEN items cover **29 problems**.

Fresh readings do not make previously examined development items an untouched confirmatory sample. Use development items for calibration and execution piloting; use test items or newly collected problems for confirmation.

Specific changes:

- **H1:** downgrade the class contrast to a secondary association. A DETERMINED–OPEN difference does not identify the proposed mechanism.
- **H2:** describe \(U(16)-U(8)\) as a bounded marginal-gain test. Do not call it a test that sampling cannot cross a ceiling.
- **H3/H4:** an upper bound below +10 points establishes “no improvement as large as 10 points”, not equivalence. For equivalence, the entire appropriate interval must lie within \([-\delta,+\delta]\). A large deterioration presently satisfies these hypotheses.
- **Net gains can conceal changed coverage:** ten newly diagnosed items and ten lost diagnoses yield zero net improvement. Report gained/lost items and overlap, not only the difference in aggregate coverage.
- **Margins need a scientific justification:** accepting a 9-point capacity gain while calling a 5-point information gain substantive cannot establish that information uniquely moves reach.

The power problem is concrete. With **zero** late discoveries among 51 independent OPEN items, the exact one-sided 95% upper bound is approximately **5.7%**. Among the 39 held-out OPEN items it is **7.4%**. Even that favourable outcome cannot establish a gain below 5 points using these bounds. Clustering prevents treating these item counts as independent evidence.

For an illustrative paired binary contrast with 20% discordance, zero true difference and no clustering, approximately **124 independent pairs** are needed for 80% power to rule out a +10-point improvement using a one-sided 5% test; approximately **495** for +5 points. These are planning illustrations, not a substitute for simulations of the actual design.

Simulate power and interval coverage using the real cluster sizes, plausible discordance, repeated-reading dependence and calibration uncertainty. **Ten thousand bootstrap draws do not create information.** Ordinary percentile bootstrapping is particularly dangerous when every observed late-discovery indicator is zero: it returns an unjustified zero-width interval.

Prespecify multiplicity. Choose a primary contrast and use hierarchical testing or simultaneous intervals for additional confirmatory comparisons. A genuinely conjunctive claim requiring every configuration to pass can use an intersection–union formulation without automatic Bonferroni correction; separate configuration claims and selecting the largest observed effect require additional protection.

**6. Put information and capacity interventions on the same population.**

Comparing E1’s effect on **29 admitted test items** against the largest capacity effect on a different population cannot establish which lever matters more.

There is a further consistency warning: those 29 admitted items comprise **19 OPEN, 2 DETERMINED, 4 AT_ODDS and 4 DISPUTED** under the taxonomy. This does not automatically invalidate their clauses, but it requires reconciliation before the taxonomy supports mechanism claims.

Use a common, independently validated population with a crossed design:

- unchanged evidence, attention pointer, partial resolution, full resolution;
- lower and higher reasoning budgets within the same model;
- execution access as an additional factor or prespecified secondary comparison.

The partial-information arm should genuinely narrow the possible contracts without resolving the target behaviour. A pointer is not a substitute. Use nested revelations of requirements or constraints, with length and attention controls, to obtain an information dose–response.

Freeze falsification criteria. For example: does additional information improve constrained coverage beyond a pointer, and does it change the return to additional computation? A strong capacity effect must remain a possible result, not something reclassified afterwards as “information from priors”.

**7. Fix the scorer and specify the execution route before freezing anything.**

I found a concrete endpoint defect. In [`judge_call`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:250>), Python `None` represents both a legitimate expected value and “no expected value supplied”. Consequently, a correctly stated expected `None` cannot receive `expected_correct=True`. I confirmed the downstream behaviour using an extracted-function check without modifying files. Four selected items have `None` as their first-failure reference output. Two others require `inf`, which the literal-only endpoint cannot express directly.

Before E5:

- Distinguish missing expected values from legitimate `None`; specify supported numerical values and exceptions.
- Validate witness inputs against the intended domain. “The reference runs” is not sufficient.
- Establish that scoring restrictions do not create artificial class-specific non-detection.
- Preserve the existing E1 record and document any correction and rescoring transparently.

For execution, keep **the same visible evidence** as the base route. “No tests” must mean no hidden tests; removing visible tests changes information as well as tools.

Specify model versions, reasoning settings, tool-call limits, time/token budgets, dependencies, permitted filesystem access, failure handling and logging. The existing `aud-gpt-sol` route is **medium**, while E5 proposes **high**. Verify the actual configuration.

A fresh directory alone is not isolation. Demonstrate that neither route can access hidden suites, references, neighbouring items or network sources, and that execution works on suitable development positive controls. Keep offline witness verification unavailable to the auditor.

The proposed schedule entails **16,800 audit sessions before retries**, with execution sessions potentially containing several model turns. Report tokens, elapsed time, tool use, retries and monetary cost, plus calibration, human validation and clause-construction costs. Failure-informed clauses require privileged access during construction; their benefit is not automatically an operationally available, equal-cost intervention.

**(b) Recommended changes**

**1. Retain the research question; replace the universal thesis.**

“Information limits what can be established” is sound but familiar. “Capacity moves rate, information moves reach” is too strong:

- More capable algorithms can make previously inaccessible diagnoses possible.
- Different models contain different learned information.
- Execution can expose consequences of information already supplied.
- An underspecified answer can still be guessed correctly.

A stronger empirical proposition is: **under specified resource and false-flag constraints, resolving independently established ambiguity changes attainable audit coverage beyond attention controls, with effects distinguishable from additional computation.** That is falsifiable and potentially valuable. Simply showing that auditors perform worse on model-labelled ambiguous tasks is unlikely to constitute an ICML-level contribution.

**2. Make one coherent paper, with one convincing transfer study.**

The evidence map currently treats unlike interventions and outcomes as if they measured the same mechanism.

| Component | Recommended role |
|---|---|
| E1, redesigned E5 and operating curves | Main paper’s experimental core. |
| Independently validated taxonomy | Main-paper measurement foundation. |
| E3 on held-out datasets | Main-paper transfer study if it tests an aligned evidence intervention and constrained endpoint. |
| Scientific results | Compact illustration or appendix unless evidence access is experimentally varied. |
| Existing SciCode reframing study | Appendix/context; it changes task scope and measures flags under substantial label uncertainty. |
| Historical route, rulebook and recovery studies | Appendix, with failures and exclusions retained transparently. |

Two mappings need correction. First, the scientific-results auditor often succeeds by calculating from supplied code, not by supplying missing domain priors. This supports a computation explanation. Provenance checks missing mutually consistent fabrications establish a limitation of those checks, not of all auditors given those artefacts.

Second, [E3’s registration](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/ai4s_e3/PREREGISTRATION-E3.md:54>) compares the **profile validator plus model** against the profile validator. Its H2 permits an additional ten points of clean flags; it does not impose a common absolute budget. Complementarity at that operating point is not evidence that an information ceiling moved.

For eight pages, prioritise the core identification experiment and one external validation. Four application headings cannot substitute for a common estimand. Add a fresh, independently validated substrate rather than deriving broad claims mainly from HumanEval+/MBPP+ failures. If scientific code remains prominent in the title, it needs direct evidence for the central mechanism.

**3. The single most important change: build an independently validated information-release experiment.**

Construct matched cases where the **same observed task and candidate are compatible with two contracts**, but the candidate is correct under one and defective under the other. Randomise the hidden contract independently of model-accessible clues, then reveal its requirements progressively while varying computation.

Without the distinguishing information, the two conditions are observationally identical: their flag probabilities must match, so recall cannot exceed the clean-flag budget on that balanced indistinguishable component. Revealing the contract breaks that restriction. Human-validated natural examples can then establish external relevance.

This gives the paper a model-independent identification argument, a causal manipulation and a clear empirical failure condition. It would raise acceptance prospects more than extending the present original-text-only sampling grid.

**(c) Verdict**

**This programme can support an ICML main-track paper, but the current design does not yet support its proposed claim.** Its strongest assets are executed verification, within-item interventions, explicit attention controls and unusually transparent records of failed designs. Its main weaknesses are an empirically unidentified asymptote, taxonomy–endpoint mismatch, conflation of underspecification with erroneous benchmark answers, and inadequately powered claims that capacity gains are negligible. I would currently lean reject on methods and contribution, rather than presentation. A controlled information-release experiment, independently validated labels, finite-budget comparisons at a genuine common clean-flag constraint and one convincing external replication could turn it into a strong paper about when audit failures are remediable by computation, clarification or better ground truth.