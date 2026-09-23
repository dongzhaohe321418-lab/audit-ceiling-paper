You are an INDEPENDENT REVIEWER from a different vendor. THIRD review of `RESULTS-RATE3.md` on branch `fusion/evidence-authority` at `eac2842` (the worktree you are in). Do not modify any file.

**What this is.** The paper's plan asks P1 for a *human from outside the project* to re-rate, blind, whether a specification's prose determines what the hidden test expects — because the existing +22.4-point missed-against-caught contrast was rated by a model (`gpt-6-astra` as L2) and by the author (L1), and so supports the *direction* of claim C4 rather than its *independence*. No outside human has been recruited. What was run instead is a third **model** rating, `L3` = `gpt-6-astra`, on a sheet that was rebuilt today.

**No model calls are needed to check this.** The ratings are committed CSVs; the analysis is arithmetic over them. If any figure here would require a new call, the report is wrong about its own provenance.

**Claimed.** Primary: items labelled `undetermined`, missed 43/68 = 63.2% against caught 23/53 = 43.4%, difference **+19.8 points**, problem-cluster percentile bootstrap [+1.5, +38.2], 10,000 resamples, seed 20260922, `cannot-tell` counted in the denominator and not the numerator. Secondary excluding `cannot-tell`: +22.6 [+2.1, +42.6]. Exploratory: the *unanswerable* version of the same sheet, rated by the same model earlier the same day, gives **+54.2 points** [+38.8, +69.8] — 2.7x the repaired contrast, in the direction that flatters C4 — because 42 of 53 caught items were rated `cannot-tell` there against 5 here.

**The analysis was registered before it was run, with the ratings already collected.** `plan/P1-ANALYSIS-REGISTRATION.md` in the paper repo says so in its first paragraph and states what was and was not seen beforehand. Judge whether that registration is honest about its own weakness, and whether the analysis actually follows it — in particular the `cannot-tell` rule, which was fixed before the arms' rates were computed and which moves the headline by 2.7 points.

**Binding.** `benchmarks/code/RESULTS-RATE3.md`, `benchmarks/code/rate3/analyse.py`, `benchmarks/code/rate3/rebuild_sheet.py`, `benchmarks/code/records/rate3/{L3.csv,L3-broken-sheet.csv,analysis.json}`, the sheet key at `~/Desktop/CrossAudit-审计天花板/人类评分任务/_items.json`, `benchmarks/code/RESULTS-RERATE.md` for the six-category comparator, `plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md` in `~/Documents/Crossaudit/audit-ceiling-paper`.

**Verify, at least:** (1) every rate and interval, recomputed independently from the CSVs and the key, with the stated seed and resample count, and whether the clustering is on the right unit; (2) whether the primary's `cannot-tell` treatment is defensible or merely convenient, given that it is the treatment under which the contrast is *smaller*; (3) whether the report is right that the six-category rating and the three-option rubric are different instruments, and whether it anywhere leans on the closeness of +22.4 to +22.6 after saying that closeness is worth nothing; (4) the exploratory broken-sheet reading — whether "evidence about sheets, not about specifications" is the correct scope, and whether any sentence smuggles it back as evidence about specifications; (5) whether the rebuilt sheet is genuinely symmetric between arms, since the repair added failing inputs to both and an asymmetric repair would manufacture the contrast it measures; (6) whether the report's refusal to claim independence is carried through every sentence, or whether some sentence quietly claims it back.

**Two standing hazards in this programme, stated so you can look for them.** First, a fix written to satisfy a reviewer is itself an unreviewed claim: of thirty-eight review rounds cleared this month, most ended in refusing a repair rather than a measurement — and in the report next door, two successive repairs of one paragraph each introduced a new false statement about another study's work. Second, **several repairs erred toward modesty and were wrong for it**: overstating a limitation is not the safe direction. This report states many limits; check whether any is larger than the truth as well as whether any is smaller.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Do not modify any file. End with "quotable / not quotable" and the single most important reason; if quotable, one reader sentence.


## What changed since the second review

All four findings were real and were verified against the records before anything was changed.

1. The "disjoint, cannot-tell excluded" row was the overlapping computation under a disjoint
   label. Fixed: 38/51 against 23/48, +26.6 [+4.8, +48.4], 52 clusters, and the move on the
   disjoint population is +3.3 points.
2. The withdrawal had overcorrected. `d5919b9`, 2026-09-21 20:24:05, registered the rubric, the
   all-entries denominator, the cluster bootstrap, 10,000 resamples, seed 20260921, Wilson, and
   the one-third `cannot-tell` gate. Both the report and the withdrawal notice now separate
   three things: registered in advance, falsely-described later registration, and never
   registered at all.
3. "The overlap affects them equally" is gone: +3.43 against +3.15, ratio 2.47x disjoint against
   2.73x on sheet groups.
4. "One analysis away from being quoted" is gone. The registered gate fires at one-third and the
   broken sheet's caught arm was 79.2%.

**I also found something in your round-2 note that neither of my versions had reported, and it
now leads the report:** the 11 duplicated instances are the same specification text and the same
witness display, rated twice in one pass, and **the rater agreed with itself on 5 of 11.**
Everything in the report is now stated under that constraint. Test whether it is stated strongly
enough, and whether any figure is still quoted as though the instrument were stable.

One more self-reported deviation: a draft ran at seed 20260922 rather than the registered
20260921. Every figure is now at the registered seed, and the point estimates are unchanged
while the interval endpoints move by a few tenths.

Not repaired, deliberately: H003/H117's escaped-newline rendering, because the sheet is the
artefact that was rated. `rebuild_sheet.py`'s "same information content" claim is corrected.

Read adversarially. Three versions of this report have now had correct arithmetic and wrong
prose, and two of the wrong things were overstatements in the direction of modesty.
