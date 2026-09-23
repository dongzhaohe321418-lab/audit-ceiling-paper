**No blocking findings or required corrections.** At `2ea6eee`, `RESULTS-SWEEP.md` is final as an exploratory result.

The revised [H19d paragraph](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-SWEEP.md:174) now survives checking against the records:

- The key contains **190 items: R 128, S 38, B 24**. Both labellers cover all 190 IDs without duplicates.
- Those items trace to R’s first reading, the separate S-text reading, and B’s first reading. Their archived run IDs do not overlap the sweep’s `self-strong` readings.
- The sweep uses `self-strong`’s **eight draws**, with all **70** four-draw subsets at common depth. H19d therefore does not adjudicate the findings counted here.

The numerical and provenance checks also pass. Running the sweep with its write intercepted in memory regenerated the committed JSON **byte-for-byte**. An independent implementation, explicitly enumerating subsets, reproduced **all 86 point-estimate/interval triples**, including the six paired contrasts, at the stated seed and 10,000 resamples. All **80 table cells** containing rates and intervals match the record. The 35 source files are tracked; every included draw covers the same 110 P and 150 C instances, both counts are present, and no rows were dropped. No figure requires a new model call.

The three round-3 repairs are substantive. Similar observed false-positive rates are no longer called a matched operating point or equal cost; the original BLOCKER rule is correctly identified as preregistered; and the subset counts are correctly distinguished as 70 and one.

I found no remaining substantive assertion that a later sentence withdraws. The three `astra` comparisons retain their distinct estimands. C2 remains valid for its original rule and configuration; exploratory re-grading reverses the observed contrast without explaining its cause or resolving the matched-rate ranking. Finding occurrence and defect recognition remain separate, and the limitations no longer deny evidence the records actually provide.

No further readings or numerical revisions are needed for this report. No files were modified.

**Quotable** — the report now confines its conclusions to reproducible, exploratory flag coverage.

Reader sentence: “Exploratory re-grading of the same archived readings reverses the observed `self-strong`–`cross` recall contrast while increasing false positives, showing that flag coverage depends on the grading rule without establishing defect recognition or the ranking at a matched false-positive rate.”
