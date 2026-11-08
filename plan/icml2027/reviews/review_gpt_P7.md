**E6: release no. E1: release yes.** Reviewed `study/icml-e1` at `5988212c4981dc70eaebf6a03ce4f975a94a1516`. The current freeze verifies. One genuine E6 blocker remains; I found no remaining E1 blocker.

References below are relative to `crossaudit-harness/benchmarks/code/`.

**(a) Remaining blocker and P6 dispositions**

**1. Executable validity — not fixed overall: the new interface restriction is inconsistent across admission and scoring.**

The restricted, finite-input guarantee is acceptable in principle as an operational validation claim. It does not establish whole-program correctness. Restricting argument types before test auditing is also defensible, provided the same scope governs construction, separation and scoring.

That consistency is currently missing:

- [PREREGISTRATION-E6.md:62](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/PREREGISTRATION-E6.md:62>) says other argument types belong to neither contract.
- [e6.py:694](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:694>) filters probes and stress inputs, but includes proposer class inputs unchanged. Those inputs count towards `separates_2` at `:707–714`.
- The [witness scorer, e6.py:1094](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:1094>), never applies `conforms()` before awarding primary credit at `:1105–1109`.

This affects frozen held-out units:

| Retained test unit | Registered interface | Separating inputs: current / after interface filtering | Admission record |
|---|---|---:|---|
| Open `Mbpp/141` | Lists of integers; proposed distinction concerns strings | 6 / **0** | `records/icml/e6_units4.jsonl:82` |
| Open2 `Mbpp/573` | Lists of integers; distinction requires mixed integers/floats | 2 / **0** | `records/icml/e6b_units4.jsonl:114` |
| Control `Mbpp/614` | Lists of tuples of integers; distinction requires non-integral floats | 5 / **0** | `records/icml/e6det_units4.jsonl:224` |

I executed the actual witness-scoring path with an in-memory reading for:

```python
pancake_sort(['apple', 'Banana'])
```

`conforms=False`, but the scorer returned `valid=True`, `in_class=True`, `oracles_differ=True` and **`verified_diagnosis=True` under contract B**.

Across the registered test populations, **12/52 open units and 7/85 controls have every proposer class input outside the interface**. This count does not assert that all have zero possible in-scope separation; the three replayed examples above establish the concrete defect.

Before E6 release, define and enforce one scope across admission separation, red-teaming and scoring. Expanding the interface to include target types requires renewed validation on that expanded scope; retaining the present interface requires removing units without sufficient in-scope separation. Recompute the populations and freeze afterwards.

The original P6 counterexamples now behave as follows:

| Counterexample | Executed result and disposition |
|---|---|
| Open `Mbpp/405`, `((1,), 1+0j)` | Disagreement persists, but `conforms=False`. **Addressed by the registered scope change**, not repaired behaviour. |
| Open2 `HumanEval/74`, combining marks | In scope; disagreement reproduces. **Excluded by red-team admission**, `e6b_redteam.jsonl:4`. |
| Control `Mbpp/170`, negative indices | In scope; disagreement reproduces despite `valid=False`. **Excluded by red-team admission**, `e6det_redteam.jsonl:10`. |

Removing or failing a red-team record excluded the unit through `units()` (`e6.py:960–967`). All **351** current red-team records matched reconstructed implementation and prompt hashes.

I also replayed **8,909 registered input rows** and tried **1,914 additional in-scope inputs** on the requested sample, finding no further agreement or predicate failures:

- Open: HumanEval/134, /162, /98; Mbpp/130, /142, /405, /629.
- Open2: Mbpp/124, /131, /421.
- Controls: HumanEval/146, /149; Mbpp/65, /798, /744.

**2. Every E6-2 estimate has bounds — fixed.**

[analyse_e6.py:234](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:234>) implements the shared bounded estimator. Primary (`:294`), configuration (`:303`), vendor (`:308`), benchmark (`:311`) and behavioural-subset (`:314`) outputs all use it.

With wholly missing synthetic problems, every applicable output returned **[−50, +50] points**, correct exclusion counts and no positive claim. A mixed observed/missing example returned the expected **[0, 50]** bounds.

**3. E1 bridge freshness and primary-analysis crash — both fixed.**

[e1.py:1494](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:1494>) selects votes by the reconstructed current evidence hash. Appending stale OPEN votes after current DETERMINED votes left the reported class **DETERMINED**. Removing one current adjudicator vote aborted completeness.

[analyse_e1.py:190](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e1.py:190>) now defines `tax`. Using executed witness evidence and synthetic classification records for retained `gen-claude-haiku45|Mbpp/465`, the primary analysis completed and correctly reported one item with a determined witness.

**4. Freeze defects — fixed within the registered commitments.**

[freeze.py:44](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/freeze.py:44>) excludes directories; `:62–79` preserves E6 kind; `:96–105` binds both E1 schedules and checks their combined multiset against the required universe; `:35` and `:78` bind red-team records.

Observed checks:

- **Current `verify()` passes**, including a final recheck.
- Empty and duplicated E1 schedules fail.
- All **54 in-memory commitment mutations** fail verification.
- Fresh-build injections changing record bytes, schedule bytes, corpus bytes, rendered prompts or package-version inventory fail.
- Intercepted test audit stages preserve their kinds and schedule **3,280 open + 880 open2 + 1,360 control readings**, totalling **5,520**. No model calls were made.

This is not a checksum of everything installed: package **versions** are bound, not package-content bytes. Same-version package modifications and files outside the registered bundle are outside this guarantee.

**5. Other v4.3 additions**

- **Executor fallback:** implemented at `e6.py:174–222`, `:254–309`; no additional blocker established. Actual process termination and `timeout`/`memory` branches passed with simulated RSS telemetry. The review sandbox denies `ps`, so I could not independently validate live RSS measurement.
- **Registered-only scheduling:** **fixed**, `e6.py:1002–1016`. Completeness separately counts unregistered admitted-unit readings at `:1149–1151`.
- **Pilot archiving:** **present**. The two named files contain 14 and 16 records and are separate from active admission records.
- **Other genuine blockers:** none found beyond the admission/scoring scope inconsistency above.

**(b) Disclosures**

- Verified populations: **dev 20 open / 31 controls; test 52 open / 85 controls**.
- Registered open2 `Mbpp/573` and control `Mbpp/614` passed red-team admission with **zero accepted inputs** (`e6b_redteam.jsonl:62`, `e6det_redteam.jsonl:116`). No minimum accepted-input count is registered, so this is a coverage disclosure rather than a separate blocker.
- E1 retains **nine test intervention items across seven problems**, with **1,928 required readings**. The previously disclosed precision and H2/H4 calibration limitations remain.
- No test readings were found in the current processed or raw audit files.
- All diagnostics were read-only, using pipe-based execution and in-memory fixtures. Freeze execution suppressed only byte-identical project-file rewrites. No files were changed and no model calls were made.

**(c) Verdict**

| Experiment | Release to test? |
|---|---|
| **E6** | **No** — reconcile and enforce the interface scope, then regenerate affected admissions, populations and freeze. |
| **E1** | **Yes** — the P6 release blockers are fixed at the reviewed snapshot. |

