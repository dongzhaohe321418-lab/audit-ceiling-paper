The numerical result reproduces, but the report needs corrections before quotation. I reviewed HEAD `24827b8` without changing files; the checkout is named `fusion/evidence-authority`, rather than `study/fpadj`.

Before reading the report, I independently obtained:

| Outcome | Recomputed result |
|---|---:|
| D / A / N | **2 / 9 / 9** |
| Primary D share | **10.0%** |
| Problem-cluster 95% interval, seed 20260924 | **[0.0%, 26.3158%]** |
| Wilson interval | **[2.7866%, 30.1034%]** |
| Union false-positive rate | **20/150 = 13.3333%** |
| Union problem-cluster interval | **[7.9470%, 19.2053%]** |

The report correctly follows the registration’s interval-includes-zero branch. That procedural reading does not erase the two observed disagreements, which the report also acknowledges.

The underlying records check out:

- All **150 candidates** match ceiling 1’s candidate hashes; the population is 77 b1, 73 b2, over 143 problems.
- Each draw contains exactly 150 successful readings. All **1,200 captured rows** match their cached finding hashes, lengths, flags and run IDs. All 1,200 prompt hashes match ceiling 1’s corresponding prompts. The archived constitution and configurations match the specified route.
- All 70 extraction prompt hashes reconstruct correctly. I found no reference-only material under the implemented leak check.
- I replayed every distinct literal candidate/reference input pair in read-only subprocesses and checked every execution row’s classification and output hashes. **Every D, A and N classification reproduces.**
- The D witnesses are `Mbpp/245([-1])`: candidate **0**, reference **−1**; and `Mbpp/123(12285)`: candidate **53226**, reference **65511**. Neither input occurs in its hidden suite. Both candidates still pass their complete hidden suites—104 and 103 cases respectively—using the benchmark’s configured suite interpreter.

These are the findings requiring attention:

1. **The closing explanation is not supported by the adjudication.** [RESULTS-FPADJ.md:69](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-FPADJ.md:69) says these findings land in A or N “by construction, because the candidate and the reference agree.” Agreement is an empirical result, not a consequence of a finding discussing tests or documentation; N establishes no agreement at all. Some alleged inconsistencies are also demonstrably mistaken: the `HumanEval/146` finding claims the candidate returns 4 on the documented example, whereas both implementations return 2. Moreover, 28 of the 70 findings come from just two instances. A qualitative description of repeated findings should not imply an established explanation of the instance-level flag rate.

2. **N is misdescribed as findings that “name no executable input.”** [RESULTS-FPADJ.md:35](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-FPADJ.md:35) conflates absence of an input with rejection by the extraction/execution procedure. Three N instances have eight concrete extracted expressions rejected as non-literals. I reproduced the sensitivity: five make the reference raise; three return `None` from both implementations, moving `HumanEval/20` from N to A. D remains 2. Likewise, line 24’s statement that both programs executed on all 87 inputs is inaccurate: **79 were executed; eight were rejected before execution**.

3. **The broader extraction review finds additional limitations.** I read all 70 findings and extractions, exceeding the author’s twenty. Archive [extractions.jsonl:31](/Users/ericdong/Documents/Crossaudit/study-data/wt-fpadj-runs/extractions.jsonl:31) extracts the two-character strings backslash-plus-`t` and backslash-plus-`n`, rather than the tab and newline named by the finding. This does not change A because both implementations behave identically, and other findings supply the actual whitespace inputs. The empty-list omission also recurs outside the author’s sample. The reported “parse failure” is an **empty reply with null cost**, not malformed nonempty JSON; another finding covers its input. All 69 nonempty replies parsed without truncation or type coercion.

4. **The blindness claim is stronger than the implementation.** [RESULTS-FPADJ.md:22](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-FPADJ.md:22) says the extractor never saw “any expected output,” but specifications, candidate docstrings and findings plainly contain expected-output assertions. The defensible claim is that no reference solution, hidden tests or separately supplied reference outputs were provided. Also, [the leak check](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/fpadj/adjudicate.py:102) tests only reference lines at least 20 characters long that are absent from the specification and candidate—not the registration’s literal “no line” assertion. All implemented checks pass; that narrower scope should be disclosed.

5. **Process and cost reporting need reconciliation.** The incomplete audit stopped with 49 missing readings, and the rerun filled exactly those readings; the failure records support provider/cooldown failures. However:
   - The audit ledger totals **$4.19887425**, not $4.16. The report omits the six-reading pilot’s **$0.0427325**.
   - Reused run IDs across retry passes inflate summed cached costs to **$5.7226745**. Use the ledger total.
   - The audit budget resets per invocation. Extraction uses locally calculated prices rather than the registered usage-ledger accounting, omits earlier retry costs, and permits an empty unpriced reply to continue. These guards do not implement the registered per-call fail-closed promise, although recorded audit spending stayed below $12.
   - The supplied archive does not independently document the claimed first extraction halt.
   - Amendment 1 predates the adjudication implementation commit. At the amendment’s **commit time**, however, 57 readings and two flagged instances had already landed. Its “six readings, none flagged” statement is labelled “known when written”; distinguish that writing-time claim from the verifiable commit-time state.

The registered **per-finding secondary rates are missing** from the report. Applying the same classification rule gives D **3/70 (4.3%)**, A **47/70 (67.1%)**, N **20/70 (28.6%)**.

Finally, the equality function works for every observed output here, but does not universally implement its advertised rule: `same("nan", "nan")` returns true, and `same("1.0", "'1'")` also returns true. Neither affects this dataset.

**not quotable — the report turns a reproducible, narrowly defined output comparison into unsupported claims about what the flags mean, especially through its N description and “by construction” closing explanation.**
