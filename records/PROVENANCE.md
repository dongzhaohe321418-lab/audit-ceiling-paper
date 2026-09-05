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
