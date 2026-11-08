**Do not freeze or release either test run yet.** V4 fixes several P3 failures, but executable validity, inference and implementation gaps remain. E1’s Amendment 4 retention rule is not connected to its audit or analysis paths.

I reviewed commit `cb54f2e` and the current registration draft. Both saved development analyses reproduce exactly. I executed adversarial inputs on **10 admitted primary open units and five admitted positive controls**, reran the three named cases, and tested failure handling in memory. Execution used the workspace’s `.venv` and `.exec`, with pipe-based I/O adapters for read-only operation. No model calls or file changes were made.

**(a) Blockers before test**

**1. Executable validity remains a blocker.**

The stricter admission checks are real: both B implementations must match the reference, and programmes must agree outside the class. However, these requirements hold only on the sampled validation inputs. Adding my probes to the actual `stage_validate4` decision procedure rejects the newly failing units below. See [e6.py:426–490](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:426>).

| Case | Re-executed result | Assessment |
|---|---|---|
| **Open Mbpp/798**, `[10**16, 1, -10**16]` | Reference and shown B return `1`; the other B implementation still returns `0.0`. | The implementation defect remains, but this open unit is now excluded. Changing oracle B to the reference also removes the original false-credit mechanism. **Contained.** |
| **Open Mbpp/557**, `"Ο\u0301Σ"` | Shown B returns `"ο\u0301σ"`; reference returns `"ο\u0301ς"`. | This open unit is now excluded. **Contained, not repaired.** |
| **Positive-control Mbpp/762**, `13` | `valid=False`; `stage_witness` records `outside_domain`. | **Fixed in the E6 pipeline.** |
| **Positive-control Mbpp/557**, `"ΟΣ"` or `"Ο\u0301Σ"` | This unit remains admitted. Its supposedly correct B programme disagrees with the reference; `valid=True`, `in_class=True`. The actual witness stage awards verified credit against B. | **Surviving clean-control defect.** A justified flag can be counted as a false positive. |
| **Open HumanEval/125**, `"a\v,b"` | Both shown programmes return `['a', ',b']`; oracle B returns `['a\v', 'b']`. `valid=True`, `in_class=False`. | **New failure of outside-class agreement.** `"è"` supplies another example: programmes return `0`, reference `1`. |
| **Open HumanEval/20**, `[-1e308, 1e308]` | Shown programmes return the pair; reference returns `None` because the distance overflows. `valid=True`, `in_class=False`. | **New reference-oracle failure on an accepted input.** |
| **Open Mbpp/130**, `['a','b','b','a']` | A and its oracle return `'b'`; B and its oracle return `'a'`; `in_class=True`, but `valid=False`. | **Unstated integer-only restriction rejects a legitimate target witness.** |
| **Open Mbpp/8**, `[3.5, 1.5]` | Both contracts execute correctly and disagree as intended; `in_class=True`, `valid=False`. | Another unstated integer-only restriction. |

The domain restrictions are not stated in these tasks. Either repair them or explicitly define and present a narrower experimental domain before auditing. Independent authorship does not make a predicate semantically correct.

The sampled open units were HumanEval/{20,125,134,162} and Mbpp/{8,65,130,142,477,784}; controls were HumanEval/30 and Mbpp/{72,557,762,798}. I found no additional failure on the other chosen inputs; this is not exhaustive validation.

**Required before release:** resolve these cases, extend independent probes systematically around the discovered failure classes, rerun admission, and regenerate affected populations and development summaries. Excluding off-class witnesses from verified coverage does **not** repair a whole-programme clean-flag endpoint.

**2. Completeness is substantially improved, but provenance and missing-data handling remain incomplete.**

The current grids are complete: **3,440/3,440 open readings and 864/864 control readings**, with no exhausted keys. Removing witnesses, removing one required reading, or duplicating a successful reading now aborts. Fixed configuration weighting and exclusion of incomplete units from a contrast are implemented.

The following adversarial checks still succeed incorrectly:

| In-memory change | Current behaviour |
|---|---|
| Replace an audit’s prompt hash with zeros | Completeness passes. |
| Replace every judge prompt hash with zeros | The same 27-unit population is admitted. |
| Supply three copies of one pre-model infrastructure failure | The reading is deemed exhausted. |
| Exhaust both readings of one required cell | Analysis drops the unit and reports `excluded_missing=1`, but supplies **no promised best/worst bounds**. |
| Append conflicting scores under one witness hash | Completeness passes; table construction takes the last score. |
| Change comparator/tolerance | E6’s witness key remains unchanged. |

Relevant code: [completeness, e6.py:746](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:746>), [witness keys, e6.py:700](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:700>), and [analysis, analyse_e6.py:140–171](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:140>).

Current judge hashes do match reconstructed prompts, and existing duplicate witness hashes have consistent results. These are **release-path failures**, not evidence that the saved pilot is corrupted.

Scoring does enforce `valid`, `in_class`, candidate–contract-oracle disagreement and a correct expected value; analysis restricts credit to blocking readings. I additionally executed **174 unique credited open calls and 143 control calls**: none had agreeing A/B oracle outcomes. However, A/B disagreement is not explicitly checked during witness scoring. Add that check if “target-discrepancy credit” is intended to require it, rather than relying entirely on admission.

Also repair the retry implementation. Registration says pre-model infrastructure failures do not consume attempts; `stage_audit` counts every stored row. `sync_auth` locks copying, not concurrent model calls, and its timeout path skips post-call synchronisation. It does not establish that refresh races are solved. See [e1.py:110–145](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:110>).

**3. Section 7 must change. Disclosure alone is insufficient.**

Choosing a method after inspecting **development** data is permissible when disclosed and frozen before test. The problem is the method’s calibration.

At 27 problems, the implemented rule produces:

- All clean-cell rates zero: **fails**, because the exact upper bound is 10.50%.
- Add one false flag in one of eight clean cells on one problem: **passes**, because the bootstrap upper endpoint becomes 1.39% and the exact safeguard switches off.

This is not merely an aesthetic discontinuity. Consider independent problem-level clean-flag rates equal to `0`, `0.125` and `1` with probabilities `0.86`, `0.10` and `0.04`. Their true mean is **5.25%**. For 60 problems, the event “no rate-1 problem, and 1–16 rate-0.125 problems” alone has probability **8.62%**; the ideal percentile-bootstrap version of the current rule certifies compliance throughout that event. Thus it cannot provide the claimed 95% budget assurance.

Use the conservative any-clean-flag bound consistently, or register a properly justified confidence procedure for the bounded problem-level mean. Do not choose between them according to which passes development. See [analyse_e6.py:119–137](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:119>).

P3’s analogous **equivalence-boundary** concern also remains: all-zero problem contrasts produce `[0,0]`, which automatically passes E6-3. Its verdict has no safeguard. The observed development interval is non-degenerate, so this does not invalidate that particular interval; it remains an unresolved test decision rule. See [analyse_e6.py:222–235](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:222>).

**4. E1 Amendment 4 is not implemented end to end.**

I confirm the stated funnel: **38 previously admitted items → 13 taxonomy-v4 OPEN items → nine test items over seven problems**. Nevertheless:

- `admitted_constructions()` still returns all **38**.
- The audit schedule still allocates intervention arms to **29 test items**.
- `analyse_e1.readings_table()` retains the old admission set; development analysis includes **nine**, rather than four, retained items.
- H6 still calls `taxonomy()` and reads taxonomy v3, rather than `taxonomy2()`.
- The registered boundary sensitivity is absent from the analysis implementation.

See [e1.py:979](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:979>), [analyse_e1.py:30](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e1.py:30>) and [analyse_e1.py:231](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e1.py:231>).

The control rechecks are complete: all **76 item–control pairs** have a passing record, including 13 regenerated controls. All retained items’ controls pass. Nevertheless, admission and scheduling should enforce those records rather than rely on a separate manual check.

The bridge also needs two corrections before freezing item 8:

1. **Non-DETERMINED does not mean convention-dependent.** Preserve OPEN, DISPUTED, AT_ODDS, OUT_OF_DOMAIN and NEITHER separately. An item without a DETERMINED witness is “not established as contract-independent”, unless its remaining evidence supports a stronger classification.
2. Bind bridge records to current evidence and require complete classification. `stage_bridge` omits keyword arguments from the rendered input despite executing them, and its cache checks only item/call/adjudicator. No pilot witness uses keywords, so that defect has not affected these 23 calls.

See [e1.py:1368–1413](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:1368>).

**5. Complete the executable freeze contract.**

The remaining P3 statuses are:

| P3 blocker | V4 status |
|---|---|
| Oracle/domain validation | Improved, but still blocking as above. |
| Semantic admission | **Substantially addressed for the operational model-screened population.** Judges receive visible tests, no leading class description, separate domain decisions and explicit instructions about absent examples. Mbpp/72 is excluded; Mbpp/784’s two reasons now consistently justify its domain interpretation. |
| Completeness/provenance | Partly fixed; remaining failures above. |
| Boundary inference | Still blocking. |
| Menu interpretation/registration | Sentence arms, routing, equivalence ordering and separate control family are implemented. Remaining specification and implementation discrepancies must be closed. |

In particular, the implemented schedule is **80 readings per open unit, not 72**. Registered secondary analyses for pooled vendors, benchmark contrasts, behavioural subsets, `t=2` and off-class witnesses are not all emitted. Construction stages also need separate record paths: current `set_kind()` points `stage_validate` at `units4`, while `stage_probe` reads legacy `units` and `stage_validate4` skips existing unit IDs. A fresh reconstruction must not silently bypass v4 admission.

I found no E1/E6 freeze bundle. Finish construction, resolve these discrepancies, then verify the checksummed populations, schedules, prompts and dependencies before any test call.

**(b) Disclosures and interpretation**

**The proposer-written class predicate is acceptable in principle.** Formalising the proposer’s intended class is not the same task as independently validating that class. The original independent prompt asked for inputs on which rules can differ; the replacement explicitly includes class members on which outcomes coincide. That explains some apparent “too narrow” failures.

However, disclose the entire change: the first predicate admitted **10/55**, whereas the replacement admitted **43/55** before semantic screening. This is development-driven construction revision. Independent probes and `valid` remain useful, but do not independently certify the replacement predicate’s fit. Preserve both predicate versions and rejection reasons, and independently challenge membership boundaries. Do not describe the whole construction as independently validated.

Other necessary qualifications:

- The primary open development population has **27 units and 2,160 readings**; 3,440 includes all 43 execution-admitted units. Controls have 48 primary units and 768 readings within the 864-reading grid.
- Behavioural evidence is **6 A, 298 B, 18 other**; only **two primary units** have observed solutions following both rules. This does not establish ambiguity prevalence.
- Sentence and matched-resolution coverage have equal means, but their difference interval is **[−4.63, 4.63] points**. The programmes’ outcomes are not identical unit by unit.
- Menu routing is strongly vendor-dependent: GPT passes approximately **95–99%** of readings; Claude escalates approximately **84–87%**. Low blocking is not a common abstention policy.
- Positive-control **J = 90.6** is a flag-based discrimination endpoint, not verified coverage.
- The bridge contains **13 DETERMINED, one OPEN and nine DISPUTED witnesses**. Five of six diagnosed programmes have a DETERMINED witness. Those five are also DETERMINED under their first-failure labels; the sixth item is AT_ODDS. This pilot does not demonstrate substantial convention-only success on retained OPEN intervention items.

Nine E1 test items across seven problems can support a **small, selected replication with item-level results and descriptive contrasts**. They cannot credibly establish precise ±5-point equivalence, a tight false-alarm guarantee, stable vendor interactions or broad prevalence. For scale, zero events across seven independent binary problem indicators still gives a one-sided 95% upper bound of **34.8%**.

**(c) Verdict and main-track assessment**

**E6: no test release yet.** Repair executable validity, provenance/missingness and the inferential decision rules, then freeze. A transparently model-screened E6 remains a legitimate narrower experiment.

**E1: no test release through the current pipeline.** Connect Amendment 4 retention, controls, taxonomy and bridge requirements to scheduling and analysis. After that, the small test cohort may run, with claims commensurate with seven problem clusters.

The strongest honest framing is:

> **An executable audit-measurement framework showing how explicit behavioural requirements change verified diagnosis, while separating benchmark-convention preference, false accusation and decision routing.**

The sentence-arm result strengthens that framing beyond the deliberately ambiguous menu. E6-3 supports a limited comparison between the tested reasoning configurations after clarification; it does not establish a general computational ceiling. The bridge currently indicates that most observed natural successes have task-determined support, limiting the evidence that convention dependence materially distorts natural-audit conclusions.

**My contribution assessment remains lean reject for the ICML main track, with unresolved methods blockers additionally preventing acceptance.** The framework has methodological value; the present evidence does not yet establish the broader empirical importance claimed for an audit ceiling.

