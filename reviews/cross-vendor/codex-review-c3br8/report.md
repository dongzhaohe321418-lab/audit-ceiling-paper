**The repair passes. The study is quotable for its stated measurements, including the explicitly post-hoc failure-reporting quantity.** I found no remaining blocker equivalent to rounds 8–9.

The reproducibility contract now holds:

- Running `report_ceiling3b.py --run <archive>`, with filesystem writes intercepted in memory, reproduced both files byte-for-byte: `numbers.json` SHA-256 `88beb237…`, `tables.md` `4e7e4115…`. The Results splice also matches.
- `secondaries` and Tables 6–7 are restored. Against pre-Amendment-4 commit `71eb0ad`, the top-level keys match exactly. After mapping the three renamed keys, **every numerical value matches**; only the explanatory note differs.
- All seven report-binding tests pass.

The [manifest](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/manifest.json:53) describes the delivered files. It freezes `b0888ba`; `fc5b002` changes only the manifest. All **41 listed file hashes** match HEAD, no tracked study file is omitted, and no previous manifest leaf was lost. Amendment 4, the seventh review, and L1’s corrected role are present. All four corpus hashes, byte counts and row counts match the symlinked corpus; the data block is unchanged. Audit-set, instance and solution hashes also verify. All **91 archive-manifest entries** pass.

**The rename is substantively complete.** The active prose, generator, generated note, rate keys, executable consumers and live adjudicator role describe failure reporting. Remaining `defect` category names preserve the original adjudication labels; they do not redefine the quantity as defect recognition.

The [strict prompt](</Users/ericdong/Documents/Crossaudit/study-data/wt-ceiling3b-runs/labels/prompt-l2-strict.md:7>) is **broader** than defect assertion: it admits reports of exceptions or wrong values even when the finding disclaims a specification requirement. [Results §1](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:157) and §4 now say that affirmatively, rather than merely deleting “narrower.” Renaming is a valid resolution for this descriptive, post-hoc quantity; withdrawal or re-adjudication is unnecessary unless the author wants to claim defect recognition.

Preserving Amendment 3 and the round-2 commit description is the right decision. [Amendment 4](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/ceiling3b/PREREGISTRATION.md:149) explicitly supersedes their interpretation while preserving evidence of what was originally promised.

I independently reconstructed union flags and the seed-20260912 cluster bootstrap from the caches, and recomputed Wilson, Tango and grid-unconditional intervals:

| Contrast | Discordant counts | Difference, points | Cluster 95% | Tango | Grid-unconditional |
|---|---:|---:|---|---|---|
| B−S, BLOCKER P | 2 / 1 | +0.9 | [−1.8, +4.5] | [−3.4, +5.6] | [−6.4, +8.2] |
| R−S, BLOCKER P | 25 / 2 | +20.9 | [+10.8, +31.8] | [+12.9, +29.9] | [+8.6, +31.8] |
| R−S, BLOCKER C | 13 / 1 | +8.0 | [+3.4, +12.7] | [+3.7, +13.7] | [+0.3, +15.3] |

Thus the older `[−1.8,+3.8]`, `[+10.8,+31.5]` and `[+3.4,+13.0]` intervals repeated in the request are not the current seed-corrected results. The report has the reproduced values.

The adjudication checks also pass:

- All 190 IDs reconstruct from the archived findings and shuffle seed; their key mappings match.
- The sheets omit arm, severity, stratum and instance metadata. Five original findings reveal rule IDs, so **metadata-blind, not allocation-blind** is accurate.
- The strict sheet contains exactly the 72 first-pass consensus-yes items, with unchanged finding and witness text.
- Both L2 raw replies parse exactly to the committed CSVs.
- Naming agreement is **179/190, κ=0.897383**; strict agreement is **60/72, κ=0.694915**.

My ten-item spot check against the witnesses:

| Items | My strict label | Agreement with consensus |
|---|---|---|
| J0001, J0031, J0073, J0089, J0091, J0130 | `defect`, meaning failure-reporting under this rubric | Yes |
| J0012, J0018, J0039 | `correct` | Yes |
| J0168 | `defect`, conditional on admission to the strict pass | Yes; I retain the disclosed first-pass inclusion objection |

The “handled correctly” findings count as naming under the reported interpretation; they do not establish recognition. Removing the five requirement-disclaiming findings reproduces the reviewer’s **22-instance sensitivity**, not a newly validated recognition estimate. Removing J0168 reproduces **26 instances, agreement 59/71, κ=0.692085, composition 24/61, and complementary first-pass count 47/128**.

Other requested checks:

- All nine archived constitutions match their assigned rules exactly; R and B are S plus their registered appendix.
- All **2,340 prompt digests** reconstruct: 2,221 initial prompts and 119 repairs. Archived findings also reproduce every cache’s finding counts and flags.
- No exact archived finding text occurs in tracked files.
- Residuals reproduce **56→53 with R; 56→56 with B**.
- Ledgers reproduce **2,460 calls and $32.21**; all four reused S draws’ provenance matches.
- Preregistration preceded the first call. Amendment 1 followed 22 calls; Amendment 2 followed **100 readings/105 calls**. The first-75 cost is `$1.391874`. The interim-informed cap raise remains a disclosed deviation: H19a did not depend on it; the S-text adjudication comparator did.
- The endpoint binary’s hash, version and full URL literal verify; configuration contains neither override. This satisfies §2 as recovered configuration provenance, with the stated wire-observation limitation.
- `src/`, product tests and kernel paths are unchanged. The worktree remains clean.

Reading §1–§2 sentence by sentence, the substantive conclusions stay within the evidence: B demonstrated no positive BLOCKER effect, which is not equivalence; R increased blocking and false positives; naming and failure reporting remain distinct; the remaining rate is not partitioned into rulebook versus model limitations. The “mostly a limit of seeing” inference is absent. The residual registration correction is accurate.

Three **nonblocking reporting defects** remain:

- Some repeated figures still lack adjacent intervals, notably §2’s −20-point any-finding contrast and 97.3%/96.0% rates. The complete intervals exist in the tables; carry them into quotations.
- The manifest’s extraction command prints path fragments, although the full endpoint itself verifies.
- The sensitivity test still does not assert `47/128`, despite its comment claiming every moved quantity is bound.

Testing limits: the statistics/architecture run produced **34 passes and three 30-second timeouts**. I stopped the timeout-disabled rerun after 139 seconds without a completed test; I do not claim those coverage tests passed. The full product suite failed during collection because the read-only environment provides no writable temporary directory.

**quotable — the complete measured outputs now reproduce, and the active interpretation matches the instrument.**

Reader sentence: “On this frozen code set at four readings, Sonnet 4.6’s referent rule increased BLOCKER recall by 20.9 percentage points (95% problem-cluster interval 10.8–31.8), alongside an 8.0-point increase in false positives (3.4–12.7), while the grading rule showed no demonstrated recall improvement (+0.9 points, −1.8–4.5).”
