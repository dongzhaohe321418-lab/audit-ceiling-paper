One required correction remains at [RESULTS-SWEEP.md:176](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:176). The substantive limitation is right, but its repaired provenance is still inaccurate:

- **“Its H19d texts come from a fifth reading”** describes only S-text. H19d adjudicated 38 S-text findings, 128 from R’s first reading, and 24 from B’s first reading. Both labellers’ files contain all 190 items.
- **“The four re-graded here”** imports study 19’s comparator into this sweep. This sweep re-grades eight `self-strong` readings; its common-depth estimate averages all 70 four-reading subsets. Study 19’s [Amendment 1](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-ceiling3b/benchmarks/code/ceiling3b/PREREGISTRATION.md:93) explicitly distinguishes its reused draws 1–4 from the separate `self-strong-S` reading.

A sufficient replacement is:

> Study 18 did not archive or adjudicate its advisory texts. Study 19’s H19d adjudicated findings from the first readings of R and B and a separate S-text reading under the shipped constitution. Those findings are not the archived readings re-graded in this sweep, so that adjudication does not establish what this sweep’s findings identified.

This is a factual correction, not a wording preference. It requires no additional readings or recomputation.

Everything else checked clears:

- All three round-3 findings are fixed. I found no other surviving assertion that its later qualification withdraws.
- The guarded, in-memory execution reproduced the entire record exactly without writes or network calls.
- An independent loader, explicit subset enumeration, and separate bootstrap reproduced all **86 estimate/interval triples** within numerical precision. All **80 table cells** match the record.
- All 35 input files are tracked; all 8,320 loaded rows contain both counts. No rows were dropped, and every included draw covers the same 110 P and 150 C instances.
- The three contrasts are correctly distinguished. The report supports exploratory rule-dependence and the scoped equal-depth comparison; it does not establish recognition, causal severity calibration, or a matched-rate ranking.

No files changed. I found no remaining statistical blocker or need to expand the analysis.

**Not quotable — the repaired provenance paragraph still misstates which readings study 19 adjudicated and which readings this sweep re-grades.**
