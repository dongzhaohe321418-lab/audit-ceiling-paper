# Derived quantities the manuscript quotes that no study report carried

Written 2026-09-23 because the first whole-manuscript review (`reviews/cross-vendor/codex-review-paper1/report-r1.md`,
finding 1) found three numbers in `tex/` that entered without passing through the ledger's
admission rule. Each is a computation over records already reviewed; the computation itself was
not. They stay out of the admitted claims until a review of **this** report ends quotable. All
are **post hoc** and registered nowhere.

## 1. The residual's composition at six families

**Inputs, both reviewed.** Study 20's `H20d_residual` (`records/code/ceiling4/numbers.json`,
C9): after six families and 40 readings (`cross` 8, `self` 8, `astra` 4, `self-strong` 8,
`self-frontier` 4, `cross-R` 8) the never-flagged set is **32 of 110** instances on 56 problems.
Study 21's labels (`records/code/rerate/`, C4): each rated instance's `L1` and `L2` label.

**Computation.** `six_family_residual()` in `figures/make_table1.py`, run by `reproduce.sh`.
An instance is consensus-undetermined when both `L1` and `L2` say `ambiguous-oracle`. The script
asserts every one of the 32 was rated.

| quantity | value |
|---|---|
| consensus-undetermined instances, all rated | **68** |
| of those, still in the six-family residual | **25** |
| so flagged by some reading of some family | **43 of 68** |
| six-family residual size | **32** |
| undetermined share of the six-family residual | **25 of 32 = 78.1%** |
| the same share at three families (study 21, reviewed) | 44 of 57 = 77.2%, cluster [62.1, 91.1] |

No interval is computed for 25 of 32. The two shares are not independent — the 32 are a subset
of the 57 — so their closeness is a description, not a test of stability.

**What it licenses.** That being consensus-undetermined is not sufficient for being missed (43 of
68 were flagged by some family), and that the residual shrinks from 57 to 32 while its
undetermined share stays near three quarters. It does not license a claim that the share is
stable in a population sense.

## 2. The bootstrap coverage table

**Computation.** `analysis/coverage_simulation.py --reps 400 --boots 600 --seed 20260923`,
record `records/coverage_simulation.json`. Two designs with the strata's actual cluster profiles
(110 instances in 56 problems; 150 in 143), within-problem concordance 0.5, seven true rates;
each cell is the share of 400 simulated datasets whose 600-resample percentile problem-cluster
interval covers the true rate. Monte Carlo standard error about 0.011.

**What it licenses.** Coverage of **single-rate** intervals under that correlation model:
near nominal (0.93–0.97) at true rates of 0.10 and above, 0.80 at 0.03 on the 56-cluster
stratum. It says nothing about the paired contrasts or category-conditioned shares in Table 1,
and the concordance of 0.5 is an assumption, not an estimate.
