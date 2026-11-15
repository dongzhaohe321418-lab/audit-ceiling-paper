# Fresh-eyes review F2 (Claude subagent, unanchored, did not read plan/; 2026-11-15) — score 5/10, confidence 4/5
Acted on (paper commit after 6caefdc):
- Data study (E3) pointed to an appendix describing a different four-table study; its design lived only in an
  un-included file (sections/data.tex). Added the E3 design to Appendix D and cite it from Section 5. Counts checked
  against e3_results_test.json (266 faulty, 266 clean held out; 84/84 dev).
- E14 in the main text now gives the worst-case estimate (19.5 [2.4, 35.4]) and the weaker stratum (+16.7 [-4.2, 36.1]).
- "The models' own solutions" -> two generator models, one also an auditor.
- Exception recrediting labelled post hoc in the Limitations; "no correct program flagged" cites Figure 2a; Claude
  Opus 5.5 named; leftover LaTeX comment removed; a minor vendor sentence cut for space.
Not acted on (recorded): the sentence effect being expected by design (the paper already reports the pointer control
E10 and positive controls); human admissibility check (no human raters); retitling further; restructuring Section 5.
