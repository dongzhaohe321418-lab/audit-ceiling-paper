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
| records/prose/study6 | benchmarks/expertlongbench/study6 | audit-stage noise floor, K=4 replicates |
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
