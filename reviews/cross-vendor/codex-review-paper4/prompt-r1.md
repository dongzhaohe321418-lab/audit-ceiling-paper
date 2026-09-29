You are an INDEPENDENT REVIEWER from a different vendor, acting as an ICML referee. Review the manuscript in the repository `audit-ceiling-paper` at `8f4c04a` (the directory you are in; branch `a4s4-diagnosis`). Do not modify any file.

This branch adds one study to the paper that `reviews/cross-vendor/codex-review-paper3/report-r2.md` reviewed: A4S-4, a held-out, executably adjudicated diagnosis study at a fixed false-positive budget, which that report named as the single change that would most improve the paper. The additions are `git diff 65deecc..8f4c04a -- tex/ manuscript/`; the study's report is `reports/RESULTS-AI4S-DIAG.md`, its registration `plan/studies/ai4s/PREREGISTRATION-DIAG.md`, its records under `records/ai4s/` (`diag_*`, `data_items_ho.json`), and its claim C20 in `manuscript/CLAIMS.md`.

1. Check every added sentence against the report and records; report anything that overstates it or drops a qualification.
2. Check that round 2's other open items (study map cells, re-execution wording, SciCode sample, reproducibility text, redaction) are resolved in `65deecc`.
3. Give an updated overall recommendation as an ICML referee, and the single change that would now most improve the paper.

Findings most severe first, each with file:line and the record involved.
