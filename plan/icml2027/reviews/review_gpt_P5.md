**E6: release no. E1: release no.** Genuine blockers remain.

I reviewed `677c78b` and the subsequently present freeze commit `af08931`. I reran the named counterexamples, executed **1,425 additional inputs across ten admitted open units and five controls**, and attacked provenance and completeness in memory. No model calls or file changes were made. Neither experiment has test audits; partial E6 test construction was not treated as a failure.

The supplied interpreter paths do not exist inside `crossaudit-harness`; I used the enclosing workspace’s `.venv/bin/python` and `.exec/bin/python`, with pipe-based execution adapters.

**(a) P4 dispositions and remaining blockers**

**1. Executable validity — not fixed overall.**

The named P4 cases are now handled as follows:

| P4 counterexample | Current result | Disposition and evidence |
|---|---|---|
| HumanEval/125: `"a\v,b"` and `"è"` | The discrepancies persist, but the unit is excluded. | **Fixed by exclusion:** `records/icml/e6_units4.jsonl:4`. |
| HumanEval/20: `[-1e308, 1e308]` | Reference returns `None`; implementations return the pair. Unit excluded. | **Fixed by exclusion:** `records/icml/e6_units4.jsonl:18`. |
| Positive-control Mbpp/557: `"ΟΣ"` and `"Ο\u0301Σ"` | Shown B still mishandles final sigma. Unit excluded. | **Fixed by exclusion:** `records/icml/e6det_units4.jsonl:43`. |
| Mbpp/130: `['a','b','b','a']` | `valid=False`; primary credit denied, reference-domain sensitivity credited. | **Fixed as an explicitly restricted credit estimand:** `PREREGISTRATION-E6.md:94–98`; `e6.py:804–813`. |
| Mbpp/8: `[3.5,1.5]` | Same primary/sensitivity distinction. | **Fixed on the same basis.** |

Two admitted units fail new probes:

| Unit | Executed counterexample | Failure |
|---|---|---|
| **Open Mbpp/124** | `angle_complex(1, 1-1j)` | `valid=True`, `in_class=False`. Reference/B return `−0.4636476090`; both A implementations return `5.8195376982`. This violates outside-class agreement. Admission: `e6_units4.jsonl:7`; predicate: `e6_probes.jsonl:66`. |
| **Control Mbpp/65** | `recursive_list_sum([1e16, 1.0, -1e16])` | `valid=True`, `in_class=False`. Reference returns `0.0`; shown B returns `1.0`. Both B/reference agreement and outside-class agreement fail. Admission: `e6det_units4.jsonl:51`; shown B: `e6det_impls.jsonl:385`. |

Adding each input to the actual admission procedure rejects its unit. The stress generator lacks complex-number mutations and misses this mixed floating-point cancellation pattern. See [e6.py:428–475](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e6.py:428>) and `e6.py:523–541`.

**The narrower-domain treatment is acceptable for verified-credit measurement, but does not establish whole-programme correctness.** For example, admitted control Mbpp/798 rejects floats through `valid`, yet `_sum([1e16, 1.0, -1e16])` produces `0.0` from shown B versus reference `1.0`. An auditor sees the unrestricted array-summation task; a flag can still be counted as a false positive. Section 6’s sensitivity does not repair that labelling problem. Reconcile the audited domain and clean-programme labels before claiming FPR: `e6.py:738`, `analyse_e6.py:332–345`.

The ten open units were HumanEval/{98,134,162} and Mbpp/{8,65,124,130,142,477,784}; controls were HumanEval/30 and Mbpp/{65,72,762,798}. This was adversarial sampling, not exhaustive validation.

**2. Provenance and missing data — partly fixed, with two remaining failures.**

| P4 check | Status | Evidence |
|---|---|---|
| Rebuild audit prompt hashes | **Fixed.** Zeroed hash aborts. | `e6.py:825–855` |
| Check judge prompt hashes | **Fixed.** Zeroed hashes abort population construction. | `analyse_e6.py:183–195` |
| Bind comparator/tolerance into witness key | **Fixed.** Changing tolerance changes the key. | `e6.py:764–770` |
| Exclude pre-model failures from attempt exhaustion | **Fixed for the registered error recognisers.** Three refresh failures leave the reading unfinished. | `e6.py:817–822,849–868` |
| Refresh retry | **Fixed as a retry mechanism.** Stubbed execution performs resynchronisation and exactly one retry; timeout now synchronises afterwards. | `e1.py:131–159` |
| Superseded readings | **Fixed for current admissions.** Dev completeness reports 320 superseded open readings and 96 controls. | `e6.py:844–846,869`; E1: `e1.py:1477–1500` |
| Conflicting primary witness scores | **Fixed.** Contradictory `verified_diagnosis` aborts. | `e6.py:859–864` |
| Conflicting sensitivity scores | **Not fixed.** Flipping only `verified_refdomain`/`verified_offclass` passes completeness; table construction uses the last score. | `e6.py:861–864`; `analyse_e6.py:44–48,62` |
| Missing-data bounds | **Not fixed across registered endpoints.** Generic contrasts now report bounds, but E6-2, E6-4 and levels omit them; an entirely missing contrast returns `None` without bounds/counts. | `analyse_e6.py:200–223,260,343–345` |

For the missing-cell attack, the main contrast correctly reported one exclusion and bounds **[83.33, 91.67] points**. The corresponding resolved levels supplied no worst/best bounds and still computed budget compliance from the remaining units.

Target credit now explicitly requires A/B oracle disagreement: **fixed**, `e6.py:793–811`.

**3. Inference — not fixed. The betting implementation is invalid.**

The critical line is:

```python
cap *= 1 - min(lam, 0.75 / m) * (x - m)
```

For this negative-direction bet, the cap must be **`0.75 / (1 - m)`**. The current denominator belongs to the opposite betting direction. This is explicit in Waudby-Smith and Ramdas, Theorem 3, equation (25). [Primary source](https://rss.org.uk/RSS/media/File-library/Events/Discussion%20meetings/Estimating-means-of-bounded-random-variables-by-betting.pdf)

See [analyse_e6.py:125–162](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e6.py:125>).

Concrete consequences:

- With `n=24`, after one zero observation, testing `m=0.1` permits a next-observation capital factor of **−0.13761** when `x=1`. Non-negativity is lost.
- Twenty-four zeros yield an upper bound of **4.952%**. Under independent Bernoulli observations with true mean **10.1%**, that all-zero event occurs with probability **7.767%**. The procedure therefore falsely certifies the 10% budget on an event already exceeding its 5% error allowance.
- Correcting only that denominator **in memory** changes the current dev FPR bound from **7.484% to 16.956%**. The dev budget claim fails.

The remaining inferential choices have these dispositions:

- **Predictability: fixed/correct.** Each bet is recorded before updating with the current observation; using fixed final sample size in the tuning formula is permissible.
- **Ordering: acceptable.** The fixed seeded permutation is not chosen by sorting outcomes. It does not itself establish independence or exchangeability.
- **10% FPR budget: acceptable as a disclosed pre-test choice**, distinct from significance level. Its current certificate is invalid.
- **E6-3’s ±10-point margin and placement last: acceptable as disclosed pre-test revisions.** The two-tail allocation is correct, but `betting_interval` inherits the defective helper and is not a generally valid 95% interval. With the denominator corrected, dev E6-3 is approximately **[−18.57, +18.84] points**, still failing equivalence.
- **Claim ordering is implemented correctly:** `analyse_e6.py:302–314`.

**4. E1 Amendment 4 — substantially wired, but not ready to freeze.**

The following P4 blockers are **fixed**:

- Retention and passing control rechecks are enforced: **38 → 13 retained items**, comprising four dev and nine test items. `e1.py:993–1002`.
- The rebuilt test universe is **1,928 readings**. Dev completeness is **784 valid, zero missing, 120 superseded**. `e1.py:1452–1500`.
- Analysis uses retained admissions; H6 uses taxonomy v4 and emits the full secondary contrast matrix. `analyse_e1.py:30–48,236–281`.
- Both saved E1 dev analyses reproduce exactly. All retained dev audit prompt hashes match the currently rendered prompts.

The bridge remains **not fixed**:

1. **Evidence freshness is still ignored when scheduling.** `have` includes the evidence hash, but `have_keys` immediately discards it. Replacing every hash with a distinct stale hash leaves all classifications unchanged and schedules **zero** refresh jobs. [e1.py:1402–1405](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/e1.py:1402>).
2. **Classification completeness is not enforced.** Removing one adjudicator’s vote leaves **22/23** classified witnesses while E1 completeness still passes. `e1.py:1435–1449,1465–1500`; neither analysis path checks bridge completeness.
3. **Keyword witnesses are rejected rather than correctly represented.** `split_words(txt='Hello\tworld!')` verifies successfully, but both bridge jobs return `"keyword arguments"`. This violates the commitment to classify every distinct verified witness. `e1.py:1411–1415`.

Keeping non-DETERMINED classes separate is **fixed**, `e1.py:1435–1438`; Amendment 4 item 8 still specifies the old convention-dependent dichotomy, `PREREGISTRATION-E1.md:276–283`.

The boundary sensitivity is **only partly fixed**. It appears when every *item* value is zero, whereas the registration says every *problem-level contrast* is zero. Two items with contrasts `+1` and `−1` in the same problem produce `[0,0]` without the sensitivity. See [analyse_e1.py:96–115](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/analyse_e1.py:96>) versus `PREREGISTRATION-E1.md:269–272`. Moreover, the sensitivity does not alter H2/H4 verdicts; it must not be presented as calibrating those decisions.

**5. Registration alignment and freeze — not complete.**

The 80-reading open schedule and separate pre-admission/final-admission paths are **fixed**: `e6.py:41–51,712–715`. Vendor contrasts, benchmark contrasts, behavioural subsets and sensitivity switches are present.

Remaining implementation mismatches include:

- **The registered one-attempt construction limit is not enforced.** A failed proposal is rescheduled because only successful records enter `have`; implementation jobs use the same pattern. I reproduced this without model calls. `PREREGISTRATION-E6.md:29–34`; `e6.py:233–234,263–264`.
- **Per-vendor levels and FPR bounds are not emitted**, although registered; `per_vendor` contains only E6-1/E6-2 contrasts. `PREREGISTRATION-E6.md:136`; `analyse_e6.py:249–255,272–276`.
- The missing-data and E1 bridge/boundary mismatches above remain.

`FREEZE_test.json` does not yet exist. That is an unfinished release prerequisite, not evidence against the ongoing construction. However, **the new freeze implementation would still be insufficient after construction finishes**.

The exact missing commitments are:

| Required content/check | Present gap |
|---|---|
| Corpus, references, hidden comparators and tolerances | The three `data/{humaneval_base,humaneval_plus,mbpp_plus}.jsonl` files are absent from the manifest. Replacing every loaded reference implementation left `e6_state()` unchanged. |
| Complete executable dependency chain | `freeze.CODE` omits corpus/execution/prompt/parser/policy dependencies outside `icml/`, including the relevant `crossaudit` sources and constitution/configuration artefacts. |
| E1 rendered prompts and actual schedules | `e1_state()` records admissions, taxonomy and a universe hash, but no rendered prompt hashes or persisted schedule/order commitments. |
| E1 behavioural counts | Amendment 4 requires per-item behavioural evidence; the bundle includes generation records, but no computed behavioural-count artefact. |
| Environment | Package versions for both environments are absent; `verify()` explicitly ignores the recorded version section. |
| Manifest integrity | Required files may hash as `"missing"`; no required-key schema is checked. An empty `{}` manifest passes `verify()` in the in-memory test. |

Evidence: [freeze.py:26–38](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/code/icml/freeze.py:26>), `freeze.py:48–88,92–99`; required contents: `PREREGISTRATION-E6.md:150–154`, `PREREGISTRATION-E1.md:273–275`.

**(b) Disclosures**

The development-driven domain, predicate, budget, margin and hypothesis-order revisions are permissible if disclosed and frozen before test. They do not remove the implementation failures above.

Current dev denominators are **39 execution-admitted / 24 primary open units**, and **48 execution-admitted / 42 primary controls**. Accordingly, 3,120 and 768 readings describe the larger grids; the primary populations contribute 1,920 and 672 readings.

Saved E6 summaries are stale: the open summary retains the old ±5 label/order, while the control summary still analyses 48 primary units. Fresh control analysis gives **42 units and J = 91.07 points**. See `e6_results_v4_dev.json:914–919` and `e6det_results_v4_dev.json:3`.

E1’s nine test items span seven problems. Its all-zero sensitivity is **34.8%** at that scale. The retained experiment can support a small selected replication; tight equivalence or false-alarm guarantees require considerably stronger evidence.

**(c) Release verdicts**

| Experiment | Release now? | Remaining conditions |
|---|---|---|
| **E6** | **No** | Resolve admitted validity/domain failures; correct and verify betting inference; finish sensitivity provenance and missing-data handling; reconcile construction limits; complete a sound freeze. |
| **E1** | **No** | Retention and H6 wiring are fixed. Bridge freshness, completeness and keyword handling remain defective; boundary implementation and the freeze contract remain incomplete. |

