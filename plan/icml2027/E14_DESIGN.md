# E14 design: rule x code form (draft, 2026-11-15)

## Why
GPT's re-review after E13 (reviews/review_gpt_M4.md, 7/10) names the remaining confound of the convention finding:
E13 added a branch to B and found little effect (+0.6 [-1.2, 2.5]), but the residual preference against B' (+20.6)
is still concentrated where A has more conditionals, so A's own implementation may be what draws flags. Its
highest-value suggestion: rewrite both programs symmetrically into ordinary and conspicuous forms and audit afresh.

## Design (on E6's registered units, reusing E13's machinery)
Four programs per unit, two rules x two forms:
- B (E6's, minimal for the benchmark's rule) and B' (E13's: B plus an explicit branch for the class);
- A_min: A rewritten to compute exactly A's behaviour with as few conditionals as possible and no branch dedicated to
  the class inputs (for example folding the special case into the general expression); checked equal to A on every
  registered input; the check records whether A_min has no more conditionals than B;
- A_br: A with an explicit branch for the class computing A's behaviour, every other line kept (E13's rule).
Fresh, interleaved readings of all four (and A as a link to E6), E6's task-alone arm, four configurations, two
readings per cell (40 per unit).

## Hypotheses (held out; E6's code and bounds)
- E14-1 (primary): preference with the form matched and minimal, flag(A_min) - flag(B): positive lower limit and
  bound means the preference does not need A's extra code.
- E14-2: preference with the form matched and conspicuous, flag(A_br) - flag(B').
- E14-3: form effect within rule A, flag(A_br) - flag(A_min), and the rule x form interaction.
Units where A_min cannot reach B's number of conditionals are reported separately (prespecified stratum).

## Steps
Development pilot of the A_min and A_br prompts and checks (16 units); preregistration; GPT review; construction on
held-out units; freeze; audits; analysis; paper (one sentence in Section 4, appendix paragraph, verdict rows).
