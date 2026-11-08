You are a senior ICML area chair and a careful methods reviewer. Review the paper draft in audit-ceiling-paper/tex
(main file paper_v3.tex; sections in tex/sections: introduction_v2, framework, e6, natural, transfer, related_v3,
discussion_v3; appendix tex/appendix/e6_protocol.tex; numbers are macros in tex/numbers.tex generated from the
held-out results). Held-out results are final and in crossaudit-harness/benchmarks/code/records/icml
(e6_results_v4_test.json, e6det_results_v4_test.json, e1_results_test.json, e1_taxonomy_test.json) and
crossaudit-harness/benchmarks/e8/records/e8_results_test.json; registrations are PREREGISTRATION-E6.md and
PREREGISTRATION-E1.md (benchmarks/code/icml) and benchmarks/e8/PREREGISTRATION-E8.md. Read-only.
Report, concisely and with file:line:
1. Every number or claim in the main text that does not match the results files or the registrations, or that
   reports a registered verdict incorrectly (claimed vs not claimed, ordered family).
2. Overclaims: sentences whose strength exceeds the evidence (e.g. exploratory results presented as confirmatory,
   development numbers presented as held-out, inconclusive results read as nulls, causal language).
3. Missing or misleading disclosures a reviewer would expect (deviations, amendments, model judges, same-vendor
   roles, generator overlap, sample sizes).
4. The three most important weaknesses for acceptance at the ICML main track as the paper now stands, and the
   concrete fix for each that is feasible in six weeks.
Do not rewrite prose; list issues.
