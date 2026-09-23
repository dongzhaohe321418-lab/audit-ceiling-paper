# What moves the ceiling on automated code audit

Private until release with the paper. The manuscript is `tex/paper.tex`; the claims it is
willing to defend, and the ones it must not make, are in `manuscript/CLAIMS.md`.

## Reproduce

    ./reproduce.sh

Regenerates Figures 1–3 and Table 1 from the records in this repository, checks that the
regenerated table is byte-identical to the one the paper compiles, and runs the manuscript's
claims check. No model calls, no network, no path outside the checkout; it has been run from a
fresh clone with `HOME` unset to prove that. Needs `python3`, `matplotlib` and `scienceplots`.
The coverage simulation behind the methods table is slower and is regenerated separately with
the command printed in `reproduce.sh`.

## Inventory — each admitted claim, where it came from, and who reviewed it

| claim | study | report (`reports/`) | cross-vendor review | records (`records/code/`) |
|---|---|---|---|---|
| C1, C5, C6 | ceiling 1 | `RESULTS-CEILING.md` | `reviews/harness/2026-09-0*-ceiling-study-astra*.md` | `ceiling/numbers.json` |
| C2 | study 18 | `RESULTS-CEILING3.md` | `reviews/harness/2026-09-10-ceiling3-r*.md` | `ceiling3/numbers.json` |
| C3 | ceiling 2 | `RESULTS-CEILING.md` | as C1 | `ceiling/numbers.json` |
| C4 | study 21 | `RESULTS-RERATE.md` | `reviews/harness/2026-09-1*-rerate*.md` | `rerate/` |
| C7 | study 17 | `RESULTS-TESTGEN-VAL.md` | `reviews/harness/2026-09-09-testgen*`, `reviews/cross-vendor/codex-review-testval8/` | not mirrored |
| C8 | study 19 | `RESULTS-CEILING3B.md` | `reviews/cross-vendor/codex-review-c3br8/` | not mirrored |
| C9 | study 20 | `RESULTS-CEILING4.md` | `reviews/cross-vendor/codex-review-c4r1/` | `ceiling4/numbers.json` |
| C10 | study 22 | `RESULTS-INJECT.md` | `reviews/cross-vendor/codex-review-inject1/` | not mirrored |
| C11 | P2 | `RESULTS-SWEEP.md` | `reviews/cross-vendor/codex-review-sweep1/` | `threshold_sweep.json` |
| C12 | P1 | `RESULTS-RATE3.md` | `reviews/cross-vendor/codex-review-rate3/` | `rate3/analysis.json` |
| C13 | P3 | `RESULTS-CLARIFY.md` | `reviews/cross-vendor/codex-review-clarify1/` | `clarify/` |
| none | study 23, closed | `RESULTS-SUBSTRATE2.md` | `reviews/cross-vendor/codex-review-sub2r1/` | — |

"Not mirrored" means the paper quotes that claim's numbers in prose but no figure or table
script reads them; they are in the study's own record at the commit named in
`records/PROVENANCE.md`. Early review rounds, archived in the harness, are mirrored in `reviews/harness/`;
later rounds of every queue live under `reviews/cross-vendor/<queue>/` as `prompt-rN.md` and
`report-rN.md`, verbatim, refusals included. `codex-review-blind1` is the blinded-review
experiment, withdrawn because it was not blind (`notes/blinded-review-experiment.md`).

## Layout

    tex/          the manuscript; tex/table1.tex is generated
    manuscript/   CLAIMS.md, the ledger every quoted number must pass
    reports/      each study's results report, mirrored at the commit in records/PROVENANCE.md
    reviews/      every independent review, verbatim
    records/      derived records: counts, labels, hashes, intervals
    figures/      figure and table scripts; outputs are generated, never hand-edited
    analysis/     the manuscript check and the coverage simulation
    plan/         the P1 and P3 registrations; plan/studies/ every other study's preregistration
                  (the severity sweep was never registered, and is post hoc throughout)

## Licences

The paper's corpora are HumanEval (MIT), HumanEval+ and MBPP+ (Apache-2.0) and, for the closed
study 23, BigCodeBench (Apache-2.0); their test inputs appear in some records. The prose
studies under `records/prose/`, which this paper does not use, derive from ExpertLongBench
(CC BY-NC-SA 4.0); those records carry ids, hashes and scores only, and the raw runs are not
redistributed.
