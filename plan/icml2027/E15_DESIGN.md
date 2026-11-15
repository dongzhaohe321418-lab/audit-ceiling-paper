# E15 design: matched pairs with symmetric branch bodies (draft, 2026-11-15)

## Why
E14 (held out) matched all code outside one branch body: M_A was flagged 28.9 [14.5, 42.8] points more often than M_B
(n=38; worst case 19.5 [2.4, 35.4]). Review M5 named the remaining difference: the two branch bodies can differ in
form (a loop against a single `return`; M_A's body longer in 9 of 38 pairs), and the preference is larger where A's
rule needs more code (+40.0 against +16.7). E15 removes that difference by construction. Decided 2026-11-15 while
the human admissibility check (H1) waits for the rater; E15 needs no human input.

## Design (E14's machinery, one added constraint)
The same matched-pair prompt, plus: inside the differing `if` body, both programs use the same statements in the
same order, of the same syntactic kinds (AST node types, depth 1), differing only in expressions; their token counts
differ by at most a factor of 1.5 (or 4 tokens). Checks: E14's (same AST position and condition, masked trees
identical, identical source outside the body, execution equality with A and B on every registered admission input,
separation on at least two valid class inputs, visible tests) plus the body-form check. Programs read afresh,
interleaved: A, B, M_A, M_B (as E14), task-alone arm, E6's four configurations, two readings per cell.

## Hypotheses (held out; E6's code; worst-case missing-unit rule as E14)
- E15-1 (primary): flag(M_A) - flag(M_B) with symmetric bodies; positive if the worst-case lower limit is above 0.
- Reported: E15-1 in E13's code-shape strata; A - B in the same readings; body sizes.

## Steps
e15.py (imports e14, adds the body-form check and prompt line; e14.py stays frozen); development pilot; preregistration;
GPT review; held-out construction; freeze; audits; analysis; paper (one clause in Section 4, appendix paragraph,
verdict row, figure row).
