**2050044 does not yet pass a clean review.** The central C4 withdrawal now reaches the primary table, standalone JSON, and CLI, and the corrected arithmetic reproduces. But several supposedly corrected claims remain elsewhere, including factual contradictions introduced or retained by the repair.

No files were modified.

1. **The gate’s role is still overstated.** [RESULTS-INJECT.md:42](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:42) still says it selects on detectability “rather than on the specification”; the same claim survives at line 336. The observed blocking-rate difference supports an association between gate acceptance and detectability. It does not establish that specification judgments played no role. This is precisely the narrowing the latest commit says it made.

2. **The probe correction remains incomplete.** [probe.py:8](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject/probe.py:8) still calls the prober “not a gate.” More substantively, [RESULTS-INJECT.md:149](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:149) says the probe shows that the edit’s cues are present; Amendment 5’s **new supersession notice** says it measures conspicuousness at 96.7%. Neither follows from this design. The corrected §3 accurately identifies the limitations: the model is a gate model, the arms share no problem, and the prompt includes the specification. Those qualifications must govern these other sentences too. The probe measures classification of these two sets; it does not identify edit salience.

3. **The rejected-population contradiction remains verbatim.** [RESULTS-INJECT.md:131](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:131) says “no duplication at all: 40 instances, 40 distinct programmes, 35 problems.” The corrected table says 35 programmes. The archive confirms **35**, with five duplicate pairs, all within problems.

4. **The kill test still demands the phrase and does not enforce its interpretation.** [test_inject_report.py:127](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:127) retains:
   ```python
   assert "the kill does not fire" in FLAT
   ```
   Its additional checks establish a denominator sentence and the existence of a `WITHDRAWN` key. They do not establish that the verdict licenses nothing. I replaced the relevant prose withdrawal with an explicit C4 endorsement **in memory**; this test still passed. The current prose withdrawal is clear, but the claimed test protection is not real.

5. **The corrected standalone summary confuses the comparators.** [CORRECTIONS.md:316](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/CORRECTIONS.md:316) describes the natural-residual contrast using “90 of 92 against 11 of 92 twins.” The twins are the unmodified stratum-C controls. The natural residual is **33 of 110**. Both contrasts survive descriptively, but they answer different questions.

6. **Some withdrawal language still withdraws too much.** [RESULTS-INJECT.md:90](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:90) says the weighted figure “has no population to be a recall of,” immediately before correctly identifying its population and appropriate estimator. It has a defined population of filter-accepted edits; it lacks the established **semantic denominator** needed for C4. “What this licenses is nothing” should likewise explicitly mean *nothing about C4*. Also, removing the one counted marker-comment instance shows that **that instance** cannot explain the effect—not that self-announcement or conspicuousness generally cannot.

Two smaller factual repairs remain. The cross-tab’s approximately 11% probability and 0.12 expected misses use the **69 answered injected items**, not all 92: over 92 they are 8.55% and 0.087. Fisher’s two-sided **p = 1.0** reproduces, so the substantive caution survives. The cost section still reports $16.47; adding the archived rejected-arm expenditure gives **$18.3687**.

The registration preserves the historical argument and now explicitly retracts its conservativeness claims. That is appropriate; old beliefs need not disappear. However, newly inserted correction notices are current assertions, and the salience claim in Amendment 5’s notice needs correction itself.

**The numerical checks passed.** I executed `report_inject.main()` with filesystem writes captured in memory. Both generated files were byte-identical to the committed versions, and the actual CLI output began with the withdrawal. The splice/report tests passed.

Independent cache calculations gave:

| Quantity | Reproduced result |
|---|---|
| Gate-accepted union, K = 8 | 90/92 |
| Unmodified twins | 11/92 |
| Paired discordances | 79 injected-only, 0 twin-only |
| Paired difference | +85.87 points; cluster interval [+77.3, +93.3] |
| Gate-rejected sample | 31/40; cluster interval [62.2, 90.5] |
| Weighted filter-accepted estimate | 84.1548%; bootstrap [73.8, 93.1] |
| Subset-averaged union curve | 94.4, 96.5, 97.0, 97.4, 97.6, 97.7, 97.8, 97.8% |
| Probe | 147 correct among 152 parsed; 32 unparsed |
| Unparsed-outcome bounds | 147/184 through 179/184: 79.9–97.3% |

The registered seed **20260916** reproduces both disputed intervals. The earlier irreproducibility explanation was wrong.

The weighted estimator
\[
\frac{92}{281}\frac{90}{92}+\frac{189}{281}\frac{31}{40}
\]
is appropriate for estimating the blocking proportion over the **281 filter-accepted instances under this protocol**. Its interval does not become a calibrated finite-population confidence interval merely because it reproduces. The report now correctly acknowledges the without-replacement sample, fully observed accepted stratum, and the cross-stratum problem, `Mbpp/614`.

I also confirmed:

- I contains **59 distinct programmes**, with 33 duplicate pairs covering 66 instances; none crosses a problem.
- The rejected sample contains five duplicate pairs: `HumanEval/43`, `Mbpp/140`, `/266`, `/569`, and `/95`.
- Whole-problem resampling keeps these duplicates together. That handles this dependence; it does not prove coverage or a general claim that problem clustering is always more conservative.
- The full results warn about Wilson intervals. The standalone tables do not carry that duplication warning; a reader extracting them loses it.
- The defined added-comment search finds **19 instances**, only `b2:Mbpp/643` in I. Both gates accepted it; all eight draws blocked it; excluding it gives **89/91**.
- The probe arms have **zero shared problems**.

**The six-filter account in §5 is substantially accurate.** I reproduced its counterexamples using the real filter and suite-result logic, passing candidate programs through `python -c` instead of temporary files to respect the read-only instruction.

F1 checks normalized text, not entailment. F2 accepts a successful early exit before an assertion finishes. F3 accepts a non-timeout unsuccessful process exit without an assertion or exception. F4 compares module-name sets. F5 remains true after an immediate `ZeroDivisionError`. F6 is exactly a truthiness check: **179 strings and 102 lists** among the 281 accepted witnesses, with no execution or semantic linkage.

F6 as registered would not have established entailment either. Execution can establish a behavioral difference; the expected behavior still needs justification from the specification.

For the requested archive sample, I used seed **20260920**, sampling 15 members of I and 10 filter-rejected instances with retained code. All 15 accepted variants again passed the visible suite and failed the hidden suite without timeout. My semantic admission judgments are below; these are review judgments, not a replacement adjudicated denominator.

| Accepted instance | Would admit as specification-determined? |
|---|---|
| `b2:Mbpp/554` | Yes: discards negative odd integers. |
| `b2:Mbpp/631` | Hold: requires resolving whether consecutive whitespace is replaced characterwise or as a run. |
| `b2:Mbpp/82` | Yes: uses radius squared for small spheres. |
| `b1:Mbpp/744` | Yes: rejects tuples containing multiple `None` values. |
| `b1:Mbpp/256` | Yes: returns one prime below 2. |
| `b2:Mbpp/171` | Yes: uses four sides for some pentagons. |
| `b2:HumanEval/9` | Yes: initializes the rolling maximum to zero for negative-leading inputs. |
| `b2:HumanEval/117` | Yes: removes repeated qualifying word occurrences. |
| `b1:Mbpp/62` | Yes: omits the last element when finding the minimum. |
| `b2:Mbpp/165` | Yes: excludes `z` at position 26; its recorded witness does not demonstrate this. |
| `b1:HumanEval/123` | Yes: removes explicitly required sorting. |
| `b1:Mbpp/79` | Yes: substitutes modulo four for oddness. |
| `b2:Mbpp/390` | Yes: formats only the first four elements. |
| `b2:Mbpp/257` | Yes: changes the sign when swapping negative inputs. |
| `b2:HumanEval/4` | Yes: rounds the mean; its recorded witness produces no output difference. |

In particular, the archived witnesses for `Mbpp/165` and `HumanEval/4` produce **0 versus 0** and **1.5 versus 1.5**, respectively.

For rejected instances, an archival limitation matters: `last_code` is populated with `setdefault`, so it retains the **first stored rejected variant**, not necessarily the final attempt. These judgments concern that retained variant:

| Rejected instance | Judgment |
|---|---|
| `b2:Mbpp/787` | Correct rejection: unchanged code. |
| `b1:Mbpp/778` | Correct protocol rejection: breaks visible tests. |
| `b1:Mbpp/130` | Correct protocol rejection: breaks visible tests. |
| `b2:Mbpp/233` | Correct rejection: retained edit introduces no demonstrated defect. |
| `b2:HumanEval/80` | Correct rejection: equivalent condition. |
| `b2:HumanEval/147` | Correct rejection: identical return in both branches. |
| `b1:Mbpp/632` | Semantically useful defect rejected by F4: negative elements disappear, but removal of test lines makes the diff eight lines. |
| `b2:Mbpp/139` | Semantically useful defect rejected by F3: wrong circumference below radius 1, but hidden tests pass. |
| `b2:HumanEval/148` | Correct rejection: swapping equal indices changes nothing. |
| `b1:HumanEval/120` | Correct rejection: equivalent behavior on the specified domain. |

Thus the filters exclude genuine specification violations too. A sparse hidden suite and a line-count limit shape the population independently of semantic correctness. A plausible remaining mechanism is selection for conspicuous special cases around visible examples; removing those edits also removes their cues. Neither the twin arm nor the rejected arm eliminates that explanation.

The amendment chronology supports Amendment 6’s limited prospective status: registration at **01:12:45**, implementation at **01:13:19**, rejected-arm run identifier beginning **01:13:20**, and results committed at **01:29:13** on September 12. It followed the original outcomes and internal review, so it was prospective for its added arm, not an outcome-independent rescue of H22a. Amendments 1–2 disclose construction-dependent pilots; Amendments 3–5 precede the recorded successful audit run.

The study diff leaves `src/` and kernel code untouched. The committed study records contain metadata rather than corpus, solution, or finding bodies. **21 read-only-compatible tests passed**; I did not run the full suite or rebuild, which would write files.

The proposed successor is the right direction, **but “someone other than the injector” is insufficient by itself**—the existing gates already satisfy that description. Membership must be established independently of auditor outcomes, using specification-grounded expected behavior and an executed violating input, with ambiguity rules and sampling fixed beforehand. A prospective test of C4 also needs a comparison that addresses task mix and artificial-edit cues. Independent labeling of natural defects is a stronger route than repairing F6 alone.

**Quotable descriptively / not quotable for C4 — the construction never established the semantic denominator C4 requires.**

Reader sentence: “Across these archived gate-accepted edits, eight auditor readings blocked 90 of 92 edited instances and 11 of their 92 unmodified twins; this demonstrates a response to the edits, without establishing detection of specification-determined defects.”
