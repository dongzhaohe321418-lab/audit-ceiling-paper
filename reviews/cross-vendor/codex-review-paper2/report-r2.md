Reviewed `3b06631` on `ai4s`, including the full diff, manuscript and appendices. No files modified.

I am a GPT-6-family reviewer: cross-vendor relative to the Claude research agent, but **not outside-family validation** of Astra’s performance, residual labels, clarification adjudication or previous reviews. My numerical checks do not resolve that conflict.

The numerical repairs hold. Several substantive round-1 findings remain because corrections did not reach the contribution bullets and full-discussion/related-work appendices.

1. **Major, blocking — scientific-code observations are still presented as established construction defects.**  
   [introduction.tex:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:53) retains the contribution that **all three** science studies identified defects in supposedly clean items. More explicitly, [discussion_full.tex:115](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:115) still says each flag was correct and that **every** clean-item flag was read.

   **Contradicting evidence:** [RESULTS-AI4S-CODE.md:111](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-CODE.md:111) describes 20 sampled first BLOCKERs and expressly declines to establish whether these flags identify defects. [C19:401](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:401) makes this restriction binding; `records/ai4s/code_posthoc_b.json` records the sample.

   The revised main Discussion now distinguishes the studies correctly. The contribution and Appendix D must make the same distinction. **R1 finding 4 is only partly fixed.**

2. **Major — the replacement contribution still upgrades an association into an effect.**  
   [introduction.tex:47](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:47) now says “each of these moves” the limit. “These” includes the preceding specification-determinacy association.

   **Contradicting evidence:** [C13:298](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:298), [RESULTS-CLARIFY.md:55](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CLARIFY.md:55), and `records/code/clarify/clarification_classification.json`. Oracle agreement was classified after outcomes; additions entirely contradicted the oracle on 23/32 instances. The informative cluster test is 0.0625. The paper’s own [results_full.tex:480](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:480) correctly separates route/rule effects from an association not isolated as a cause.

   Removing “varied alone” fixes one overstatement, but the replacement contribution needs that same separation. **R1 finding 1 remains partially unresolved.**

3. **Major — the broader experiment and novelty claim survives in Appendix F.**  
   [related_full.tex:77](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/related_full.tex:77) still claims the scientific-code/results/data measurement alongside checks a shipped system runs, then says Section 4 performs that measurement.

   **Contradicting evidence:** [RESULTS-AI4S-CODE.md:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-CODE.md:18) and `code_results.json` contain model-route and framing comparisons, not an independently evaluated deterministic audit tier. [RESULTS-AI4S-DATA.md:22](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DATA.md:22) describes a separately constructed validator. Only the results study evaluates the shipped `science` profile.

   The main Introduction, System and Related Work now describe this accurately. Appendix F still asserts the broader measurement and omits both newly relevant works. **R1 findings 2 and 8 are not closed throughout the paper.**

4. **Major, nonblocking individually — the preregistration and availability claims exceed the archived evidence. New finding.**  
   [method_full.tex:162](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/method_full.tex:162) says numbered amendments were committed before the step they governed.

   **Contradicting record:** the [A4S-2 registration erratum:148](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s-results/benchmarks/ai4s/PREREGISTRATION-RESULTS.md:148) records pilot calls at 00:08:44 and 00:08:55, followed by the amendment commit at 00:09:20. The mirrored [report:158](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-RESULTS.md:158) discloses this.

   Separately, [reproducibility.tex:5](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/reproducibility.tex:5) promises every study’s preregistration and amendments in this repository. At this commit, the four operative science registrations—CODE, CODE-B, RESULTS and DATA—are absent. `plan/AI4S-PROGRAM.md` is the programme outline, not those amended protocols. I could inspect the external worktrees; the advertised repository does not supply them.

   Preserve the distinction between initially registered studies and departures recorded retrospectively, and make the promised protocols available.

5. **Moderate — uncertainty and post hoc qualifications remain inconsistently propagated.**  
   Most R1 repairs are correct, including the exploratory operating points, scientific-code contrast intervals, recall-change sign-flip sensitivity and dataset-stratified data intervals. Remaining omissions include:

   - [ai4s.tex:52](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:52) adds the same-route clean rates, **27.3% and 18.0%**, without their intervals **[18.4, 37.3]** and **[11.5, 25.6]**. Appendix C repeats this. These are in `code_results.json` and `code_results_b.json`.
   - [introduction.tex:22](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:22) still omits the stronger general-code route’s **3.3% [0.7, 6.7]** interval required by C2.
   - [discussion_full.tex:100](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/discussion_full.tex:100) quotes **21 sound findings** and **18/28 fault-specific flags** without their post hoc labels. The source records are `results_posthoc.json` and `data_posthoc.json`.
   - [limitations_full.tex:19](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/limitations_full.tex:19) still describes primary intervals universally as problem-cluster bootstraps, contrary to the data study’s within-dataset resampling.

   **R1 finding 5 is substantially, but incompletely, fixed.**

6. **Minor — several appendix-wide method statements are false after adding science. New finding.**  
   [method_full.tex:6](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/method_full.tex:6) says every result uses EvalPlus; line 134 says all analysis uses only Python’s standard library. [limitations_full.tex:8](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/limitations_full.tex:8) calls the science faults synthetic and says each science study used one auditor model.

   **Contradicting evidence:** the scientific-code population consists of naturally generated failures and uses **two** auditor routes ([code report:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-CODE.md:18)); data also uses two ([data report:15](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DATA.md:15)). Its bootstrap uses NumPy in `analyze_data.py`.

   Scope the old method statements to the general-code studies and distinguish generated code failures from injected results/data faults.

7. **Minor — Table 1’s repaired completeness claim is still too broad.**  
   [table1.tex:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:2) now promises every primary quantity of the general-code studies, including Appendix B.

   **Contradicting evidence:** the registered generated-test primary outcomes—**11/90, 15/101**, and their retention counts—appear in [RESULTS-TESTGEN-VAL.md:30](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:30) and Appendix B, but not Table 1. “Selected primary quantities” would describe the table accurately.

8. **Minor — Figure 2 is improved but still undersized.**  
   The caption now correctly distinguishes model, profile, validator and re-execution flags. However, the compiled figure’s category labels are approximately **5.49 pt**, its code-panel legend **5.29 pt**, and other legends **5.90 pt**. They remain difficult to read at publication size.

   **Evidence:** font settings at [make_fig4_ai4s.py:57](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/figures/make_fig4_ai4s.py:57) and line 116, confirmed in the compiled PDF. I found no clipping or overlap. **R1 finding 7 is partly fixed.**

Every round-1 finding has the following disposition:

| R1 | Disposition |
|---|---|
| 1 — isolated effects | Partial; replacement contribution still overstates specification evidence. |
| 2 — three-domain comparison | Main text fixed; Appendix F retains broader claim. |
| 3 — flags versus diagnoses | Numerical distinction fixed in summaries; Appendix D still lacks post hoc labels. |
| 4 — framing and exhaustive adjudication | Framing fixed; contribution and Appendix D retain unsupported adjudication claims. |
| 5 — uncertainty and labels | Substantial repair; remaining omissions listed above. |
| 6 — numerical tolerance | **Fixed in both locations.** The differences, not necessarily the outputs, fall within tolerance. |
| 7 — figure and table | Caption fixed; labels remain small and table completeness still overstated. |
| 8 — literature | Sources verified and main positioning narrowed; Appendix F remains unreconciled. |

Both new citations support their attributed findings. **SciCode-Verified** documents contradictory specifications, unreproducible targets and excessive tolerances; the new statement that some benchmark-labelled failures *may* be correct is appropriately qualified. Its bibliography metadata matches the source. [Primary paper](https://arxiv.org/html/2608.04975). **The Replication Trap** reports 94–100% sensitivity and 17–50% false positives, supporting the new related-work sentence. [Primary report](https://www.clawrxiv.io/abs/2604.00898).

As an ICML empirical paper, the useful contribution is the documented operating points, task-framing sensitivity and complementary failure patterns. The evidence supports that narrower contribution. It does not establish a causal decomposition of a ceiling or a general vendor advantage.

Verification covered all **10,224 retained science readings**, matching program hashes across code arms, independent reproduction of the repaired paired intervals and exact cluster test, data flag counts, and byte-identical in-memory regeneration of Table 1. The manuscript checker passes despite the prose contradictions above. The compiled main text ends on page 8; the named-author preprint still needs an anonymised submission build under [ICML’s instructions](https://icml.cc/Conferences/2026/AuthorInstructions). :codex-file-citation{path="/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.pdf" purpose="source"}

**Not submittable.** The single most important reason is that the contribution statements and appendices still assert stronger validation than the records establish, despite the corrected main-text descriptions.
