Reviewed commit **13efbb9**, read-only. `numbers.tex` exactly matches regenerated output; the new verdict-table estimates and verdicts match the supplied E6/E1/E8 results. Paths below are relative to `audit-ceiling-paper/tex`, unless stated otherwise.

**R1 §1 — Numerical and factual mismatches**

| R1 item | Status | Finding and location |
|---|---|---|
| E6-2 scale | **Fixed** | Explicitly defined as half the diagnosis-rate difference: `sections/introduction_v2.tex:32–33`; `sections/e6.tex:97–98`. |
| “Neither flags” | **Fixed** | GPT now blocks “about 3%”, consistent with 9/328; Claude zero: `sections/e6.tex:111`. |
| OPEN-subgroup denominator | **Fixed** | Reports 17/19 overall and 2/4 among OPEN failures: `sections/natural.tex:45–47`. |
| Sentence versus resolve false flags | **Fixed** | Separates zero observed sentence-arm flags from 2.1% under resolution: `sections/introduction_v2.tex:37–39`. |
| E3 sample size | **Fixed** | 266 faulty plus 266 clean: `sections/transfer.tex:33–34`. |
| E3 comparator | **Fixed**, with a new qualification below | Identifies the profile comparator and correctly quotes +23.3 [13.2, 33.3] against the weaker validator: `sections/transfer.tex:34–38`. |
| Admission protocol | **Partly fixed** | Interface scope and conditional red-team retry corrected at `sections/e6.tex:29–35`; blanket “each stage … once” remains at `appendix/e6_protocol.tex:7–8`. |
| Executable witness scoring | **Fixed** | Removes two-judge witness acceptance: `sections/discussion_v3.tex:33–35`. |

**R1 §2 — Overclaims**

| R1 item | Status | Finding and location |
|---|---|---|
| H6 interpreted as null | **Fixed** | Explicitly allows sizeable differences in either direction: `sections/natural.tex:43–45`. |
| Placebo “does nothing” | **Partly fixed** | Adds the 34.8% sensitivity bound, but introduces a false zero-diagnosis statement: `sections/natural.tex:55–56`; see below. |
| E8 “little selectivity” | **Fixed** | Correctly distinguishes positive selectivity from unresolved comparison with 20 points: `sections/discussion_v3.tex:39–42`; `appendix/e6_protocol.tex:82–85`. |
| Full table/tools null | **Partly fixed** | “Detectably” improves calibration, but zero still labels the wrong contrast; tools also remain confounded with reading count: `sections/transfer.tex:39–40`. |
| Natural information-limited share | **Partly fixed** | Explicitly disclaimed at `sections/natural.tex:5–7` and `sections/framework.tex:79–82`; the introduction still promises decomposition of hidden-test recall into determined/undetermined failures: `sections/introduction_v2.tex:53–55`. |
| Capacity/information dichotomy | **Fixed** | Capacity now means the gap below the attainable ROC; overlapping distributions acknowledged: `sections/framework.tex:41–47`. |
| “Default reading” | **Fixed** | Replaced with shared model convention and explicit interpretative uncertainty: `sections/discussion_v3.tex:4–7`; 89% agrees with 415/466. |
| Mechanistic attribution | **Partly fixed** | Menu uncertainty cue acknowledged at `sections/e6.tex:85–88`; positive controls still supposedly establish an information rather than capability explanation at `sections/e6.tex:113–116`, without acknowledging unmatched difficulty. |

**R1 §3 — Disclosures**

| R1 item | Status | Finding and location |
|---|---|---|
| Pooled versus held-out taxonomy | **Fixed** | 43/107 split, all held-out class counts and κ = 0.71 correctly reported: `sections/natural.tex:8–18`. |
| Reused behavioural pool and clustering | **Partly fixed** | Exclusion, reused generators and problem bootstrap corrected at `sections/natural.tex:21–37`; implemented in `../figures/make_fig_natural.py:33–53`. However, `sections/framework.tex:80` still says “independent programmers”. |
| Construction–judging overlap | **Fixed** | Implementer, probe and red-team roles disclosed: `sections/e6.tex:35–37`; `sections/discussion_v3.tex:23–25`. |
| Selected/concentrated population | **Fixed** | 41/406, 37 MBPP units and only two exhibiting both rules disclosed: `sections/discussion_v3.tex:25–27`. |
| During-run amendments | **Fixed** | Timing, attempt accounting and 10-second/60-second timeout treatment disclosed: `appendix/e6_protocol.tex:169–172`. |
| E3 contamination/rerun history | **Partly fixed** | Production reruns and prior test analysis acknowledged at `sections/transfer.tex:40–43`. Actual clean-source access is still understated, and the mandatory side-by-side Amendment-2 results remain absent from the included appendix; the abstract’s preregistration qualification remains generic (`paper_v3.tex:69`). |
| Transfer endpoint qualifications | **Fixed** | 21/25 fault-related findings explicitly post hoc: `sections/transfer.tex:25–26`; H2 controls called test-passing: `sections/natural.tex:57`. |

**New errors or overclaims introduced by the revision**

- **Zero placebo diagnoses is false.** `sections/natural.tex:55` confuses a zero *contrast* with a zero *level*. Placebo verified diagnosis is **11.1%**, identical to original-arm diagnosis; see `crossaudit-harness/benchmarks/code/records/icml/e1_results_test.json:73–99`. The table’s H4 contrast and 34.8% sensitivity bound are correct.

- **Behavioural counts are correct, but “most” is not.** After excluding each failing program, I reproduce **930 defective / 559 reference / 71 neither**, **90 versus 57** pairwise preferences, and **89.1%** defective agreement within AT_ODDS. However, absolute majorities occur on **85 versus 55** items; `sections/natural.tex:24–25` should describe more matches to one output than the other, rather than “most”.

- **The newly attached E3 zero is not an effect of showing the full table.** `sections/transfer.tex:39–40`: **0.0** is model-plus-profile minus profile on the **42 faulty 12,000-row items across three datasets**, not full-table minus partial-table performance. Source: `e3_results_test.json:26–38`; the +1.3 contrast also compares configurations with different reading counts.

- **“Card alone” and the information attribution are unsupported.** `sections/transfer.tex:37–39` says the clean reference, “not the card”, carries most information. The weaker validator itself uses reference-sample non-integer frequencies (`crossaudit-harness/benchmarks/ai4s_e3/build_e3.py:119–121`), and localisation rates do not decompose information content; the weaker validator already localises **67.7%**, versus **91.0%** for the profile.

The revision substantially improves reporting, but I would not yet judge the paper ready for ICML main-track submission. Residual factual errors, mislabelled E3 contrasts and incomplete rerun disclosure still require correction. More fundamentally, independent semantic validation and convincing evidence connecting constructed information limits to natural auditing remain the principal acceptance weaknesses.

