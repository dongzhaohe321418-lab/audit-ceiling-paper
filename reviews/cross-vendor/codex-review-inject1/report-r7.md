**The descriptive measurements survive. The binding fails again, and I would not mark `5e497fb` final yet.** The remaining work is reporting and verification work; it does not require another experiment or a new C4 denominator.

I changed no files.

1. **The “rendered” binding still checks a weaker representation than the reader’s document.**  
   At [test_inject_report.py:63](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:63), Pandoc produces **plain text**, which discards presentation semantics.

   I replaced the complete §2 withdrawal, in memory, with:

   ```html
   <span hidden>**What this licenses about C4 is nothing, and that is the finding.**</span>
   **The study confirms C4 prospectively.**
   ```

   **All 11 report tests passed.** Pandoc’s plain output contains both sentences. Its HTML output retains the `hidden` attribute, hiding the withdrawal while displaying the endorsement. A second mutation using `<del>…</del>` also passed all 11: the withdrawal becomes struck-out prose, but the binding treats it as an unchanged assertion.

   I verified the Pandoc plain and HTML outputs; browser automation timed out, so I am not claiming screenshot verification.

   **Recommendation: abandon the semantic guarantee, retain the useful regression check.** Describe it as: “These selected strings must occur in Pandoc’s normalized plain-text output. This does not establish visibility, assertion status, or consistency of the document’s conclusions.” Arbitrary prose cannot acquire that stronger guarantee from substring matching. A browser check could catch particular visibility failures, but it would still not establish the withdrawal’s meaning.

2. **The missing-pandoc path does not skip.**  
   [Line 190](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:190) calls `pytest.skip`, but this module never imports `pytest`. Exercising that path raises:

   ```text
   NameError: name 'pytest' is not defined
   ```

   This fails closed; it does not silently weaken the check. Nevertheless, the stated behavior is false. Import `pytest`, test the absent-tool path, and distinguish absence from a nonzero Pandoc exit: renderer failure should report its error, not be described as “pandoc is not installed.”

3. **Amendment 7 retains the probe inference the latest repair intended to remove.**  
   [Lines 417–424](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject/PREREGISTRATION.md:417) say the construction concentrates conspicuous edits, then call the probe result a measured “consequence” and “the same phenomenon seen from the other side.”

   Adding “some feature the probe does not identify” does not justify that causal connection. Task composition alone could produce the classification result. Replace those claims with: the proposed construction mechanism remains compatible with the observations; the probe neither identifies nor verifies it. If preserving this paragraph historically, put that correction immediately beside it.

4. **The paired table still promotes an independence-based interval beyond its demonstrated scope.**  
   [RESULTS-INJECT.md:153](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:153) says Tango is “the one to read.” Its calculation uses `(79, 0, 92)`; it does not account for the 54 problem clusters or duplicated programmes. Ceiling 1’s cited Amendment 5 explicitly says its coverage exercises used independent instances and did not validate the clustered design.

   Keep the cluster interval, disclose its coverage limitation, and label Tango as an independence-based sensitivity calculation. No new simulation is necessary to finish a **descriptive** report if no calibrated clustered coverage is claimed.

The numerical reconstruction is sound:

| Check | Independently reproduced |
|---|---|
| Injected population | 90/92 blocked |
| Unmodified twins | 11/92 blocked |
| Discordance | 79 injected-only; 0 twin-only |
| Paired difference | +85.8696 points; cluster interval [77.2727, 93.2584] |
| Gate-rejected sample | 31/40; cluster interval [62.2222, 90.4762] |
| Weighted estimate | 84.154804%; historical bootstrap interval [73.7523, 93.1016] |
| Subset-averaged curve, K = 1…8 | 94.4, 96.5, 97.0, 97.4, 97.6, 97.7, 97.8, 97.8% |
| Probe | 147/152 parsed classifications correct; 32 unparsed |
| Probe bounds over 184 items | 79.8913%–97.2826% |
| Cross-tab | Edited 63/65; ONEPASS 4/4; unparsed 23/23 blocked |
| Uniform-placement calculation | 8.5523%; expected count 0.0869565 |

The two misses are exactly the two instances of `Mbpp/404`. Fisher’s two-sided p is 1.0 both for edited versus all other classifications and for the answered-only comparison. The report’s uniform-placement and clustering qualifications are correct. Neither calculation adjudicates the proposed mechanisms.

The weighted estimator is appropriate for the **281 filter-accepted instances**, under the sampling protocol. Its historical interval reproduces; reproducibility does not establish finite-population coverage. The report now correctly acknowledges that I was measured completely, 40/189 rejected instances were sampled without replacement, and `Mbpp/614` crosses the sampled strata.

Duplication also checks out: I contains 59 programmes over 54 problems, with 33 duplicate groups covering 66 instances; none crosses a problem boundary. The rejected sample contains 35 programmes over 35 problems, with five within-problem duplicate pairs. Resampling whole problems preserves those duplicate groups. That establishes the resampling behavior, not a general coverage guarantee.

The cost reconciliation is correct:

| Component | USD |
|---|---:|
| Retained construction | 9.582760 |
| Main audit invocation | 6.255886 |
| Probe | 0.633535 |
| Gate-rejected readings | 1.89651875 |
| **Retained subtotal** | **18.36869975** |
| **4,794 distinct ledger events** | **18.52886775** |

The difference is exactly **$0.160168**: $0.110073 construction, $0.049900 earlier audit invocation, and $0.000195 route probe.

The 2,292 paid attempts and 2,135 reaching filters are correct **for the retained injection archive**. The project ledgers contain 2,326 injection events including earlier construction work. One provenance caution: the original injected/twin caches reuse 644 run IDs, so blindly summing both arms’ per-row `cost_usd` overcounts. The $6.255886 invocation total is supported by the ledger and manifest.

The filter account is substantially accurate. F6 is exactly the truthiness check described; the 179-string/102-list split reproduces. F2, F3, F4 and F5 have the implementation gaps listed in §5. F4 also enforces the positive, at-most-four-added/deleted-lines condition; none of these checks connects specification entailment to the actual failure.

For the requested spot checks, I sampled with seed **20260921**. These are reviewer judgments about the retained code, not a replacement population adjudication.

| Accepted instance(s) | Would admit as a specification-relevant defect? |
|---|---|
| `b1:Mbpp/62` | Yes: ignores the last list element when finding the minimum. |
| `b1:HumanEval/29`, `b2:HumanEval/29` | Yes: substring membership replaces prefix matching. |
| `b1:Mbpp/441` | Yes: wrong cube surface area below side length 3. |
| `b1:Mbpp/111` | Yes for disjoint, nonempty lists; the named class needs narrowing and the witness argument structure is wrong. |
| `b1:HumanEval/35` | Yes: returns the singleton value minus one. |
| `b1:Mbpp/89`, `b2:Mbpp/89` | Yes: returning n is not returning a smaller number. |
| `b1:Mbpp/292` | Yes: truncation replaces downward rounding. |
| `b2:HumanEval/117` | Yes: removes required repeated word occurrences. |
| `b2:HumanEval/0` | Yes: equality is admitted despite the strict threshold. |
| `b2:HumanEval/123` | Yes: removes required output sorting. |
| `b1:Mbpp/775` | Yes: checks only the first odd position; recorded witness lacks the argument-list wrapper. |
| `b2:Mbpp/809` | Yes: equality replaces “smaller.” |
| `b1:HumanEval/9` | Yes: zero initialization breaks negative rolling maxima; witness lacks the argument-list wrapper. |

For rejected instances, `last_code` is retained using `setdefault`, so it is the **first retained rejected candidate**, not necessarily the last attempt. The archive does not support reviewing every rejected attempt’s code.

| Filter-rejected instance(s) | Judgment on retained candidate |
|---|---|
| `b2:HumanEval/77` | Correct rejection: cube-root truncation breaks visible cases. |
| `b2:Mbpp/749` | Correct: removing `strip()` does not produce the claimed integer-parsing defect. |
| `b1:Mbpp/460`, `b2:Mbpp/460` | No demonstrated false rejection: empty-sublist handling changes, but no established specification-required failure or hidden failure. |
| `b1:HumanEval/131` | Correct: multiplying by zero breaks visible cases such as 120. |
| `b2:Mbpp/68` | Correct: every length-two sequence is monotonic; quote also fails F1. |
| `b1:Mbpp/457` | Correct: maximum length breaks visible minimum-length tests. |
| `b2:Mbpp/101` | Correct: indexing shift breaks visible tests. |
| `b1:Mbpp/787` | Correct for retained candidate: no edit and no hidden failure. |
| `b2:Mbpp/271` | Correct: shifted summation range breaks visible tests. |

Thus, this sample demonstrates that real specification-relevant defects exist in I. It does **not** establish the semantic denominator for all 92 or 281. Conversely, I found no demonstrated wrongful exclusion among these ten retained rejected candidates.

The 19 self-announcing instances also reproduce. Only `b2:Mbpp/643` belongs to I; all eight readings flag it, and exclusion gives 89/91. Those explicit BUG/DEFECT comments do not explain the aggregate contrast. That does not eliminate other forms of conspicuousness.

The chronology supports Amendment 6 preceding its added arm: commit `3ffb0c6` is at **01:12:45 +0800**, wiring commit `57239bb` at **01:13:19**, and the first rejected-arm ledger event at **01:13:26.617**. Amendments 1–2 were construction-yield adaptations, not audit-outcome-blind construction from the original protocol; they are disclosed. Amendments 4–5 precede the audit, Amendment 6 follows earlier outcomes but precedes its own arm, and Amendment 7 is a retrospective withdrawal.

**What concretely remains before calling the descriptive report final:**

- Make the four corrections above, including their generated text where applicable.
- State the final deliverable as descriptive blocking observations after withdrawal of the C4 interpretation. Mark naming adjudication and the deferred gate sensitivity as final omissions, rather than implying completion depends on buying them.
- Correct the stale reporting metadata: “five amendments,” the injector docstring’s 150-instance frame, “numbers below are left unedited,” “no figure here is typed by hand,” and the duplicate §5 numbering.
- Qualify the successor claim. An independent party must validate the actual violation and specification-entailing expected behavior under a fixed, blinded protocol. Independence alone—and a second substrate alone—does not remove task composition or construction confounding. This is a condition for a future C4 study, **not work required to finish this one**.

I rebuilt the report in memory: `numbers.json` and `tables.md` are byte-identical, and the splice checks pass. Archived finding flags match the retained cache flags. The branch diff leaves `src/`, the kernel, comparator implementation and study-21 files untouched. **22 tests passed; five write-dependent tests were deselected.** I did not run the full repository suite or claim a normal-host clean-suite result.

**Quotable descriptively / not quotable for C4 — the semantic denominator was never established.**

Reader sentence: “Across eight readings, the auditor blocked 90 of 92 gate-accepted injected variants, compared with 11 of their 92 unmodified twins and 33 of 110 natural residual instances; these observations do not establish recall on specification-determined defects.”
