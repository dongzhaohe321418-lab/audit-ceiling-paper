**§5’s reconstruction correction survives both demonstrations, but the withdrawal remains incomplete elsewhere.**

Using in-memory substitutions only:

| Demonstration | Result |
|---|---|
| Empty study-17 `rows.jsonl` | 43 passed; the suite never reads it |
| Set A’s `right_failing_retained.k` to `999` | 43 passed |
| Change the results prose “A 79” to “A 999” | 43 passed |

The revised [§5](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/RESULTS-TESTGEN-VAL.md:264) now accurately separates independent reconstruction from automated table comparisons and selected string checks. These demonstrations no longer contradict that paragraph.

Three surviving claims prevent accepting the repair as complete:

1. **The targeted docstring still promises renderer state.** [_scan’s opening sentence](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/tests/test_testgen_val.py:205) remains: “Every line with the state a renderer would be in.” The newly added paragraph says it is **not** renderer-equivalent. The repair appended a withdrawal but left the original promise intact.

2. **Blanket figure protection remains asserted.** [splice_tables.py](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/testgen/splice_tables.py:5) says “a figure edited in the results file … fails.” [render_tables](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/testgen_val.py:637) similarly says “a figure cannot be edited in the prose file and survive.” The third demonstration directly disproves both as written. The guarantee covers generated block contents, not every figure.

3. **Unqualified heading and fence guarantees remain.** The [HEADINGS comment](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/testgen/splice_tables.py:46) still says a subheading cannot place a table under an unregistered caption. The [placement-test docstring](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/tests/test_testgen_val.py:301) still promises that no marker sits in a fence or blockquote. These describe rendered properties more broadly than the scanner establishes, including categories the revised text explicitly acknowledges remain open.

These require consistent wording about **recognized source lines and marked blocks**. They do not require further Markdown hardening. I invented no rendering mutations.

The measurement remains intact:

- Both archive manifests and all three copied study-16 input hashes verify. Replay from archived outcome records reproduced `numbers.json`, `exploratory.json`, and `tables.md` byte for byte. Independent Wilson/bootstrap calculations matched all **66 rate blocks**.
- Independent aggregation reproduced **A 11/90, B 15/101, C′ 11/86**, retaining **5, 6, 5 of seven**. All remain killed. Complete numerical records are unchanged from round 4.
- Preregistration contains the primary redefinition, comparator baseline, selection order and kill. The earliest inferred request was **22:46:34.725**, after the **22:46:23** implementation commit. Rules consume candidate-failure sets; execution uses study 16’s path.
- The **29/1,188 floor**, **23/32 versus 13/189** recurrence comparison, **13/222 and 8/222** response identity, retry and **$3.3493315** spend reproduce. “Marginal prevalence” correctly describes 16.7%. The first two sections’ quantitative claims remain supported.

All 46 selected tests were attempted: **43 passed; three failed because temporary directories are unavailable**. This does not certify normal-host executor execution. Protected implementation paths are unchanged; I found no committed generated test text and modified no files.

**not quotable — the most important reason is that the withdrawal remains half-applied: surviving documentation still promises rendering and figure protection the tests do not establish.**
