You are an INDEPENDENT REVIEWER from a different vendor. SECOND review of the whole manuscript in the repository `audit-ceiling-paper` at `93615fd` (the directory you are in). Do not modify any file.

Round 1 reviewed `306bd8d` and returned **not submittable** with fifteen findings; it is archived at `reviews/cross-vendor/codex-review-paper1/report-r1.md`. The author's account of what was done for each is the last section of `reviews/presubmission/MASTER-TRACKER.md`. Treat that account as a set of claims to check, not as fact. The changes are `git diff 306bd8d..93615fd`.

**Do three things.**

1. **Each round-1 finding: is it actually fixed?** Check the repaired text against the records, and check that each repair did not introduce a new error or overcorrect. A repair is itself an unreviewed claim; in this programme most refusals have been of repairs.

2. **Rule explicitly on `reports/RESULTS-DERIVED.md`.** It writes up the quantities round 1 found in `tex/` without admission: the six-family residual composition (43 of 68; 25 of 32 = 78.1%) and the bootstrap coverage table. Recompute them from `records/code/` and `records/coverage_simulation.json` (the coverage command is in `reproduce.sh` and takes about a minute), and end that part with **quotable / not quotable** for each of its two sections. If not quotable, the numbers leave the paper.

3. **One point the author raised, not round 1:** the results and C13 now say the clarification study's registered bootstrap criterion was close to guaranteed by construction, because every discordant pair points one way. Check that reasoning and the figure of about 0.003 for a resample missing all five success-bearing problems, and say whether the paper now gives the result the weight it can bear — neither more nor less.

Then read the whole paper once more as a referee would, for anything round 1 did not reach. `./reproduce.sh` is described in the Reproducibility section; run it on a copy if your sandbox allows, and say plainly if it does not.

You are `gpt-6-astra` or a sibling; that family is measured in this paper and is one of the clarification study's two adjudicators and its reviewer. Say where that conflicts your judgement.

Tooling: `python3` with matplotlib and scienceplots; `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src` for harness code. Findings most severe first, each with file:line and the record that contradicts it. End with **submittable / not submittable** and the single most important reason.
