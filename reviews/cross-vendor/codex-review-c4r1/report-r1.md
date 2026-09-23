## Review: b7a20ea

**The numerical results reproduce. The ceiling headline is not supported as written.** No files were modified.

### Findings requiring correction

1. **P1 — Higher eight-reading flag coverage is presented as an established ceiling increase.**  
   The [headline](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:1) exceeds the evidence. H20a establishes higher union BLOCKER coverage at K = 8. H20b establishes a positive difference between the registered fitted asymptotes, conditional on that model. It does not resolve the true saturation difference: `cross` remains unflattened, heterogeneous low-probability detection can resemble a ceiling over eight readings, and the secondary ZIBB estimates reach 100% for both families. Moreover, neither eight-reading union has been adjudicated for defect recognition.

   Retain the positive H20a result and the registered kill verdict, but qualify the ceiling conclusion wherever it appears.

2. **P1 — Amendment 1’s kill cannot establish the proposed flag-versus-naming comparison.**  
   [§3 correctly warns](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:330) that 30.0% at K = 8 and 4.5% at K = 1 are different quantities. However, the [generated kill block](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:327) still repeats the proposed headline juxtaposing them without those qualifications.

   More fundamentally, **the kill fires even with perfect adjudication**: only nine P instances received any finding, so the maximum possible defect-asserting count is nine, already below twenty. Its robustness to rater disagreement is real, but does not validate a naming-rate interpretation of the historical union. The matched observation is nine instances flagged versus five consensus defect-asserting instances **within this one reading**.

3. **P2 — Durable provenance and interruption disclosure are incomplete.**  
   The [run manifests](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/records/ceiling4/manifest-2026-09-11T045616Z.json:51) do not satisfy `EXPERIMENT_RECORD.md` §2: they omit the frozen-code/clean-tree record, source-file digests, dataset provenance linkage, sampling settings, endpoints, per-arm UTC bounds, and environment.

   L2’s raw reply, prompt, launcher and execution log exist only under temporary `scratchpad/c4-adjud/`, outside the durable archives. They should be archived and digested. The execution log records **high reasoning effort**, absent from the adjudication manifest.

   The results acknowledge a later invocation, but should state the actual **12:40:09 gap within draw 5** and distinguish operator-reported balance exhaustion from the recorded HTTP 429 errors.

4. **P2 — Several prose statements need correction.**

   - [“No text was adjudicated”](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:227) contradicts §3. The eight-reading unions were not fully adjudicated.
   - [“The raw union … is more conservative still”](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:142) is numerically false for `cross-R`: its raw union exceeds its fitted asymptote.
   - [The attribution of disagreement to findings rather than raters](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling4/benchmarks/code/RESULTS-CEILING4.md:285) is too definite. My item review finds inconsistent judgments by both raters.
   - The mixed-arm prose should acknowledge its lower false-positive rate relative to all-`cross-R`, even though it still fails the product constraint.

## Numerical verification

I reran `report_ceiling4.main(--run …)` with only filesystem output operations intercepted in memory:

| Output | Result |
|---|---|
| `numbers.json` | Byte-identical, 60,395 bytes |
| `tables.md` | Byte-identical, 13,179 bytes |
| Results splice | All 16 blocks identical |

Separately, I loaded the underlying records independently, enumerated draw-subset probabilities, implemented an independent optimizer, and refitted both asymptotes in every paired problem-cluster resample.

- **H20a:** 67 versus 33 instances; discordance 38 versus 4; **+30.9 points**, cluster 95% **[19.1, 43.1]**. Independently reproduced Tango **[20.8, 41.0]**, grid-unconditional **[16.8, 42.7]**, McNemar **5.6531×10⁻⁸**, and sampled cluster sign-flip **9.99995×10⁻⁶**. Registered kill does not fire.
- **H20b:** `cross-R` A **58.6% [46.8, 70.2]**, τ **0.8459**; `cross` A **31.5% [21.5, 46.0]**, τ **3.2658**, **an extrapolation**. Paired fitted difference **+27.1 points [10.9, 39.0]**. Gains **0.5682 [0.1147, 1.0417]** and **1.9318 [1.1261, 2.8153]** points. The registered point-estimate flattening classifications are correct.
- **H20c:** 55 versus 24 instances; **+20.7 points [12.8, 28.8]**. Single-draw mean FP **23.6% [17.1, 30.3]**; all eight draws exceed the 6.7% bar.
- **H20d:** residual **56 → 32**; exactly **23 unexercised-edge** and **one spec-misreading** instance leave; none enter. Residual cluster interval **18.5–40.2%**.

## Cache, ladder and timing

All nine draws contain **260 unique, in-scope readings**, matched to archived findings and usage-ledger entries. I verified solution digests, prompt digests, finding hashes/counts, and model-only BLOCKER flags. The archived R constitutions equal the archived T constitution plus the exact referent rule.

- Preregistration and initial driver precede the first call.
- Amendment 1 was committed at **2026-09-10 14:28:43 UTC**, during draw 1, after **93 ledger calls had completed**. The ledger verifies timing; it cannot verify the assertion that nobody had read results.
- Draw 5 contains **165 readings before** and **95 after** the gap from **September 10 15:31:49.682 UTC** to **September 11 04:11:59.066 UTC**.
- The 7,000 failed rows comprise **6,903 local cooldown refusals**, **96 HTTP-429 failure rows**, and **one SSL-EOF failure row**. None contributes an accepted reading or additional recorded usage. The blanket claim of zero provider-side spending is stronger than these local records establish, particularly for the transport failure.
- Total ledger cost: **$19.83767825**, over **2,340 calls/readings**.

## Adjudication

The sheet has the expected blind fields and no explicit arm/severity/instance metadata. I independently reconstructed all **80 shuffled key mappings**, checked specifications and solutions against source records, matched findings to the archive, and verified every manifest digest. L2’s raw reply is **byte-identical** to its committed CSV.

Naming agreement reproduces:

- Both yes **39**, L1-only **7**, L2-only **16**, both no **18**.
- Agreement **57/80**; κ **0.3907284768**.
- Recognition on consensus-named items: **39/39 defect/defect**. **Undefined κ is correct:** observed and expected agreement both equal one, giving **0/0**.

All sixteen counts and their Wilson/cluster intervals reproduce:

| Route / question | Consensus | L1 | L2 | Either |
|---|---:|---:|---:|---:|
| T naming | 5 | 5 | 7 | 7 |
| T defect-asserting | 5 | 5 | 7 | 7 |
| R naming | 26 | 29 | 36 | 39 |
| R defect-asserting | 26 | 29 | 32 | 35 |

Every count is over 110 P instances.

### My fifteen blinded ratings

I froze these judgments on the first fifteen shuffled items before opening either CSV or the key. Recognition is “defect” for each naming-yes item.

| Item | Naming | Reason |
|---|---|---|
| K0001 | Yes | Negative-bound square-root failure matches. |
| K0002 | No | Import complaint does not identify the timeout. |
| K0003 | No | Final-newline issue differs from displayed failures. |
| K0004 | Yes | Ignoring `n` matches the failing class. |
| K0005 | No | Import complaint differs from unsorted-input failures. |
| K0006 | No | Proposed inclusion of nonletter-leading names does not explain the observed overcounts. |
| K0007 | Cannot tell | Timeout-only witness cannot link the overflow allegation to the hidden failure. |
| K0008 | Yes | Unhashable elements match the TypeErrors. |
| K0009 | No | Same mismatch as K0006. |
| K0010 | No | Missing leading digits differs from the displayed failures. |
| K0011 | Yes | Unequal lengths match the IndexErrors. |
| K0012 | No | Huge-input overflow differs from the demonstrated rounding failure. |
| K0013 | Yes | Floor division identifies the wrong results. |
| K0014 | No | Same overflow-versus-rounding mismatch. |
| K0015 | Yes | Duplicate handling identifies the pair-count failure. |

**I favor the stricter interpretation of “names the failing class.”** That supports L1 on K0012/K0014. L2 is correct on K0006/K0009, and K0007 lacks enough evidence. This sample supports tightening the rubric; it does not establish either rater as uniformly reliable.

## Scope and tests

All 33 changed files are under `benchmarks/code/`. Product `src/`, kernel areas, and inherited estimator files are untouched. I found no committed corpus or finding text. The worktree remains clean.

- Study-20 report tests: **16 passed**.
- Inherited statistics tests: **19 passed; three exceeded pytest’s 30-second timeout**.
- Full suite: blocked during collection by the read-only environment’s lack of a writable temporary directory. No full-suite-green claim.

**not quotable — the headline turns verified higher eight-reading flag coverage into an established higher ceiling, which these results do not establish.**
