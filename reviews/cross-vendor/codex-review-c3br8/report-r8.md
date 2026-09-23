# Eighth review — `study/ceiling3b` at `71eb0ad`

**Not quotable. The proposed resolution is reasonable, but the branch still describes Table 5b as measuring defect assertion.**

## Blocking finding: the rename is incomplete

The caption, table header, §2’s positive claims and outer JSON key have changed. These active definitions have not:

- [Results §1](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:157) still calls the quantity **“Recognition”** and asks whether the finding “assert[s] the code is *wrong*.”
- [The report](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/report_ceiling3b.py:198) retains that definition in its comment and generated `note`.
- [numbers.json](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/numbers.json:236) consequently still says “whether the finding asserts a defect.” All three nested rate keys remain `recognised_rate_over_all_P`.
- The manifest still describes L1’s role as answering “recognition questions.” Amendment 3 still promises a “defect-asserting finding” rate; it needs an explicit subsequent correction, preserving the historical amendment.

Furthermore, [§4](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:238) calls the instrument **“narrower than ‘asserts a defect’.”** Its inclusion criterion is broader: it admits reported failures despite an express disclaimer of a requirement. The accompanying claim that the quantity is renamed “throughout this file” is demonstrably false.

### Renaming or withdrawing?

**Renaming is an appropriate resolution; I would not withdraw the descriptive quantity.** The frozen labels can support “reports a failure on the named class,” with the prompt’s inclusion rule stated explicitly. They cannot support the narrower defect-assertion interpretation without another adjudication.

Removing the five identified items reproduces **27 → 22 instances**. Reporting this as the reviewer’s sensitivity, without adopting it as the study’s estimate, is appropriate. It is not a separately validated recognition estimate or a formal bound on true recognition.

## Numerical reproduction

I ran the report and splice with writes intercepted in memory. All three outputs match the checkout byte-for-byte:

| File | SHA-256 |
|---|---|
| `numbers.json` | `abe36bfae24eae836e79fe2f0f01e56adbe3021f4e321459e6fd68c5d4664b3f` |
| `tables.md` | `4e7e411531e9b0125c95e54c26aead07ab345336c2a268ff723c41f718e32243` |
| Results | `8cec07b8ffe956c96f43e379c70666f2a97f359f041540a76143f9df0dc3f6a0` |

**Every JSON value is unchanged from round 7 after normalizing the renamed outer key.** The historical `fe81c861…` and `cb75ec53…` hashes therefore no longer apply, legitimately.

Raw-cache recomputation, including an independent bootstrap and Tango implementation, gives:

| BLOCKER contrast | Union counts | Discordant counts | Difference, points | Cluster, seed 20260912 | Tango | Grid-unconditional |
|---|---:|---:|---:|---|---|---|
| B − S, P | 3 / 2 | 2 / 1 | +0.9 | [−1.8, +4.5] | [−3.4, +5.6] | [−6.4, +8.2] |
| R − S, P | 25 / 2 | 25 / 2 | +20.9 | [+10.8, +31.8] | [+12.9, +29.9] | [+8.6, +31.8] |
| R − S, C | 16 / 4 | 13 / 1 | +8.0 | [+3.4, +12.7] | [+3.7, +13.7] | [+0.3, +15.3] |

Wilson intervals reproduce: P—B `[0.9, 7.7]%`, S `[0.5, 6.4]%`, R `[15.9, 31.4]%`; C—R `[6.7, 16.6]%`, S `[1.0, 6.7]%`.

The older cluster endpoints in the request are superseded by these seed-corrected values.

## Adjudication

Verified:

- All 190 shuffled IDs, key mappings and finding texts reconstruct from the archive.
- The original sheet contains only ID, specification, solution, hidden failure and finding.
- The strict sheet contains exactly the 72 first-pass consensus-yes items, with matching content.
- Both L2 raw replies parse exactly to their committed CSVs; the files also match byte-for-byte.
- Naming agreement: **179/190**, κ **0.8973830216**.
- Strict agreement: **60/72**, κ **0.6949152542**.
- Five original findings and three strict findings expose rule IDs. The metadata-blind, not allocation-blind disclosure is accurate.

### Ten strict spot-checks

These are my labels **under the actual strict rubric**:

| Item | Mine / consensus | Basis |
|---|---|---|
| J0001 | defect / defect | Reports the empty-string wrong result |
| J0018 | correct / correct | Explicitly says the class is handled correctly |
| J0031 | defect / defect | Reports float truncation despite unspecified behavior |
| J0039 | correct / correct | Explicitly denies a defect |
| J0073 | defect / defect | Reports corrupt negative-input output, disclaiming a requirement |
| J0089 | defect / defect | Reports an empty-input exception, disclaiming a requirement |
| J0091 | defect / defect | Reports negative-input exceptions, disclaiming specification coverage |
| J0130 | defect / defect | Reports an empty-input exception despite the disclaimer |
| J0156 | correct / correct | Describes correct handling or untested cases |
| J0168 | defect / defect | Asserts a zero-input defect |

For the naming pass, I agree on the other nine but **would not label J0168 yes**: its witnessed failures concern negative integers and `False`, while its finding addresses zero. Its strict label is defensible only conditional on its admission to that pass.

All stated J0168 sensitivities reproduce:

- R instances: **27 → 26**
- Agreement: **60/72 → 59/71**
- κ: **0.694915 → 0.692085**
- R correct/untested composition: **24/62 → 24/61**
- First-pass R no count: **46/128 → 47/128**

However, [the binding test](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/tests/test_ceiling3b_report.py:168) still does **not** recompute/assert the last quantity.

## Results §2 and provenance

The substantive §2 conclusions now fit the measurements: the registered kill fires; equivalence is not established; naming and reported failure are separated; the “mostly a limit of seeing” conclusion is absent; the remaining rulebook/model distinction is explicitly unresolved. The 28 S findings concern other matters, predominantly missing imports. The R composition and residual statements reproduce.

One inventory statement remains wrong: [§2 calls both residual analyses unregistered](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:202), but [preregistration §3 explicitly registers the B residual](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/ceiling3b/PREREGISTRATION.md:73). R’s residual is unregistered.

**The recovered L2 endpoint satisfies EXPERIMENT_RECORD §2.** I verified the binary’s stated SHA-256, `codex-cli 0.153.4`, ChatGPT login status, absence of configuration overrides, and the literal `https://chatgpt.com/backend-api/codex`. A wire capture is unnecessary for recording the configuration-determined base URL. The stored reproduction command remains inaccurate: it extracts path fragments and concatenated suffixes rather than the full URL.

Other checks pass:

- All **40** manifest-listed files match frozen commit `e2faa54`; none required at that freeze is missing. The round-7 review was added afterward.
- Corpus, solution and audit-set hashes/counts verify; all four reused S draws’ provenance verifies.
- All **91** archive-manifest entries verify.
- All **2,340** prompt digests reconstruct: **2,221 initial**, **119 repair**. Constitutions are exactly S plus the registered appendix.
- Preregistration precedes the first call; Amendment 1 follows 22 R calls; Amendment 2 follows **100 readings/105 calls**. First-75 cost is **$1.391874**.
- R+B cost **$29.981646**: H19a completion did not depend on the cap raise; complete S-text adjudication did. The interim look remains a disclosed design limitation.
- Cost **$32.206689**, **2,460 calls**; residual **56 → 53** with R, unchanged with B.
- No complete archived finding text occurs in tracked files; `src/`, product tests and kernel paths are unchanged.

**Seven focused tests passed.** The full product suite was not run in this read-only review. No files were modified; the worktree remains clean.

**not quotable — the active report still presents the broader failure-reporting adjudication as defect recognition, despite claiming that interpretation was removed.**
