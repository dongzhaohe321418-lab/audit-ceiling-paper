Reviewed `6b1a787` on `ai4s`. No files modified. The principal numerical results reproduce, but several new summary claims exceed their reviewed evidence.

I am a GPT-6-family reviewer. This is therefore **not outside-family validation** of Astra’s comparisons, the residual labels it helped produce, the clarification adjudication, or the programme’s previous reviews. My arithmetic checks do not remove that conflict.

1. **Major, blocking — the contributions claim isolated effects that the studies do not identify.**  
   [introduction.tex:40](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:40) says each factor is “varied alone”; line 44 says the limit is “set jointly” by the auditor, rulebook, decision rule and specification.

   C2 explicitly says model and sampling change together. C13 does not isolate specification-determinedness: additions often contradict the oracle, the agreement split was measured after outcomes, and the informative cluster test is \(p=0.0625\). The appendix correctly says the association is **not isolated as a cause**.

   **Contradicting evidence:** [CLAIMS.md:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:36), [CLAIMS.md:298](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:298), and [results_full.tex:480](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:480).

   The contribution should describe route comparisons, controlled rule changes, and a post hoc association separately. The current wording upgrades their inferential authority.

2. **Major, blocking — the claimed three-domain head-to-head was not performed.**  
   [introduction.tex:47](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:47), [system.tex:60](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/system.tex:60), and [related.tex:37](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:37) describe LLM-versus-deterministic comparisons on scientific **code, results and data**, including checks that a shipped system runs.

   A4S-1 compares two model routes and two task framings. Its scientific tests supply the labels; they are not an independently evaluated audit tier. A4S-3 uses a separately constructed validator. Only A4S-2 measures the shipped `science` profile alongside the model.

   **Contradicting evidence:** [RESULTS-AI4S-CODE.md:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-CODE.md:18), [code_results.json](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/code_results.json), and [RESULTS-AI4S-DATA.md:22](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DATA.md:22).

   Narrow the contribution to scientific-code auditing plus complementary-tier comparisons on results and data. The exact “first” claim cannot stand around an experiment the paper does not contain.

3. **Major — summary passages turn item flags into fault detections.**  
   [paper.tex:48](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:48) and [introduction.tex:32](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:32) say the data auditors “caught” 92 and 65 faults, together 112. The latter two numbers count items receiving **any BLOCKER**. Four of the model’s faulty-item flags concern documentation rather than the injected fault. Under the report’s post hoc fault-relevance rule, the corresponding counts are **61 and 110**.

   Likewise, the abstract’s “recomputing … flagged 23” and [discussion.tex:15](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:15) omit the important distinction between **23 flagged fabrications and 21 sound diagnoses**. Section 4.2 preserves it.

   **Contradicting records:** [data_posthoc.json](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/data_posthoc.json), [results_posthoc.json](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/results_posthoc.json), and [RESULTS-AI4S-DATA.md:71](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DATA.md:71).

   Retain the registered counts, call them flags, and carry the post hoc diagnosis qualification into the summaries.

4. **Major — the scientific-code framing result becomes a stronger intervention and adjudication claim.**  
   [paper.tex:52](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:52) attributes the reduction to “naming the step.” The intervention also moved the problem description, marked it as context, and exempted earlier functions. Arms ran sequentially without randomisation.

   More seriously, [discussion.tex:26](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:26) declares the construction objections correct and says every clean-item flag was read. For scientific code, the report describes a **sample of 20 first BLOCKERs**, an unvalidated pattern count, and expressly declines to establish which flags identify defects.

   **Contradicting evidence:** [RESULTS-AI4S-CODE.md:97](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-CODE.md:97), particularly lines 111–142, and C19. Report the effect of the complete task reframing; do not present the code-study observations as exhaustive adjudication.

5. **Major — compression drops required uncertainty, operating points and analysis labels.**  
   These are omissions, not incorrect underlying estimates:

   | Location | Qualification lost |
   |---|---|
   | [introduction.tex:20](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:20) | The −26.4 contrast lacks the stronger route’s own false-positive rate and sampling qualification; +26.8 lacks its false-positive cost. C2 and C3 explicitly require these to travel with the claims. |
   | [ceiling.tex:49](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:49) | The exploratory 59.1% versus 34.5% comparison omits its 34.0% versus 19.3% false-positive rates and intervals. Astra’s following rates also lose their intervals. |
   | [ai4s.tex:45](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:45) | The −46.9-point route contrasts lose their intervals and same-route clean rates. The following K=1 figures lose intervals. |
   | [ai4s.tex:90](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:90) | Data intervals are not identified as resampling **items within dataset**. The general statement at [discussion.tex:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:36) incorrectly calls the primary intervals problem-cluster bootstraps. |
   | [ai4s.tex:97](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:97) | The “at least 48” finding loses its **post hoc lower-bound** label. The clean-result adjudication at line 75 and the 18/28 statement in Discussion also lose their post hoc labels. |

   **Records:** C2, C3, C17–C19; `code_results*.json`, `data_results.json`, `data_clean_flag_exemplars.json`, and `results_posthoc.json`. For example, −46.9 carries intervals **[−63.0, −30.7]** and **[−61.5, −34.4]**, respectively. Data’s 2.9% clean-flag rate carries **[0.7, 5.7]**, with no between-dataset uncertainty.

   Also retain the scientific-code recall-change sensitivity: its bootstrap excludes zero, but the cluster sign-flip result is **0.0625**. That distinction disappeared from both manuscript versions of the science results.

6. **Minor — the explanation of re-execution’s four misses is numerically wrong.**  
   [ai4s.tex:73](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:73) says their outputs are within `np.allclose`’s default absolute tolerance of zero. One true output is approximately **−1.616×10⁻⁷**, outside \(10^{-8}\). Its **5% change**, approximately \(8.08×10^{-9}\), is absorbed by the tolerance.

   **Contradicting record:** `reexec_missed_true_values` in [results_posthoc.json](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/results_posthoc.json). Say the *differences* fall within the comparison tolerance. The same error appears in Appendix C.

7. **Minor — the science figure needs a caption correction and larger labels.**  
   [ai4s.tex:21](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:21) says “any model BLOCKER” is the flag rule throughout. That applies to model series, not deterministic failures, re-execution or their unions. The report defines these separately.

   In the compiled **Figure 2** (`fig4_ai4s.pdf`), category labels render at approximately **4.68 pt**, and legends near **5.08 pt**. They are difficult to read at publication size. The plotted values themselves agree with the records; I found no clipping or overlapping labels. [make_fig4_ai4s.py:57](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/figures/make_fig4_ai4s.py:57) fixes the small category font.

   [table1.tex:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/table1.tex:2) also still promises “Every primary quantity this paper quotes,” although it contains no science-study results.

8. **Minor, but relevant to novelty — the literature positioning needs two additions and a narrower conclusion.**  
   [related.tex:28](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:28) omits **SciCode-Verified**, published before this manuscript, which directly audits contradictory specifications and defective scientific tests. It is particularly relevant to the scientific-code interpretation. [Primary paper](https://arxiv.org/abs/2608.04975).

   **The Replication Trap** also measures sensitivity and false positives for LLM review of constructed scientific statistical workflows, including prompt changes and repeated-review conditions. It does not establish the exact deterministic-tier comparison claimed here, but it limits any broader claim to first measuring scientific-auditor operating points. [Primary report](https://www.clawrxiv.io/abs/2604.00898).

   The cited **SPOT 21.1%/6.1%** and **SciCoQA 46.7%** figures are supported. Luo et al. already report both true- and false-positive rates, as the appendix acknowledges. Thus the plausible novelty is the particular measurement programme and its results/data comparisons, not scientific auditing or paired operating-point reporting themselves. [SPOT](https://arxiv.org/abs/2505.11855), [SciCoQA](https://arxiv.org/abs/2601.12910), [Luo et al., Table 11](https://arxiv.org/html/2509.08713v2).

The **restructure itself is faithful** when compared with its immediate parent: headings and labels change, and Table 1 and two figures relocate. Compared with `cb30d49`, however, preceding commits also rewrite prose, remove correction histories, correct rater identities and revise the blinding description. It is not a verbatim preservation of the round-13 manuscript. I found no unexplained change to the retained general-code numerical results; the substantive problems above arise principally in the new summaries and science framing.

The four-part story is coherent and potentially useful as an empirical evaluation paper. Its strongest evidence is the measured operating points and complementary failure patterns. It does not establish an isolated causal decomposition of a ceiling or a general advantage of cross-vendor auditing.

Verification included all **10,224 retained science readings**, independent recomputation of the scientific-code headline and paired bootstrap intervals, exact regeneration of the data-analysis record, and in-memory byte-identical regeneration of Table 1. The committed PDF matches the checkout. I inspected its main pages and all figures; I did not rebuild because that would write files.

The main text ends on **page 7**, references end on **page 8**, and appendices begin on **page 9**. It meets ICML’s eight-page main-body limit. The current PDF is explicitly a named-author preprint and would need an anonymised submission build. [ICML instructions](https://icml.cc/Conferences/2026/AuthorInstructions). :codex-file-citation{path="/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.pdf" purpose="source"}

**Not submittable.** The single most important reason is that the new contribution statements claim isolated effects and a three-domain tier comparison that the reviewed study designs do not establish.
