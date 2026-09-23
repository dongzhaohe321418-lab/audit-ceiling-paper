**Not quotable yet.** The seven replacements and chronology correction are sound, but the distinction between false content claims and filesystem-delivery disputes remains inconsistent.

I reviewed `4bcc1c2` without modifying files. I read all **56 exemplar texts** against their items and all **49 BLOCKER texts on the 11 excluded items**. All 2,240 reading task/program hashes match; all 280 CSVs have 120 complete rows, matching card headers, and untruncated named-file rendering. The registered analysis and both post hoc scripts reproduce their saved JSON exactly, with writes intercepted in memory.

1. **The seven replacements are valid; the retained delivery exemplars remain problematic.**

   All seven replacement row-count allegations are explicit and unwithdrawn:

   | `supercond.clean.N` | Replacement | Claimed data rows |
   |---|---|---:|
   | 4 | d4 b0 | 146 |
   | 5 | d2 b1 | 121 |
   | 6 | d3 b0 | 102 |
   | 13 | d1 b0 | 100 |
   | 24 | d3 b0 | 100 |
   | 26 | d1 b0 | 100 |
   | 31 | d4 b0 | 121 |

   Each file has 120 data rows. Across the complete record, all **28 row-count, seven column/header/target, two field-count and one truncation exemplars** contain directly refutable, unwithdrawn statements.

   The **18 absent-file exemplars are not uniformly of that character**. For example:

   - [`supercond.clean.12|d3|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d3.jsonl:223) explicitly acknowledges the named path header and CSV contents, then says no actual artifact was delivered to the filesystem.
   - [`supercond.clean.23|d1|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d1.jsonl:234) distinguishes successful parsing from confirmation that the file exists in the working directory.
   - [`supercond.clean.22|d4|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d4.jsonl:233) acknowledges the labelled CSV block but disputes its status as a standalone file.

   Their opening “missing” assertions must be interpreted with those qualifications. A program-hash match establishes correspondence with the supplied contents; it does not refute the filesystem distinction these texts make.

   **This corrects an overly permissive judgment in round 3**, which accepted these retained texts “under the increment’s defined representation.” That supports calling them protocol disputes, but does not establish the present, narrower claim that each denies inclusion of the CSV under its named path.

2. **The account of the 11 exclusions is incomplete.**

   The five original exclusions—`concrete.clean.5`, `.7`, `.18`, `.28`, `.30`—are reasonably described as documentation/requirement judgments, with the stated plausibility qualification for `.18`. The missing-target allegation in `.8` is withdrawn.

   However:

   - [`supercond.clean.15|d3|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d3.jsonl:226) says the audited increment’s artifact list contains only `CARD.md`, despite acknowledging the CSV listing. Under the criterion used to retain other absent-file exemplars, this is a candidate counterexample to the exclusion.
   - [`supercond.clean.2|d3|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d3.jsonl:213) says the raw rows have no indication of file-path structure, although the named path is supplied. Its following BLOCKER also alleges deviations from “documented stated ranges”; the card supplies none.
   - [`concrete.clean.24|d1|b0`](/Users/ericdong/Documents/Crossaudit/ai4s/runs/data_audit/self.d1.jsonl:25) acknowledges the Age values but **retains** the claim that the column count and structure do not match the card. All nine headers match, and every row is complete. Describing this solely as a withdrawn missing-column allegation omits the surviving false schema claim.

   Conservative exclusion is acceptable for a lower-bound count. Claiming that these items have no qualifying exemplar, or that their relevant allegations are wholly withdrawn, is stronger than the evidence supports.

3. **The per-kind checks reproduce the record but do not fully verify its advertised meaning.**

   The row-count, field-width and truncation checks corroborate the selected factual discrepancies. Retraction and interpretation still require manual reading.

   The [column branch](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ai4s/benchmarks/ai4s/clean_flag_exemplars.py:117) checks nonempty last fields and `len(header) == width`, where `width` was defined as `len(header)`. It never checks the allegedly missing column’s identity.

   I confirmed this with an entirely in-memory negative control: renaming `Age (day)` to `UNRELATED_COLUMN` in `concrete.clean.13` still passes every assertion. The actual item is correct; the claimed automated verification is incomplete. Likewise, the absent-file branch verifies a hash, not the semantic distinction between missing contents and unestablished filesystem delivery.

4. **The chronology correction is fixed; the registered reading remains supported.**

   The erratum now attributes the no-analysis claim to the study agent rather than certifying it.

   The whole-report reread found no additional numerical blocker. The registered flag sets reproduce; I also reread a fault-identifying finding for each of the 18 post hoc additional fault-relevant items. The distinctions between flags and detections, registered and adjusted rules, and route-specific results remain appropriate. The disclosed baseline, construction, uncertainty and budget limitations remain limitations of the unchanged experiment.

**not quotable — the single most important reason is that the 56-item clean-flag claim still treats some filesystem-delivery disputes as directly refuted facts, while applying a different standard to excluded items.**
