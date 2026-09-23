You are an INDEPENDENT REVIEWER from a different vendor. FIFTH review of `RESULTS-RATE3.md` on branch `fusion/evidence-authority` at `4dfaa3f` (the worktree you are in). Do not modify any file.

**What this is.** The paper's plan asks P1 for a *human from outside the project* to re-rate, blind, whether a specification's prose determines what the hidden test expects — because the existing +22.4-point missed-against-caught contrast was rated by a model (`gpt-6-astra` as L2) and by the author (L1), and so supports the *direction* of claim C4 rather than its *independence*. No outside human has been recruited. What was run instead is a third **model** rating, `L3` = `gpt-6-astra`, on a sheet that was rebuilt today.

**No model calls are needed to check this.** The ratings are committed CSVs; the analysis is arithmetic over them. If any figure here would require a new call, the report is wrong about its own provenance.

**Claimed.** Primary: items labelled `undetermined`, missed 43/68 = 63.2% against caught 23/53 = 43.4%, difference **+19.8 points**, problem-cluster percentile bootstrap [+1.5, +38.2], 10,000 resamples, seed 20260922, `cannot-tell` counted in the denominator and not the numerator. Secondary excluding `cannot-tell`: +22.6 [+2.1, +42.6]. Exploratory: the *unanswerable* version of the same sheet, rated by the same model earlier the same day, gives **+54.2 points** [+38.8, +69.8] — 2.7x the repaired contrast, in the direction that flatters C4 — because 42 of 53 caught items were rated `cannot-tell` there against 5 here.

**The analysis was registered before it was run, with the ratings already collected.** `plan/P1-ANALYSIS-REGISTRATION.md` in the paper repo says so in its first paragraph and states what was and was not seen beforehand. Judge whether that registration is honest about its own weakness, and whether the analysis actually follows it — in particular the `cannot-tell` rule, which was fixed before the arms' rates were computed and which moves the headline by 2.7 points.

**Binding.** `benchmarks/code/RESULTS-RATE3.md`, `benchmarks/code/rate3/analyse.py`, `benchmarks/code/rate3/rebuild_sheet.py`, `benchmarks/code/records/rate3/{L3.csv,L3-broken-sheet.csv,analysis.json}`, the sheet key at `~/Desktop/CrossAudit-审计天花板/人类评分任务/_items.json`, `benchmarks/code/RESULTS-RERATE.md` for the six-category comparator, `plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md` in `~/Documents/Crossaudit/audit-ceiling-paper`.

**Verify, at least:** (1) every rate and interval, recomputed independently from the CSVs and the key, with the stated seed and resample count, and whether the clustering is on the right unit; (2) whether the primary's `cannot-tell` treatment is defensible or merely convenient, given that it is the treatment under which the contrast is *smaller*; (3) whether the report is right that the six-category rating and the three-option rubric are different instruments, and whether it anywhere leans on the closeness of +22.4 to +22.6 after saying that closeness is worth nothing; (4) the exploratory broken-sheet reading — whether "evidence about sheets, not about specifications" is the correct scope, and whether any sentence smuggles it back as evidence about specifications; (5) whether the rebuilt sheet is genuinely symmetric between arms, since the repair added failing inputs to both and an asymmetric repair would manufacture the contrast it measures; (6) whether the report's refusal to claim independence is carried through every sentence, or whether some sentence quietly claims it back.

**Two standing hazards in this programme, stated so you can look for them.** First, a fix written to satisfy a reviewer is itself an unreviewed claim: of thirty-eight review rounds cleared this month, most ended in refusing a repair rather than a measurement — and in the report next door, two successive repairs of one paragraph each introduced a new false statement about another study's work. Second, **several repairs erred toward modesty and were wrong for it**: overstating a limitation is not the safe direction. This report states many limits; check whether any is larger than the truth as well as whether any is smaller.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Do not modify any file. End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.


## What changed since the fourth review

All five findings were real and each was checked against the records first.

1. **"Count identically in every table below" was false of the abstention-excluded rows**, where
   `cannot-tell` leaves the denominator rather than collapsing into agreement. Verified: 7 pairs
   survive with no abstention and 5 agree. Three numbers now stand for three analyses — 7/11 on
   the primary binary outcome, 5/11 on the full label, 5 of 7 abstention-free — each qualifying
   only its own, all on 6 problems.
2. **Table 2's heading** no longer claims a publication ban. It says what the gate did.
3. **The docstring's new distinction was also wrong.** It now states the supportable one —
   determinacy without a supplied target against entailment of a supplied target, which is what
   the comparator asked — and names both of its own earlier overstatements.
4. **"The Wilson intervals are wider still" was false.** Verified: 22.3 and 25.8 points against
   31.0 and 36.1. Corrected, and the report now says they are intervals for different quantities.
5. **Emphasis.** The title, the opening quotation and the limits bullet all lead with the
   primary's 7 of 11. "No figure in this report" is scoped to the rebuilt-sheet rows and exempts
   the comparator.

`CLAIMS.md`'s row carries all three consistency numbers with their scopes.

Read adversarially. Five versions of this report have had arithmetic you reproduced exactly, and
every refusal has been about what the prose claims that arithmetic licenses. **Six of those
errors were overstatements toward modesty or alarm rather than in my favour**, so weight both
directions, and treat headings, titles and limits bullets as claims rather than as packaging --
two of the last four findings were exactly that.
