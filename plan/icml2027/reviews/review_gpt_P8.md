**E6: release no at `712bfe55f382bf2f4cfb7eb407843304f751fc9c`. E1 Amendment 5 stands. E8: release no.**

The P7 interface-scope blocker is fixed. One separate E6 blocker remains in attempt accounting.

**(a) Remaining blockers**

**1. E6 retry eligibility still depends on model-generated content.**

[`counts_as_attempt()`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:1215>) applies the `PRE_MODEL_INFRA` substring exclusion even when usage was recorded or the error describes an invalid model reply.

I exercised the actual audit stage with a mocked successful provider response containing:

```json
{"verdict":"PASS","sections_applied":["Not logged in"],"findings":[]}
```

The validator correctly rejects the invented rule. However, its diagnostic contains `"Not logged in"`, so E6 treats the reading as pre-model infrastructure despite recorded input/output tokens. **Four successive calls all remained `attempt: 1`; none consumed an attempt.** `e1.reached_model()` correctly charged all four.

This violates both the attempt cap and Amendment 5’s explicit content-independence requirement. Charge successful, usage-bearing, timed-out and invalid-reply calls before considering infrastructure exclusions; do not classify parser-generated diagnostics as transport failures. Then regenerate the freeze. I found **no existing development reading affected** by this discrepancy, but the execution path is demonstrably wrong.

**2. E8 does not implement its retry rule or a fixed-denominator estimand.**

In [`pilot_discover.py`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/e8/pilot_discover.py:60>):

- Every persisted row enters `done`, including infrastructure failures. Two invocations with mocked quota failures made only the original two calls; neither reading was retried.
- Usage/error metadata and judge-call status are not retained sufficiently to implement the registered retry rule.
- `bool(jo["match"])` converts `"false"` into **True**. I reproduced positive credit from `{"match":"false","question_index":99}`.
- A valid empty question list becomes missing rather than a defined negative outcome.

The analysis then silently averages available readings and drops wholly missing problems. My fixture with one successful and three missing readings returned only `{"p": 1.0}`. That is not the registered mean over two readings per registered unit.

Before release, define and implement strict response validation, separate elicitor/judge retry accounting, treatment of empty lists and terminal failures, and completeness checks against the **238-reading universe**.

**3. E8’s selectivity inference needs correction.**

The held-out open and control populations share **13 problem IDs**. [`analyse_e8.py`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/e8/analyse_e8.py:29>) nevertheless bootstraps them independently. Problem-level inference for their difference must preserve dependence for shared problems, or use a prospectively justified alternative.

The promised two-sided reporting is also implemented directionally: a synthetic interval of **[−100, −100]** produced `S_excludes_0=False`. Report both directions explicitly.

**4. E8’s promised freeze is not enforced.**

An `E8_RELEASED` marker permits execution, but the runner neither verifies E6’s freeze nor checks a frozen E8 bundle. Recording template hashes alongside results does not prevent resuming with changed prompts, routes, units or scoring code. Bind and verify those inputs before the first held-out call and on resumption.

**No other genuine release blocker was established.**

**(b) Disclosures and resolved checks**

**Scope consistency — fixed.** Replaying P7 gave:

| Case | Separating proposer inputs, unscoped → scoped | Current disposition |
|---|---:|---|
| Open `Mbpp/141` | 6 → 0 | Excluded |
| Open2 `Mbpp/573` | 2 → 0 | Excluded |
| Control `Mbpp/614` | 5 → 0 | Excluded |

`pancake_sort(['apple', 'Banana'])` still produces an executable disagreement, but `in_interface=False` now removes **primary, reference-domain and off-class credit**. All 16 combinations of the other Boolean credit flags also received no credit when outside the interface. Missing, failed and zero-input red-team records excluded their units.

**Hidden-suite and predicate checks — passed.** I re-executed **26,475 hidden-suite inputs across all 119 registered held-out units**. Every input was recognised as in scope; no agreement or predicate violation appeared. A further **7,157 proposer/probe/red-team input rows** produced no violation under the reference-success condition. The slow `HumanEval/94` replay required smaller batches; 16 rows timed out in the reference under my two-second diagnostic limit.

**Witness migration and freshness — passed.** The prescope archives exist. Executing `stage_rescope` on an older-stage fixture added the missing executable checks and interface flag. Crucially, migration retains the old key: subsequent execution under the current credit-rule hash supplies the usable scores.

Across the admitted development units, all **2,282 current-key witness records** had the required checks and consistent aggregate flags; none shared a key with the prescope archives. Completeness rejected injected unscoped records, empty interfaces, conflicting scores and missing current scores. Interface-extraction failure became retriable infrastructure. The held-out witness stage invoked freeze verification before work. **I found no route by which the existing older-stage records could supply held-out credit through the normal checked analysis path.**

**Aliasing, populations and freeze — passed.** Intercepting the actual `__main__` audit entry point confirmed that `analyse_e6` and `freeze` see the selected module and kind.

| Population | Development units | Held-out units | Held-out readings |
|---|---:|---:|---:|
| Open, first attempt | 13 | 34 | 2,720 |
| Open, second attempt | 3 | 7 | 560 |
| Controls | 30 | 78 | 1,248 |
| **Total** | **16 open / 30 controls** | **41 open / 78 controls** | **4,528** |

Section 1’s development results reproduce. Per-unit behaviour records reconcile with their visible-passing counts. The added E6-1b/E6-3 missing-data outputs behave conservatively in the exercised missing-data fixtures; wholly missing data yield no positive verdict. **Freeze verification passed again at the end.** No E6 or E8 held-out audit records were found.

The pickle addition protects newly written red-team records. Existing registered records predate it; four printed complex inputs for open2 `Mbpp/252` could not be reconstructed through the current literal parser. Their retained historical verdicts remain a disclosed verification limitation.

**E1 Amendment 5 — acceptable, with corrected operational accounting.** Excluding documented quota/HTTP failures without recorded usage is a defensible infrastructure amendment, rather than outcome-based replacement. The auditor filter works. Appending test bridge rows leaves the freeze checksum unchanged; changing development bridge rows changes it.

The current records contain **665 uncharged failures across 333 reading keys**, rather than 666: 332 keys have two, one has one. There are **1,927 valid readings out of 1,928**. The remaining reading has one chargeable tool-use failure and is still unfinished, not exhausted. Preserve that distinction before analysis. The assertion that only failure metadata was inspected when amending remains an author disclosure.

E8’s discovery estimands and pilot-informed thresholds are reasonable for a narrowly described, model-judged study. Same-vendor judging and six-question breadth are limitations, not independent blockers; they do not establish human-validated requirement discovery.

All checks were read-only, with pipe-based execution and in-memory fixtures. No model calls or file changes were made.

**(c) Verdict**

- **E6 release: no.** Repair the demonstrated content-dependent attempt exemption and regenerate the freeze. The P7 scope blocker is resolved.
- **E1 Amendment 5: stands.** Complete the remaining reading under its existing attempt rule before analysis. The same principle is acceptable for E6, but E6 currently implements it incorrectly.
- **E8 held-out release: no.** Resolve the retry/scoring, missing-data, selectivity-inference and freeze defects before its first held-out call.

