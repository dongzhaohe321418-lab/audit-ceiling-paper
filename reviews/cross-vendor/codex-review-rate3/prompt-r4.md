You are an INDEPENDENT REVIEWER from a different vendor. FOURTH review of `RESULTS-RATE3.md` on branch `fusion/evidence-authority` at `5c87e4c` (the worktree you are in). Do not modify any file.

**What this is.** The paper's plan asks P1 for a *human from outside the project* to re-rate, blind, whether a specification's prose determines what the hidden test expects — because the existing +22.4-point missed-against-caught contrast was rated by a model (`gpt-6-astra` as L2) and by the author (L1), and so supports the *direction* of claim C4 rather than its *independence*. No outside human has been recruited. What was run instead is a third **model** rating, `L3` = `gpt-6-astra`, on a sheet that was rebuilt today.

**No model calls are needed to check this.** The ratings are committed CSVs; the analysis is arithmetic over them. If any figure here would require a new call, the report is wrong about its own provenance.

**Claimed.** Primary: items labelled `undetermined`, missed 43/68 = 63.2% against caught 23/53 = 43.4%, difference **+19.8 points**, problem-cluster percentile bootstrap [+1.5, +38.2], 10,000 resamples, seed 20260922, `cannot-tell` counted in the denominator and not the numerator. Secondary excluding `cannot-tell`: +22.6 [+2.1, +42.6]. Exploratory: the *unanswerable* version of the same sheet, rated by the same model earlier the same day, gives **+54.2 points** [+38.8, +69.8] — 2.7x the repaired contrast, in the direction that flatters C4 — because 42 of 53 caught items were rated `cannot-tell` there against 5 here.

**The analysis was registered before it was run, with the ratings already collected.** `plan/P1-ANALYSIS-REGISTRATION.md` in the paper repo says so in its first paragraph and states what was and was not seen beforehand. Judge whether that registration is honest about its own weakness, and whether the analysis actually follows it — in particular the `cannot-tell` rule, which was fixed before the arms' rates were computed and which moves the headline by 2.7 points.

**Binding.** `benchmarks/code/RESULTS-RATE3.md`, `benchmarks/code/rate3/analyse.py`, `benchmarks/code/rate3/rebuild_sheet.py`, `benchmarks/code/records/rate3/{L3.csv,L3-broken-sheet.csv,analysis.json}`, the sheet key at `~/Desktop/CrossAudit-审计天花板/人类评分任务/_items.json`, `benchmarks/code/RESULTS-RERATE.md` for the six-category comparator, `plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md` in `~/Documents/Crossaudit/audit-ceiling-paper`.

**Verify, at least:** (1) every rate and interval, recomputed independently from the CSVs and the key, with the stated seed and resample count, and whether the clustering is on the right unit; (2) whether the primary's `cannot-tell` treatment is defensible or merely convenient, given that it is the treatment under which the contrast is *smaller*; (3) whether the report is right that the six-category rating and the three-option rubric are different instruments, and whether it anywhere leans on the closeness of +22.4 to +22.6 after saying that closeness is worth nothing; (4) the exploratory broken-sheet reading — whether "evidence about sheets, not about specifications" is the correct scope, and whether any sentence smuggles it back as evidence about specifications; (5) whether the rebuilt sheet is genuinely symmetric between arms, since the repair added failing inputs to both and an asymmetric repair would manufacture the contrast it measures; (6) whether the report's refusal to claim independence is carried through every sentence, or whether some sentence quietly claims it back.

**Two standing hazards in this programme, stated so you can look for them.** First, a fix written to satisfy a reviewer is itself an unreviewed claim: of thirty-eight review rounds cleared this month, most ended in refusing a repair rather than a measurement — and in the report next door, two successive repairs of one paragraph each introduced a new false statement about another study's work. Second, **several repairs erred toward modesty and were wrong for it**: overstating a limitation is not the safe direction. This report states many limits; check whether any is larger than the truth as well as whether any is smaller.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Do not modify any file. End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.


## What changed since the third review

All five findings were real; each was verified against the records before anything changed.

1. **Consistency scope.** Verified: 5/11 on the three-option label, **7/11 on the binary outcome
   the contrasts are built from**, 11 pairs on **6 problems**, and 55 of 81 identical-text pairs
   agreeing. The report now leads with 7/11, gives 5/11 second, discloses the 6 problems, and
   marks the 81-pair figure as dependent rather than a second estimate. The apportionment
   sentence is withdrawn outright. I also verified and added what you implied: `L1` and `L2` each
   agreed with themselves **11 of 11** on the same instances, on a different instrument.
2. **The gate.** Verified against Amendment 1's wording: inconclusive, decision waits for P1.
   The report now says only that the broken result could not have authorised proceeding under
   the registered positive branch, and names "could not have been published" as the third
   overcorrection toward modesty in this report's history.
3. **Blanket qualifications.** Restricted to the four rebuilt-sheet contrasts (+1.2, +2.0, +2.4,
   +4.8), in both the table prose and the limits list; the consistency caveat is withdrawn from
   the six-category row.
4. **The abstention-excluded secondary** is now labelled post hoc in the provenance section, the
   table and the limits. Verified: Amendment 1 contains no such secondary.
5. **`rebuild_sheet.py`'s anchoring claim** is replaced with what is supportable — showing a
   value changes the question asked — and says the anchoring effect is unmeasured here.

Both synchronisation issues are fixed: "before the **rebuilt** ratings", and `CLAIMS.md`'s row
now carries [+2.0, +43.6], drops its own "not registered in advance" overcorrection, and states
the 7-of-11 constraint.

Read adversarially. Four versions of this report have had correct arithmetic; the failures have
all been in what the prose claims the arithmetic licenses, and **four of them were overstatements
in the direction of modesty or alarm** rather than in my favour. Weight both directions.
