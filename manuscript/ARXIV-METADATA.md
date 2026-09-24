# arXiv submission metadata

Prepared from `main` (the commit that last changed this file); package built by `./make_arxiv.sh` → `arxiv/audit-ceiling-arxiv.tar.gz` (tested: builds from a clean directory with pdflatex ×2 and the shipped .bbl).

**Title:** What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data

**Authors:** Zhaohe Dong

**Primary category:** cs.SE (Software Engineering). **Cross-lists:** cs.LG, cs.AI.

**Licence:** the author chooses at submission (CC BY 4.0 suggested; all corpora permit redistribution).

**Comments:** 27 pages, 4 figures, 1 table. Preregistrations, reviews and records: https://github.com/dongzhaohe321418-lab/audit-ceiling-paper

**Abstract (1575 characters; arXiv limit 1920):**

Models increasingly check what other models write. We measure how much one shipped arrangement catches, against ground truth no model supplies: an auditor from a different vendor reads the work, and deterministic checks verify what code can verify. On general-purpose code with hidden tests, eight readings of the auditor catch 30.0% [20.0, 40.7] of defective programs that pass their visible tests while flagging 16.0% [10.1, 22.3] of correct ones, with diminishing returns and no plateau. That figure belongs to a configuration, not to the auditor: the reading model and its sampling, one rulebook sentence and the decision rule each move it, and much of what is missed is, on a post hoc rating, behaviour the specification never determined. In three preregistered science studies the two tiers failed in different places. Checking that reported numbers trace to their sources caught all 49 inconsistent reports and none of 25 consistent fabrications; the model auditor flagged 23 of those 25 (21 for the right reason, post hoc). On data, a documentation-derived validator and the auditor flagged overlapping but different faulty items, together 112 of 140 at a 2.9% [0.7, 5.7] flag rate on clean data. On scientific code, naming the step rather than the whole problem as the task cut flags on correct code from 68.7% to 36.0%. Where both tiers ran, every flag on a clean item and every wrong finding came from the model. Studies making model calls were preregistered, the two unregistered analyses are named, and every quoted report passed independent cross-vendor review.

## Before submitting

1. v1 was submitted on 2026-09-24 from the no-link package; the repository is now public, so v2 can use `arxiv/audit-ceiling-arxiv.tar.gz`, which cites it.
2. Upload `arxiv/audit-ceiling-arxiv.tar.gz`, confirm arXiv's compiled PDF matches `arxiv/paper-from-package.pdf`, accept the licence, and submit (these steps need the author's arXiv account).
3. The anonymous ICML build is `tex/paper_submission.tex`; it is not for arXiv.
