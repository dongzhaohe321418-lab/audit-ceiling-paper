**I would not mark this repair clean.** The C4 withdrawal is clear in the report, CLI, and generated records, but its claimed bindings still fail under attack. The corrected arithmetic reproduces.

1. **[P1] The withdrawal can still be reversed while every report test passes.** In [test_inject_report.py:135](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:135), the assertion that every load-bearing sentence is protected is false.

   I changed only the in-memory document, leaving all files untouched:

   | Mutation | Report checks |
   |---|---:|
   | Previous attack: replace “What this licenses about C4 is nothing…” | **9/10: caught** |
   | Replace the kill’s “licenses nothing either” with “licenses a prospective confirmation of C4” | **10/10 pass** |
   | Replace §2’s second conclusion with “The study therefore contradicts the claim that C4 is unreplicated: C4 is now prospectively confirmed” | **10/10 pass** |
   | Replace the filter conclusion with “no filter … establishes specification ambiguity; together the filters establish entailment” | **10/10 pass** |
   | Replace the curve’s explanation with “all six filters establish that” | **10/10 pass** |
   | Put the required withdrawal sentence inside an HTML comment and display “The study confirms C4 prospectively” | **10/10 pass** |

   These are five new successful attacks. Two assertions explicitly truncate their strings before the decisive words; others preserve an introductory fragment while allowing its conclusion to reverse. Searching the entire source also accepts invisible text. Bind the complete, visible passages in their intended locations, and retain these mutations as regression cases. That would protect those passages—not establish that arbitrary contradictory prose is impossible.

2. **[P2] The probe’s non-identification is acknowledged but still contradicted elsewhere.** [RESULTS-INJECT.md:158](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:158) says the probe “shows those cues are there.” [Amendment 6:366](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject/PREREGISTRATION.md:366) still says it shows salience is detectable. Those claims exceed the three correctly stated limitations.

   The probe distinguishes these two sets. It does not identify edit cues as the distinguishing feature: the tasks differ, the specification is visible, and the prober is a gate model. Amendment 6 needs an adjacent correction preserving its historical wording. The current report needs consistent interpretation throughout.

   Also, §3 still introduces a model “neither the auditor nor a gate.” If that describes the original proposal, say explicitly that the implemented probe departed from it; otherwise it contradicts the corrected table.

3. **[P2] The cross-tab arithmetic is right, but the probability model is misdescribed.** At [RESULTS-INJECT.md:259](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:259),

   \[
   1-\binom{88}{2}/\binom{92}{2}=0.08552317,\qquad 2(4/92)=0.08695652.
   \]

   These describe uniformly placing two misses among 92 instances. They are **not** probabilities derived from the hypothesis that the auditor follows the probe’s signal. No such model is specified. Moreover, the two observed misses are the two instances of one problem, so this is not a cluster-aware calculation.

   Fisher’s two-sided result is indeed **p = 1.0**. That supports “this table does not distinguish the proposed explanations,” not the stronger assertion that both explanations predict the same result or that the table literally contains no information.

The **cost correction stands**, with an important provenance qualification. I initially obtained an apparent extra twin cost; checking the cost-stamping implementation showed that this double-counted shared totals.

| Component | Recorded cost |
|---|---:|
| Construction | $9.582760 |
| Injected and twin audit, counting each `run_id` once | $6.255886 |
| Probe | $0.633535 |
| Rejected arm: 320 unique reading IDs | $1.89651875 |
| **Total** | **$18.36869975 → $18.37** |

Adding the rejected arm to rounded $16.47 gives $18.36651875, also $18.37.

There are **644 injected/twin `run_id` collisions**. Each matching pair has the same combined cost because [explore.py:335](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/explore.py:335) constructs IDs without the study arm, and subsequent cost stamping writes the accumulated ID total into both rows. Consequently, these cache fields are not independent per-reading costs. The rejected arm has 320 unique IDs, so your derivation for that arm is unaffected.

The remaining numerical checks reproduce:

- **Population:** 910 archived instances, 281 filter-accepted, 92 gate-accepted.
- **Blocking:** 90/92 injected, 11/92 twins, 31/40 gate-rejected; paired discordance **79 versus 0**.
- **Subset-averaged curve:** 94.4, 96.5, 97.0, 97.4, 97.6, 97.7, 97.8, 97.8%.
- **Weighted descriptive estimate:** \((90+189\times31/40)/281=84.1548043\%\). Independently resampling problem clusters within strata at seed 20260916 gives **[73.7523, 93.1016]%**, reproducing [73.8, 93.1].
- **Rejected cluster interval:** **[62.2222, 90.4762]%**, reproducing [62.2, 90.5].
- **Duplication:** I contains 59 programmes, with 33 duplicate pairs; the rejected sample contains 35 programmes, with five pairs—HumanEval/43 and Mbpp/95, /140, /266, /569. None crosses a problem.
- **Probe:** 147/152 classifications correct; bounds 147/184 to 179/184; no problem overlap between arms.
- **Witnesses:** 179 strings, 102 lists.
- **Self-announcement:** 19 instances under the stated search; only `b2:Mbpp/643` belongs to I, flagged eight times. Removing it gives **89/91**.

The weighted estimator is appropriate descriptively for the **281 filter-accepted edits**. Its interval remains explicitly uncalibrated for the finite-population design: I was fully measured, the other stratum was sampled without replacement, and Mbpp/614 crosses the sampled strata. Reproducibility does not establish coverage.

The **six-filter account is accurate**. I reproduced the documented counterexamples through `filter_one`, retaining production suite-verdict handling and replacing temporary-file transport with `python -c`:

- An early successful exit passes F2 and F5 without completing the assertion.
- `os._exit(2)` satisfies F3 without an assertion or exception.
- Immediate `ZeroDivisionError` leaves F5 true.
- Adding `from math import cos` beside `import math` passes F4.
- An unrelated nonempty dictionary satisfies F6.

F6 is exactly the truthiness expression identified in the withdrawal. Neither its implementation nor its registered recovery step establishes semantic entailment. The gate does inspect semantics, but on the injector’s asserted class; the observed recall difference establishes association with acceptance, not that semantic judgments played no role.

I also sampled with seed **20260921**, from sorted IDs. For the 15 gate-accepted instances, I would independently admit each as containing at least one specification-determined defect:

| Instance(s) | Independently apparent violation |
|---|---|
| `b1:Mbpp/62` | Ignores the last element when finding the minimum |
| `b1:HumanEval/29`, `b2:HumanEval/29` | Substring matching replaces prefix matching |
| `b1:Mbpp/441` | Incorrect cube surface area for sides 1 and 2 |
| `b1:Mbpp/111` | Returns non-common elements for disjoint nonempty lists |
| `b1:HumanEval/35` | Singleton maximum is reduced by one |
| `b1:Mbpp/89`, `b2:Mbpp/89` | Returns the input itself where a smaller number is required |
| `b1:Mbpp/292` | Truncates negative quotients instead of rounding down |
| `b2:HumanEval/117` | Removes repeated qualifying words |
| `b2:HumanEval/0` | Accepts equality where strictly closer is required |
| `b2:HumanEval/123` | Removes required sorting; input 27 demonstrably returns unsorted output |
| `b1:Mbpp/775` | Checks only the first odd index |
| `b2:Mbpp/809` | Accepts equal corresponding elements |
| `b1:HumanEval/9` | Incorrect rolling maximum for negative inputs |

That is **not** validation of every recorded witness or named class. For example, Mbpp/111’s witness has the wrong argument packaging, while its actual defect is independently clear. These examples also show why withdrawing the population’s certification must not become a claim that its members contain no genuine semantic defects.

For ten rejected instances with archived candidate code:

| Instance | Would I retain the archived candidate? |
|---|---|
| `b1:Mbpp/632` | Semantically useful: discards negative nonzero values. Excluded by diff size. |
| `b1:HumanEval/141` | No new semantic edit; added comment only. |
| `b1:Mbpp/429` | No established defect on the specified domain; unequal-length behavior is unclear. |
| `b1:HumanEval/49` | Negative-exponent case needs domain clarification. |
| `b1:HumanEval/152` | `None` scores are not established as admissible inputs. |
| `b1:Mbpp/269` | Semantically useful: wrong ASCII values for lowercase characters. Excluded by diff size. |
| `b2:HumanEval/44` | Added comment only. |
| `b2:HumanEval/15` | Negative-input branch preserves the previous behavior. |
| `b1:Mbpp/424` | Empty-string behavior is not specification-settled. |
| `b2:HumanEval/127` | Real defect, but breaks visible tests; exclusion is appropriate. |

Thus the filters discard scientifically relevant semantic defects, including for purely syntactic size reasons. That is selection, not necessarily incorrect enforcement of the registered rules. For rejected instances, `last_code` can retain an earlier attempt; I did not equate it with the final attempt’s filter vector.

Nothing replaces the failed conservativeness argument. A surviving alternative is selection for conspicuous, narrowly targeted exceptions that avoid visible tests; removing those exceptions in the twin arm removes their semantic changes and cues together. The probe does not establish that this mechanism caused the gap, but neither control excludes it.

The successor is **directionally right, insufficient as a one-sentence guarantee**. Independent membership adjudication must be prospective and blind to audit outcomes, establish specification-derived expected behavior on admissible inputs, and distinguish detecting a certified defect from merely blocking its containing programme. Natural defects avoid the injection-specific confound; task composition, selection, and the comparator still need control. Executing the injector’s witness alone remains insufficient.

History supports the claimed ordering: Amendment 6 was committed at **01:12:45 +08**, before the rejected run’s **01:13:20** identifier and its results commit at **01:29:13**. Amendments 1–5 preceded the auditor outcomes they govern, while disclosing construction-dependent adaptations. Amendment 7 is correctly retrospective.

Finally, `report_inject.main()` reproduced both generated files byte-for-byte with writes intercepted in memory; the CLI begins with withdrawal, and splicing all seven blocks is an identity operation. No files changed; `src/` is unchanged across the study branch. The committed study-record schemas contain no solution or finding-text fields. The targeted tests returned **21 passed, three failures and two setup errors**, all five blocked by unavailable temporary directories. The full suite also stopped on that filesystem restriction; I cannot endorse the claimed normal-host green run from this environment.

**Quotable descriptively / not quotable for C4 — the decisive reason remains that the measured population lacks the independently established semantic denominator C4 requires.**

Reader sentence: “Across eight readings, the auditor blocked 90 of 92 gate-accepted injected programmes versus 11 of their 92 unmodified twins; this describes responses to these edits, not a prospective replication of C4.”
