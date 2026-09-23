**Not quite final at `67523e0`. The descriptive results are quotable now, but two concrete reporting/verification repairs remain. Neither requires another experiment.**

1. **The absent-Pandoc verification is incomplete.** In [test_inject_report.py:252](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:252), the purported skip-path test calls `pytest.skip()` directly; it never exercises `_rendered()` or the report check. The renderer-failure test also depends on Pandoc actually being installed. With discovery mocked absent, the report suite produces **1 failed, 11 passed, 1 skipped**.  
   **Required:** exercise the actual absence-to-skip path, and mock successful discovery in the renderer-failure test. Check its stderr too. The implementation’s actual skip path works—I verified it independently.

2. **The successor qualification has not reached §3.** [RESULTS-INJECT.md:285](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:285) still says the needed separation is what “study 23’s second substrate and a human rater would supply.” That assurance conflicts with the new, appropriately qualified §5.  
   **Required:** replace that assurance with a reference to §5’s fixed, blinded validation requirements, without promising that substrate/rater independence alone resolves the confounding.

**The binding’s abandonment is acceptable.** Hidden and struck-out passages still pass, exactly as its new limitation permits. I am not requiring another semantic binding or a browser check.

The substantive verification succeeded:

- `build()` and `render_tables()` reproduce both committed artifacts byte-for-byte in memory; the splice checks pass.
- Independently recovered **90/92**, **11/92**, **31/40**, **79/0** discordances, and the complete curve.
- Independently reproduced the weighted **84.1548%**, bootstrap **[73.7523, 93.1016]**, with the report’s calibration qualification retained.
- Probe counts, cross-tab, duplicated programmes, witness types, and paid-versus-filtered attempts match.
- Costs reconcile to **$18.36869975 retained** and **$18.52886775 across 4,794 distinct ledger events**, including the three stated differences.
- Amendment 7’s causal withdrawal and Tango’s independence qualification are adequate.

Nonblocking cleanup: the report introduction still says **five amendments** at line 27, and `_visible()` still calls itself a “fallback” despite the explicit no-fallback behavior. Shortening the accumulated review history would merely be an editorial preference.

With Pandoc installed, **13 report tests pass**. I cannot certify a green full suite here: the broader selection encountered read-only temporary-file failures and three statistics-test timeouts. No files were modified.

The naming adjudication and deferred gate can remain final omissions. **No further readings or new semantic denominator are required to finish this descriptive report.**

**Quotable descriptively / not quotable for C4:** the blocking observations reproduce, while specification entailment was not established.

Reader sentence:

> Across eight readings, the auditor blocked 90 of 92 gate-accepted injected variants, compared with 11 of their 92 unmodified twins; this describes a response to the edits, without establishing detection of specification-determined violations.
