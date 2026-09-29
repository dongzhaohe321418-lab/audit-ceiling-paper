# arXiv submission metadata

Prepared from `main` (the commit that last changed this file); package built by `./make_arxiv.sh` → `arxiv/audit-ceiling-arxiv.tar.gz` (tested: builds from a clean directory with pdflatex ×2 and the shipped .bbl).

**Title:** What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data

**Authors:** Zhaohe Dong

**Primary category:** cs.SE (Software Engineering). **Cross-lists:** cs.LG, cs.AI.

**Licence:** the author chooses at submission (CC BY 4.0 suggested; all corpora permit redistribution).

**Comments:** 30 pages, 4 figures, 1 table. Preregistrations, reviews and records: https://github.com/dongzhaohe321418-lab/audit-ceiling-paper

**Abstract (1909 characters; arXiv limit 1920):**

Models increasingly check what other models write. We measure one shipped arrangement against ground truth: an auditor from a different vendor reads the work, and deterministic checks verify what code can verify. On general-purpose code with hidden tests, at least one of eight independent readings flagged 30.0% [20.0, 40.7] of defective programs that pass their visible tests, and 16.0% [10.1, 22.3] of correct ones, with diminishing returns and no plateau. That rate belongs to a configuration, not to the auditor: the auditor route (model and sampling together), one rulebook sentence and the counting rule each move it, and on a post hoc rating most missed programs fail where the specification's prose does not entail the value the hidden suite expects. Three preregistered studies examine scientific code, reported results and data. Checks that every reported number traces to its source flagged every inconsistency and no fabrication written consistently into every artefact; the model auditor flagged nearly all such fabrications, twice on a wrong calculation (on post hoc inspection). On data, a documentation-derived validator and the model flagged overlapping but different faults, so together they covered more than either; on held-out data, at a clean-flag budget fixed in advance, adding the model raised faults whose finding names the injected column by 10.7 points [6.0, 15.9] (scored by code), and on our unblinded post hoc reading 14 of the 15 added items locate the fault correctly. On scientific code with no tests shown, reframing the task around one step sharply reduced flags on correct programs. Where both tiers ran, every flag on a clean item and every wrong finding came from the model, partly by construction of the clean items. Studies making model calls were preregistered, the two unregistered analyses are named, and every quoted report passed independent cross-vendor review.

## Before submitting

1. v1 was submitted on 2026-09-24 from the no-link package; the repository is now public, so v2 can use `arxiv/audit-ceiling-arxiv.tar.gz`, which cites it.
2. Upload `arxiv/audit-ceiling-arxiv.tar.gz`, confirm arXiv's compiled PDF matches `arxiv/paper-from-package.pdf`, accept the licence, and submit (these steps need the author's arXiv account).
3. The anonymous ICML build is `tex/paper_submission.tex`; it is not for arXiv.
