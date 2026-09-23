**Not quotable at `62bd280`.** The direction correction is right, and the retained numerical values reproduce. But Amendment 4 introduced another repair regression: it deleted the cost/residual records and generated tables, breaking reproduction and the binding tests.

1. **The committed outputs no longer reproduce.** I ran `report_ceiling3b.py --run <archive>` with writes intercepted in memory. The regenerated JSON contains the entire `secondaries` block that Amendment 4 deleted; the regenerated tables contain Tables 6–7 that it also deleted. RESULTS still contains those tables.

   Consequently, neither committed output is byte-identical to regeneration, and the committed table file differs from the RESULTS splice. The regenerated tables **do** match that splice exactly. See [numbers.json](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/numbers.json:1166) and [tables.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/tables.md:69).

   After normalizing the renamed keys and explanatory note, regenerated JSON equals the parent commit’s JSON exactly. Thus **no numerical value changed, but entire measured quantities disappeared from the committed artifact**. “Nothing moved” does not adequately describe this commit.

2. **The rename still misses executable consumers.** The active report, report generator’s explanation, generated note, and three JSON rate keys now use failure-reporting terminology. However, [the binding test](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/tests/test_ceiling3b_report.py:81) still expects the old sentence and accesses `recognised_rate_over_all_P`; its docstring still calls the quantity recognition.

   More importantly, [the live manifest generator](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/ceiling3b/finalise_manifest.py:120) still generates “adjudicator, naming and (post hoc) recognition questions.” That is executable current documentation, not an immutable historical quotation.

   The focused suite gives **3 failed, 4 passed**: splice mismatch, stale H19d assertion, and missing `secondaries`. These failures directly catch this repair.

3. **The current manifest is stale.** Its hashes correctly describe the clean `e2faa54` freeze, but five now differ from HEAD. It omits Amendment 4 and the subsequently archived round-7 review. The previous provenance repair remains valid for its stated freeze; it does not cover the current deliverable. See [manifest.json](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/manifest.json:2).

The strict instrument is **broader than defect assertion**. I read [the actual prompt](/Users/ericdong/Documents/Crossaudit/study-data/wt-ceiling3b-runs/labels/prompt-l2-strict.md:7). Its permission to count an exception even when the specification is silent admits findings that disclaim any requirement violation. Non-blocking severity alone would not establish this distinction; the explicit requirement disclaimers do.

The report now states that plainly, rather than merely removing “narrower”: §1 says “broader than asserting a defect” and forbids quoting it as recognition; §4 explains why. **Renaming is a valid resolution for this descriptive, post-hoc quantity. I would not require withdrawing it or rerunning adjudication merely to retain that narrower reporting claim.** A defect-recognition claim would require a properly defined new adjudication.

Preserving Amendment 3 and the historical round-2 commit description is appropriate. Additive corrections preserve the record of the claim’s movement. But that rationale does **not** justify the live manifest’s current role description or its generator. A reader opening only the manifest still encounters recognition terminology without Amendment 4’s correction. Preserve historical quotations, identify their supersession where readers encounter them, and update current descriptive fields.

The numerical checks completed as follows. These are the seed-20260912 results; the older intervals in the request are superseded.

| BLOCKER contrast | Discordant counts | Difference, points | Cluster 95% | Tango | Grid-unconditional |
|---|---:|---:|---:|---:|---:|
| B − S, P | 2 / 1 | +0.9 | [−1.8, +4.5] | [−3.4, +5.6] | [−6.4, +8.2] |
| R − S, P | 25 / 2 | +20.9 | [+10.8, +31.8] | [+12.9, +29.9] | [+8.6, +31.8] |
| R − S, C | 13 / 1 | +8.0 | [+3.4, +12.7] | [+3.7, +13.7] | [+0.3, +15.3] |

I independently reconstructed unions, discordances, the bootstrap and Wilson intervals from the caches, and recomputed Tango/grid intervals with the statistical routines. Wilson intervals reproduce: B 3/110, **0.9–7.7%**; S 2/110, **0.5–6.4%**; R 25/110, **15.9–31.4%**; C’s R 16/150, **6.7–16.6%**, and S 4/150, **1.0–6.7%**. H19a fails its registered criterion; this demonstrates neither equivalence nor “the grading rule did nothing.”

The post-hoc failure-reporting counts remain **S 3/110, R 27/110, B 3/110**, with unchanged intervals. Naming remains **6/37, 58/104, 4/24** on the registered denominator, and **6/110, 58/110, 4/110** on the derived denominator. Both denominators and their intervals are rendered.

Adjudication checks passed:

- All 190 sheet/key mappings reconstruct from archived findings and the shuffle seed.
- The original sheet omits arm, severity, stratum and instance ID; five finding texts reveal rule IDs. Metadata-blind, not allocation-blind, is accurate.
- The strict sheet contains exactly the 72 consensus-yes items.
- Both L2 raw replies parse exactly to the committed CSV labels.
- Naming agreement is **179/190**, κ **0.8973830216**; strict agreement is **60/72**, κ **0.6949152542**.

I read these ten strict items against their hidden witnesses:

| Item | Consensus strict label | My assessment |
|---|---|---|
| J0001 | defect | Agree: explicitly reports wrong empty-string result |
| J0018 | correct | Agree: explicitly claims correct handling |
| J0031 | defect | Agree under broad rubric; disclaims float requirement |
| J0039 | correct | Agree: claims correct duplicate handling |
| J0073 | defect | Agree under broad rubric; disclaims negative-input requirement |
| J0089 | defect | Agree under broad rubric; reports empty-input exception |
| J0091 | defect | Agree under broad rubric; exception type is misstated |
| J0130 | defect | Agree under broad rubric; empty-input exception despite disclaimer |
| J0156 | correct | Agree: correctness/untested discussion |
| J0168 | defect | Agree conditional on admission; disagree with first-pass naming |

Naming “yes” for findings claiming correct handling is consistent with the report’s operational naming interpretation; it does not establish recognition. J0168 remains the exception: its discussion of zero does not adequately identify the witnessed negative inputs. Removing the five requirement-disclaiming items reproduces **27 → 22 distinct R instances**. That is a sensitivity calculation, not a validated replacement recognition estimate.

Dropping J0168 reproduces **26/110**, agreement **59/71**, κ **0.6920852909**, composition **24/61**, and first-pass `no` **47/128**. The existing test still does **not** recompute the last quantity, despite its comment claiming to cover every moved quantity.

My sentence-level review of §2 finds the measured rates, withdrawal of the severity-policy inference, and refusal to separate rulebook from model limitation supported. “Mostly a limit of seeing” is absent. Two older reporting defects remain:

- [The inventory](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:205) calls both residual analyses unregistered, although [preregistration §3](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/ceiling3b/PREREGISTRATION.md:73) explicitly registers B’s residual analysis. The total of twenty non-primary quantities still adds up.
- Repeated effects, including ceiling 2’s **+26.8 points**, lack accompanying intervals in §2, contrary to EXPERIMENT_RECORD §9.

Other verification:

- All **2,340 prompt digests** reconstruct: 2,221 initial prompts and 119 malformed-reply repairs. R/B constitutions are exactly S plus the registered appendix.
- All **91 archive-manifest entries** verify; no exact archived finding text appears in tracked files. `src/`, product tests and kernel code are unchanged.
- Residual reproduces **56 → 53 with R; 56 → 56 with B**. Ledgers contain **2,460 calls**, totaling **$32.206689**, displayed as $32.21.
- Preregistration precedes the first call. Amendment 1 follows 22 calls; Amendment 2 follows **100 readings/105 calls**. First-75-reading cost is **$1.391874**. R+B cost **$29.981646**. The cap raise is a disclosed post-interim stopping-rule deviation; the S-text adjudication comparator depended on it.
- Reused S provenance and relevant corpus/solution hashes and row counts verify. The manifest’s additional, unused BigCodeBench file was unavailable locally.
- Endpoint recovery satisfies §2: binary hash, version, ChatGPT login mode, absent configuration overrides and the full endpoint literal verify. A wire capture is not required for a clearly qualified configuration-derived endpoint. The stored `strings` filter still reproduces suffixes, not the complete URL.
- Statistics suite: **19 passed, 3 timed out** at 30 seconds each. Full product suite and rebuild were not run. No files were modified.

**not quotable — Amendment 4’s own regeneration deleted measured outputs and broke the report’s reproducibility contract, despite claiming that the repair changed no values.**
