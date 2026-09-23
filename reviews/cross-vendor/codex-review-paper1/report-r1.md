Reviewed `306bd8d` read-only, including the requested history and diff. No files modified. I share the measured `gpt-6-astra` model family; my judgments about its ranking and adjudication are therefore conflicted and do not supply the independent-family validation the manuscript requests.

The principal numerical results reproduce. The manuscript’s claims and process descriptions do not yet consistently match them.

1. **Blocking — new numerical claims bypass the admission rule.**  
   [results.tex:191](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:191) introduces **43/68**, **25/32**, and **78.1%**, also printed in [table1.tex:24](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:24). These cross-study quantities have no admitted ledger entry. The table generator expressly says it computes the join because no committed record held 25/32. Likewise, the fourteen coverage estimates at [methods.tex:98](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:98) appear in neither an admitted claim nor a reviewed study report.

   **Evidence:** [CLAIMS.md:527](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:527), [make_table1.py:14](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/figures/make_table1.py:14), and `records/coverage_simulation.json`. I reproduced these calculations; arithmetic correctness does not satisfy the declared admission gate.

2. **Blocking — a withdrawn substrate-dependent conclusion remains affirmative.**  
   [related.tex:64](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:64) claims a contribution is “the finding that its direction is substrate-dependent.” Study 23 licenses no finding, and its clean same-vendor contrast is **+6.9 points [−4.9, +18.6]**, which does not establish the reversal.

   **Evidence:** [CLAIMS.md:519](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:519) and [RESULTS-SUBSTRATE2.md:367](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SUBSTRATE2.md:367). The manuscript correctly withdraws this claim elsewhere. The checker nevertheless passes.

3. **Major — the clarification study is given interpretations its design excludes.**  
   [discussion.tex:64](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:64) calls it evidence “not conditioned on being missed.” Its population explicitly consists of previously missed, consensus-oracle-defined instances. Intervention within that selected population does not remove the selection.

   [paper.tex:75](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:75) attributes the clarifier’s 23/32 oracle contradictions to “the benchmarks, not … the generator.” The study does not separate those explanations. And [methods.tex:8](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:8), “no model judges any outcome,” is false for the new primary diagnosis outcome, which requires an author–model conjunction.

   **Evidence:** `records/code/clarify/population.json`, [RESULTS-CLARIFY.md:19](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:19), and C13’s explicit selected-population, noncausal scope.

4. **Major — finding counts become defect recognition again.**  
   [results.tex:98](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:98) says the stronger model “writes down more of what is wrong” and makes −26.4 “a fact about severity calibration.” The sweep counts findings without establishing whether their content identifies the hidden failure. It establishes dependence on the counting rule, not the cause of the original difference.

   **Evidence:** [RESULTS-SWEEP.md:109](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:109) expressly withdraws the corresponding recognition claim; [CLAIMS.md:203](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:203) forbids that interpretation.

5. **Major — the “no measurements moved” account is still false, including its repaired version.**  
   [methods.tex:179](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:179) and [results.tex:421](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:421) exempt clarification but assert no measurements moved in the first six studies. The sweep is one of those six. Its first review found missing readings and different populations; its report says every initial cross-family figure was recomputed. [paper.tex:89](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:89) retains the unrestricted “no measurement ever moved.”

   **Evidence:** [RESULTS-SWEEP.md:3](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:3) and `reviews/cross-vendor/codex-review-sweep1/report-r1.md`.

   Moreover, review-round counts cannot establish reviewer recall when repairs introduce new defects between rounds. The “single pass has low recall” inference requires a fixed defect population that these records do not provide.

6. **Major — the introduction incorrectly ranks `astra` on both axes.**  
   [introduction.tex:25](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:25) says a third model “beats both on recall and false positives.” `astra` has **10.7%** false positives; `self-strong` has **3.3%**. It therefore does not beat that comparator on false positives. Against shipped `cross`, its observed recall is higher, but the paired complete-ladder contrast **+2.7 [−6.5, +13.0]** does not establish higher population recall.

   **Evidence:** [RESULTS-CEILING3.md:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING3.md:43) and `records/code/threshold_sweep.json`, `paired_astra_minus_cross.cross_complete_ladder`. This finding concerns my own model family.

7. **Major — mandatory qualifications disappear from the abstract and table.**  
   At [paper.tex:44](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:44), −26.4 lacks C2’s required **3.3% versus 16.0%** operating-point disclosure. At line 46, +26.8 lacks its interval and false-positive cost. At line 50, the clarification result lacks both its interval and the nonsignificant preferred cluster test, which C13 requires beside the successful bootstrap criterion.

   [table1.tex:14](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:14) likewise presents C2 without its stronger-model false-positive rate; line 24 omits the available interval for 44/57.

   **Evidence:** [CLAIMS.md:5](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:5), C2, C3 and C13. A qualification elsewhere does not meet these explicit “wherever” and “beside” conditions.

8. **Major — the interval policy and its claimed validation exceed what was done.**  
   [methods.tex:81](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:81) says every one-sided discordance uses an unconditional interval instead of the bootstrap. Clarification has **9 treatment-only versus 0 reference-only** discordances and retains its preregistered bootstrap. The manuscript needs to state that exception accurately.

   Separately, [table1.tex:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:2) directs readers to “their measured coverage,” although the simulation measures **single-rate intervals**, under a particular correlation model, not the paired contrasts or conditional category intervals occupying much of the table.

   **Evidence:** `records/code/clarify/h3.json:110` and [coverage_simulation.py](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py). All fourteen simulation cells reproduce; they do not validate these other estimators.

9. **Major — Figure 2 conceals different reading depths.**  
   [results.tex:134](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:134) describes families’ operating points without saying that `cross`, `self`, and `self-strong` use **K=8**, while `astra` and `self-frontier` use **K=4**. Neither the figure nor its caption labels those budgets. The script reads the full-ladder rows and discards `_k` when plotting.

   **Evidence:** [make_fig2_sweep.py:34](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/figures/make_fig2_sweep.py:34) and `records/code/threshold_sweep.json`, which separately provides the common-K=4 analysis. This figure cannot be read as an equal-depth family comparison.

10. **Major — the review archive is not complete as claimed.**  
    [paper.tex:113](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:113) promises every independent review, verbatim. Study 19’s rounds 1–7 are absent here but present in its source worktree. The mirrored `2026-09-09-testgen-r*.md` reviews also do not substitute for study 17’s `testgen-val` reviews.

    **Evidence:** the missing files include [ceiling3b-r1.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/reviews/2026-09-10-ceiling3b-r1.md) and [testgen-val-r1.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/reviews/2026-09-10-testgen-val-r1.md). The paper checkout lacks their corresponding archives.

    [methods.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:56) additionally promises the prompts, constitution and every capability card in this repository. The supplied manifests contain hashes and descriptions; the actual harness assets are not included.

11. **Moderate — the new third-rater paragraph compares different constructs as a smaller estimate of one quantity.**  
    [results.tex:226](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:226) presents 38/57 as a “smaller majority” supporting the earlier “most” interpretation. The source distinguishes more than rubric option counts: the earlier category includes **prose contradicting the oracle**, whereas L3’s `undetermined` category does not. L3 never sees the expected values and cannot test their entailment.

    **Evidence:** [RESULTS-RATE3.md:104](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-RATE3.md:104). Both marginals may be described, but the ten-point difference is not a calibrated downward revision of the same estimand. The post-hoc designation also needs to travel with the residual-only reading.

12. **Moderate — clarification omits two reporting obligations.**  
    [results.tex:391](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:391) omits the registered secondary **8/23 versus 0/23, +34.8 [10.0, 60.9]**, required beside the primary “always.” It also omits disclosure that the promised naming-rate secondary was never computed, despite C13 making that omission part of the claim’s limits.

    **Evidence:** [P3-PREREGISTRATION.md:264](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:264), [RESULTS-CLARIFY.md:35](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:35), and `records/code/clarify/h3.json`.

13. **Moderate — several review-status statements remain stale.**  
    [introduction.tex:71](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:71) says the seventh study was refused twice and licenses nothing. C13 passed round 3 and is reported throughout. [results.tex:5](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:5) still describes four studies in the seven-study subsection. [methods.tex:216](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:216) says the closed study appears nowhere except that sentence, although it appears repeatedly.

    **Evidence:** [CLAIMS.md:522](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:522), the clarification round-3 review, and the manuscript’s actual results. The global “four to eleven rounds” range also excludes ceiling 1’s 21 rounds.

14. **Moderate — a limitation again overcorrects beyond the reviewed result.**  
    [methods.tex:141](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/methods.tex:141) says the unregistered sweep “tests nothing.” Its reviewed report explicitly rejects that restriction: exploratory analysis can support exploratory inference.

    **Evidence:** [RESULTS-SWEEP.md:172](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:172). Preserve the exploratory designation without denying the inference its review permits.

15. **Moderate — the reproduction description is too broad.**  
    [paper.tex:117](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:117) promises “no path outside the checkout”; [reproduce.sh:10](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reproduce.sh:10) writes `/tmp/table1.$$`. The script generates figures under `figures/`, while LaTeX consumes separate copies under `tex/`; only the table is compared. The claim at line 122 that regenerating records requires fresh model calls also overlooks deterministic reanalysis of archived readings.

    These are limitations of the stated contract, not evidence that ordinary execution fails. I **did not execute `reproduce.sh`**, because this sandbox cannot write a temporary copy.

Verification completed: Table 1 regenerated byte-identically in memory; all three figure copies rendered identically; the main union counts, selected bootstrap intervals, loop contrast, clarification outcomes and agreement reproduced. All fourteen coverage cells reproduced. The quoted external **63%** and **43.67%** match their sources, and the stated HumanEval/EvalPlus licence names match upstream. [Critic paper](https://arxiv.org/abs/2407.00215), [SWR-Bench](https://arxiv.org/abs/2509.01494), [HumanEval licence](https://github.com/openai/human-eval/blob/master/LICENSE), [EvalPlus licence](https://github.com/evalplus/evalplus/blob/master/LICENSE).

**not submittable — the manuscript still asserts conclusions outside its admitted evidence, including an explicitly withdrawn substrate-dependent finding.**
