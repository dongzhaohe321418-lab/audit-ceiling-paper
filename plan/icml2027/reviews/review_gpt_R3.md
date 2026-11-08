Reviewed **fac2352**, read-only. Most R2 corrections hold, but **one contrast remains mislabelled and the construction funnel contains stale counts**.

Paths below are relative to `audit-ceiling-paper/tex`; `H/` means `crossaudit-harness/benchmarks/`.

**1. Every R2 item**

| R2 item, including its four new findings | Status | Current location |
|---|---|---|
| E6-2 half-difference scale | Fixed | `sections/e6.tex:98–99` |
| “Neither flags” | Fixed | GPT approximately 3%, Claude zero: `sections/e6.tex:110–112` |
| OPEN-subgroup denominator | Fixed | 17/19 overall; 2/4 OPEN: `sections/natural.tex:45–47` |
| Sentence versus resolve false flags | Fixed | `sections/introduction_v2.tex:38–40` |
| E3 sample size | Fixed | 266 faulty plus 266 clean: `sections/transfer.tex:41–42` |
| E3 comparator; “card alone” and information attribution | Fixed | Reference-dependent weaker validator identified; unsupported attribution removed: `sections/transfer.tex:42–47` |
| Admission scope and conditional retry | Fixed in prose | `sections/e6.tex:30–38`; `appendix/e6_protocol.tex:7–11`; separate funnel discrepancy below |
| Executable witness scoring | Fixed | `sections/discussion_v3.tex:34–36` |
| H6 interpreted as a null | Fixed | `sections/natural.tex:43–45` |
| H4 overstatement; false zero-placebo diagnosis | Fixed | Both levels correctly 11.1%; 34.8% sensitivity retained: `sections/natural.tex:55–56` |
| E8 selectivity interpretation | Fixed | `appendix/e6_protocol.tex:83–89` |
| Full-table/tools null; newly mislabelled E3 zero | **Partly fixed** | Zero now labels the correct contrast, and reading-count confounding is disclosed; +1.3 still inherits the wrong population: `sections/transfer.tex:47–49` |
| Natural information-limited share | Fixed | `sections/introduction_v2.tex:54–56`; `sections/framework.tex:78–80` |
| Capacity/information dichotomy | Fixed | `sections/framework.tex:41–47` |
| “Default reading” | Fixed | `sections/discussion_v3.tex:4–7` |
| Mechanistic attribution and unmatched controls | Fixed | Menu caveat and control-difficulty limitation: `sections/e6.tex:85–89,114–118` |
| Pooled versus held-out taxonomy | Fixed | `sections/natural.tex:8–18` |
| Reused behavioural pool, clustering and “most” | Fixed | Counts and majority distinction reproduce; independence claim removed: `sections/natural.tex:21–37`; `sections/framework.tex:75–80` |
| Construction–judging overlap | Fixed | `sections/e6.tex:36–38` |
| Selected/concentrated population | Fixed | `sections/discussion_v3.tex:25–27` |
| During-run infrastructure amendments | Fixed | `appendix/e6_protocol.tex:178–181` |
| E3 contamination and required side-by-side results | Fixed | Actual clean-source access and prior analysis disclosed; comparison supplied: `appendix/e6_protocol.tex:186–207` |
| Fabrication endpoint and test-passing controls | Fixed | `sections/transfer.tex:32–33`; `sections/natural.tex:57` |

**2. Numerical audit**

- **Exact regeneration:** `numbers.tex` and all 20 numerical rows of `table1.tex` match their generators’ output from the stored results.
- **Matches:** E1/E6/E8 estimates, intervals, sample sizes and registered verdicts in `appendix/e6_protocol.tex:147–163`; the ordered E6 family is correctly reported.
- **Matches:** natural-failure counts, κ values, 930/559/71 behavioural totals, 90/57 pairwise preferences and 85/55 absolute majorities (`sections/natural.tex:8–57`); E6 behavioural counts and percentages (`appendix/e6_protocol.tex:71–89`).
- **Matches:** scientific-code/results values and E3 estimates, including both amendment columns (`sections/transfer.tex:20–52`; `appendix/e6_protocol.tex:204–207`). The 57% access-attempt figure is 304/532 completed GPT held-out agentic readings.
- **Matches:** E7’s development/test funnel, **5 < 12** stopping decision and absence of auditing (`appendix/e6_protocol.tex:126–132`), against `H/e7/PREREGISTRATION-E7.md:40–50`.

**Exception: the E6 construction table uses archived admissions.** At `appendix/e6_protocol.tex:29–30`, the correct counts from the frozen final records are:

| Stage; development / held-out | Printed | Frozen final |
|---|---:|---:|
| First-attempt open admissions | 25 / 81 | **24 / 79** |
| Second-attempt open admissions | 18 / 53 | **17 / 52** |
| Control admissions | 38 / 105 | **37 / 100** |
| Controls passing red team | 35 / 82 | **35 / 83** |

The printed values reproduce `*_units4_v43c.jsonl`, preceding the final hidden-input correction documented at `H/code/icml/PREREGISTRATION-E6.md:97–110`. The current admission and red-team files match their frozen hashes (`H/code/records/icml/FREEZE_test.json:2148–2166`); the final **41 open units and 78 controls remain correct**.

Consequently, `sections/transfer.tex:14–15` also repeats a stale E6 comparison: against final admissions, **13/79**, rather than **15/81**, fail the red-team gate. E7’s registration itself repeats the historical counts, so matching that registration does not establish their consistency with final E6 records.

**3. Remaining or newly introduced misstatements**

1. **E3’s +1.3 contrast still has the wrong sample attached.** `sections/transfer.tex:47–49` places both contrasts under “42 faulty items … 12,000-row”. Only **0.0** belongs there; **+1.3 [−2.7, 5.8]** compares configurations on **112 faulty 120-row items across eight datasets**. Source: `H/code/records/icml_e3/e3_results_test.json:26–38`.

2. **E7 construction failure does not establish multiple unstated behaviours.** `sections/transfer.tex:15–16` interprets implementation/reference disagreements as suggesting that tasks leave many behaviours unstated. Those failures also admit ordinary implementation errors or inadequate construction procedures; report the failed construction, or explicitly retain these competing explanations.

3. **Trimming removes the earlier data study’s endpoint qualification.** `sections/transfer.tex:52` gives **+10.7 [6.0, 15.9]** without saying that it measures a lexical finding-naming endpoint. It is not directly interchangeable with E3’s fault-type-and-column localisation; the distinction remains explicit only at `appendix/ai4s_full.tex:175–178,190–202`.

I would **not submit the paper as it stands**: correct the frozen-funnel counts and E3 population label, and qualify the E7 interpretation and earlier data endpoint. These are bounded reporting fixes; independent semantic validation and demonstrated transfer beyond the constructed short-function population remain substantive acceptance weaknesses.

