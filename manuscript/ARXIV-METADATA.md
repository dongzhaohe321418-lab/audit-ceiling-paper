# arXiv submission metadata

Prepared from `main` at 6fbf0b0; package built by `./make_arxiv.sh` → `arxiv/audit-ceiling-arxiv.tar.gz` (tested: builds from a clean directory with pdflatex ×2 and the shipped .bbl).

**Title:** What Moves the Ceiling on Automated Audit: from General Code to Scientific Code, Results and Data

**Authors:** Zhaohe Dong

**Primary category:** cs.SE (Software Engineering). **Cross-lists:** cs.LG, cs.AI.

**Licence:** the author chooses at submission (CC BY 4.0 suggested; all corpora permit redistribution).

**Comments:** 27 pages, 4 figures, 1 table. Preregistrations, reviews and records: https://github.com/dongzhaohe321418-lab/audit-ceiling-paper

**Abstract (1848 characters; arXiv limit 1920):**

When models write code, report results and prepare data, other models increasingly check them. We study one shipped arrangement for doing so, in which an auditor from a different vendor reads the work and deterministic checks verify what code can verify, and we measure what limits it against ground truth no model supplies. On general-purpose code with hidden test suites, eight readings of the shipped auditor reach 30.0% union recall [20.0, 40.7] at 16.0% flags on correct code, and returns diminish without a plateau. Which model reads, one added rulebook sentence, and the decision rule each move that figure (the model contrast confounded with sampling), and on a post hoc rating much of what is missed is behaviour the specification never determined, so a recall figure is a property of auditor, rulebook, rule and benchmark together. We then test the arrangement on science, in three preregistered studies. On reported results, checking that every number traces to its source flagged all 49 inconsistencies among report, results and log and none of 25 results that were wrong consistently; the model auditor flagged 23 of those 25, 21 with a sound finding (post hoc). On data, a validator written from the documentation and the auditor flagged different faulty items (92 and 65 of 140) and together 112, at the auditor's 2.9% flag rate on clean data. On scientific code with no tests shown, reframing the task around the step rather than the whole problem cut the auditor's flags on correct code from 68.7% to 36.0% on the same programs. Where both tiers ran, the deterministic one flagged no clean item and could not see consistent error; the model saw some of it and erred itself. Every study that made model calls was preregistered, the two unregistered analyses are named, and every report quoted passed independent cross-vendor review.

## Before submitting

1. The repository cited in the paper and in Comments is private. Make it public (or remove the link) before the arXiv version appears.
2. Upload `arxiv/audit-ceiling-arxiv.tar.gz`, confirm arXiv's compiled PDF matches `arxiv/paper-from-package.pdf`, accept the licence, and submit (these steps need the author's arXiv account).
3. The anonymous ICML build is `tex/paper_submission.tex`; it is not for arXiv.
