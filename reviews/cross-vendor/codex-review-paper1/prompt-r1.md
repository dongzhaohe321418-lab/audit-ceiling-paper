You are an INDEPENDENT REVIEWER from a different vendor, reviewing a whole MANUSCRIPT before arXiv submission: the repository `audit-ceiling-paper` at `306bd8d` (the directory you are in). Do not modify any file.

**What it is.** An empirical paper on what moves the recall of an automated code auditor, against hidden test suites executed by an interpreter. The manuscript is `tex/paper.tex` with `tex/sections/*.tex` and the generated `tex/table1.tex`; the compiled `tex/paper.pdf` is beside it. Its rule is that no number enters the paper unless it appears in `manuscript/CLAIMS.md` as an admitted claim, at the scope written there, from a study report that passed independent review.

**Sources you have.** `manuscript/CLAIMS.md` (the ledger, including a "must not appear" list and a pending table); `reports/RESULTS-*.md` (each study's report); `records/code/` (derived records); `reviews/` (every review, verbatim); `plan/` (registrations); `README.md` (an inventory mapping each claim to report, review and record); `reproduce.sh`. The harness that produced the records is at `~/Documents/Crossaudit/crossaudit_integ` (read-only for you) if you need to go further.

**This revision is large.** Run `git log --oneline 7a470d8..306bd8d` and `git diff 7a470d8..306bd8d -- tex manuscript` to see it. Every change in that range is itself an unreviewed claim. Judge it on the records, not on the commit messages.

**Verify, at least:**
1. Every number in `tex/`: that it is in CLAIMS.md as admitted, that it matches the report and the record it cites, and that the sentence around it claims no more — and no less — than CLAIMS.md licenses. Recompute where you can.
2. That nothing in CLAIMS.md's "must not appear" list, or in any admitted claim's own prohibitions, appears in `tex/` in substance, whatever the wording.
3. That `./reproduce.sh` does what the Reproducibility section says, from a clean state, and that the figures show what their captions say. Read the figure scripts against the records.
4. That every statement about process — preregistration, review rounds, exceptions, which model reviewed or rated what, licences, what the repository contains — is true of the repository and the reports.
5. Internal consistency: abstract, introduction, results, discussion, limitations and Table 1 saying the same thing about the same quantity.
6. Anything stale: text describing an experiment as not run that has run, a withdrawn study as present, or a corrected number in its old form.

**Standing hazards in this programme.** Checks have repeatedly claimed more than they delivered, and repairs have erred in BOTH directions — overstatement, and modesty larger than the truth. A heading, a caption, a title and a limitation are claims. You are also `gpt-6-astra` or a sibling model: `gpt-6-astra` is one of the auditor families the paper measures and a rater in two of its studies; where a sentence ranks or rates that family, say so if you think your judgement is conflicted.

Tooling: `python3` with matplotlib and scienceplots; `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src` for harness code. Do not modify any file. `reproduce.sh` writes figures, so run it only on a copy in a temporary directory; if your sandbox cannot write anywhere, read the scripts against the records instead and say plainly that you did not execute them.

List findings most severe first, each with file:line and the record that contradicts it. End with "submittable / not submittable" and the single most important reason.
