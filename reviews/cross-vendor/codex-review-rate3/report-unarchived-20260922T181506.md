**Not ready to quote.** The arithmetic in `analysis.json` reproduces, but the revision introduces another population-label error and overstates the absence of prior analysis commitments. No files were modified; no model calls were made.

1. **Blocking: the “disjoint, cannot-tell excluded” row is not disjoint.** [Table 1, line 37](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:37) reports the overlapping-sheet sensitivity, +22.6 [2.1, 42.6], under a disjoint-population label. The actual disjoint sensitivity is **38/51 versus 23/48: +26.6 points [4.7, 47.9]**. The cause is explicit in [analyse.py:100](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/analyse.py:100): `secondary` is computed without `disjoint=True`. Accordingly, excluding abstentions moves the disjoint contrast by **+3.3 points**, not +2.7. Either restore the overlapping-row label and denominators or report the actual disjoint calculation.

2. **Blocking provenance overcorrection: the late P1 registration was invalid, but not every underlying choice originated after the result.** Paper commit `d5919b9`, **2026-09-21 20:24:05**, already specified the share of `undetermined` among **all 68 and all 53 entries**, problem-cluster percentile bootstrapping over their union, 10,000 resamples, seed **20260921**, and Wilson intervals. That precedes the committed broken ratings (`4031acd`, September 21, 23:45:23) and rebuilt result (`b0719cd`, September 22, 16:32:20).

   Thus [“Nothing here was registered in advance”](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:89), “neither was chosen in advance,” and the withdrawal document’s blanket statement about the denominator and interval method are too strong. The record supports **earlier commitments to those methods**, followed by a falsely described P1 registration and later analytical additions. It does **not** make the whole revised analysis preregistered: the new seed, disjoint diagnostic and other additions need their actual chronology stated.

   Conversely, [analyse.py:2](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/rate3/analyse.py:2) still claims analysis “exactly as” the withdrawn P1 registration fixed it. The provenance correction has not reached every binding artefact.

3. **The overlap does not affect the two sheet contrasts equally.** [Lines 69–70](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:69) overstate what using identical groups guarantees. Removing the missed-arm duplicates changes:
   - Rebuilt: **19.839 → 23.270**, a **3.431-point** increase.
   - Broken: **54.218 → 57.365**, a **3.148-point** increase.

   The broken-minus-rebuilt difference becomes **34.095**, versus **34.378** with overlap; the ratio becomes **2.465×**, versus **2.733×**. The fixed-sheet comparison remains legitimate descriptively, and its direction survives. Say that; do not claim equal effects or exact cancellation.

4. **“One analysis away from being quoted” is not established by the chronology.** [Line 83](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-RATE3.md:83) omits that P3’s earlier amendment already specified an inconclusive outcome when either arm exceeded one-third `cannot-tell`, and the committed broken-sheet outcome explicitly applied that rule. Quoting it as supporting the premise would have required disregarding that recorded gate. The report can describe the misleading contrast without inventing a near-publication history.

I independently recomputed the following from the CSVs and key, without calling `analyse.py`’s calculation functions. All intervals below use 10,000 problem-cluster resamples and seed 20260922.

| Reading | First group | Caught group | Difference, points | 95% percentile interval |
|---|---:|---:|---:|---:|
| Rebuilt, overlapping | 43/68, 63.2% | 23/53, 43.4% | +19.8 | [1.5, 38.2] |
| Rebuilt, disjoint | 38/57, 66.7% | 23/53, 43.4% | +23.3 | [2.4, 44.0] |
| Overlapping, abstentions excluded | 43/61, 70.5% | 23/48, 47.9% | +22.6 | [2.1, 42.6] |
| **Disjoint, abstentions excluded** | **38/51, 74.5%** | **23/48, 47.9%** | **+26.6** | **[4.7, 47.9]** |
| Broken, overlapping | 42/68, 61.8% | 4/53, 7.5% | +54.2 | [38.8, 69.8] |

The four stored contrasts, their Wilson intervals, problem counts and successful-resample counts match independently. Clustering by `problem_id` is appropriate: it keeps both candidate batches and cross-arm copies of a problem together. There are 56 clusters for the full readings, 53 for the overlapping sensitivity and 52 for the actual disjoint sensitivity.

The other requested checks resolve as follows:

- **The denominator rule is defensible for the stated estimand:** the fraction of entries *labelled* `undetermined`. Abstentions are not thereby classified as determined. Exclusion estimates a different, conditional fraction. Its smaller contrast here does not establish that the rule is generally conservative.
- **The instruments really differ.** I verified the comparator’s consensus counts, 46/68 and 24/53, yielding +22.364 points. Differences include raters, available evidence, hierarchy and response options. The revised prose does not subsequently use numerical closeness as corroboration.
- **The exploratory scope is substantially repaired.** “Evidence about sheets” is appropriate for the observed association; the report no longer turns it into evidence that specifications themselves changed. The 67 label changes, split 21/46, and rate movements +1.47/+35.85 all reproduce. A repair plus a fresh model run does not isolate the causal effect of presentation. Indeed, six of the eleven identically presented duplicate-instance pairs received different rebuilt labels.
- **The repair applies symmetric rules, with imperfect resulting material.** All specifications and visible tests match the key, allowing outer whitespace. The same witness selection and formatting operate in both arms; all eleven overlapping witness records match. Concrete inputs exist for 61/68 and 49/53; the remaining cases are exactly five timeouts plus two unrecovered inputs, and four timeouts.
- **Preserving H003/H117 is correct.** Editing the artefact retrospectively would misdescribe what was rated. However, these caught-arm defects are absent from the report’s limitations and should be disclosed. Also, `rebuild_sheet.py`’s claim of “the same information content” as the old prose classes is unsupported: some old descriptions explicitly described oracle behaviour, whereas the replacement supplies concrete inputs.
- **The outside-human limitation survives the revised report.** I found no sentence reclaiming delivery of P1’s human independence. L1’s coverage of 121 entries/110 instances also checks out.

**not quotable — the revised table still presents an overlapping-group estimate as a disjoint-population result.**
