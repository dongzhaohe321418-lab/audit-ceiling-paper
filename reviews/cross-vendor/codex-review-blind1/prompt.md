You are an INDEPENDENT REVIEWER from a different vendor. Review `RESULTS-RATE3.md` on branch `fusion/evidence-authority` at `8f66bab` (the worktree you are in). Do not modify any file.

**This prompt deliberately tells you nothing about what the report claims, what any figure is, or what any previous review concluded.** That is the point of this particular dispatch, and it is not an oversight: read the report and the records and form your own account of what is established.

**What the study is.** Instances of a code benchmark on which a cross-vendor auditor was run. Each instance carries a specification, a candidate implementation, a visible test suite the candidate passes, and a hidden suite it fails. Some instances were flagged by the auditor and some were not. A rating sheet asks a rater, for each instance, whether the specification's prose determines what should be returned on the inputs where the hidden suite fails. `RESULTS-RATE3.md` reports a rating of that sheet.

**Binding artefacts.** `benchmarks/code/RESULTS-RATE3.md`; `benchmarks/code/rate3/`; `benchmarks/code/records/rate3/{L3.csv,L3-broken-sheet.csv,analysis.json}`; the sheet key at `~/Desktop/CrossAudit-审计天花板/人类评分任务/_items.json`; `benchmarks/code/RESULTS-RERATE.md`; and in `~/Documents/Crossaudit/audit-ceiling-paper`, `plan/P3-PREREGISTRATION.md`, `plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md`.

**Your task, in this order.**

1. **Before reading the report's numbers, compute your own.** From the CSVs and the key, work out what the sheet's groups are, what each group's rates are, and what any contrast between them is, with whatever interval you judge appropriate for the dependence structure you find. Write those down first.
2. **Then read the report** and say where it agrees with you and where it does not.
3. **Say what the study establishes** — in your own words, at the scope you judge the evidence supports.
4. **Say what is wrong with it.** Anything: the population, the provenance, the instrument, the prose, the limits, the headings.

**Two things worth knowing about this programme, stated because they are about failure modes rather than about this report's content.** Checks here have repeatedly claimed more than they delivered — a digest that froze a defect as faithfully as a fix, a test named for a code path that never called it, a gate satisfied by the very defect it was built to catch. And several repairs erred *toward* modesty and were wrong for it, so a limitation larger than the truth is as much a finding as a limitation smaller than it.

Tooling: `~/Documents/Crossaudit/crossaudit_integ/.venv/bin/python` with `PYTHONPATH=src`. Do not modify any file. End with "quotable / not quotable" and the single most important reason.
