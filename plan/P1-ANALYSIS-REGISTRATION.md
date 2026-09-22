# P1 — registration of the analysis, written before it was run (2026-09-22)

## What this registers, and what it cannot

The 121 ratings in `records/rate3/L3.csv` **already existed** when this was written: `L3` finished
labelling the rebuilt sheet at 16:30 today. Registering an analysis after its data exists is
weaker than registering it before, and saying otherwise would be false.

What is true, and is the reason to write this now: **no analysis script exists and no contrast
has been computed.** I have seen the sheet, the label distribution over all 121 items
(`determined` 43, `undetermined` 66, `cannot-tell` 12) and the arm sizes (68 missed, 53 caught).
I have not seen either arm's rate, and every rule below is fixed before I do.

## The honest limitation, first

The plan asks P1 for **a human from outside the project**, blind, because the existing
+22.4-point contrast was rated by a model and the author, and so establishes the direction of
C4 rather than its independence. `L3` is `gpt-6-astra`. **It is a third model, not an outside
human, and this analysis therefore does not deliver the independence P1 exists to provide.**
What it delivers is a third rating on a sheet whose control arm was unanswerable until today,
by a rater that is not the author. The outside human remains owed.

## The instruments are not the same instrument

The existing figures — `ambiguous-oracle` on 46 of 68 missed (67.6%) against 24 of 53 caught
(45.3%), a difference of +22.4 points — come from a **six-category** rating in which
`ambiguous-oracle` was one option among `unexercised-edge`, `disputed`, `timeout` and others.
`L3` answered a **three-option** rubric: `determined` / `undetermined` / `cannot-tell`.

A rater choosing among six categories and a rater choosing among three are not performing the
same task, and their rates are not interchangeable. The two are reported **side by side and
labelled as different instruments**. Neither is described as a replication of the other, and no
difference between them is reported as a change in what the specifications say.

## The contrasts, fixed now

1. **Primary.** The proportion of items labelled `undetermined`, missed arm minus caught arm,
   with `cannot-tell` counted in the denominator and not in the numerator — the same treatment
   the six-category table gave to its non-`ambiguous-oracle` labels. Interval: percentile
   bootstrap over **problem clusters**, 10,000 resamples, seed 20260922. Wilson reported beside
   it and marked too narrow, as everywhere else in this programme.
2. **Secondary.** The same contrast with `cannot-tell` items excluded from both arms. Reported
   whatever it shows. It is not the primary, and if the two disagree, both are reported and
   neither is chosen afterwards.
3. **Exploratory — what the broken sheet cost.** `L3` rated the *unanswerable* version of this
   sheet earlier today (`L3-broken-sheet.csv`), where 42 of 53 caught items carried no failing
   input class at all. Comparing the two gives a direct reading of how much an unanswerable
   control arm moved the contrast. It is exploratory, reported as a count and a difference, and
   **it is not evidence about specifications** — it is evidence about sheets.

## Stopping rule

All three are reported whatever they show, including a primary contrast that excludes zero in
the wrong direction, or one that contains zero. This analysis buys no model readings, costs
nothing, and there is nothing to stop.
