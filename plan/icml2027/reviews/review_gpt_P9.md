**At HEAD `1c242f6`: E6 release no; E1 Amendment 6 stands and E1 analysis may run; E8 release no.** The original E6 attempt-accounting blocker is fixed. Remaining blockers concern E6’s implementation of Amendment 6 and E8’s terminal-missing-data analysis.

**(a) Remaining blockers**

1. **E6 bypasses Amendment 6 when checking the benchmark reference’s domain.**

   In [`e1.judge_witness()`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:1315>), supplying an E6 oracle first invokes `judge_call(p, args, kwargs)` with the default **10-second** limit. A reference timeout immediately returns `outside_domain`, even when the caller supplies `limit=60, timeout_terminal=True`.

   I reproduced this through the actual E6 witness stage: both contracts persisted `outside_domain`, `reference: timeout`, **`infra: False` on the first scoring**. Consequently, these records neither accumulate the required timeout history nor receive the 60-second retry.

   Apply the registered escalation rule to this preliminary reference check, and invalidate affected cached scores before regenerating the freeze.

2. **E8’s terminal-missing-data handling remains incomplete.**

   Two executable defects remain in [`analyse()`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/e8/e8.py:149>):

   - **No complete units in either population causes a crash.** A fixture with complete open readings and terminal failures for every control reading raised `IndexError`, preventing even the full-universe bounds from being reported. Return an explicitly unavailable primary estimate and verdict while still calculating the bounds.
   - **Setting missing outcomes identically in both populations does not bound \(S\).** With two shared problems—one observed with open = 1 and control = 0, the other wholly missing—both reported imputation scenarios give **S = 50 points**, although its possible full-universe value ranges from **0 to 100**. For selectivity, use open-missing = 0/control-missing = 1 for the lower endpoint, and the reverse for the upper endpoint, preserving problem pairing.

   **No other genuine blocker was established.**

**Resolved checks and E1 Amendment 6**

| Check | Replay result |
|---|---|
| E6 P8 content-dependent exemption | Fixed: the `"Not logged in"` reply consumed attempts **1, 2, 3**; the fourth invocation made no call. |
| E6 freeze at HEAD | **Passed**, including final re-verification. |
| E8 `"false"` string / invalid positive index | Rejected; valid Boolean `false` retained as negative. |
| E8 retries | Invalid model replies exhausted two charged attempts; quota exits exhausted six total calls without model charges. |
| E8 empty question list | Persisted `outcome=False`; no judge call. |
| E8 universe / absent readings | **238 readings**, with **13 shared problems**; one present and three absent readings correctly caused refusal. |
| E8 paired inference | Identical outcomes on shared problems yielded **S interval [0, 0]**. |
| E8 directional reporting | **[−100, −100]** correctly yielded `S_below_0=True`. |
| E8 freeze enforcement | Matching in-memory manifest passed; changed prompt failed; each run invocation checked the gate before calls. |

The E8 freeze implementation resolves P8’s enforcement defect. **`FREEZE8_test.json` does not yet exist**; it must be generated after the remaining corrections.

**E1 Amendment 6 is acceptable as a runtime-based scoring rule.** Its E1 path returns retriable infrastructure at 10 seconds and terminal no-credit at the escalated 60-second limit. The five terminal witness records all have at least two preceding reference-timeout records. The live completeness check reports **1,928 scheduled, 1,928 valid, no missing readings and no unscored witnesses**. No E1 held-out analysis was run during this review. The authors’ assertion about what they inspected before amending remains a disclosure.

**(c) Verdicts**

- **E6 release: no** — repair Amendment 6’s benchmark-domain check. The P8 attempt-accounting blocker is closed.
- **E1 Amendment 6 stands: yes. E1 analysis may now run: yes.** No remaining E1 blocker identified.
- **E8 release: no** — repair terminal-empty-population handling and selectivity bounds, then freeze.

All replays were read-only, using mocked calls and in-memory outputs; no model calls or file changes were made.