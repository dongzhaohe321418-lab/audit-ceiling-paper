**One required correction remains: the repair now falsely denies study 19’s adjudication.**

**R5-M1 — [RESULTS-SWEEP.md:178](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:178).** “No study 19 record adjudicates finding content either” and “work neither did” are false.

Study 19 is absent from this checkout, but its committed records exist at `92e0bc7` and in the local review worktree:

- [L1-h19d.csv](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/L1-h19d.csv) and [L2-h19d.csv](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/records/ceiling3b/L2-h19d.csv) each contain **190 adjudication labels**.
- [Study 19’s adjudication description](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:143) identifies the finding-content question, hidden-failure evidence and two labellers.
- Its [scope qualification](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/RESULTS-CEILING3B.md:235) explains the relevant limitation: the shipped-constitution adjudication used an **additional reading**, not study 18’s reused readings.

The correct distinction is **adjudication of different readings**, not **no adjudication**. This is another limitation overstated against another study’s work.

A sufficient replacement is:

> **Flag coverage is not naming.** This sweep re-grades counts without assessing finding content against the hidden failure. Study 18 did not archive or adjudicate its advisory texts; study 19 adjudicated separate readings, which does not establish what the findings re-graded here identified.

That change is required; no additional measurements or model readings are needed.

Otherwise, the three round-3 fixes hold. I found no further substantive contradiction in the report’s interpretation of C2, matched rates or the three `astra` contrasts. I also replayed the computation **in memory, stopping before its file write**: all 40 table rows and six paired contrasts, including their intervals, exactly match the record. All loaded draws contain 260 rows with both integer counts; none was dropped. The numerical record is byte-identical to the parent commit. No files were modified.

**Not quotable — the corrected paragraph still makes a false claim about study 19, whose committed finding-content adjudications exist.**
