**Version 2 is substantially stronger, but I would not preregister E6 unchanged.** The main remaining problems are the mismatch between the theorem and the scoring endpoint, the proposed extension to natural failures, and E6-2’s interpretation.

I read the previous review, revised programme, E1 registration, implementation and frozen records. Read-only, in-memory checks confirm that expected `None` is now distinguished from missing expectations, and that the non-finite literals parse. The earlier scorer defect is closed; semantic validation remains separate.

**(a) Must-fix before preregistering E6**

**1. State the theorem precisely, and remove the unsupported natural-population corollary.**

Proposition 1 is correct for a **common binary decision rule** applied to a complete observation. Define \(E\) explicitly to include the candidate programme, specification, visible tests and all other accessible information. For a randomised flagging policy \(\phi(E)\in[0,1]\),

\[
\operatorname{TPR}-\operatorname{FPR}
=\int\phi\,d(P_1-P_0)
\leq \operatorname{TV}(P_1,P_0).
\]

The sharp constrained envelope is

\[
\beta_E(\alpha)=
\sup_{\phi:\,\mathbb E_0\phi\leq\alpha}\mathbb E_1\phi.
\]

This is the Neyman–Pearson testing problem, allowing randomisation at thresholds. **It is a textbook fact, not a new theoretical contribution.** Present it as a classical testing bound specialised to auditing, with a short proof and explicit assumptions. Referees should credit the experimental identification and measurement framework built around it. [Rigollet’s notes, §5.3](https://ocw.mit.edu/courses/18-s997-high-dimensional-statistics-spring-2015/619e4ae252f1b26cbe0f7a29d5932978_MIT18_S997S15_CourseNotes.pdf)

The corollary is also correct **with its stated component-specific constraint**. If \(S\) denotes the indistinguishable component, \(\pi=P(S\mid D=1)\), and \(\operatorname{FPR}_S\leq\alpha\), then

\[
\operatorname{TPR}\leq1-\pi+\pi\alpha.
\]

It does **not** follow from an overall FPR constraint alone. If \(q=P(S\mid D=0)\), the corresponding bound is only

\[
\operatorname{TPR}\leq
1-\pi+\pi\min(1,\alpha/q).
\]

More seriously, [Section 4](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/plan/icml2027/CEILING_PROGRAM.md:91>) does not establish distributional indistinguishability at all. Two contracts being compatible with a specification is a statement about **logical ambiguity**. It does not imply that natural defective and correct programmes have identical evidence distributions. Benchmark provenance, coding conventions, programme structure and memorisation can all predict the benchmark’s fixed contract.

Consequently:

- Human validation estimates **ambiguity prevalence in the selected failure population**, not \(\pi\) in a demonstrated natural-distribution ceiling.
- An OPEN miss cannot automatically be attributed to missing information.
- A DETERMINED miss is a residual audit failure, not an experimentally isolated capacity deficit.
- The theorem does not imply that computation cannot improve natural audit performance.

The clean information bound belongs to the **deliberately randomised contract population**. Keep the natural-population analysis descriptive unless additional identification assumptions are supplied.

**2. Separate flag discrimination from verified diagnosis.**

The programme currently combines verified-diagnosis recall with clean-programme flags, then calls their difference Youden \(J\). These are useful operational quantities, but they are not the same binary test.

For one unrevealed unit, let \(f_A\) and \(f_R\) be flag probabilities on \(C_A\) and \(R\). With balanced contracts and identical readings reused under both,

\[
\operatorname{TPR}_{\rm flag}
=\operatorname{FPR}_{\rm flag}
=\tfrac12(f_A+f_R).
\]

Thus **flag-based \(J=0\) exactly by construction**, including at fixed aggregation thresholds. Repeated scoring supplies no additional independent observations.

If \(v_{AB}\) and \(v_{RA}\) instead denote verified diagnoses in the two defective cells,

\[
\operatorname{TPR}_{\rm verified}-\operatorname{FPR}_{\rm flag}
=\tfrac12(v_{AB}+v_{RA}-f_A-f_R)\leq0.
\]

Equality need not hold. The TV upper bound still follows because verified detection implies a flag, but the indistinguishability equality does not. Defining clean FPR as *verified disagreement* would be worse: it is necessarily zero for a correct oracle implementation and no longer measures false accusations.

Register two distinct outcomes:

1. **Flag discrimination:** conventional TPR, FPR and \(J\), using one observable decision policy.
2. **Actionable audit performance:** verified-diagnosis coverage under the cumulative flag constraint.

Does symmetry make E6-1 trivially true? **It makes its unrevealed baseline trivial, not its positive result.** Auditors could ignore resolution, flag both programmes, or produce invalid witnesses. However, demonstrating merely \(J_{\rm resolve}>0\) establishes that auditors can use an explicit requirement in an engineered task. That alone is a modest contribution.

The substantive empirical content is the magnitude of valid detection at low FPR, failures despite resolution, sensitivity to computation, and persistence across independently constructed cases. With the mixed endpoint, a positive improvement could even mean moving from \(-0.4\) to \(-0.2\), so require satisfactory absolute performance too.

There is another consequence: with ordinary flag \(J\), **E6-3’s menu high-minus-low term is identically zero**. Its “interaction” reduces to the reasoning-budget effect after resolution. That is useful, but should not be presented as an independently observed interaction between two non-degenerate effects.

**3. Strengthen construction beyond agreement on existing hidden inputs.**

The [admission rule](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/plan/icml2027/CEILING_PROGRAM.md:45>) does not establish “same discrepancy, no new defect”.

| Failure mode | Required protection |
|---|---|
| \(C_A\) changes unrelated behaviour outside the existing suite. | Define the target input class explicitly; inspect the semantic change and test target, boundary and non-target inputs independently of construction. |
| \(C_A\) changes only one memorised failing input, while retaining B elsewhere in the target class. | Specify A as a general behavioural rule. Require class-wide consistency on independently generated cases, rather than merely one separating input. |
| `suite_A` reproduces an accidental mistake in \(C_A\). | Define contract A independently of \(C_A\), then validate an oracle against that contract. Deriving every expectation from the audited implementation is circular. |
| Return values agree but mutation, exceptions or other relevant behaviour differ. | Freeze the behavioural scope and domain. Validate those behaviours where the contract includes them. |
| Numerical comparison makes A and B effectively equivalent, or treats valid outputs inconsistently. | Freeze tolerances, shapes, types, NaN/inf handling and exception semantics before construction. |

A defensible construction order is:

**behavioural contracts → independent implementations → independent validation inputs → admission → frozen audit prompts.**

The existing hidden inputs remain useful validation evidence, but cannot certify unrestricted programme equivalence. Restrict claims to a validated target discrepancy unless stronger equivalence evidence exists.

For the arms and programme presentation:

- **Menu order and wording:** randomise option order independently of contract assignment; make the same menu bytes available under both hidden contracts. Avoid labels such as “standard”, “reference”, “alternative” or “corrected”.
- **Distinguish two leakage problems:** putting B first cannot reveal a genuinely independent hidden contract. It can nevertheless induce B preference and contaminate E6-2. Actual information leakage occurs when presentation depends on the assigned contract.
- **Resolution:** use the same menu plus a short selection requirement, with equal specificity for A and B. Do not supply a witness, implementation patch or extra algorithmic guidance only in resolving arms. Stating the disputed requirement is the intended intervention; explaining how to fix the programme is an additional intervention.
- **Reference recognition:** an untouched HumanEval/MBPP reference paired with a model-edited \(C_A\) is asymmetric. Memorisation and suspicious editing style can explain preference for \(R\). They cannot defeat exact contract randomisation, but they can dominate E6-2.
- **Counterbalance construction provenance:** include pairs where both implementations undergo the same rewriting pipeline, and sensitivity variants with neutral names and formatting. Include fresh tasks; renaming alone does not remove memorisation.
- **Retain all four resolved programme–contract cells**, including the correct cells needed to measure false flags.

DETERMINED controls also need their own definition. If they undergo the same balanced counterfactual relabelling, their unrevealed flag \(J\) is zero too. To expect \(J>0\), evaluate them under their uniquely valid contract with appropriate correct controls.

**4. Replace E6-2’s “natural recall” interpretation.**

As registered, let

\[
r_B=P(\text{verified diagnosis of }C_A\text{ under B}),\qquad
r_A=P(\text{verified diagnosis of }R\text{ under A}).
\]

Then E6-2 is exactly

\[
r_B-\tfrac12(r_B+r_A)=\tfrac12(r_B-r_A).
\]

It measures **directional asymmetry on constructed programme pairs**. It does not identify inflation of E1 recall.

The problem is substantive: \(C_A\) is a rewritten reference. E1 audited the original generated programme \(G\), which can differ in structure, difficulty and additional defects. Moreover, \(r_B-r_A\) can reflect asymmetric editing, memorisation, witness complexity or expectation formatting, rather than convention preference alone.

Use two linked analyses:

- Rename the constructed contrast **benchmark-convention advantage**, with the construction and memorisation controls above.
- Establish the natural connection using **E1’s actual outputs on \(G\)**. Classify successful witnesses by the discrepancy they diagnose, then rescore relevant witnesses against validated alternative contracts.

Preserve E1’s programme-level union endpoint. If a reading supplies both a convention-dependent witness and a valid determined-defect witness, its successful diagnosis does not depend solely on the convention. Report successes supported **only** by convention-dependent witnesses separately from successes with independently valid support.

Even then, “inflation” requires a named comparator. Agreement with B is legitimate performance when B is the evaluation target. The defensible concern is that benchmark-conformance recall overstates **contract-robust diagnosis**.

**5. Make human validation proportionate, but validate every primary experimental pair.**

Two independent programmers are feasible for the current pool. At an assumed 10–20 minutes per person per unit:

- 51 units require approximately **17–34 person-hours**;
- 150 units require approximately **50–100 person-hours**;

both exclude adjudication and implementation checking. Pilot these timings rather than treating them as established costs.

My minimum acceptable protocol would be:

1. Train the rubric on approximately 10–15 development cases excluded from confirmation.
2. Have two programmers who did not construct the pairs independently assess each contract against the original specification and visible tests. Randomise order; hide benchmark provenance, model labels and auditor outcomes.
3. Require separate **compatible / incompatible / unresolved** judgements for A and B, with requirement citations, domain assumptions and a general behavioural rule.
4. Validate implementations and separating witnesses separately. One input-output example is insufficient to validate an entire input class.
5. Adjudicate disagreements and unresolved cases with a third person; inspect a random sample of agreements. Do not force unresolved cases into COMPATIBLE-BOTH.
6. Freeze eligibility before confirmatory auditing. Report initial agreement, class-specific disagreements, exclusions and adjudication changes.

Add a **neither-compatible** category. The current taxonomy does not cover all logical possibilities.

**Sampling is acceptable for population measurement.** For the existing 150-item frame, I would accept a prespecified sample of roughly **100 items covering at least 60 problems**, stratified by provisional class, benchmark and generator, with known inclusion probabilities and weighted estimates. Ensure meaningful representation of every provisional class. This is my practical review threshold, not an ICML rule or a precision guarantee.

For context, approximately 97 independent observations give a worst-case 95% margin near ±10 percentage points for a proportion; approximately 385 give ±5 points. Clustering and unequal weights reduce effective sample size; finite-population correction helps only for inference about the frozen frame.

**Sampling cannot silently certify unreviewed E6 pairs.** Either validate every pair entering the primary human-validated analysis, or restrict that analysis to the validated probability sample and power it accordingly. Validate every specific benchmark-error claim individually.

**6. Power the number of independent problems, and define the enlarged population.**

I recomputed:

| Current model-labelled OPEN pool | Items | Distinct problems |
|---|---:|---:|
| All | 51 | 38 |
| Development | 12 | 9 |
| Held-out test | 39 | 29 |

These are screening labels, not yet admitted E6 pairs. Some will disappear under stronger validation.

For a mean problem-level paired contrast with standard deviation \(\sigma_\Delta\), an approximate requirement for 80% power at a 10-point effect, using a two-sided 5% test, is

\[
n\approx
\frac{(1.96+0.842)^2\sigma_\Delta^2}{0.10^2}.
\]

| Problem-level contrast SD | Independent problems needed |
|---:|---:|
| 0.30 | 71 |
| 0.40 | 126 |
| 0.50 | 197 |
| 0.60 | 283 |

These are planning calculations, not an E6 power simulation. At \(\sigma_\Delta=0.5\), 29 problems support a detectable effect around **26 points**, not 10.

**My planning target would be approximately 200 eligible held-out problems**, with an outcome-blind enlargement rule if development simulations show greater variance. There is no defensible universal minimum without the pilot covariance structure. E6-2’s half-difference scaling must be included explicitly.

Simulations must reproduce programme pairing, repeated readings, configurations, cluster sizes, missingness and frozen aggregation. If the scientific success criterion requires *both* E6-1 and E6-2, target joint power; 80% marginal power for each is not 80% joint power.

Adding generators is valid for estimating treatment effects **within the resulting admitted population**, provided selection precedes auditor outcomes. It changes the population being sampled. Therefore:

- Freeze generators, generation budgets, selection rules and construction-attempt limits.
- Preserve problem-level development/test separation across generators.
- Report the entire admission funnel, including unsuccessful constructions.
- Specify whether weighting targets problems, generator–problem pairs or generated failures.
- Prioritise new problems over additional generations of the same problems.

More generators on the existing 38 OPEN problems do not create 200 independent problems. Nor can weights recover unobserved types of ambiguity that the construction process never admits.

The proposed grid costs **160 readings per unit**, or approximately **32,000 readings for 200 units**, before execution-route additions and retries. Reduce secondary factors before sacrificing independent problem coverage.

**7. Finish the operating-point specification.**

The revised common constraint is an improvement, but preregistration still needs numerical \(\alpha\), primary \(k\), threshold selection, missingness rules and the criterion for held-out compliance.

The stated union formula applies to an OR rule. Once the policy requires \(t>1\) flags, evaluate that actual policy through exact subset enumeration or the appropriate hypergeometric tail. For verified diagnosis, score the findings produced by the deployable policy; do not aggregate using hidden verification information unavailable to the auditor.

If compliance means an upper confidence bound below \(\alpha\), calibrate below \(\alpha\). Even with zero false flags, **59 independent clean cases** are needed for a one-sided 95% upper bound below 5%. Paired replicas and related programmes are not automatically independent controls.

**(b) Recommended**

**1. Make the empirical contribution larger than the engineered zero baseline.**

Report contract-conditioned false accusations, correct abstention or clarification requests, verified witnesses, and computational cost. Conditional statements such as “this is wrong if ties must be broken lexicographically” should not automatically count as unconditional defect allegations.

A useful additional arm would reveal the contract for a randomly chosen fraction of cases. This provides an intermediate information condition with a known theoretical envelope. It would make the study more informative than a binary comparison between complete ambiguity and explicit resolution.

Do not claim that finite experiments estimate the optimal ROC on natural programmes, or that changing model capacity cannot change useful performance.

**2. Scientific transfer is worthwhile only if it tests the same mechanism.**

**I would not incur substantial cost merely to preserve scientific code in the title.** A strong general-code identification study is preferable to a weak scientific extension.

The most practical offline substrate is a **prespecified numerical subset of DS-1000, especially NumPy/SciPy tasks**. Its release contains locally loadable data, reference computations and executable test contexts. Select deterministic tasks that can be adapted to explicit function contracts, and disclose adaptations and any changes to surface-form constraints. This supports numerical/data-science transfer, rather than broad claims about research software. [Official DS-1000 release](https://github.com/xlang-ai/DS-1000/blob/main/README.md)

SciCode is scientifically closer but operationally harder. Its official evaluation requires separately downloaded HDF5 targets. Your historical gate records gold-code limitations and environment-sensitive failures; the recorded local data paths are currently absent. That history does not establish present offline readiness. [Official SciCode setup](https://github.com/scicode-bench/SciCode)

There is also directly relevant recent work: **SciCode-Verified** addresses missing conventions, contradictory specifications and defective grading targets, with released corrections and an audit trail. It must inform both benchmark choice and novelty positioning. Your distinguishing contribution would be randomised-contract **auditing**, rather than another demonstration that repairing specifications improves scores. [SciCode-Verified](https://arxiv.org/abs/2608.04975)

For a modest transfer claim, approximately **50 independent scientific/numerical problems** could be reasonable if the intended effect is around 20 points and pilot variance supports it. Ten-point claims require substantially more.

Drop the prediction that scientific \(\pi\) is larger unless both domains use comparable sampling and validation. Selecting scientific examples specifically because they contain convention ambiguity cannot establish greater natural prevalence.

**3. Present the theory as an organising tool.**

The creditable package is a validated experimental design, reliable measurement, and substantive findings about when clarification changes useful auditing. Explicitly distinguish:

- classical statistical limits;
- guarantees supplied by experimental construction;
- observed model behaviour;
- transport to natural programmes.

This separation strengthens the contribution rather than diminishing it.

**(c) Verdict**

The prospective one-sentence contribution is:

> **A human-validated, contract-randomised audit benchmark separates benchmark-convention agreement from reliable defect diagnosis and measures how clarification and computation affect verified detection at a fixed false-flag budget.**

**My current judgement is borderline, improved from reject.** I would lean accept for a well-executed programme incorporating the corrections above, especially a convincing bridge to original E1 programmes and substantial gains in verified detection at controlled false-flag rates.

A textbook inequality, an algebraically zero baseline and positive performance after explicit resolution would not, by themselves, clear the ICML main-track contribution bar.

