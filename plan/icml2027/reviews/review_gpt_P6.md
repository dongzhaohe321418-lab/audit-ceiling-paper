**E6: release no. E1: release no.** I reviewed `c06b1faa42e0c02f94a8c38fed8d58b7e21f101c`. Several P5 fixes work, but genuine executable blockers remain.

References below are relative to `crossaudit-harness/benchmarks/code/`.

**(a) Remaining blockers and P5 dispositions**

**1. Betting inference — fixed.**

At `icml/analyse_e6.py:146`, the corrected negative-direction cap is `0.75/(1-m)`. Each capital factor is at least 0.25. Bets are recorded before updating with the current observation (`:139`); fixed sample-size tuning and the predetermined permutation preserve predictability.

The inversion is monotone in \(m\), and `betting_interval` correctly allocates \(\alpha/2\) to each transformed tail (`:159`). These conclusions require the stated sampling assumptions; shuffling alone does not establish them. The cap agrees with [Waudby-Smith and Ramdas, Theorem 3](https://rss.org.uk/RSS/media/File-library/Events/Discussion%20meetings/Estimating-means-of-bounded-random-variables-by-betting.pdf).

Adversarial checks:

- The P5 negative-factor example now gives **0.25**.
- Twenty-four zeros give an upper bound of **15.057%**, removing the previous false 10% certificate.
- Exhaustive enumeration of all 4,096 Bernoulli sequences at \(n=12\), across means 0.01–0.99, gave maximum non-coverage **3.585%**. This checks implementation behaviour, rather than proving general validity.
- Forty zero contrasts give **[−11.648, +11.648] points**, consistent with section 10’s warning that ±10 equivalence will likely be inconclusive.

E6-1b is separate and non-gating (`analyse_e6.py:333`, `:343`). E6-3 uses the betting interval, ±10 margin and last position in the family (`:327`, `:336`, `:343`). The precision limitation is explicitly registered at `PREREGISTRATION-E6.md:159`.

**2. Proposal/implementation attempt limits — fixed.**

Failed records now consume attempts:

- Proposal: `icml/e6.py:244`.
- Implementation: `icml/e6.py:277`.

Injecting failed records scheduled **zero replacement jobs** for `open`, `open2` and `det`. Existing proposal and implementation records contain no duplicate attempt keys.

**3. Outcome-blind enlargement — fixed and acceptable before test.**

Eligibility uses first-attempt admission and the two judges, without audit outcomes: `icml/e6.py:232`, `:246`; `icml/analyse_e6.py:181`.

I verified:

- All **374 eligible test problems** have second-attempt proposal records; none is extra or missing.
- First- and second-attempt primary problem sets are disjoint.
- `merged_open` produces **40 distinct problems: 32 + 8** (`analyse_e6.py:243`).
- First-attempt selection succeeds when reads of audit files are deliberately prohibited.

The enlargement changes the construction-selected population and must remain disclosed, but it is not itself a release blocker.

**4. Reporting and provenance — not fully fixed.**

The following are **fixed**:

| Check | Evidence and adversarial result |
|---|---|
| Per-vendor levels and FPR bounds | `analyse_e6.py:300`; emitted for none/menu/resolve. |
| Primary missing-data bounds | `:213`, `:226`, `:287`, `:375`; entirely missing contrasts return bounds and exclusion counts, with no positive verdict. |
| Judge identities | `:198`; duplicating one judge cannot substitute for the other. |
| Judge prompt hashes | `:193`; an altered hash aborts population construction. |
| Conflicting sensitivity scores | `e6.py:885`, `analyse_e6.py:47`; flipping only `verified_refdomain` aborts completeness. |

**Remaining mismatch:** secondary E6-2 estimates still call `boot` directly, omitting the registered missing-data bounds and exclusion counts:

- Per configuration: `analyse_e6.py:296`.
- Per vendor: `:302`.
- Per benchmark: `:306`.
- Behavioural subset: `:311`.

With one wholly missing problem, primary E6-2 reports **[−50, +50] points and one exclusion**, while the corresponding secondary entries return `None`. This remains inconsistent with `PREREGISTRATION-E6.md:108`.

**5. E1 bridge and boundary handling — not fully fixed.**

These P5 fixes **pass**:

- Evidence freshness in scheduling: `icml/e1.py:1456`, `:1468`. Replacing all stored hashes with stale hashes triggered **46 classification calls** to a stub.
- Completeness enforcement: `e1.py:1479`; both analysis paths call it at `analyse_e1.py:188` and `:302`. Removing one current adjudicator vote aborts.
- Keyword witnesses: `e1.py:1436`. The executor successfully built the bridge evidence for `split_words(txt='Hello\tworld!')`, retaining the keyword call.
- Amendment 4 item 8 now keeps non-DETERMINED classes separate: `PREREGISTRATION-E1.md:279`.
- Problem-level cancellation: `analyse_e1.py:112`. Two items with contrasts +1 and −1 in one problem trigger the boundary sensitivity.
- The sensitivity explicitly leaves H2/H4 verdict rules unchanged (`analyse_e1.py:115`, `:149`, `:151`). It does **not** calibrate those decisions.

Two defects remain:

**Stale classifications can still determine the reported class.** `bridge_complete` checks whether current votes exist, but `bridge_classes` selects each adjudicator’s last stored evidence hash without restricting it to current evidence (`e1.py:1499`). Keeping current DETERMINED votes and appending obsolete OPEN votes makes completeness pass while the reported class becomes **OPEN**.

**The primary analysis crashes when a retained item has a bridge witness.** Its bridge summary references undefined `tax` at `analyse_e1.py:199`. Injecting one such witness produces:

```text
NameError: name 'tax' is not defined
```

The current dev run avoids this branch because its retained intervention items have no bridge witnesses. That does not make the test path safe.

**6. Freeze — not fixed overall.**

The expanded commitments are substantially improved:

| Commitment | Status |
|---|---|
| Corpus, references and comparator data | **Fixed coverage:** `icml/freeze.py:105`. |
| CrossAudit sources and constitution/configuration | **Fixed coverage:** `:106`, `:107`. |
| E1 rendered prompts and required universe | **Fixed:** `:80`. |
| E1 behavioural artefact | **Fixed:** `:34`, `:92`; 150 items, no infrastructure-only entries. |
| Both environments’ package versions | **Fixed:** `:109`; versions participate in verification at `:136`. |
| Empty manifest / missing required files | **Fail closed:** `:121`. `{}` raises `KeyError`; a required file marked missing is refused. |
| Dirty-code refusal when writing | **Fixed:** `:148`; injected dirtiness caused refusal before any write. |
| Test-stage verification gates | **Present:** `e6.py:743`, `e1.py:1242`; both refuse the absent manifest before model calls. |

However, three freeze defects block release:

1. **The unmodified builder crashes on the existing directory tree.**  
   `tree_sha` includes directories, then `fsha` calls `read_bytes`: `freeze.py:43`, `:48`, `:107`. Actual result:

   ```text
   IsADirectoryError: .../records/icml/project/project-cross
   ```

2. **Verification silently changes the requested E6 experiment.**  
   `e6_state` resets the global kind to `open` (`freeze.py:76`), and `build` calls it during verification (`:117`). After bypassing only the directory error in memory, both:

   ```text
   stage_audit(test), selected kind det
   stage_audit(test), selected kind open2
   ```

   scheduled **4,880 first-attempt open readings into `e6_audits_v4.jsonl`**. Their intended schedules contain **944** and **2,480** readings respectively. I intercepted execution before any calls.

3. **Persisted E1 schedules remain outside verification.**  
   `e1_state` hashes the reconstructed universe, but neither `RECORDS` nor that state binds the actual schedule files (`freeze.py:26`, `:95`). `e1.schedule` trusts an existing file (`e1.py:1225`). Supplying an empty test schedule in memory made **verification pass and scheduling return zero jobs**.

For the requested mutation question: with the directory failure bypassed solely for diagnostic testing, changed frozen-record hashes, corpus/reference hashes, parser-source hashes, rendered prompts and package-version state were **rejected**. A changed **E1 schedule record passed**. There is therefore no complete freeze guarantee yet.

**7. Executable validity — not fixed overall.**

The named P5 failures are now excluded: open Mbpp/124 (`records/icml/e6_units4.jsonl:7`), control Mbpp/65 (`e6det_units4.jsonl:51`) and control Mbpp/798 (`e6det_units4.jsonl:64`). The broader reference-domain agreement check is implemented at `icml/e6.py:543`.

New probes nevertheless break retained primary dev units:

| Retained unit | Counterexample and executed result | Admission evidence |
|---|---|---|
| Open **Mbpp/405** | `check_tuplex((1,), 1+0j)`: `valid=True`, `in_class=False`; reference/B return `True`, both A implementations return `False`. | `e6_units4.jsonl:26`; implementations `e6_impls.jsonl:160`, `:163`. |
| Open2 **HumanEval/74** | `total_match(['\u0301\u0301'], ['a'])`: `valid=True`, `in_class=False`; reference returns `['a']`, shown A returns the combining-mark list. | `e6b_units4.jsonl:11`; implementations `e6b_impls.jsonl:46`, `:49`. |
| Control **Mbpp/170** | `sum_range_list([1,2,3], -2, -2)`: reference returns `2`, both A implementations return `0`; outside the class. Although `valid=False`, v4.2 explicitly requires agreement wherever the reference evaluates successfully. | `e6det_units4.jsonl:23`; implementations `e6det_impls.jsonl:208`, `:211`. |

I reran the actual admission logic with each additional input, using read-only execution adapters. **All three admissions became rejections for `outside_class_agree`.** HumanEval/74 also exhibits disagreement between its A implementations on `(['a\u0903'], ['b'])`, a valid in-class input.

These are concrete failures of the registered labels, not merely the general limitation that finite testing cannot prove correctness.

**(b) Disclosures**

- Test populations independently match the supplied counts: **61/32 open, 31/8 open2, 59/54 controls**. No E6 or E1 test audit was found.
- E1 retains **nine test items across seven problems**, with **1,928 required readings**. Its all-zero problem-event sensitivity is about **34.8%**; tight H2/H4 guarantees are not established by a collapsed bootstrap interval.
- The development-driven construction, population, budget, margin and ordering revisions remain disclosures. E6-1b’s separate status does not establish joint error control across all reported claims.
- The running open2 dev audit was not treated as a completed analysis or as a blocker.
- At my snapshot, `icml/` was clean and `FREEZE_test.json` absent. The freeze builder has a reproducible failure beyond dirty-state refusal.
- The supplied repository-local interpreters do not exist. I used the enclosing workspace’s `.venv` and `.exec`, with pipe-based execution and in-memory stubs. **No files were changed and no model calls were made.**

**(c) Verdict**

| Experiment | Release to test? | Required before reconsideration |
|---|---|---|
| **E6** | **No** | Resolve retained validity failures, freeze traversal/kind defects, and remaining registered missing-data reporting gaps. |
| **E1** | **No** | Ensure bridge outputs use current evidence, fix the non-empty bridge analysis crash, and bind schedules in a working freeze. |

