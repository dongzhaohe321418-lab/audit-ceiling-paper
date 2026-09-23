## Independent review

**Verdict: blocking concerns remain.** The recorded audit outcomes are arithmetically correct, but the revised 84.2% headline is neither the preregistered primary nor a reproducible estimate of “defects the specification determines.” It estimates recall on a post hoc target consisting of mechanically filter-accepted injections. Those filters do not establish specification-determinedness.

### Major concerns

**IR-M1, Blocking. The 84.2% population does not enforce the property named in the claim.**

The six filters establish only that:

- some six-word specification substring was supplied;
- the edit passes visible tests and fails the hidden suite;
- the diff is small and executable;
- a nonempty witness string exists.

In particular:

- F1 does not connect the quotation to the edit.
- F6 is only `bool(witness_input)`. It neither parses nor executes the witness and does not recover a hidden input as the preregistration promises. See [inject.py](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/inject.py:200).
- There is no mechanical check that `input_class` describes the actual failure, that exactly one semantic defect was introduced, or that the edit lacks an artificial marker.
- Once gate-rejected instances are restored for the 84.2% estimator, no semantic adjudication remains.

Therefore 84.2% is defensible only as recall on “small, visible-clean, hidden-failing injected edits that supplied a literal quote and nonempty witness.” It is not an estimate for specification-determined defects generally.

A concrete manufacturing mechanism exists. F3 selects edits caught by the benchmark’s hidden oracle. Worse, a failed F3 is fed back to the injector as “Your edit did not change the behaviour on any other input,” after which the model retries [inject.py](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/inject.py:375). That discloses the hidden-suite verdict despite Amendment 1 saying retries see nothing about the hidden suite. Repeatedly selecting visible-clean edits that trigger the hidden suite can enrich for broad, local, conspicuous defects that the auditor also blocks easily. The rejected-gate arm never reaches edits discarded by F3, F4, or the retry process.

Nothing replaces the withdrawn conservativeness argument. The rejected arm measures gate selection only. The probe documents artificiality but does not control it, and the twin arm controls problem identity but not edit salience.

**IR-M2, Blocking. The Amendment 6 headline is post hoc and absent from the reproducible record.**

Git ordering confirms:

- Amendment 6 was committed at `3ffb0c6`, before the rejected arm was wired at `57239bb`.
- Rejected-arm caches and the 77.5% outcome arrived later at `efe3caf`.
- But H22a, the twin result, and the probe were already known in `2199eaf`.
- Amendment 6 preregistered auditing 40 rejected instances. It did not specify the population-weighted 84.2% estimator, its bootstrap, or replacing the primary headline with it. Those were introduced after observing 31/40.

The reproduction claim is also false as written. The in-memory `report_inject.build()` exactly reproduces the committed `numbers.json`, and `render_tables()` exactly reproduces `tables.md`, but neither contains the rejected arm or the 84.2% estimate. The Amendment 6 table is typed directly into [RESULTS-INJECT.md](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/RESULTS-INJECT.md:46), outside the registered splice. [report_inject.py](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/report_inject.py:128) never loads the rejected sample.

The point estimator itself is appropriate for the finite 281-instance filter-accepted population, assuming the 40 are a simple random sample:

\[
\frac{92}{281}\frac{90}{92}+\frac{189}{281}\frac{31}{40}
=84.1548\%.
\]

My independent problem-cluster bootstrap reproduces **[73.7523, 93.1016]**. The prose honestly says that 189 instances are estimated from 40. The “95% cluster CI” label is not calibrated, however. It bootstraps the fully observed 92-instance stratum as though sampled, resamples problem clusters although the rejected arm was sampled by instance, and does not apply the finite-population design. As a transformed interval, it also lacks the coverage simulation required by `EXPERIMENT_RECORD` §10. It should be called uncalibrated until that is supplied.

**IR-M3, Blocking. Sections 1 to 3 still turn blocking into defect detection.**

The records measure whether an instance received any blocking finding, not whether a finding identified the injected failure. Nevertheless the results say:

- “The auditor is responding to the defect” [line 98](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/RESULTS-INJECT.md:98).
- “One reading catches 94.4%” and “ability to see a defect” [line 120](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/RESULTS-INJECT.md:120).
- “not a limit on detecting specification-determined defects” [line 132](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/RESULTS-INJECT.md:132).

The twin contrast proves that the edit causes many more blocks. Amendment 6 correctly says the edit also carries salience. It does not prove that the blocking findings name or reason from the defect. Those sentences contradict the report’s own §5 boundary.

The statement that the new gap is larger than Study 21’s post hoc split is also no longer true for the revised headline. Study 21’s contrast was 92.0% versus 35.3%, a 56.7-point gap. The stratified headline is 84.2% versus 30.0%, a 54.2-point gap. Only the withdrawn gate-selected headline has the larger gap.

### Arithmetic reproduced

From the caches, independently:

- Gate admission: **92/281 = 32.74%**. Sonnet voted yes on 127; Opus on 110.
- Gate-accepted audit rate: **90/92 = 97.83%**.
- Gate-rejected sample: **31/40 = 77.5%**, problem-cluster bootstrap **[62.22, 90.48]**.
- Stratified estimate: **84.1548%**, bootstrap **[73.75, 93.10]**.
- Stratified minus frozen comparator: **+54.15 points**. An analogous three-population cluster bootstrap gives approximately **[+39.63, +67.71]**, though this does not remove the construction confounds.
- Paired result: **90/92 versus 11/92**, **+85.87 points**, cluster bootstrap **[+77.27, +93.26]**; discordance **79/0**. The separately printed Tango interval is **[+77.31, +91.55]**.
- Curve: **94.429, 96.506, 97.030, 97.360, 97.593, 97.748, 97.826, 97.826%** for K = 1 through 8.
- Frozen comparator: **33/110 = 30.0% [20.0, 40.7]**, consistent with ceiling 1.

### Construction sample

I sampled deterministically with `random.Random(20260915)` over sorted IDs.

Accepted population sample:

| Instance | Admit? | Assessment |
|---|---:|---|
| b1:HumanEval/123 | Yes | Removing sorting directly violates the ordered-result requirement. |
| b1:HumanEval/35 | Yes | Singleton branch returns one below the maximum, though conspicuously contrived. |
| b1:Mbpp/19 | **No** | Defect is determined, but `[5]` is not a valid argument list for a list-valued argument. F6 should have rejected it. |
| b1:Mbpp/256 | Yes | Counts 2 below 2; plainly wrong. |
| b1:Mbpp/292 | Yes | Truncation instead of floor fails negative quotients. |
| b1:Mbpp/476 | Yes | Omits a last-position minimum. |
| b1:Mbpp/79 | Yes | Modulo 4 is not oddness. |
| b2:HumanEval/0 | Yes | Changes strict “closer than” to inclusive. |
| b2:HumanEval/42 | Yes | `abs(x)+1` mishandles negatives. |
| b2:Mbpp/171 | Yes | Four sides for nonmultiples of five contradicts pentagon perimeter. |
| b2:Mbpp/455 | Yes | Omits January from 31-day months. |
| b2:Mbpp/476 | Yes | Byte-identical duplicate of b1:Mbpp/476. |
| b2:Mbpp/643 | **No** | The injected comment literally says `DEFECT: should be +`, violating the promised no-marker construction. Both gates nevertheless admitted it. |
| b2:Mbpp/809 | Yes | Replaces strict smaller-than with `<=`. |
| b2:Mbpp/89 | Yes | Zero returns zero rather than the closest smaller integer. |

Thus 13/15 satisfy the promised overall construction in my reading. All 15 contain a substantively specification-determined edit, but two fail claimed mechanical or realism requirements.

For ten filter-rejected instances, the archive preserves only the first parsed rejected code because `setdefault("last_code", ...)` is used [inject.py](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/inject.py:386). Later rejected proposal text and its `input_class` are unavailable.

| Instance | Should keep? | Assessment |
|---|---:|---|
| b1:HumanEval/112 | No | Set conversion is behaviorally equivalent here. |
| b1:HumanEval/24 | No | Loop change plus final `return 1` remains equivalent on intended positive inputs. |
| b1:HumanEval/94 | No | Breaks visible cases and exceeds the diff limit. |
| b1:Mbpp/253 | **Yes for the scientific target** | Excluding negative integers is plainly contrary to “integer elements”; F3 discarded it only because hidden tests omitted negatives. |
| b1:Mbpp/281 | **Probably yes for the target** | Returning true on duplicate unhashable elements is a determined defect unless the domain is restricted to hashables; discarded by F3/F4. |
| b1:Mbpp/435 | No | Negative-number “last digit” semantics are not settled, and the quote was not literal. |
| b1:Mbpp/68 | No | Every length-two list is monotonic, so the edit is equivalent. |
| b1:Mbpp/767 | No | Breaks visible tests and is too large. |
| b2:Mbpp/233 | No | Returning zero for a zero cylinder dimension is still correct. |
| b2:Mbpp/422 | No | Breaks all relevant visible examples. |

The sample therefore directly shows that F3 and F4 discard at least plausible specification-determined defects. The rejected-gate arm does not measure this selection.

### Duplication, probe, and cross-tab

The population-I duplication calculation is correct: **59 distinct hashes**, **33 duplicate groups**, **66 covered instances**, and **no duplicate hash spans problem IDs**. Problem-cluster resampling keeps those duplicates together.

The statement that the rejected sample has “40 distinct programmes” is false. It has **35 distinct `modified_sha256` values**. Five b1/b2 duplicate pairs occur for HumanEval/43 and Mbpp/140, 266, 569, and 95. They remain within problem IDs, so its problem bootstrap also absorbs them. The Wilson figures should be marked directly as ignoring clustering; prose elsewhere is not sufficient, especially because the rejected-sample prose incorrectly denies duplication. “Problem clustering is at least as conservative as programme clustering” is not guaranteed merely by nesting, though it does capture the dependence here.

The probe arithmetic is correct: 147/152 = 96.7%; bounds 147/184 = 79.9% and 179/184 = 97.3%. It is appropriately prominent as the main limitation. But its claimed independence is false. `claude-opus-4-8` is both the second gate and the prober [inject.py](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/inject.py:44), while the report repeatedly says it is “not a gate.” Because Opus helped select I, the probe is also evaluated on a population partly selected by the same model.

The cross-tab is correct. For classified items the table is 63/65 caught in the artificial cell and 4/4 in the natural cell. Fisher’s two-sided p is exactly **1.0**. The chance either of two misses falls in the four-item natural cell is **11.34%**, with expectation **0.116**. No current sentence uses that table as evidence against salience.

### Other record and boundary findings

- Results and `report_inject.py` still say there are five amendments, not six.
- Results §5 resurrects the withdrawn conservativeness argument by saying the same-vendor gate is weaker and therefore conservative [RESULTS-INJECT.md](/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad/wt-inject/benchmarks/code/RESULTS-INJECT.md:220).
- The stated $16.47 total omits the $1.90 rejected arm. Main-arm accounting is about **$18.37**; unique archived usage entries total **$18.53** including pilots and failed/preliminary calls.
- `src/` and kernel directories are untouched.
- No full archived solution or finding text is committed, but the strict “no specification text, no solution text” boundary is violated by literal corpus quotations and edit fragments in Amendment 2, Amendment 6, and Results §1.
- Focused tests have **four genuine failures**: the obsolete ladder assertion and three report/splice assertions. Three additional filter tests could not run because this read-only environment provides no writable temporary directory. The full suite was therefore not green or fully runnable. The worktree remains clean and unchanged.

**not quotable — the 84.2% headline removes the only semantic gate, so its denominator is not shown to be “defects the specification determines”; it is a post hoc, non-reproducibly reported estimate over hidden-suite-selected artificial edits.**
