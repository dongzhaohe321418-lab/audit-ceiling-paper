All three outstanding round-2 findings are fixed at `cb3b8d9`. Only `RESULTS-CODE.md` changed; I modified no files.

| Finding | Third-review assessment |
|---|---|
| Reversed evidence for `15.1.s3` | **Fixed.** The [revised passage](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-code/benchmarks/ai4s/RESULTS-CODE.md:121) correctly distinguishes the two cases: `39.1.s3` targets follow the header’s 2×2 output; `15.1.s3` targets follow the background’s complex coefficients. Targeted execution confirms both. |
| Normalization examples misclassified as consensus-undetermined | **Fixed.** The [revised paragraph](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-code/benchmarks/ai4s/RESULTS-CODE.md:89) explicitly identifies both normalization instances as disputed. Their records show L1 determined and L2 undetermined. |
| Unsupported historical pre-call identity check | **Fixed as reporting.** The [historical statement](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-code/benchmarks/ai4s/RESULTS-CODE.md:37) is now attributed to the agent and expressly excluded as evidence. The retained evidence establishes program identity: all **7,392 task/program hash pairs** match reconstructed inputs. |

The other examples remain accurate: the unshifted `60.2.s1` candidate passes all three comparisons, and constant zero passes all three `21.2.s1` comparisons.

On rereading the whole report, I found no remaining substantive blocker. H1 stays descriptive; H3 is a route comparison; B1 meets its registered criterion; H2 is killed in both arms. The report distinguishes regex matches from semantic categories, flags from demonstrated defects, and determinacy ratings from explanations of misses. It retains the selection limitation, sequential arm order, complete framing treatment and rating limitations.

I independently reproduced the headline rates, residual membership, regex counts and seeded samples. Unchanged intervals and p-values agree with the retained results and round 1’s verification; I did not repeat their entire computation or run the full suite.

**quotable — the report now keeps its interpretations within what the registered outcomes and inspected evidence establish.**

Reader sentence: On SciCode steps this generator sometimes solved, sequentially changing the complete task framing reduced cross-auditor K=8 flags on test-passing instances by 32.7 percentage points (95% cluster interval −42.8 to −22.4), alongside a 14.8-point reduction on test-failing instances (−28.6 to −2.7), without establishing which flags identified actual defects.
