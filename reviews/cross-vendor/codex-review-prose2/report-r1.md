Reviewed all six changed files against `153d830`, the claims register, and the relevant report passages. No files were modified. I found four ambiguities introduced or worsened by the revision, rather than a demonstrated change in the underlying measurements.

1. **Ambiguous attribution to the intervention arm** — [tex/appendix/results_full.tex:292](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/tex/appendix/results_full.tex:292), also affecting line 298.

   **Old:** “This reproduces §[rulebook]’s effect … A post hoc quantity … is 3 of 110 under the shipped constitution and 27 of 110 under the rule.”

   **New:** The replication sentence moves before the grading intervention. The text then discusses that intervention and its failed hypothesis before reporting “27 of 110 under the rule.” The next paragraph continues with “the same rule.”

   Moving the sentence removes the intervening reference back to the referent-rule result. “The rule” now most naturally refers to the grading rule. This matters numerically: [RESULTS-CEILING3B.md, Table 5b](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/reports/RESULTS-CEILING3B.md:82) assigns **27/110 to the referent arm and 3/110 to the grading arm**. CLAIMS C8 and C9 likewise assign these effects to the referent rule. Name “the referent rule” explicitly at both locations.

2. **The new backward reference conflates potentially different quantities** — [tex/appendix/results_full.tex:299](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/tex/appendix/results_full.tex:299).

   **Old:** “union recall (the identical quantity: blocked by at least one BLOCKER, unioned over eight readings)”

   **New:** “This is the identical quantity used above: blocked by at least one BLOCKER, unioned over eight readings.”

   “Used above” adds an unspecified comparator. The immediately preceding paragraph reports four-reading BLOCKER recall and then a separately adjudicated, post-hoc reports-a-failure count. Neither is the eight-reading quantity being introduced. [RESULTS-CEILING4.md, Table 1](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/reports/RESULTS-CEILING4.md:41) identifies the intended comparison: `cross-R` and `cross`, both at K=8. Name that comparison or explicitly reference the earlier eight-reading headline.

3. **The sentence split obscures which instances the qualification covers** — [tex/appendix/discussion_full.tex:76](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/tex/appendix/discussion_full.tex:76).

   **Old:** “moved diagnosis on 9 of 32 such instances, all of them where the added rule did not contradict the hidden suite”

   **New:** “moved diagnosis on 9 of 32 such instances. In every one of them the added rule did not contradict the hidden suite”

   The detached “every one of them” can refer to the 32 selected instances rather than the nine with changed diagnosis. The following clause forces the reader to reconsider that interpretation. [RESULTS-CLARIFY.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/reports/RESULTS-CLARIFY.md:53) and CLAIMS C13 distinguish the nine diagnosed instances from the 23 wholly contradictory additions. Replace the pronoun with “the nine instances with changed diagnosis.” This finding concerns the newly weakened antecedent connection.

4. **“Does not reach it” loses its clear threshold reference** — [tex/appendix/related_full.tex:57](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/tex/appendix/related_full.tex:57).

   **Old:** “against a preregistered 2% threshold, over a frozen set … Corroboration across independent generations does not reach it”

   **New:** “judged against a preregistered 2% threshold. It is taken over a frozen set … Corroboration across independent generations does not reach it”

   The inserted sentence uses “It” for the measurement, then introduces “that set”; the final “it” must jump back to the threshold. [RESULTS-TESTGEN-VAL.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-paper-prose/reports/RESULTS-TESTGEN-VAL.md:20) and CLAIMS C7 establish the intended statement: neither paid rule meets the registered validation criterion. Say “does not meet that validation criterion.”

I found no other revision-induced change to numerical attachment, procedural meaning, causal interpretation, or what a cited paper is said to show.

**revise** — Most importantly, the revised ordering can attach the referent arm’s 27/110 result to the grading arm.
