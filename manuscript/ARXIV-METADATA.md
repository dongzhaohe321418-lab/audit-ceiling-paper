# arXiv submission metadata

Prepared from `main` at e1ae582; package built by `./make_arxiv.sh` → `arxiv/audit-ceiling-arxiv.tar.gz` (tested: builds from a clean directory with pdflatex ×2 and the shipped .bbl).

**Title:** What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data

**Authors:** Zhaohe Dong

**Primary category:** cs.SE (Software Engineering). **Cross-lists:** cs.LG, cs.AI.

**Licence:** the author chooses at submission (CC BY 4.0 suggested; all corpora permit redistribution).

**Comments:** 27 pages, 4 figures, 1 table. Preregistrations, reviews and records: https://github.com/dongzhaohe321418-lab/audit-ceiling-paper

**Abstract (1482 characters; arXiv limit 1920):**

Models increasingly check what other models write. We study one shipped arrangement, in which an auditor from a different vendor reads the work and deterministic checks verify what code can verify, and measure its limits against ground truth no model supplies. On general-purpose code with hidden tests, eight readings of the auditor reach 30.0% recall [20.0, 40.7] at 16.0% [10.1, 22.3] flags on correct code, with diminishing returns and no plateau. The reading model (confounded with its sampling), one rulebook sentence and the decision rule each move that figure, and much of what is missed is, on a post hoc rating, behaviour the specification never determined. In three preregistered science studies, checking that reported numbers trace to their sources flagged all 49 inconsistent reports and none of 25 consistent fabrications, of which the model auditor flagged 23 (21 with a sound finding, post hoc); on data, a documentation-derived validator and the auditor flagged overlapping but different faulty items, together 112 of 140 at a 2.9% [0.7, 5.7] flag rate on clean data; and on scientific code, reframing the task around one step cut flags on correct code from 68.7% to 36.0%. Where both tiers ran, the deterministic one flagged no clean item and could not see consistent error; the model saw some and erred itself. Studies making model calls were preregistered, the two unregistered analyses are named, and every quoted report passed independent cross-vendor review.

## Before submitting

1. The repository cited in the paper and in Comments is private. Make it public (or remove the link) before the arXiv version appears.
2. Upload `arxiv/audit-ceiling-arxiv.tar.gz`, confirm arXiv's compiled PDF matches `arxiv/paper-from-package.pdf`, accept the licence, and submit (these steps need the author's arXiv account).
3. The anonymous ICML build is `tex/paper_submission.tex`; it is not for arXiv.
