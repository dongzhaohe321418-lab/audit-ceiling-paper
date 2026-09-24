Reviewed `e1ae582..153d830` against the ledger, reports and records. No files changed. I found qualification losses and stronger interpretations, but no changed numerical point estimate or test value.

1. **The science summary attributes a bundled intervention to one component.**  
   [tex/paper.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:56), [tex/sections/introduction.tex:46](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:46).

   “Naming the step … cut flags” replaces “reframing the task around [the] step.” C19 explicitly prohibits attributing the change to one component. Arm B also moved the problem description last, marked it as context and exempted earlier functions. It was registered after A’s outcomes and run subsequently, without randomised order. The introduction additionally deletes **“with no tests shown”**, an important distinction from the general-code experiment.

   Records involved: `reports/RESULTS-AI4S-CODE.md`, “Reading” item 1; `records/ai4s/code_results_b.json`, `paired_change_A_to_B`; `manuscript/CLAIMS.md:390–406`.

   Suggested wording: “On scientific code, with no tests shown, flags on correct programs fell under a task reframing that specified the step as the deliverable, moved the overall problem into context and exempted earlier functions.” Keep the sequential-arm qualification with the quantitative comparison. The body at `ai4s.tex:48–49` correctly retains it.

2. **The stronger-model comparison loses an interval and its exploratory designation.**  
   [tex/sections/introduction.tex:30](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:30).

   The revision deletes **[0.7, 6.7]** after 3.3% and **“exploratory”** before the any-finding comparison. “Exploratory” later in the paragraph applies to the separate rulebook intervention and cannot qualify this result. Both deletions violate the ledger’s explicit reporting requirements.

   Records involved: `records/code/ceiling3/numbers.json`, `primary_H18b_self_strong_minus_cross_P` and `EXPLORATORY_any_finding_rule`; `reports/RESULTS-CEILING3.md`, Tables 1 and 4; ledger C2 and C11.

   Suggested wording: “A stronger same-vendor model, sampled differently, had 26.4 percentage points lower union flag recall [−37.3, −15.6], while flagging 3.3% [0.7, 6.7] of correct programs. Exploratory re-grading under an any-finding rule reversed the comparison.”

3. **“Catch” blurs the distinction between flagging an item and identifying its defect.**  
   [tex/paper.tex:47](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:47), [tex/sections/introduction.tex:27](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:27), introduction line 30, and [tex/sections/ai4s.tex:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:50).

   These replace operational “recall” statements with “catch/caught.” The measurements count an instance whenever any reading supplies a BLOCKER; they do not establish that its finding identifies the hidden failure. The stronger-model sentence is particularly vulnerable because the ensuing any-finding reversal measures coverage without adjudicating finding content.

   Records involved: `reports/RESULTS-SWEEP.md`, “What the sweep shows”; `reports/RESULTS-CEILING3.md`, Table 4; `records/ai4s/code_results.json`, `self_minus_cross_K8`; ledger C11.

   Use **“flag”** consistently, and define the union once: “Across eight independent readings, at least one reading flagged 30.0% …” For scientific code, retain “union recall was 46.9 percentage points lower.”

4. **The opening example is factually supported, but its conclusion exceeds the records.**  
   [tex/sections/introduction.tex:7](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:7).

   “Whoever reads this code … has little to object to” generalises beyond the observed auditors. “The defect is real only because…” turns a benchmark-relative classification into an unqualified judgement. The rerating report explicitly says failure to supply an entailment sentence is evidence, **not proof**, that none exists.

   Records involved: `reports/RESULTS-RERATE.md`, “What this does and does not say,” item 4; `records/code/rerate/{key.jsonl,L1.csv,L2.csv}`; ledger C4 and the prohibited claim about what an auditor “cannot see.”

   Replace the closing sentences with: “The task does not state how leading underscores should be handled. Both model raters classified this instance as undetermined by the prose in a post hoc assessment. It nevertheless counts as defective under our hidden-test definition.”

5. **The new transition implies that all three science studies compare two tiers.**  
   [tex/paper.tex:51](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:51), [tex/sections/introduction.tex:39](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:39).

   “In three … studies the two tiers failed in different places” overextends the design. Scientific code measures model auditors and task framing; the results and data studies compare model and deterministic checks. The later “where both tiers ran” does not make this opening description precise.

   Records involved: `reports/RESULTS-AI4S-CODE.md`, “What was measured”; `reports/RESULTS-AI4S-{RESULTS,DATA}.md`; ledger C17–C19.

   Rewrite: “Three preregistered studies examine scientific code, reported results and data. The results and data studies compare model auditing with deterministic verification.”

6. **Two smaller revisions turn qualified observations into stronger claims.**

   - [tex/sections/ceiling.tex:61](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ceiling.tex:61): “What the sentence did not visibly change is the outcome” suggests an observed absence of change. The point estimate changed by +5.4 points; its interval leaves improvement unresolved. The subsequent sentence is appropriately cautious, but the new opening conflicts with it.  
     Record: `records/code/ceiling/numbers.json`, `ceiling2.contrasts.referent-loop__vs__cross-loop`.  
     Rewrite: “An improvement in hidden-suite pass rate after revision was not established: +5.4 points [−0.9, +12.1].”

   - [tex/sections/introduction.tex:68](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:68): “false-positive rate **measures** the evaluator” replaces “**can measure**.” Construction errors can contaminate that rate without accounting for all of it. In the results study, eight clean-item flags exposed construction defects and four were wrong.  
     Record: `records/ai4s/results_posthoc.json`, `clean_flags_correct` and `clean_flags_wrong`.  
     Rewrite: “Otherwise, its apparent false-positive rate can include valid findings about defects in the evaluation materials.”

7. **Some ledger violations remain in rewritten sentences, although this revision did not introduce them.**  
   [tex/paper.tex:55](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:55), paper lines 56–57, and [tex/sections/introduction.tex:44](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:44).

   The ledger requires intervals whenever its figures are restated. The science summaries retain interval-free code rates and several data rates/count ratios. Examples include 68.7% versus 36.0%, whose intervals are [56.6, 79.7] and [26.4, 45.6], and the data union of 112/140, whose 80.0% interval is [73.6, 86.4]. The introduction’s 2.9% also lacks [0.7, 5.7].

   Records involved: `records/ai4s/code_results{,_b}.json`, `records/ai4s/data_results.json`; ledger’s opening rule and C17/C19. These are inherited omissions, not newly changed values. Moving secondary figures into the body is preferable to adding still more brackets to these paragraphs.

The opening example checks out as follows.

| Statement | Verification and record |
|---|---|
| Task and three visible examples | `clarify/conditions.json`, `conditions["b1:Mbpp/102"].original`, at the supplied worktree path. The task requests snake-to-camel conversion and supplies exactly the three described examples. |
| Generated candidate | Supplied `inputs/solutions-b1.jsonl:166`; SHA-256 `73329c7a…23b5`, matching the clarification candidate and audited instance. It splits on `_` and joins `word.capitalize()` results. |
| Passes all three examples | `records/code/study1/scored.jsonl:166` records three visible tests passed. I also executed the candidate and visible assertions successfully. |
| Hidden input and expected output | `records/code/clarify/clarification_classification.json`, row `b1:Mbpp/102`, records `___python_program` → `___PythonProgram`. The candidate returns `PythonProgram`. |
| No reading of the first three families flagged it | Confirmed across all 20 readings: cross 8, self 8, astra 4. The inherited readings are in `records/code/study1/arm-{cross,cross-replicate,self}.jsonl:63` and `study2/arm-holistic-{cross,self}.jsonl:7`; remaining readings are in `ceiling/records/cache/holistic__{family}__d*.jsonl`. All have zero model findings. |
| Both raters judged it undetermined | `records/code/rerate/key.jsonl:38` maps the instance to `Q038`; `L1.csv:39` and `L2.csv:39` both say `ambiguous-oracle`. This supports the proposed qualified wording, although the opening currently does not state it. |

The other retained numerical values, intervals and tests in the changed passages agree with the cited records. The external SciCode-audit description is also supported by [SciCode-Verified](https://arxiv.org/abs/2608.04975).

Reading the abstract and introduction as a new ICML referee, I would still lose the thread at these points.

- **The opening lacks the candidate’s actual output and introduces “families” before explaining auditors.** At introduction lines 2–8, name `Mbpp/102`, replace “families” with “model configurations,” and explicitly contrast `PythonProgram` with `___PythonProgram`. That makes the example intelligible without mentally executing the code. The records above support every element.

- **The central distinction becomes less precise immediately after the example.** At introduction lines 18–24, “whether the benchmark defines the behaviour” obscures the distinction between the hidden tests and the specification shown to the auditor. Rewrite: “A benchmark score combines whether the auditor flags a program, which findings count as blocking, how often the auditor is queried, and whether the expected behaviour follows from the specification it sees.” Then state the sampling confound and post hoc status separately. This follows C1–C4/C11.

- **“Different vendor” appears to be a universal rule, then same-vendor auditors appear without explanation.** At introduction lines 13–16 and 30, add: “The shipped configuration pairs different vendors; our comparisons also include same-vendor controls.” `tex/sections/system.tex:17` already explains how those controls run.

- **The general-code paragraph becomes a miniature results section.** At introduction lines 26–37, the reader must track repetition, a model substitution, re-grading, a rulebook intervention, revision outcomes and residual labels. Keep the 30.0%/16.0% operating point and the example connection. Replace the middle numerical catalogue with: “The measured flag rate also changes with the auditor route, its instructions and the counting rule. These contrasts do not isolate model ability, and the association between missed cases and specification ambiguity is post hoc.” Put the numerical contrasts in Section 3.

- **The data sentence is the worst numerical bottleneck.** At introduction lines 44–46, `92`, `65`, `140`, `112`, `2.9`, `61` and `110` arrive before the reader understands the two counting rules. Rewrite: “On data, the validator and model flagged overlapping sets of faulty items, so their union covered more items than either alone. A post hoc reading distinguished findings about the injected fault from complaints about the documentation.” C17 and `data_posthoc.json` supply the distinction.

- **The contribution and review paragraphs delay the scientific conclusion.** At introduction lines 50–81, the first two contributions repeat the preceding paragraph, while “killed” and the round counts require procedural interpretation. Merge the first two contributions; replace “killed” with “met their preregistered rejection criteria”; move the detailed review history to Methods.

For the **abstract**, I would retain **eight readings, 30.0% and 16.0%, with their intervals**. A referee would not miss **112/140, 2.9%, or 68.7%→36.0%** if these appeared only in the body. The nested **49/25/23/21** accounting can also move there; retain its substantive result in words: provenance checks missed consistent fabrications, while the model identified many but sometimes supplied incorrect reasoning. The abstract then has one numerical anchor and three understandable science findings.

**revise** — the most important reason is that “naming the step … cut flags” attributes the SciCode result to a component the experiment did not isolate.
