**Updated recommendation: weak reject, with substantial improvement over round 1.** The registered result is now described honestly in the body, and the missing experimental artefacts are available. However, the abstract and introduction still misdescribe the new post hoc result. Completing the separate study review will not resolve that discrepancy.

I reviewed `591f6b2` and the repair diff against `8f4c04a`. No files were modified.

1. **Major — endpoint interpretation is partly fixed. The headline now conflates two different post hoc analyses.**

   [tex/paper.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:56) and [tex/sections/introduction.tex:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:43) attribute **+10.0 [5.4, 15.1]** to requiring each finding to state the fault itself. That is not what the records show.

   | Analysis | Union count | Gain over validator |
   |---|---:|---:|
   | Registered lexical rule | 105/140 | +10.7 points |
   | Post hoc fault-specific executable rule | 105/140 | +10.7 points |
   | Additional agent inspection excluding one incorrect column mapping | 104/140 | +10.0 points |

   The controlling records are [diag_posthoc.json:31](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_posthoc.json:31) and [diag_supplement.json:275](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_supplement.json:275). The excluded item is `concrete.F5.0`, whose finding describes a three-column reassignment instead of the injected two-column swap ([cross.d1.jsonl:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d1.jsonl:56)).

   The body, appendix and [revised report:87](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:87) distinguish these analyses correctly. The abstract and introduction must do so too, including that the fourteen-item assessment is **the study agent’s unblinded post hoc reading, not independent adjudication**, as [C20:418](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:418) requires.

   The original “correctly diagnosed” claim has otherwise been removed from the authoritative manuscript. The explicit lexical limitation and observed counterexamples satisfy C20’s must-not-write clause in the body. This repairs the interpretation of the registered endpoint; it does **not** validate either scorer as a measure of correct diagnosis.

2. **Open — the review-completion statement remains false at this snapshot.**

   [tex/paper.tex:59](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:59) claims every quoted report passed independent review. [tex/sections/introduction.tex:72](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:72) likewise presents review as completed.

   The controlling record remains [C20:411](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:411), explicitly **pending round 2 and not quotable**. The archived first study review concluded “not quotable as written.” I recognize this is knowingly pending on the review branch. Submission requires a favorable disposition of the revised report and reconciliation of the ledger and manuscript; merely finishing another review is insufficient.

3. **Partly fixed — the reproducibility gap is substantially closed, but the usage ledger remains absent.**

   The new inventory at [records/PROVENANCE.md:101](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/PROVENANCE.md:101) now includes all **280 CSVs and 280 cards**. I verified every CSV hash, regenerated every card, reproduced every validator output, and checked every reading’s CSV and task hashes. No held-out CSV hash overlaps development.

   The inspection sample is now identifiable and reproducible from [diag_supplement.json:294](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_supplement.json:294) and [diag_supplement.py:86](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/analysis/diag-2b4855e/diag_supplement.py:86). This closes the substantive artefact and sample-selection objections.

   However, the A4S-4 usage ledger is still not mirrored. Consequently, [tex/appendix/ai4s_full.tex:197](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:197) and the report’s **$24.41 / 2,244 completion events** rely on the earlier reviewer’s verification rather than independently inspectable accounting records in this snapshot. Mirror that ledger or remove the unsupported accounting precision. This does not undermine the experimental counts.

4. **Minor — two new descriptive details need correction.**

   - [reports/RESULTS-AI4S-DIAG.md:76](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:76) and [tex/appendix/ai4s_full.tex:201](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:201) overcompress the unrelated `self` findings into complaints about row counts, cards or missing ranges. `supercond.F4.2` includes a **near-duplicate-record allegation** and an affirmative documentation statement; `supercond.F7.3` explicitly affirms structural compliance. See [self.d2.jsonl:263](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d2.jsonl:263) and [self.d4.jsonl:279](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d4.jsonl:279). They remain unrelated lexical matches, so the conclusion is unchanged.
   - The new fault-type table at [reports/RESULTS-AI4S-DIAG.md:55](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:55) combines **counts** with **percentage intervals** without labeling the latter’s units. For example, `5 [7.1, 45.5]` needs an explicit percentage label. The underlying values in `diag_supplement.json` reproduce.

5. **Fixed — budget versus realized rate.**

   [tex/sections/ai4s.tex:115](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:115) now correctly says **budget fixed in advance**. The appendix explicitly distinguishes the observed 6.4% from its interval reaching 10.5% ([ai4s_full.tex:192](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:192)). This agrees with the registration and `diag_results.json`. H1 passes its registered empirical-rate criterion; population-level budget assurance is no longer claimed.

6. **Fixed — the clean-flag qualification is restored.**

   [tex/appendix/ai4s_full.tex:210](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:210) now says the nine airfoil documentation objections may be fair readings rather than errors. This matches the report, C20 and the archived findings, for example [cross.d1.jsonl:75](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d1.jsonl:75).

The study’s other round-1 reporting concerns are also repaired: the `self` operating point explicitly requires four flags but only one matching reading; the conservative/lower-bound interpretation is withdrawn; fault-specific intervals and the degenerate validator-clean interval are supplied; and cost is described as ledger valuation with a periodically checked halt.

I reproduced the **90/57/40/105** registered counts, **53/32** post hoc-rule counts, all reported aggregate and fault-specific intervals, both McNemar tests, and the fourteen-item sensitivity interval. The mechanical manuscript checker passes, but misses the headline mismatch above.

**Beyond the pending review, the headline correction and the smaller reporting/archive repairs remain before submission.** I found no further numerical or artefact-integrity blocker within this second-round scope. My weak-reject recommendation now rests primarily on scientific strength: the prospective result establishes lexical coverage, while the stronger diagnostic interpretation still depends on post hoc assessment.

**The single most valuable improvement remains complete independent, fault-specific adjudication at the frozen operating points**, checked against the corrupted files, with explicit treatment of incidental mentions and partially incorrect explanations. Preserve the registered lexical result alongside it.
