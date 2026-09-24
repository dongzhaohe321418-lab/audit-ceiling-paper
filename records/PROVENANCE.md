# Records provenance

Mirrored from `dongzhaohe321418-lab/crossaudit-harness` (local branch
`fusion/evidence-authority`) at commit `e7d03c271dca41aa05b04d9aec30544d590f630c` on 2026-09-05. Each study's own
`manifest.json` names the commit it was produced at.

| here | source | study |
|---|---|---|
| records/code/study1 | benchmarks/code/records/study1 | audit vs hidden tests, EvalPlus, model-free truth |
| records/code/study2 | benchmarks/code/records/study2 | decomposed vs holistic (n=110) |
| records/code/explore | benchmarks/code/records/explore | 15 architectures under a preregistered FP constraint |
| records/code/checks | benchmarks/code/records/checks | can the auditor emit executable checks (kill fired) |
| records/prose/study5 | benchmarks/expertlongbench/study5 | cross-vendor premise (self / sibling / cross), n=30; the generation-inclusive floor SD 1.84 |
| records/prose/study6 | benchmarks/expertlongbench/study6 | audit-stage noise floor, K=4 replicates |
| records/prose/gate | benchmarks/expertlongbench/records/gate | oracle revision gate replay, 86 transitions |
| CORRECTIONS.md | benchmarks/CORRECTIONS.md | every withdrawn number, with evidence |
| reviews/ | benchmarks/reviews | independent cross-vendor reviews, verbatim |

Prose records carry ids, hashes, scores and counts only; the ExpertLongBench
corpus and any model output containing it stay in the local archive named in
`ARCHIVE_MANIFEST.json`. EvalPlus records may carry solutions (MIT / Apache).

## Corpus check

`python3 analysis/corpus_scan.py` lists every string field over 60 characters
in the prose records, by field name, with its longest value, and exits 1 if a
free-text field is present. Run on 2026-09-05: the longest strings are git
status lines, provider error messages, methodology prose from manifests, and
sha256 digests. The only dataset-derived strings are rubric-item labels of at
most 78 characters, which this project treats as identifiers. No draft,
prompt, passage, or model output text is present.

## Two provenance files

`PROVENANCE.md` at the repository root names the product commit the **standards**
(`EXPERIMENT_RECORD.md`) were copied at; this file names the commit the
**records** were mirrored at. They differ whenever the standard was updated
after the records were mirrored, or the reverse. Each study's own
`manifest.json` remains the authority for the commit it was produced at.

## Mirror added 2026-09-23 (R3-M3: the paper must regenerate from a clean checkout)

Every source was a clean checkout at the commit named.

| here | source | commit |
|---|---|---|
| records/code/ceiling/numbers.json | harness `benchmarks/code/records/ceiling/` | `e510057` |
| records/code/ceiling3/numbers.json | harness `benchmarks/code/records/ceiling3/` | `e510057` |
| records/code/ceiling4/numbers.json | study/ceiling4 worktree `benchmarks/code/records/ceiling4/` | `05b433f` |
| records/code/rerate/ (numbers, keys, L1/L2 labels) | harness `benchmarks/code/records/rerate/` | `e510057` |
| records/code/rate3/analysis.json | harness `benchmarks/code/records/rate3/` | `e510057` |
| records/code/clarify/ (h3, manipulation check, agreement, classification, population) | harness `benchmarks/code/records/clarify/` | `e510057` |
| records/code/threshold_sweep.json | harness `benchmarks/code/records/` | `e510057` |
| reports/RESULTS-{CEILING,CEILING3,RERATE,RATE3,CLARIFY,SWEEP}.md | harness `benchmarks/code/` | `e510057` |
| reports/RESULTS-CEILING3B.md | wt-ceiling3b | `92e0bc7` |
| reports/RESULTS-CEILING4.md | wt-ceiling4 | `05b433f` |
| reports/RESULTS-INJECT.md | wt-inject | `a39eeaa` |
| reports/RESULTS-SUBSTRATE2.md | wt-sub2 | `7d7fb2c` |
| reports/RESULTS-TESTGEN-VAL.md | wt-testval | `036f2dc` |
| reviews/harness/ | harness `benchmarks/reviews/`, paper-study files only | `e510057` |
| reviews/cross-vendor/<queue>/ | `codex-review-queue/<queue>/` prompts, reports and model, not in any repository before | 2026-09-23 |

The code-study corpora (HumanEval MIT; HumanEval+, MBPP+, BigCodeBench Apache-2.0) permit
redistribution, so these records may carry test inputs. Scanned for credentials before commit.

| records/code/fpadj/{adjudication,extraction_audit,sensitivity_nonliteral}.json | harness `benchmarks/code/records/fpadj/` | `2d20b9f` |
| reports/RESULTS-FPADJ.md | harness `benchmarks/code/` | `2d20b9f` |
| plan/studies/fpadj-PREREGISTRATION.md | harness `benchmarks/code/fpadj/` (with Amendment 1) | `2d20b9f` |

## Science studies (records/ai4s)

Mirrored from `dongzhaohe321418-lab/crossaudit-harness`, `benchmarks/code/records/ai4s/`, at the
commits each study's report became quotable (the reports in `reports/RESULTS-AI4S-*.md` are
byte-identical copies from the same commits):

| here | harness branch | commit | study |
|---|---|---|---|
| records/ai4s/data_*.json | study/ai4s-code | 6c4bdbb | A4S-3, scientific data |
| records/ai4s/results_*.json | study/ai4s-results | e3baa55 | A4S-2, scientific results |
| records/ai4s/strata.json, code_*.json, residual* | study/ai4s-codeaudit | cb3b8d9 | A4S-1 and A4S-1b, scientific code |

Raw readings are mirrored in `records/ai4s/runs/` (copied 2026-09-24 from the run archive
`~/Documents/Crossaudit/ai4s/runs/`): audited items, readings, rating sheets (which quote SciCode,
Apache-2.0) and logs. The product rulebook copies inside it are the harness's published templates. Home-directory prefixes in logs and tracebacks were replaced by `~`; readings keep each
BLOCKER's text, and non-blocking findings are counted without their text. The final analysis
scripts are mirrored in `records/ai4s/analysis/` (see its README); `runs/analysis/` holds earlier
snapshots.

## General-code records mirrored 2026-09-24

| here | harness branch | commit | study |
|---|---|---|---|
| records/code/testgen-val/ | study/testgen-val | 036f2dc | study 17, test validation (C7) |
| records/code/ceiling3b/ | study/ceiling3b | 92e0bc7 | study 19 (C8) |
| records/code/inject/ | study/injection | a39eeaa | study 22 (C10) |

## A4S-4 (held-out diagnosis), mirrored 2026-09-24 — pending review

| here | harness branch | commit |
|---|---|---|
| records/ai4s/data_items_ho.json, diag_results.json, diag_calibration_dev.json, diag_readings/ | study/ai4s-diagnosis | 25071d0 |
| records/ai4s/analysis/diag-25071d0/ | study/ai4s-diagnosis | 25071d0 |
| reports/RESULTS-AI4S-DIAG.md, plan/studies/ai4s/PREREGISTRATION-DIAG.md | study/ai4s-diagnosis | 25071d0 (registered at a6c04af) |
