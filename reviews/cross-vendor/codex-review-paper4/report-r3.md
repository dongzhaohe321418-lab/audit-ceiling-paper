**Updated recommendation: weak reject, now principally on scientific strength rather than reporting accuracy.** The round-2 manuscript findings are fixed except for the explicitly pending review gate. One minor wording error remains.

Reviewed `463138f` against `591f6b2`, including the revised study report, records, ledgers and C20. No files were modified.

1. **Open — C20 and the review-completion claim remain a submission blocker.**

   [tex/paper.tex:59](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:59) says every quoted report passed independent review. The controlling record, [manuscript/CLAIMS.md:411](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:411), still marks C20 **pending round 3, not quotable**; the archived [study round-2 disposition:84](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reviews/cross-vendor/codex-review-a4s4/report-r2.md:84) is “not quotable as written.”

   This remains the acknowledged branch-state issue. Submission requires a study review ending quotable and reconciliation of the claim ledger and manuscript. This manuscript review does not itself admit C20.

2. **New minor finding — one appendix sentence overcompresses the three strength cases.**

   [tex/appendix/ai4s_full.tex:202](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:202) says the three psi-converted strength items are “described as a decimal shift or a wrong factor.”

   That describes `concrete.F1.2` and `.F1.3`, but not `.F1.1`. Its findings identify anomalous scaling without proposing either explanation. See [cross.d1.jsonl:37](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d1.jsonl:37) and the corrected [verdict:271](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_supplement.json:271).

   Use the report’s accurate formulation: three locate the anomaly without explaining the conversion; **one** calls it a decimal shift and **one** reconstructs a wrong factor. This does not affect any count or interval.

3. **Fixed — the abstract and introduction no longer conflate the post hoc analyses.**

   [tex/paper.tex:56](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.tex:56) explicitly attributes the fourteen-item result to the study agent’s unblinded post hoc reading. [tex/sections/introduction.tex:43](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/introduction.tex:43) now reports only the registered lexical contrast. The body distinguishes localization from explanation at [tex/sections/ai4s.tex:120](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/ai4s.tex:120).

   The records support these separate quantities:

   | Analysis | Result |
   |---|---|
   | Registered lexical rule | Union 105/140; gain **10.7 points [6.0, 15.9]** |
   | Stricter post hoc keyword filter | Cross 53, self 32; union still **105** |
   | Agent’s post hoc localization assessment | 14 added items; **10.0 points [5.4, 15.1]** |
   | Agent’s post hoc transformation-explanation assessment | 11 added items; **7.9 points [3.7, 12.5]** |

   Controlling records are [diag_results.json:109](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_results.json:109), [diag_posthoc.json:1](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_posthoc.json:1), and [diag_supplement.json:281](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_supplement.json:281). I reproduced these counts and intervals.

   The associated study-round-2 findings are also repaired in substance. The report calls the stricter filter lexical, discloses its erroneous exclusion of `ccpp.F5.1`, separates localization from explanation, and defines the endpoint as column naming with the duplication exception. The accidental Kelvin match inside “task ” is corrected at [posthoc_diag.py:46](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/analysis/diag-b8a0693/posthoc_diag.py:46); aggregate counts remain unchanged. These repairs satisfy C20’s interpretive restrictions without establishing independently adjudicated diagnosis.

4. **Fixed — the usage ledger is mirrored and the accounting reconciles.**

   [records/PROVENANCE.md:101](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/PROVENANCE.md:101) now includes both ledgers. I summed [cross.usage.jsonl:1](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_ledger/cross.usage.jsonl:1) and [self.usage.jsonl:1](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_ledger/self.usage.jsonl:1):

   **$13.57609225 + $10.83371550 = $24.40980775**, across **1,120 + 1,124 = 2,244 events**. All 2,240 expected reading identifiers are represented; four self identifiers have an extra event. The report correctly distinguishes ledger valuation from an invoice.

5. **Fixed — both previously overcompressed counterexamples are accurately described.**

   [reports/RESULTS-AI4S-DIAG.md:74](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:74) and [tex/appendix/ai4s_full.tex:200](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:200) now include the near-duplicate allegation and affirmative statements.

   This matches `supercond.F4.2` in [self.d2.jsonl:263](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d2.jsonl:263) and `supercond.F7.3` in [self.d4.jsonl:279](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/self.d4.jsonl:279). Neither establishes the injected corruption.

6. **Fixed — the fault-table interval units are explicit.**

   [reports/RESULTS-AI4S-DIAG.md:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-AI4S-DIAG.md:53) now specifies counts out of twenty and intervals on percentages, consistent with [diag_supplement.json:2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_supplement.json:2).

7. **Still fixed — budget interpretation and clean-flag qualification.**

   [tex/appendix/ai4s_full.tex:192](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/appendix/ai4s_full.tex:192) distinguishes the observed rate from population assurance. The reproduced clean-rate interval reaches **10.5%**. Lines 203–205 preserve the qualification that the nine documentation objections may be fair readings, consistent with [cross.d1.jsonl:75](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/ai4s/diag_readings/cross.d1.jsonl:75) and C20.

**The main body still ends on page 8.** I inspected the rendered boundary in [tex/paper.pdf](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/paper.pdf): Related Work finishes on page 8; page 9 begins with the Impact Statement and references. The manuscript checker passes. All 280 held-out CSV hashes match the manifest, with no development CSV hash overlap.

Apart from C20’s admission gate, I found **no further substantive submission blocker within this repair review**. Correct the minor appendix sentence before submission.

My **weak-reject** recommendation remains because the prospective result establishes lexical coverage on new samples from four previously used tables and seven synthetic faults. The stronger diagnostic interpretation still rests on the study agent’s post hoc assessment. The reporting is now substantially sound; complete independent, fault-specific adjudication at the frozen operating points remains the most valuable scientific improvement.
