The corrected **descriptive result is quotable**. I found no disagreement with the current 32-row classification and reproduced the primary results independently. This does **not** establish C4’s proposed causal mechanism.

Reviewed `c63ac660423f86b3633a139f41161e185ec7afda`. No files modified.

Before reading the report’s conclusions, my classifications were:

| Verdict | Instances | Jointly diagnosed |
|---|---|---:|
| Consistent on all archived cases | Both batches of `391`, `556`, `576` | 6/6 |
| Broadens a stated precondition | `b2:597` | 1/1 |
| Partial | Both batches of `559` | 2/2 |
| Contradicts | All remaining 23 | 0/23 |

These agree with every published row. I checked the exported evidence against the original archive and executed both candidate and oracle programs: **all 137 candidate outputs and all 137 expected outputs reproduced**.

There are four residual corrections or qualifications:

1. **The report retains an obsolete count.** [Line 145]( /Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:145) says 21/32 additions are wrong. The current classification has **23 entirely contradicting additions, plus two partially contradicting additions**. State those categories explicitly.

2. **The repair narrative exaggerates one error.** [Lines 65–66](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:65) say the fourth and fifth cases of `b1:Mbpp/559` contradict its addition. **Only the fifth does.** The fourth is all-negative and correctly predicts zero. The published row’s current reasoning gets this right; the report and classifier docstring do not.

3. **The candidate proof’s description still exceeds its coverage.** [Its docstring](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/prove_candidate_is_the_instances.py:18) claims to catch transformation “in transit,” but the script executes the condition-file candidate, examines only the first three witness cases, and never examines the recorded audit prompts. It genuinely rejects the original canonical-candidate defect; it is not an end-to-end transit check. My separate prompt reconstruction and all-case execution close that evidential gap **for this run**.

4. **One registered secondary remains unreported.** [Registration §3](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:60) promises flag rate and naming rate. The outcome record contains flag rates and no-finding counts, but no naming rate. Disclose that omission rather than claiming complete execution of every registered secondary. It does not alter the defined primary diagnosis outcome.

None changes the narrow result being quoted.

The independent arithmetic is:

| Quantity | Recomputed result |
|---|---:|
| Original / clarified / placebo | **0/32; 9/32; 0/32** |
| Clarified − original | **+28.125 points** |
| Problem-cluster bootstrap 95% interval | **[+7.6852, +51.4286]** |
| Exact McNemar | **0.00390625** |
| Problem-cluster sign-flip | **0.06019398** |
| Exact sign-flip enumeration | **0.0625** |
| Registered secondary | **8/23 versus 0/23; +34.7826 points** |
| Secondary bootstrap interval / sign-flip | **[+10.0000, +60.8696]; 0.06319368** |
| Agreement | **84/91; κ = 0.85203252** |

The bootstrap reproduces with **10,000 resamples and seed 20260921**. The permutation flips once **per problem**, correctly keeping both batches together. Re-executing the report with its output intercepted in memory reproduced the entire committed `h3.json`.

The nine successes occupy exactly **five problems: 391, 556, 559, 576, 597**, contributing 2, 2, 2, 2 and 1 successes. Thus the explanation of the p-value difference is correct: McNemar treats nine discordances as independent, whereas the cluster test has five informative signs. The exact two-sided cluster probability is \(2/2^5=0.0625\). The registered bootstrap criterion is met; that does not make the cluster test significant at 0.05.

The provenance repair is complete **in the observed data**:

- There are **384 unique successful replacement readings**, with no missing instance–arm–draw combinations; four failed rows are retained separately.
- All 32 candidates match their frozen batch sources **byte for byte**. Candidate and visible suite are identical across arms.
- Reconstructing all **96 condition prompts** reproduced every successful reading’s saved prompt hash. Each contains its intended specification, candidate and visible suite, without truncation.
- The specifications were unchanged by the candidate repair. The candidate proof rejects all 32 voided configurations.
- All 91 sheet items match their corresponding findings, candidates and displayed witnesses.

The adjudication conjunction is implemented correctly. There are 46 joint yes labels; every L2 yes also has an L1 yes. The disclosed `P0021` inconsistency and `P0053` false example do not change the instance outcome. The report adequately acknowledges that **L1 is the author**, and that agreement is not accuracy. Amendment 12 names L2; this is not two independent raters or a third-vendor adjudication.

The flat ladder is genuine: each successful instance has draw pattern `1111`; every other instance has `0000`. The subset-averaging function itself is not forcing flatness—it returns 25%, 50%, 75%, 100% for a planted `1000` pattern.

Both leak counts reproduce: **1/87 contiguous overlap and 39/87 vocabulary overlap**. The report appropriately declines to infer successful blinding from them. The manipulation results also reproduce: **+28.1 [2.6, 54.3]** against original and **+18.8 [−9.4, 45.2]** against placebo. That unresolved contrast now receives proper weight beside the mechanistic interpretation. “Cannot separate” should mean **unresolved here**, not that the instrument is inherently incapable.

The cost split reproduces as **$0.0537675 preflight/smoke, $2.1395125 discarded audit, $1.79740075 replacement audit**, totaling $3.99068075 in this audit ledger.

I ran the four read-only proof programs and independent computations. I did not run the filesystem-writing full suite or rebuild.

**Quotable — the corrected classification and independently reconstructed evidence support the report’s explicitly limited, selected-population association.**

Reader sentence: “On 32 selected instances across 19 problems, jointly adjudicated diagnosis rose from 0/32 to 9/32 under the added specifications, versus 0/32 under placebo (+28.1 points, cluster-bootstrap 95% interval [7.7, 51.4]; cluster sign-flip p=0.0602), without establishing that specification underdetermination caused the original misses.”
