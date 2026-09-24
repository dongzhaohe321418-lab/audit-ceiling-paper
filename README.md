# What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data

The manuscript is `tex/paper.tex` (the anonymous ICML build is `tex/paper_submission.tex`); the
claims it is willing to defend, and the ones it must not make, are in `manuscript/CLAIMS.md`.
`./make_arxiv.sh` builds the arXiv source package and proves it compiles from a clean directory;
`manuscript/ARXIV-METADATA.md` has the submission metadata.

## Reproduce

    ./reproduce.sh

Regenerates Figures 1–4 and Table 1 from the records in this repository, checks that each
regenerated figure and the table are byte-identical to the copies the paper compiles, and runs
the manuscript's claims check. Script names follow the order the figures were made, not their
numbers in the paper: `figures/src/make_figures.py` makes Figure 1, `make_fig4_ai4s.py` Figure 2,
`make_fig2_sweep.py` Figure 3 and `make_fig3_residual.py` Figure 4. No model calls, no network, no path outside the checkout; it has been run from a
fresh clone with `HOME` unset to prove that. Needs `python3`, `matplotlib` and `scienceplots`.
The coverage simulation behind the methods table is slower and is regenerated separately with
the command printed in `reproduce.sh`.

## Inventory — each admitted claim, where it came from, and who reviewed it

| claim | study | report (`reports/`) | cross-vendor review | records (`records/`) |
|---|---|---|---|---|
| C1, C5, C6 | ceiling 1 | `RESULTS-CEILING.md` | `reviews/harness/2026-09-0*-ceiling-study-astra*.md` | `code/ceiling/numbers.json` |
| C2 | study 18 | `RESULTS-CEILING3.md` | `reviews/harness/2026-09-10-ceiling3-r*.md` | `code/ceiling3/numbers.json` |
| C3 | ceiling 2 | `RESULTS-CEILING.md` | as C1 | `code/ceiling/numbers.json` |
| C4 | study 21 | `RESULTS-RERATE.md` | `reviews/harness/2026-09-1*-rerate*.md` | `code/rerate/` |
| C7 | study 17 | `RESULTS-TESTGEN-VAL.md` | `reviews/harness/2026-09-09-testgen*`, `reviews/cross-vendor/codex-review-testval8/` | `code/testgen-val/` |
| C8 | study 19 | `RESULTS-CEILING3B.md` | `reviews/cross-vendor/codex-review-c3br8/` | `code/ceiling3b/` |
| C9 | study 20 | `RESULTS-CEILING4.md` | `reviews/cross-vendor/codex-review-c4r1/` | `code/ceiling4/numbers.json` |
| C10 | study 22 | `RESULTS-INJECT.md` | `reviews/cross-vendor/codex-review-inject1/` | `code/inject/` |
| C11 | P2 | `RESULTS-SWEEP.md` | `reviews/cross-vendor/codex-review-sweep1/` | `code/threshold_sweep.json` |
| C12 | P1 | `RESULTS-RATE3.md` | `reviews/cross-vendor/codex-review-rate3/` | `code/rate3/analysis.json` |
| C13 | P3 | `RESULTS-CLARIFY.md` | `reviews/cross-vendor/codex-review-clarify1/` | `code/clarify/` |
| C14, C15 | derived quantities | `RESULTS-DERIVED.md` | `reviews/cross-vendor/codex-review-paper1/` | `code/rerate/`, `code/ceiling4/numbers.json`, `coverage_simulation.json` |
| C16 | P4 | `RESULTS-FPADJ.md` | `reviews/cross-vendor/codex-review-fpadj1/` | `code/fpadj/adjudication.json` |
| C17 | A4S-3, scientific data | `RESULTS-AI4S-DATA.md` | `reviews/cross-vendor/codex-review-a4s3/` | `ai4s/data_*.json` |
| C18 | A4S-2, scientific results | `RESULTS-AI4S-RESULTS.md` | `reviews/cross-vendor/codex-review-a4s2/` | `ai4s/results_*.json` |
| C19 | A4S-1 and A4S-1b, scientific code | `RESULTS-AI4S-CODE.md` | `reviews/cross-vendor/codex-review-a4s1/` | `ai4s/strata.json`, `ai4s/code_*.json`, `ai4s/residual*` |
| none | study 23, closed | `RESULTS-SUBSTRATE2.md` | `reviews/cross-vendor/codex-review-sub2r1/` | — |

Every quoted study's records are under `records/`; where no figure or table script reads them,
the paper quotes their numbers in prose, and `records/PROVENANCE.md` names the harness commit
each copy was taken from. The science studies' raw readings are in `records/ai4s/runs/`. Early review rounds, archived in the harness, are mirrored in `reviews/harness/`;
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
    plan/         the P1 and P3 registrations; plan/studies/ every other study's preregistration,
                  plan/studies/ai4s/ the science studies' (the severity sweep was never
                  registered, and is post hoc throughout)

## Licences

This repository's own code (`analysis/`, `figures/`, the shell scripts) is MIT-licensed
(`LICENSE`). The manuscript, preregistrations, reviews and records written for this project are
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Third-party corpora keep their own
licences:
the paper's corpora are HumanEval (MIT), HumanEval+ and MBPP+ (Apache-2.0), SciCode
(Apache-2.0), four UCI datasets (CC BY 4.0: concrete, airfoil, combined-cycle power plant,
superconductivity) and, for the closed study 23, BigCodeBench (Apache-2.0); their test inputs
appear in some records. The prose
studies under `records/prose/`, which this paper does not use, derive from ExpertLongBench
(CC BY-NC-SA 4.0); those records carry ids, hashes and scores only, and the raw runs are not
redistributed.
