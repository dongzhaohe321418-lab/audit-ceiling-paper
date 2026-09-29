**Updated recommendation: weak reject.** A4S-4 materially improves the design, and its registered arithmetic reproduces. However, the executable endpoint does not establish correct diagnosis, and the records contain actual false matches. The experiment therefore only partly resolves round 2’s main objection.

I reviewed `8f4c04a`, the specified additions, and the repairs in `65deecc`. No files were modified.

1. **Major, blocking for the new diagnostic claim. “Correctly diagnosed” overstates what the scorer measures, including on observed cases.**

   **Manuscript:** [tex/paper.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:56), [tex/sections/introduction.tex:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:43), [tex/sections/ai4s.tex:115](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:115), [tex/appendix/ai4s_full.tex:172](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:172), and [C20:411](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:411).

   The registration explicitly says the rule can count a finding that names the right column for the wrong reason ([PREREGISTRATION-DIAG.md:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/ai4s/PREREGISTRATION-DIAG.md:50)). This is an observed failure, not merely a hypothetical limitation:

   | Counted item | What the archived finding actually says |
   |---|---|
   | `cross`, `airfoil.F2.3` | Its only flagged reading requests better column documentation. It never identifies the injected negative values. Nevertheless, mentioning “displacement thickness” earns a diagnosis. [cross.d4.jsonl:114](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d4.jsonl:114); [manifest:2096](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/data_items_ho.json:2096). |
   | `self`, `supercond.F4.0` and `.F4.1` | The matching findings complain about dataset size, mentioning `critical_temp` while describing the schema. Neither diagnoses shuffled targets. [self.d4.jsonl:261](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d4.jsonl:261), [self.d2.jsonl:262](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d2.jsonl:262). |
   | `self`, `supercond.F7.3` | The matching BLOCKER lists the columns and explicitly says the structure requirement is satisfied. It says nothing about rounding the injected column. [self.d4.jsonl:279](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d4.jsonl:279); [manifest:5753](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/data_items_ho.json:5753). |

   There is also a qualification within the **15 incremental primary catches**. For `concrete.F5.0`, the sole flagged reading alleges a three-column reassignment involving coarse aggregate. The manifest specifies a two-column swap of superplasticizer and fine aggregate, leaving coarse aggregate unchanged. It identifies a relevant problem but gives an incorrect mapping ([cross.d1.jsonl:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d1.jsonl:56); [manifest:1166](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/data_items_ho.json:1166)).

   Thus **57, 40, 105 and their contrasts are reproducible lexical-score counts**, not established counts of correct diagnoses. The false `airfoil.F2.3` match does not change the union gain because the validator already catches it; it does invalidate the literal interpretation of the model’s 57. I would not mechanically subtract the examples above and present a replacement semantic result without adjudicating all findings consistently.

   The body’s “necessary, not sufficient” caveat is useful, but the abstract and introduction drop it. The appendix’s claim that this study *answers* whether faults are correctly diagnosed is also too strong.

2. **Major, nonblocking for arithmetic reproduction. The held-out artefacts needed to verify the new findings are absent from this snapshot.**

   **Manuscript:** [tex/appendix/ai4s_full.tex:174](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:174) and [:199](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:199).

   **Records:** the mirror inventory at [records/PROVENANCE.md:101](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/PROVENANCE.md:101) contains manifests, readings, results and scripts, but no held-out `data.csv`/`CARD.md` files. The builder expects external source tables and writes the items outside this repository ([build_data_items_ho.py:24](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/analysis/diag-25071d0/build_data_items_ho.py:24)).

   I could verify that every reading’s hash agrees with its manifest and that development and held-out manifests share no CSV hash. I could not independently verify the held-out file contents, validator outputs or numerical allegations against those bytes. The ten-finding inspection also lacks archived sample IDs and a selection script. Its sentence agrees with the report, but the exact sample is not independently identifiable.

   Mirror the held-out artefacts and inspection selection. The **$24.41** sentence agrees with the report, but its usage ledger is likewise not mirrored.

3. **Minor. Two qualifications from the report are weakened or omitted.**

   **Fixed budget versus fixed rate:** [tex/sections/ai4s.tex:116](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:116) says “a clean-flag rate fixed in advance.” The **budget and decision thresholds** were fixed; the realised rate was not. The registration explicitly allows a held-out budget exceedance ([PREREGISTRATION-DIAG.md:72](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/ai4s/PREREGISTRATION-DIAG.md:72)). Use “budget” here.

   H1 legitimately passes its registered **point-estimate** criterion. This does not establish a population false-positive rate below 10%; the reported union interval reaches 10.5%. This is a scope clarification, not a reason to reverse the registered H1 outcome.

   **Clean-flag interpretation:** [tex/appendix/ai4s_full.tex:203](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:203) correctly describes the nine documentation objections, but omits the report’s explicit qualification that these may be fair readings of the task rather than erroneous findings ([RESULTS-AI4S-DIAG.md:62](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:62)). Restore that distinction wherever they are characterised as false positives.

4. **Minor, but must be reconciled before submission. The review-completion claims are false at this commit.**

   [tex/paper.tex:59](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:59) says every quoted report passed independent review; [tex/sections/introduction.tex:72](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:72) likewise says every report was reviewed.

   **Controlling record:** [C20:411](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:411) explicitly marks A4S-4 pending and not quotable. I recognise that this is deliberately a review branch. Nevertheless, the snapshot’s manuscript and ledger disagree; this review does not make the current diagnostic wording quotable.

The five requested round-2 repair areas **are resolved in `65deecc`**, with the stated reproduction limitation:

| Area | Verification |
|---|---|
| Study-map cells | [results_full.tex:51](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/results_full.tex:51), :53, :59 and :61 now correctly distinguish \(K=8/4\), the 112-instance revision population, wrong applications **among retained failing applications**, and reference disagreements **among flagged instances**. Consistent with the registrations and `records/code/testgen-val/tables.md`. |
| Re-execution wording | [ai4s.tex:82](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:82) and appendix :105 restrict the advantage to the sensitivity subset and retain 70/74 versus 72/74 and the eight real construction defects. Matches `results_posthoc.json`. |
| SciCode sample | [ai4s.tex:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:54) and its appendix counterpart now specify the first BLOCKER of the first flagged reading and the four excluded-earlier-function findings. Matches `RESULTS-AI4S-CODE.md` and `code_posthoc_b.json`. |
| Reproducibility text | [reproducibility.tex:16](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/reproducibility.tex:16) correctly promises blocking texts, identifies final scripts and discloses the harness dependency. The final `posthoc_results.py` contains the previously missing adjudication and sign-flip outputs. This repairs the disclosure and archive gap; it does not make the analyses standalone. |
| Redaction | All 17 identified home-path occurrences were replaced. I verified that the six affected record files changed only by home-prefix substitution. No matching personal home paths remain in the scanned science archive, mirrored scripts or test-validation records. |

For the remaining added sentences, I verified the 280-item balance, complete 2,240-reading grid, development thresholds and calibration counts, unchanged construction apart from seed/paths, fault-type totals, six uncounted `cross` flags, and nine clean documentation flags. All quoted endpoint intervals and both McNemar values reproduce in memory. The same-table/synthetic-fault and route-confounding qualifications are accurate. The metadata’s 30 pages and 1,675-character abstract are correct, although that abstract still omits A4S-4.

The finite-budget definition of “ceiling” also improves the earlier framing. I no longer regard the requested held-out comparison as wholly absent. The remaining decisive concern is whether its endpoint measures the scientific construct claimed.

**The single change that would now most improve the paper is a complete, independently validated, fault-specific adjudication of A4S-4 at the already frozen operating points.** Check findings against the actual corrupted artefacts using executable witnesses or blinded expert adjudication, including incorrect explanations and incidental column mentions. Preserve the registered lexical result and clearly distinguish any subsequent semantic rescoring. That would directly address the gap now preventing this otherwise useful study from supporting its headline.
