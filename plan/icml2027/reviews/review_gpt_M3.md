**I would raise the score to 7/10, narrowly.** E11 provides credible evidence that the sentence effect extends to constructed library tasks. It does not establish generalisation to ordinary library code. No files changed.

**A. Numerical and claim checks.** I reproduced the primary estimates and bootstrap intervals from the stored audit and witness records. The construction funnels, 18 problems, 576/576 valid readings, diagnosis levels, vendor estimates, admissibility results, subset contrasts and verdict-table entries reconcile. The total of 59 units is also correct.

The following corrections are needed. Paper paths below are relative to `audit-ceiling-paper/tex/`.

| Location | Finding and exact correction |
|---|---|
| `sections/transfer.tex:16`; `appendix/e6_protocol.tex:191` | **Median 4 matches the JSON but uses the upper middle observation.** Across 36 programs, the middle values are 3 and 4; the conventional median is **3.5**. Replace “median 4” with **“median 3.5”**, or **“upper median 4”** to retain the numeral. The maximum, 12, is correct. The implementation is `e11_report.py:41`. |
| `sections/transfer.tex:22`; `appendix/e6_protocol.tex:202` | **26.4% is a policy rate, not a reading rate.** It is 19/72 correct-program cells, flagging if either reading flags. Individual readings give 35/144 = 24.3%. Replace “on 26.4% of readings” with **“with a 26.4% false-flag rate”**; in the appendix use **“The two-reading policy’s sentence-arm false-flag rate was 26.4% [11.1, 43.1] (betting upper bound 46.0%).”** |
| `sections/transfer.tex:23–25`; `appendix/e6_protocol.tex:207–208` | **“Share the reference outside one branch” is false as a structural guarantee.** For example, BigCodeBench/872 rewrites the surrounding comprehension as loops; /813 changes assignment and return code outside the condition. See `records/e6b_impls.jsonl:288` and `:266`. Replace with **“The edited branches cue the relevant behaviour in every arm; the result is conditional on these constructed library tasks.”** |
| `sections/transfer.tex:24–25` | **“Not peculiar to short functions” exceeds the evidence.** These audited programs are themselves short functions. Replace the conclusion with **“The sentence effect extends to these constructed library tasks; its applicability to ordinary library code remains untested.”** |
| `paper_v3.tex:65` | The abstract omits the construction qualification. Replace “18 data-science tasks from BigCodeBench” with **“18 reference-edited BigCodeBench data-science tasks”**, using the shorter sentence below. |
| `appendix/e6_protocol.tex:201–202` | **“Above … 30.9” is strictly incorrect:** the minimum is 30.88235. Replace with **“The minimum leave-one-problem-out lower limits were 38.2 and 30.9 points.”** |
| `appendix/e6_protocol.tex:206` | “17 units most of them accept” obscures the denominator. Replace with **“17 units accepted in at least three of four judge–order readings”**. This is a majority of readings, not a majority among two judges. |

**B. Integrity.** The recorded sequence supports separation of construction from held-out auditing:

`5b96ffc` protocol freeze → `6fc800e` descriptive-report implementation → `9c28fe4` construction/archive → `e482d6b` rerun/archive → `782f690` population freeze → `5d7ec30` results.

The bound source/data and construction-record hashes match; all 576 recorded audit prompt hashes match the population freeze. At the population-freeze commit, the audit files contain development readings only.

- **Primary decisions:** I found no evidence that hypotheses, admission criteria, arms, scoring or the gate threshold changed after held-out audit outcomes. Reducing the draft gate from 20 to 12 followed the development pilot and preceded held-out construction; the registration discloses this.
- **Post-audit implementation:** The E11-3 subset adapter, `e11_admissibility.py`, first appears in the results commit. The audit log records the original subset-analysis failure immediately beforehand. This repairs a preregistered descriptive analysis, rather than introducing a new primary hypothesis, but should be disclosed as a post-audit implementation correction.
- **Outage handling:** Repeating transport failures under the existing amendment is acceptable **in principle**. The archive contains **81 failed calls across 69 distinct tasks**; rerun prompt hashes match. However, its rows retain neither `usage` nor `reached`, and `e6.py:348–359` discards that metadata. Consequently, the released archive **cannot independently establish that these calls never reached a model**. Supply contemporaneous transport logs if retained; otherwise qualify that assertion.
- **Gate disclosure:** The registration says the gate is evaluated once. Logs show preliminary values **12, then 17**, followed by final **18**. Construction nevertheless continued to completion. Replace the appendix’s preliminary-gate sentence with **“Preliminary gate reports were 12 and 17; the final gate was evaluated after all eligible construction calls were completed.”**
- **Framing:** “Extension, not replication on unused tasks” is honest. E7 construction outcomes informed E11, while E11 audit outcomes remained held out. The appendix explains this adequately; the abstract needs the construction qualifier.

**C. Revised scores.**

| Dimension | Score |
|---|---:|
| Soundness | **3/4** |
| Presentation | **3/4** |
| Significance | **3/4** |
| Originality | **3/4** |
| Overall | **7/10** |
| Confidence | **4/5** |

The upgrade rests on substantial effects under both controls, consistency across vendors and robustness to removing individual problems. The high false-flag rate and Claude’s **47.2%** exclusion of explicitly contradicted alternatives limit stronger conclusions.

**Single highest-value next change:** one preregistered study on **30–50 previously unused library tasks**, with less conspicuous behavioural edits and contradiction controls. That would address the remaining dependence on familiar construction cases and explicit branch cues.

**D. Shorter wording.** The following replacements preserve the reported numerals. Corrections to factual scope are identified above; “upper median” preserves 4 accurately. Unquoted text and cross-references can remain unchanged.

- **Transfer, construction sentence**

  “A second preregistered study (E11) changed only how programs are built: each implementing vendor edits the reference so that an explicit branch follows one rule (median 4 changed lines).”

  → “The second preregistered study (E11) changed only construction: each implementing vendor edited the reference to follow one rule in an explicit branch (upper median 4 changed lines).”

- **Transfer, sample sentence**

  “It yielded 18 held-out units from 18 problems, with all 576 registered readings valid”

  → “It yielded 18 held-out units from 18 problems; all 576 registered readings were valid”

- **Transfer, effect sentence**

  “One sentence stating the requirement raised verified diagnosis by 58.3 points [41.7, 73.6] over the task alone (66.7% against 8.3%) and by 48.6 [34.7, 62.5] over a note naming the input class; the note alone added 9.7 [2.8, 16.7].”

  → “Stating the requirement in one sentence increased verified diagnosis by 58.3 points [41.7, 73.6] over the task alone (66.7% versus 8.3%) and 48.6 [34.7, 62.5] over a note naming the input class; the note added 9.7 [2.8, 16.7].”

- **Transfer, robustness sentence**

  “Both registered hypotheses hold, no problem’s effect is negative, and leaving out any one problem keeps both lower limits above 30.”

  → “Both registered hypotheses hold. No problem has a negative effect; omitting any problem leaves both lower limits above 30.”

- **Transfer, convention sentence**

  “With the contract withheld, the convention advantage was 8.3 [2.8, 13.9] (not registered here).”

  → “Without the contract, the convention advantage was 8.3 [2.8, 13.9] (not registered here).”

- **Transfer, false flags**

  “Unlike on HumanEval+ and MBPP+, the sentence arm still flagged the correct program on 26.4% of readings.”

  → “Unlike on HumanEval+ and MBPP+, the sentence arm had a 26.4% false-flag rate.”

- **Abstract**

  “One added sentence stating the missing requirement raises verified diagnosis by `\NSixFive{}` points, and by 58.3 on 18 data-science tasks from BigCodeBench.”

  → “One sentence stating the missing requirement adds `\NSixFive{}` points to verified diagnosis and 58.3 on 18 reference-edited BigCodeBench data-science tasks.”

- **Introduction**

  “On 18 data-science tasks from BigCodeBench, built by editing the reference, it adds 58.3 points [41.7, 73.6]”

  → “On 18 BigCodeBench data-science tasks with edited references, the sentence adds 58.3 points [41.7, 73.6]”