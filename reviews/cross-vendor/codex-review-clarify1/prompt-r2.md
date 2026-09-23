You are an INDEPENDENT REVIEWER from a different vendor. SECOND review of `RESULTS-CLARIFY.md` on branch `fusion/evidence-authority` at `8f66bab` (the worktree you are in). Do not modify any file.

**What this is.** P3, the only experiment in this programme that tries to turn a correlation into a causal claim. The paper's claim C4 says most of what a cross-vendor auditor misses is failure the specification never determined. That is a correlation between two measured quantities. P3 intervenes: it takes 31 instances the auditor missed, adds the missing behavioural rule to the specification prose, and asks whether the auditor's diagnosis changes. A placebo arm adds text of matched length that settles nothing.

**The result claimed.** Correct diagnosis, requiring BOTH adjudicators to say yes, at K = 4 readings per arm: original **0/31**, clarified **9/31 = 29.0%**, placebo **0/31**. Clarified minus original **+29.0 points**, problem-cluster percentile bootstrap **[+9.1, +51.7]**, 10,000 resamples, seed 20260921. Exact McNemar **p = 0.0039**; cluster sign-flip permutation **p = 0.0615**. The report says H3 holds on the registered criterion (the bootstrap interval excluding zero) and states the 0.0615 immediately beside it, because the registration itself names the sign-flip as the test that respects clustering.

**The history you must weigh, because it is unusual.** Thirteen amendments, each committed before the step it governs. **Amendment 13 discarded all 384 readings of the first audit**: `generate.py` had set the audited code to `Problem.canonical_solution`, which is per problem, while an instance is per (batch, problem). No gate caught it — the code-identity gate checks that the candidate is identical ACROSS the three conditions, and it was, identically wrong. It was found by the author reading the adjudication sheet by hand. Judge whether the repair is complete and whether the new check (`prove_candidate_is_the_instances.py`) actually closes the hole rather than appearing to.

**Binding.** `benchmarks/code/RESULTS-CLARIFY.md`; everything under `benchmarks/code/clarify/`; `benchmarks/code/records/clarify/*.json`; the readings at `~/Documents/Crossaudit/study-data/wt-clarify-runs/rows.jsonl` and the void ones beside them; the sheet, key and both raters' CSVs in `.../sheet/`; `plan/P3-PREREGISTRATION.md` and `manuscript/CLAIMS.md` in `~/Documents/Crossaudit/audit-ceiling-paper`.

**Verify, at least:**
1. Every rate, interval, and both p-values, recomputed independently from the rows, the key and the two rater CSVs — including whether the cluster sign-flip is implemented as the registration describes (flipping per PROBLEM, not per instance) and whether 10,000 resamples and the stated seed are what actually ran.
2. That the audited code is each instance's own: the readings must correspond to the frozen batch solutions, and the witness evidence shown on the sheet must belong to the same program. This is the defect that voided the first run.
3. That the three conditions differ ONLY in the specification — candidate and visible suite byte-identical per instance across arms — and that the specification actually reached the auditor under each condition.
4. The adjudication. Both raters' labels against the sheet; whether `L1` (the author) and `L2` (`gpt-6-astra`) are treated as the registration requires, with disagreement counting as not diagnosed; and whether the reported agreement (80 of 87, Cohen κ = 0.844) reproduces. **`L1` is the author and therefore not independent** — say whether the report's handling of that is adequate.
5. Whether the nine diagnosed instances are really on five problems, and whether the report's account of why McNemar and the sign-flip differ is correct.
6. The flat ladder: union at K = 1 equals union at K = 4 in every arm. Check it, and say whether it is what the data show or an artefact of how union at K is computed.
7. The leak check — 4 of 83 clarified findings reproducing half an added sentence — and whether the two metrics are described honestly.
8. Whether any sentence claims causality beyond what a within-instance intervention on 31 instances and 18 problems supports, and whether the manipulation check's unresolved contrast (clarified minus placebo determinacy, +18.8 points, interval −9.4 to +45.2) is given its proper weight rather than parked in a limits section.

**Two standing hazards in this programme.** First, a fix written to satisfy a reviewer is itself an unreviewed claim: of the review rounds cleared this month, most ended in refusing a repair rather than a measurement. Second, **several repairs erred toward modesty and were wrong for it** — a registration whose chronology its own repository contradicted, a publication prohibition a registered gate never imposed, a limitation credited to another study's work that the other study had not performed. Overstating a limit is not the safe direction. This report states many limits; check whether any is larger than the truth as well as whether any is smaller. Headings, titles and limits bullets are claims.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Do not modify any file. End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.


## What changed since the first review

Every finding was real. Each was verified against the records before anything moved.

**R1-M1, the blocking one.** Confirmed and acted on. Every clarification is now classified by
hand against its own oracle, and the table is published row by row in
`records/clarify/clarification_classification.json` so any row can be disputed: **7 state the
oracle's rule, 1 relaxes a stated precondition, 3 are right on some exercised inputs and wrong
on others, and 21 contradict the oracle.** The cross-tabulation with the outcome is
**7/7, 1/1, 1/3, 0/21**. The report's claim is narrowed accordingly and the registered contrast
is still reported as registered rather than replaced by its favourable half. Two caveats are
stated with it: the classification is post hoc, and the oracle-consistent instances may simply
be the easier problems.

**R1-M2.** Confirmed. `overlap()` never checked order — it asked whether each word appeared
anywhere, and a reversed sentence scored 1.00. `added_sentences()` folded the specification's
own assertions into the addition on 21 of 31. Both fixed; the counts are now **1/87 contiguous
and 39/87 vocabulary**, which match your independent recount of 1 and 39. A planted reversal
case was added that the old implementation fails. The heading claiming the clarification "is not
being read back" is gone.

**R1-M3.** Confirmed: all three "hidden" lines are printed in `b1:Mbpp/427`'s own specification
and visible tests. The leak gate now excludes public text, the instance is back, and the
population is **32 on 19 problems** — the same 32 the manipulation check used. The claim that a
different program cannot reproduce another's outputs is corrected: the frozen-source comparison
establishes identity, the witness agreement only consistency.

**R1-M4.** Confirmed and added. Amendment 2's secondary on the both-undetermined subgroup is
**23 instances on 15 problems, clarified 8/23 against original 0/23, +34.8 points
[+10.0, +60.9]**, sign-flip 0.0632. Amendment 9's three yields are reported together. Amendment
10's claim that no duplicate structure exists is corrected in the registration itself — 13
duplicate original specifications, 12 of 13 agreeing.

Headline on the corrected population: original **0/32**, clarified **9/32**, placebo **0/32**;
+28.1 points [+7.7, +51.4]; McNemar 0.0039; sign-flip **0.0602**. Agreement 84/91, κ 0.852.
Costs are split: \$2.13 for the discarded run and \$1.86 for this one.

Read adversarially, and weight the new classification table hardest — it is a hand judgement
published as data, and if any row is wrong the conclusion drawn from it is wrong.
