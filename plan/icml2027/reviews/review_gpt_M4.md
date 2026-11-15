**I retain 7/10.** E13 strengthens the paper, but its main-text interpretation exceeds the intervention tested. No files changed.

**A. Verification and corrections**

I reproduced the E13 and exploratory code-shape estimates and intervals from stored readings. The reported numbers reconcile: **40/41 units, 960/960 readings, +0.6 [−1.2, 2.5], and residual preference +20.6 [6.9, 33.8]**; the 20/21-unit exploratory split and its diagnosis contrasts also match. The remaining F1 numerical claims reconcile, including the two units containing followers of both rules.

Paper paths below are relative to `audit-ceiling-paper/tex/`.

| Location | Finding and exact correction |
|---|---|
| `sections/e6.tex:102` | **“extra conditionals alone do not draw flags” overgeneralises.** Replace with **“this added-branch intervention had little effect”**. E13 tests particular rewrites of B, not conditional statements generally. |
| `appendix/e6_protocol.tex:207`; `:300` | Replace the final interpretative sentence with **“E13 detects little effect of adding branches to B; it does not test other features of A’s code or distinguish convention from the behaviour A implements.”** Change the table verdict **“no shape effect” → “within margin”**. |
| `appendix/e6_protocol.tex:128` | **“pools four, hence 15.2%” is an incorrect explanation.** E6 still gives **15.2439%** when restricted to E10’s two low-budget configurations. Replace the parenthesis with **“(E6 reported 15.2%; E10 uses fresh readings)”**. |
| `paper_v3.tex:69` | The blanket preregistration claim conflicts with explicitly exploratory analyses. Replace with **“Confirmatory analyses were preregistered; deviations are disclosed.”** |
| `crossaudit-harness/benchmarks/e13/PREREGISTRATION-E13.md:45–47`; `e13.py:384–399` | **Prespecified secondary reporting is incomplete:** between-stratum differences, per-vendor estimates and added-line summaries are absent from the results. Supply them or disclose their omission. My recomputation gives B′−B of **−1.25 points for Claude, +2.50 for GPT**; residual preferences remain positive for both. This omission does not invalidate the primary results. |

**B. E13 integrity**

The retained history supports the chronology:

`a762a07` P14 corrections and development rerun → `22bb71b` construction amendment/initial freeze → failed verification with no readings → `d10c719` corrected freeze → held-out readings → `029bc34` results.

The corrected freeze was committed at **03:20:13 UTC**; the earliest timestamped held-out GPT thread starts at **03:20:17.004**. Neither audit file contains test readings at the freeze commit. Frozen source, registration and construction hashes match; all 960 recorded prompt hashes match.

The duplicate-edit amendment changes bookkeeping, preserves the two-attempt limit and leaves Mbpp/93 missing. The population/path fixes occurred before recorded outcomes. These are defensible repairs; I found no evidence of outcome-driven changes.

**The current E13 sentence says too much.** The justified conclusion is that preference survives **this added-branch control**, whose estimated effect satisfies the registered ±10-point criterion. It neither establishes zero effect nor eliminates other implementation cues. These are fresh outcomes on reused tasks.

**C. Scores and highest-value next change**

| Soundness | Presentation | Significance | Originality | Overall | Confidence |
|---:|---:|---:|---:|---:|---:|
| 3/4 | 3/4 | 3/4 | 3/4 | **7/10** | 4/5 |

The substantial requirement effects and transparent records support acceptance. Selected constructions, dependent model validation and unresolved implementation cues prevent an upgrade.

**One highest-value change:** preregister a **rule × code-presentation experiment** on existing units, rewriting both A and B symmetrically into ordinary and conspicuous forms, with execution checks and fresh interleaved audits. This directly tests whether preference survives changes to implementation. It is feasible without human raters or downloads. I would retire my previous unused-library-task recommendation: E12’s documented feasibility projects only about five qualifying units.

**D. Three weakest main-text sentences**

Each replacement is shorter in both words and characters.

1. `sections/introduction_v2.tex:36`, “The convention the benchmark rewards …”  
   **“The models share the benchmark’s convention; flagging departures becomes a false positive when the alternative rule is intended.”**

2. `sections/e6.tex:119`, “The flat … arm … auditors that cannot read …”  
   **“The controls show that these auditors can discriminate clear misreadings, although they are not matched to the open units in difficulty.”**

3. `sections/discussion_v3.tex:44`, “Selectivity was … so the question largely returns …”  
   **“Selectivity was 16.8 points [10.5, 23.2]; the interval crosses the registered 20-point threshold.”**