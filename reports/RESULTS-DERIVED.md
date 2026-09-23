# Derived quantities the manuscript quotes that no study report carried

Written 2026-09-23 because the first whole-manuscript review (`reviews/cross-vendor/codex-review-paper1/report-r1.md`,
finding 1) found three numbers in `tex/` that entered without passing through the ledger's
admission rule. Each is a computation over records already reviewed; the computation itself was
not. They stayed out of the admitted claims until a review of **this** report ended quotable, which
round 2 of the manuscript review did for both sections (`codex-review-paper1/report-r2.md`),
with the two corrections now made below. All
are **post hoc** and registered nowhere.

## 1. The residual's composition at six families

**Inputs, both reviewed.** Study 20's `H20d_residual` (`records/code/ceiling4/numbers.json`,
C9): after six families and 40 readings (`cross` 8, `self` 8, `astra` 4, `self-strong` 8,
`self-frontier` 4, `cross-R` 8) the never-flagged set is **32 of the 110** defective instances (which come from 56 problems);
the 32 themselves span **20 problems**.
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
interval covers the true rate. Monte Carlo standard error about 0.011 near 95% coverage and
about 0.020 at the 0.80 cell.

**What it licenses.** Coverage of **single-rate** intervals under that correlation model:
near nominal (0.93–0.97) at the tested true rates 0.10, 0.16, 0.30, 0.48 and 0.60, 0.80 at 0.03 on the 56-cluster
stratum. It says nothing about the paired contrasts or category-conditioned shares in Table 1,
and the concordance of 0.5 is an assumption, not an estimate.

## 3. The pooled union's false-positive rate

**Why.** The paper quoted the pooled three-family recall, **53/110 = 48.2%**, beside the shipped
route's **16.0%**, which is eight readings of one route. The paper's rule is that a union recall
appears only beside the false-positive rate *it* cost. Manuscript review round 5 recomputed the
pooled union on the correct stratum.

**Computation.** `benchmarks/code/ceiling/pooled_union.py` in the harness (commit `ce8f43d`),
record mirrored at `records/code/ceiling/pooled_union.json`: the Boolean union of `cross` d1–8,
`self` d1–8 and `astra` d1–4, each asserted complete on all 260 instances, with ceiling 1's own
`clustered_rate` and seed 20260908, 10,000 resamples.

| stratum | union | cluster 95% |
|---|---|---|
| defective (P) | 53/110 = 48.2% | [36.4, 59.8] |
| correct (C) | **54/150 = 36.0%** | **[28.2, 44.2]** |

The paper keeps the reviewed interval [36.7, 60.0] for the recall, which comes from study 21's
record at seed 20260924; the [36.4, 59.8] here is the same quantity at ceiling 1's seed and is
not quoted.

**What it licenses.** Pooling twenty readings of three routes buys 48.2% recall at 36.0% false
positives, more than twice the shipped route's price. It does not license a comparison of
pooling against any single route at a matched operating point.
