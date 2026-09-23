The numerical result survives independent recomputation. The second revision still has a blocking error in its new classification, plus several incomplete repairs. Reviewed at `8f66bab`; no files modified.

1. **Blocking: three classification rows are wrong or overstate their coverage.** The [classification code](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/classify_clarifications.py:45) assigns both `b1:Mbpp/305` and `b2:Mbpp/305` to “partial” because a supposed “`None`-when-fewer-than-two” rule matches the oracle. Neither addition says that. Both require a **tuple** of the available matching words. On the first two displayed cases, they prescribe `()` while the oracle expects `None`; on the third, they prescribe `('python', 'Programming')` while the oracle expects `('PHP', 'Programming')`. Both also contradict the remaining archived witnesses. These belong in “contradicts.”

   Separately, the exporter [silently takes `cases[:3]`](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/classify_clarifications.py:94), despite defining consistency over “every exercised input.” There are **137 archived witness cases**, of which it publishes 87. `b1:Mbpp/559`’s fifth case is:
   ```
   ([-100, -50, -30, -20, -10, 5, -3, -2, -7], -1)
   ```
   The oracle expects `0`. Its addition requires the maximum nonempty contiguous-sublist sum in this case, which is `5`. That row is **partial**, not consistent.

   Against all archived failing witnesses, the corrected descriptive table is:

   | Classification | Instances | Diagnosed |
   |---|---:|---:|
   | Consistent | 6 | 6/6 |
   | Broadens a precondition | 1 | 1/1 |
   | Partial | 2 | 2/2 |
   | Contradicts | 23 | 0/23 |

   This remains a classification of the archived witnesses, not proof of agreement on every hidden-suite input. The report’s **7/7, 1/1, 1/3, 0/21** conclusion is therefore unsupported as written.

2. **The title and interpretation exceed the evidence.** “[Only when it is right](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:1)” reads as a necessity claim. Two diagnosed instances have partially contradictory additions. A narrower description could concern agreement on the particular behaviour diagnosed.

   The post-hoc and problem-difficulty caveats are appropriate. They do not make the correctness classification an independently manipulated factor. This experiment supports a specification-edit contrast on these selected instances; it does not establish C4’s broader causal explanation of “most” misses.

   The manipulation-check qualification is numerically accurate but remains confined to [the limits section](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:103). Its unresolved clarified–placebo contrast belongs beside the mechanistic interpretation. It **does not invalidate the registered H3 criterion**, and requiring it to pass a newly invented threshold would also be wrong.

   Also, [the registered contrast](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:69) averages **all four classification strata**, not just the two populations the sentence names.

3. **The cost split is another incorrect repair.** The reported $2.13/$1.86 exactly matches splitting the ledger after its first **384 entries**, but that is not the run boundary. The [usage ledger](/Users/ericdong/Documents/Crossaudit/study-data/wt-clarify-runs/project/project-cross/.crossaudit/usage.jsonl:399) contains:

   | Phase | Charged entries | Cost |
   |---|---:|---:|
   | Preflight/smoke | 14 | $0.05376750 |
   | Discarded main audit | 384 | $2.13951250 |
   | Corrected audit | 384 | $1.79740075 |

   Thus the corrected audit cost **$1.80**. All pre-repair charges total **$2.19**, including preflight/smoke. The overall **$3.99** is correct.

4. **Corrections have not propagated through the binding artifacts.**

   - The report’s adjudication note names `P0001`; the accepted sorted-array docstring finding is now **[P0021](/Users/ericdong/Documents/Crossaudit/study-data/wt-clarify-runs/sheet/sheet.md:867)**. Current `P0001` concerns date conversion and both raters reject it.
   - The [candidate-proof docstring](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/prove_candidate_is_the_instances.py:8) and [Amendment 13](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:700) still claim a different program cannot reproduce another program’s outputs. The report corrects this; those sources do not.
   - The registration still asserts [“no duplicate structure”](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:591), despite correcting that assertion earlier.
   - Its outcome section retains the superseded 31-instance results. [CLAIMS.md](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:483) likewise retains those numbers, “not yet reviewed,” and “the causal reading of C4.”

The requested quantitative checks otherwise passed:

| Check | Independent result |
|---|---|
| Diagnosis | Original **0/32**, clarified **9/32**, placebo **0/32** |
| Primary contrast | **+28.125 points**, bootstrap **[7.685185, 51.428571]** |
| Tests | McNemar **0.00390625**; cluster sign-flip **0.06019398** |
| Registered secondary | **8/23 versus 0/23**, 15 problems; **+34.782609**, interval **[10, 60.869565]**, sign-flip **0.06319368** |
| Agreement | **84/91**, κ **0.85203252** |
| Clarified overlap | **1/87** contiguous; **39/87** vocabulary |
| Manipulation check | Original **15/32**, clarified **24/32**, placebo **18/32**; all three reported intervals reproduce |

The primary bootstrap reproduces with **10,000 resamples and seed 20260921**. The permutation flips once per **problem**, correctly retaining the paired instances together. Successes occupy problems **391, 556, 559, 576 and 597**, with contributions **2, 2, 2, 2, 1**. Exact enumeration gives **0.0625**; the reported 0.0602 is its seeded Monte Carlo estimate. The explanation of the McNemar discrepancy is substantively correct.

The candidate repair also passes a stronger check than its standalone proof: **all 384 successful readings’ actual prompt hashes reproduce** from the frozen candidates, visible tests, constitution, deterministic checks and condition-specific specifications, without truncation. Candidate and visible-suite bytes are identical across arms. All 32 candidates match their frozen batch sources exactly; all **137** recorded actual outputs reproduce. All 91 sheet items match their keyed reading, candidate and witness. The 384 successful void readings match the canonical candidates. The identity hole is closed for this archived run.

Adjudication correctly requires both raters’ `yes`; disagreements and abstentions fail diagnosis. The author’s lack of independence is adequately disclosed for this registered operational outcome. Agreement does not establish accuracy. The inconsistent docstring judgment and false example remain real, but other accepted findings preserve both the nine-instance total and the flat ladder.

The ladder is genuine: every successful instance has draw pattern **1111**, every other instance **0000**. The overlap repair now measures order, and its explicit warning that lexical overlap cannot establish blinding is appropriate. The public-text exclusion for Mbpp/427 and the **25/44, 29/44, 32/44** generation yields also reproduce.

I ran the read-only candidate, gate and overlap proofs plus independent in-memory checks. I did not run the full application suite or write-producing harness tests.

**not quotable — the new, load-bearing classification mislabels two additions and truncates away a counterexample to a third.**
