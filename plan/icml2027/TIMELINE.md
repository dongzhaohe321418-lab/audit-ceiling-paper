# ICML 2027 timeline (2026-11-08)

Official call not yet posted (icml.cc: "will be posted soon"). Third-party trackers project abstract ~2027-01-16 and
full paper ~2027-01-22 AoE (estimate from the previous cycle); ICML 2025's rule was 8 pages of main text, references,
impact statement and appendices unlimited. Re-check icml.cc before relying on any date. Current main text: ~7.3
pages (dev placeholders).

The binding constraint is the Codex (GPT) quota, exhausted until 2026-11-11 18:26. Order of GPT use after the reset:

| When (target) | Step | GPT use |
|---|---|---|
| 11-11 to 11-12 | E6 construction top-up (1 control), refreeze; E1 333 retries, witnesses, bridge | small |
| 11-12 | GPT review P8 (E6 release, E1 Amendment 5, E8) | 1 long call |
| 11-13 to 11-16 | E6 held-out audits (4,528 readings, half GPT), witnesses, analysis; E8 (Claude only) | ~2,300 calls |
| 11-16 | E1 held-out analysis (main, taxonomy, bridge) | none |
| 11-17 to 11-30 | E7 construction (121 tasks), go/no-go; if go: preregistration, GPT review, held-out audits | ~1,500 calls |
| 12-01 to 12-15 | Fill numbers, figures from held-out results, trim, full draft | none |
| 12-15 to 01-10 | GPT methods review of the paper, GPT + Claude humanisation rounds, citations audit | few long calls |
| 01-10 to 01-16 | Final checks, anonymity, abstract registration (needs the author's account: user action) | none |

Fallback (user's second choice): a workshop, or TMLR, if the held-out results or E7 do not support a main-track
claim. Submission itself requires the user's OpenReview account and approval; Claude never logs in.

## Decision (2026-11-08)
Venue: ICML 2027 main track with the current paper (the user's stated first choice; human semantic validation was
declined by the user and is reported as a limitation). Fallback: a workshop or TMLR if rejected or if the official
call changes the requirements. Ready: paper (tex/paper_v3.pdf, anonymous build tex/paper_v3_submission.tex),
supplementary (audit/supplementary/supplementary_anon.zip), citation audit. Remaining, user only: re-check the official
call on icml.cc when posted, and submit through the user's OpenReview account (Claude never logs in).

## Official call (posted 2026-11-14; supersedes the estimates above)
Source: icml.cc/Conferences/2027/CallForPapers, AuthorInstructions, UseOfGenerativeAIByAuthors.
- Submission site opens 2027-01-08; OpenReview account suggested by 2027-01-08 (institutional email activates at
  once, other emails can take up to two weeks).
- Abstract deadline 2027-01-14 23:59 AoE; full paper 2027-01-22 23:59 AoE; supplementary material has no separate
  deadline (same as the paper).
- Two-stage review: first-stage rejections notified by 2027-02-23; final decisions 2027-05-03. Conference: Rio de
  Janeiro, 31 July to 6 August 2027.
- Format: 8 pages of main text; references, impact statement and appendices unlimited, one PDF (at most 50 MB);
  official 2027 style files; Type-1 fonts requested. ICML will announce submission-process changes (not format
  changes) by late November 2026: re-check then.
- Required unnumbered sections: Impact Statement (before references) and AI Disclosure Statement (before or after
  references; not counted in pages; must describe substantive AI use and how outputs were verified).
- Quotas: each submission designates one author as reciprocal reviewer; an author may appear on at most one
  submission in which no author is an eligible reciprocal reviewer (so a sole-author paper is allowed once).
- Preprints are allowed; the submission must not cite the non-anonymous version, and code links must be anonymous
  (upload the zip as supplementary material instead).

Done on 2026-11-14: switched to icml2027.sty/.bst (identical to 2026 apart from the year); replaced "Use of AI
models" with an AI Disclosure Statement under the 2027 policy; regenerated the four appendix figures with embedded
TrueType instead of Type-3 fonts (same records, same content). Both builds compile; main text ends on page 8;
anonymous build has no identifying strings. Body text now uses the template's Type-1 Times (Nimbus) via T1 fontenc under XeTeX; figure text is embedded TrueType (no Type 3). Contribution type to choose at submission: Datasets, Evaluations and
Benchmarks (or General ML).
