**The binding fails again. The descriptive results survive, but `53927c1` is not ready to mark final.** Four issues remain.

1. **The binding still checks source text, and one protected conclusion remains a fragment.** At [test_inject_report.py:38](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/tests/test_inject_report.py:38), `_visible()` removes HTML comments without rendering Markdown. I replaced the §2 withdrawal with:

   ```markdown
   [withdrawal]: / "**What this licenses about C4 is nothing, and that is the finding.**"

   **The study confirms C4 prospectively.**
   ```

   Pandoc’s CommonMark rendering contains the endorsement and omits the withdrawal. **All 22 runnable injection/report tests still pass.** This removes a protected passage from the reader’s document; it does not merely add contradictory prose elsewhere.

   A second mutation also passes: in [§1’s conclusion](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:183), replace “nothing in this construction establishes that” with “all six filters establish that.” The binding still protects only `**That conclusion is withdrawn**`. Bind the actual rendered passages and include this subordinate clause, or narrow the assurance accordingly.

2. **The cross-tab still explicitly “carr[ies] no information.”** [Lines 244–245](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:244) retain that verdict immediately above the new paragraph rejecting it. The new account is accurate: **8.5523%**, **0.0869565** expected misses, a uniform-placement illustration without clustering, and Fisher’s **p = 1.0**. Neither that calculation nor Fisher establishes that competing explanations predict the same outcomes. Remove the stale introduction and update its splice anchor.

3. **The probe’s qualification has not reached every conclusion.** The [banner](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:15) still infers from separability that the populations “differ in more than specification-determinedness”; Amendment 7 and the generated `WITHDRAWN.what_survives` account repeat that inference. The [§3 heading](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:205) still calls the defects “detectably artificial.”

   The observed classification result survives. What feature produced it remains unidentified—including whether the model used specification-relevant differences. Known differences in task composition independently establish a confound; classification accuracy does not establish an additional distinguishing property. Carry that distinction into the banner, heading and standalone record.

4. **$18.37 reproduces as the stated subtotal, but not as cumulative study spend.** The [cost section](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:363) sums to **$18.36869975** before rounding, including exactly **$1.89651875** for the 320 rejected-arm readings. That addition is correct.

   However, summing `api_value_usd` across the archived project usage ledgers—**4,794 distinct event IDs**—gives **$18.52886775**. The difference is:

   | Additional recorded expenditure | USD |
   |---|---:|
   | Construction beyond the retained injection/gate caches | 0.110073 |
   | Earlier audit invocation `inject-0911042818` | 0.049900 |
   | Route probe | 0.000195 |

   Report approximately **$18.53 in recorded API value**, still below $35, or explicitly label $18.37 as the retained-record subtotal. “Never to the ledger” is also inaccurate literally: the rejected arm appears in both usage ledgers and its committed manifest.

   Finally, **2,135 counts attempts reaching the filters**, not all injector attempts. The injection archive contains **2,292 paid attempts**, including **157 without filter results**.

The following checks passed:

- Rebuilt the report **in memory**: serialized `numbers.json` and rendered `tables.md` reproduce byte-for-byte; table splices match.
- Independently recovered **90/92** injected, **11/92** twins, **31/40** rejected; discordance **79 versus 0**; and every point of the union curve.
- Recomputed the weighted estimate **84.154804%** and bootstrap interval **[73.7523%, 93.1016%]**. It estimates blocking over the **281 filter-accepted edits**. The report correctly labels its finite-population coverage uncalibrated.
- Confirmed **59 distinct programmes**, 33 duplicate pairs in I, no cross-problem duplicate group; the rejected sample has **35 programmes** and five within-problem pairs.
- Recovered probe accuracy **147/152**, bounds **147/184 to 179/184**, no shared problems between arms, and the two misses belonging to **Mbpp/404**.
- Confirmed **179 string / 102 list witnesses**, **19** instances meeting the stated comment search, and only `b2:Mbpp/643` in I. It was flagged eight times; removing it gives **89/91**.
- Reproduced the F2–F5 counterexamples using the real filter logic and suite interpretation, with subprocess execution through `-c` to avoid temporary files. The revised filter account is accurate.
- Amendment 6’s commit precedes its first recorded reading: **01:12:45 versus 01:13:26 on September 12, +08:00**. It followed the existing outcomes but preceded the added arm, as disclosed.
- No study changes touch `src/` or kernel directories. I modified no files. **22 tests passed; five requiring writes/execution infrastructure were deselected. The full suite was not run in this read-only environment.**

For the requested construction sample, I used seed **20260921**, sampled sorted I first, then sorted filter-rejected instances with archived code. My semantic judgments were:

| Accepted instance(s) | Admit the edit? Reason |
|---|---|
| `b1:Mbpp/62` | Yes—omits the final element from the minimum. |
| `b1,b2:HumanEval/29` | Yes—substring membership replaces prefix matching. |
| `b1:Mbpp/441` | Yes—incorrect cube area for positive sides below three. |
| `b1:Mbpp/111` | Yes for nonempty disjoint lists; its named class also includes a nonfailing empty-list case. |
| `b1:HumanEval/35` | Yes—incorrect singleton maximum. |
| `b1,b2:Mbpp/89` | Yes—returns a value that is not smaller. |
| `b1:Mbpp/292` | Yes—truncation replaces explicitly required floor rounding. |
| `b2:HumanEval/117` | Yes—drops repeated qualifying words. |
| `b2:HumanEval/0` | Yes—admits equality despite “closer than.” |
| `b2:HumanEval/123` | Yes—removes required sorting; the named class needs tightening. |
| `b1:Mbpp/775` | Yes—checks only the first odd index. |
| `b2:Mbpp/809` | Yes—admits equal corresponding elements. |
| `b1:HumanEval/9` | Yes—incorrect rolling maxima for initially negative values. |

These judgments do not validate their witness metadata or establish the whole denominator.

Among the ten rejected instances, I would retain the rejection of `b2:HumanEval/77`, `b1:HumanEval/131`, `b1:Mbpp/457`, `b2:Mbpp/101`, and `b2:Mbpp/271`: the archived edits break visible tests. For `b2:Mbpp/749`, `b1,b2:Mbpp/460`, `b2:Mbpp/68`, and `b1:Mbpp/787`, the archived edits do not establish the required hidden-failing defect. This sample supplied no mistaken exclusion under the registered mechanical eligibility rules.

**No new experiment is necessary to finalize this as a descriptive report.** Resolve the four issues above and verify the repaired bindings. Keep the measured contrasts and the withdrawal of C4 support. A prospective successor needs independent judgments connecting the **actual failure** to a specification-required outcome, frozen before auditor outcomes, plus sampling and controls addressing task mix and artificiality. “Someone other than the injector” alone is insufficient—the existing gates already satisfy that description.

Reader sentence: “Across eight readings, the shipped auditor blocked 90 of 92 gate-accepted injected variants and 11 of their 92 unmodified twins; the contrast identifies a response to the edit, without establishing specification-based detection.”

**Quotable descriptively / not quotable for C4 — the blocking outcomes reproduce, but their denominator was never established as specification-determined defects.**
