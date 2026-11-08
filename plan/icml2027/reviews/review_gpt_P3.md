**Do not freeze E6 or begin test audits yet.** The complete-data arithmetic is sound, but I found reproducible oracle failures, incomplete enforcement of the reading policy, and unresolved semantic admission problems. These affect the experiment’s labels and estimand.

I reviewed commit `9dca3a7`, the three previous reviews, programme v3, both registrations, and the requested code and records. I inspected **20 open units and 14 positive controls**, including their specifications, rules, shown implementations and arm texts. Both saved development analyses reproduce exactly. I also re-executed the stored class/other-input comparisons for all 125 execution-admitted development units. No files were changed or model calls made; no test audits exist.

First, the headline mixes populations:

| Quantity | Registered 50-unit population |
|---|---:|
| None: flag TPR = FPR | **11.75%** |
| Menu: flag TPR = FPR | **1.00%** |
| Resolved flag TPR | **100%** |
| Resolved FPR | **0.75% [0, 2.00]** |
| Resolved verified coverage | **94.50% [89.00, 98.75]** |
| Resolve-minus-menu verified coverage | **+94.50 [89.00, 98.75] points** |
| Convention advantage | **+10.50 [6.00, 15.50] points** |
| High-minus-low after resolution | **+1.00 [−1.00, 3.00] points** |

The supplied 13.4%, 1.6%, 95% and +0.9 figures describe **all 55 execution-admitted units**. There are 3,520 valid development readings overall, but **3,200 belong to the registered population**.

The positive-control results reproduce as supplied, with one qualification below. Their **94.8% is flag TPR; verified coverage is 90.1%**, so the apparent “95% versus 95%” comparison mixes endpoints.

**(a) Blockers before test**

**1. Repair and validate the executable contracts. Other-vendor implementation is not sufficient oracle validation.**

Two concrete counterexamples survived the current admission procedure:

| Unit | Read-only execution result | Consequence |
|---|---|---|
| **Mbpp/798, contract B** | On `_sum([10000000000000000, 1, -10000000000000000])`, the shown B programme returns the correct integer sum, `1`; its B oracle uses `sum(array, 0.0)` and returns `0.0`. A witness expecting `0.0` receives `verified_diagnosis=True`. | The scorer can certify a false accusation against the supposedly correct programme. This input is also outside the proposed floating-point discrepancy class. |
| **Mbpp/557, contract B** | On `toggle_string("Ο\u0301Σ")`, the shown B programme returns `"ο\u0301σ"`; the B oracle returns `"ο\u0301ς"`. The scorer verifies their disagreement. | The designated correct B programme fails the contextual final-sigma rule on an uppercase Greek word containing a combining accent. |

These are **new stress probes**, not witnesses found in the saved audit records. They do not establish numerical inflation of the reported pilot; they establish that its correctness assumptions are insufficiently enforced.

The relevant admission checks in [e6.py](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:285>) are asymmetric:

- B–reference agreement is required on hidden inputs, but not explicitly on every proposed class/other input.
- A implementations must agree, but agreement does not establish that they implement A correctly.
- Separation on two examples and agreement on a few other examples do not establish that programmes differ only on the target discrepancy.
- The validation inputs come from the proposer; there is no independent boundary-testing stage.

All stored development class/other comparisons reproduced consistently with their intended behaviour, including the deliberate exceptions in positive-control Mbpp/65. The new counterexamples therefore demonstrate a **coverage problem in validation**, rather than corrupted stored results.

**Required change:** add independently constructed target, boundary and non-target probes; validate both implementations against each rule’s specified behaviour; require same-contract agreement throughout that validation set; and define executable domain and target-class predicates. Either make the programmes reliable whole-programme controls or restrict the primary endpoint to the validated target discrepancy, reporting unrelated defects separately.

The domain check also needs repair. In [judge_witness](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:1253>), “reference returns normally” is treated as domain membership. For positive-control Mbpp/762, `check_monthnumber_number(13)` passes that gate despite the explicit domain **1–12**. Reference execution is a useful check, but not a semantic domain validator.

**2. Reconcile semantic admission and downgrade what the judge panel certifies.**

My detailed open-unit sample was HumanEval/{18,20,89,125,146,162} and Mbpp/{8,65,72,129,130,142,233,276,429,465,477,557,784,798}. The positive-control sample was HumanEval/{0,30,146} and Mbpp/{8,65,72,172,421,424,435,557,762,798,804}.

My assessment is mixed:

| Cases | Assessment |
|---|---|
| HumanEval/20 tie-breaking; HumanEval/162 encoding; Mbpp/130 frequency ties | Convincing admissible alternatives. |
| Mbpp/142 numeric equality; Mbpp/477 casing convention; Mbpp/129 normal versus general magic squares | Defensible, with explicit interpretation assumptions. |
| HumanEval/125 empty fields; HumanEval/146 float digit representations; Mbpp/233 and /276 rounding | Plausible, but domain, representation and precision choices must be explicit. |
| **Mbpp/72, zero excluded from squares** | I would exclude this from a primary semantic-OPEN population. Zero is a square; absence of a zero example does not make that mathematical fact optional. |
| **Mbpp/784, missing parity** | Domain ambiguity remains unresolved. One judge explicitly says the task assumes both parities, then admits arbitrary fallback values. A domain extension is being treated as clarification. |
| HumanEval/89 uppercase rotation; Mbpp/8 sorted squares; Mbpp/465 retaining empty containers | Borderline interpretations deserving a sensitivity category, not unquestioned ground truth. |

The inspected positive-control misreadings are substantially cleaner: “closer than” excludes equality; positive numbers include 0.5; squaring a negative number gives a positive result; array summation counts occurrences; “all characters” excludes an ASCII-only case toggle. I found no comparable admission failure among these 14 controls. However, they are generally simple, conspicuous defects and are not difficulty-matched controls.

There is also a specific judging-prompt problem: class descriptions sometimes already assert that treatment is **“unspecified”**. Passing that assertion to the panel biases the question it is meant to answer. Furthermore, for HumanEval, `{spec}` contains the docstring examples, but does **not** include the full separate visible test file that auditors receive.

**Required change:** give judges neutral input-class descriptions and the complete visible evidence; require separate domain and rule-admissibility decisions; distinguish absent examples from genuinely permissible alternatives; resolve the identified contradictions before freezing.

**Human validation replacement:** a transparent model-screened benchmark can be acceptable research. This panel is **not equivalent to independent human semantic validation**, and behavioural frequency does not supply the missing validity evidence. The judges are also the same model routes used to implement the contracts, albeit in separate calls without programme text.

Use an operational population definition such as **execution-validated, two-model-compatible contract pairs**. Do not treat it as independently established ambiguity prevalence or human-validated correctness. E1 Amendment 4 acknowledges the change, but programme v3 still contains human-validation assumptions that must be reconciled.

For the actual primary development population, behavioural counts are **22 A, 540 B and 35 other**. Thus B accounts for **96.1% of A/B-classified solutions**, not 94.5%; the latter uses all 55 units. Only **five primary units** have at least one solution following each rule. That sensitivity subset will be small.

**3. Add a real completeness gate and freeze missing-data behaviour.**

In [analyse_e6.py](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:27>):

- Missing or infrastructure-failed witness scores silently become `False`.
- Any nonempty cell is accepted, even with one reading instead of two.
- Successful duplicate rows are accumulated rather than rejected or resolved by reading key.
- Configurations are averaged separately within each arm. Missingness can therefore make an arm contrast compare different configuration mixtures.
- The population filter checks the number of judges, rather than explicitly requiring the exact registered judge identities and matching evidence hashes.

I reproduced these failures in memory:

- Removing every witness record produces **0% resolved coverage over all 50 units**, without an error.
- One reading in one configuration is sufficient for a unit to enter the resolved analysis.
- Duplicating a single flagged reading converts a failed `t=2` cell into a successful one.

The open pilot is currently complete: no duplicate successful keys, missing required readings or missing required witness records. **The positive-control pilot is not:** Mbpp/797, programme A, Sonnet-low, reading 1 has one malformed attempt and no valid replacement. Its registered population has **847 rather than 848 valid readings**. It is nevertheless analysed.

**Required change:** reconstruct the exact frozen key universe; enforce unique readings, expected counts and prompt hashes; finish retries before analysis; distinguish a valid reply without a witness from an unscored witness. After exhausted failures, retain the frozen population and report prespecified missing-data bounds. Do not silently change the reading budget or configuration weights.

E6’s witness cache also lacks E1’s content-bound provenance: it keys reuse by reading and contract, without binding programme, oracle, comparator and scorer bytes. Repair this before rescoring or freezing.

**4. Fix boundary inference and specify which policy satisfies the false-flag budget.**

The cell mapping is correct: resolved A scores programme B against oracle A, and vice versa. Unrevealed readings are reused correctly under both contracts. Verified credit is restricted to flagging readings. Complete-data configuration averaging, paired contrasts and the registered bootstrap quantile indices are correct.

The remaining inference problem is substantive: `boot()` returns **[0,0] when every observed value is zero**. Both Sonnet FPR intervals currently have this form. Such intervals cannot certify a population error rate of zero or automatically establish equivalence.

For illustration, with zero events among 50 independent binary cases, the one-sided 95% upper bound is **5.82%**, not zero. This is not a replacement interval for the weighted E6 endpoint, but it exposes the problem.

Register and implement a boundary-sensitive method or conservative decision safeguard. For FPR, a problem-level indicator of *any* clean-cell flag supplies a conservative binary upper bound on the mean clean-cell flag rate. Equivalent safeguards are needed for claims about negligible computation gains.

Also distinguish:

- the **equally weighted average across four configurations**;
- each individual configuration;
- a union of configurations.

Only the first is currently primary. Terra-low’s development FPR upper endpoint is **5.0%**, so it does not satisfy the stated strict `<5%` criterion even under the existing bootstrap. Pooled compliance must not be reported as compliance of every configuration.

**5. Freeze the menu’s interpretation, and complete the registration contract.**

I found **no A/B contract leakage** in the unrevealed menu construction. Order is contract-independent, and resolution selects the correct numbered option. Shown provenance is balanced 25/25 in the primary development population.

However, “the task author has fixed which” plus “The task does not say which” explicitly tells the auditor that the missing decision cannot be recovered from the supplied task. It is a strong uncertainty cue. The resulting near-zero BLOCKER rate is therefore partly an expected response to the intervention’s wording. It is not independent evidence of a computational ceiling.

Nor is it uniformly abstention:

- **Sonnet:** 289/400 menu readings escalate; 111 pass.
- **Terra:** 8/400 escalate; 388 pass; four block.

Raw responses explicitly cite the missing selection when declining to issue a BLOCKER. The present experiment identifies the effect of **this menu-and-selection intervention**. A broader claim about ordinary clarification requires a wording control.

Make these exact amendments to [PREREGISTRATION-E6.md](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E6.md>):

| Section | Required edit |
|---|---|
| Prior exposure | Separate the 55-unit and 50-unit results; correct primary behavioural counts and SDs; disclose this review and every resulting amendment. |
| Population | Freeze exact IDs, exclusions, validation revisions, domain/target predicates, judge identities and evidence hashes. Define positive-control eligibility separately. |
| Construction | Freeze proposal/implementation attempt limits and selection rules; distinguish infrastructure failure from substantive rejection. |
| Design | State that unrevealed observations receive balanced counterfactual scoring under both contracts; these are not independent additional readings. |
| Policy | Specify exactly two scheduled readings, retry handling, duplicate handling, fixed configuration weights, missing-data bounds and the treatment of `ESCALATE`. |
| Scoring | Define behavioural scope, target-discrepancy credit, domain validation, oracle validation, exceptions/timeouts, literals and numerical comparison. |
| Hypotheses | Retain E6-1’s conjunction; distinguish FPR budget \(\alpha_{\mathrm{FPR}}=.05\) from significance level; specify interval sidedness and boundary rules. |
| E6-3/order | Make equivalence the prespecified confirmatory question or choose a separate directional hypothesis. “Equivalence **or** difference” does not define a clear sequential gate. Specify whether positive controls are a prerequisite or a separate confirmatory family. |
| Secondary analyses | Implement per-vendor/configuration contrasts, benchmark contrasts and behavioural subsets. Define “unanimous judge reasons”; current unanimous verdicts do not define an additional subset. Distinguish pass, clarification and blocker outcomes. |
| Precision | Replace the old SDs with **17.71, 17.56 and 7.07 points**; simulate the actual paired design, boundary behaviour, missingness and joint criteria. “Fewer than 60 is underpowered” is not a power analysis. |
| Freeze bundle | Include all materials and dependencies below, with verification before the first test call. |

The bundle must contain the corpus and split; construction attempts and exclusions; all four implementations; independent validation inputs/results; panel prompts/votes/reasons; behavioural records; selected populations; shown-vendor and option-order mappings; rendered audit prompts and required schedules; constitution, parser and policy; scorer, comparator and tolerance code; analysis code; model/CLI configurations; interpreter and dependency versions; and checksums binding them.

The E6 records remain untracked, and I found no E6 freeze manifest. At inspection, open test construction had **140 execution-admitted and 132 panel-admitted units**; positive-control test construction had no unit records. These are construction counts, not test outcomes.

**(b) Recommended additions, ranked by contribution per cost**

1. **E1 witness bridge — my single strongest recommendation.**  
   Reuse E1’s actual programmes and successful findings. Classify the targeted discrepancy and rescore relevant witnesses against validated alternative contracts. Preserve programme-level unions: separate successes supported **only** by convention-dependent findings from successes with at least one contract-independent valid witness.

   This connects the engineered experiment to the measurement problem the paper claims matters. Development already contains seven overlapping E1 problems, with successful current-scorer witness records on five. The pilot overlap is small, but the workflow can be frozen before E1 test auditing. This requires validation and offline execution rather than another large audit grid.

2. **Analyse decision routing in the existing menu records.**  
   Report false accusations, explicit clarification/escalation, and unsupported acceptance separately, by vendor. The 72.25% versus 2% escalation contrast is more informative than calling both vendors’ low BLOCKER rates “abstention”. Freeze a rubric for identifying clarification requests rather than equating every advisory with one.

3. **Add an ordinary-language reveal arm.**  
   Append a self-contained requirement sentence without the alternative menu, option numbers or explicit missing-information announcement. Keep both contract versions and both programme versions. Using one prespecified budget per vendor costs **16 additional readings per unit**, versus the current 64. This tests whether the large effect survives a realistic clarification format.

4. **Execution access on a prespecified computational subset.**  
   The remaining resolved failures include hashing and numerical aggregation, where calculating a witness matters. This would give the computation comparison more substance, but route isolation and tool-budget validation make it less cheap than the preceding analyses.

5. **A partially informative intervention.**  
   Potentially valuable, but a truthful deterministic clue distinguishing two binary contracts often reveals the entire relevant bit. A genuine intermediate-information experiment needs a calibrated noisy signal, additional contracts or multiple independently unresolved decisions. Avoid adding a merely vaguer sentence and calling it an information dose.

**(c) Verdict**

**No test release now.** Repair the demonstrated oracle failures, semantic admission, completeness/provenance handling and boundary inference; finish development validation; then freeze the corrected registration and verified bundle.

The result is more than a literal reading-comprehension score because it measures **executable witness production at a specified false-flag operating point**. Nevertheless, explicit rule selection on simple constructed programmes, near-perfect resolved detection, and a saturated high-versus-low comparison provide a modest contribution by themselves.

The defensible empirical contribution is a controlled measurement framework separating **benchmark-convention preference, unjustified accusation, clarification behaviour and verified diagnosis**. Its strongest route to an ICML paper is demonstrating that these distinctions materially change conclusions on actual E1 audits.

**My main-track assessment is currently lean reject.** The human-validation replacement does not automatically disqualify the work, but it removes part of the foundation behind P2’s conditional optimism. A repaired, transparently model-screened E6 can proceed as a narrower experiment; strong main-track claims still need convincing evidence beyond the constructed zero baseline and explicit-resolution success.

