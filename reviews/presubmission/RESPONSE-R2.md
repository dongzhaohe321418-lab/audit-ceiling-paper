# Response to Referee 2

We thank the referee for reproducing six headline quantities from the raw records with an
independent implementation before criticising anything. That the six matched is the part of this
review we found most useful, because it localises the problem: the instrument is sound and four
sentences built on it were not.

We accept the characterisation that three of those four errors run toward our hypothesis. That
is the failure mode this paper spends a section describing, and it was still present.

---

**R2-M1, the +12.50 interval.** *Accepted in full. This was the worst error in the paper.*

The record marks that contrast `one_signed_discordance` with 7 discordant pairs against 0, and
carries its own note stating that the percentile bootstrap's bound at zero is then an artefact
and an exact unconditional interval must be quoted. That interval is [−3.6, +26.8] and contains
zero. We quoted the forbidden [5.17, 21.82] in four places including the abstract, three pages
after stating the rule that governs it, and the introduction used it to conclude the rule is
outside the product's constraint.

All four sites now carry the exact unconditional interval and say it does not exclude zero, with
the exact McNemar p of 0.0156 against that study's Bonferroni threshold of 0.003125. The
directed statement rests on the pooled contrast, 23 discordant one way against 1 the other at
p = 3.0 × 10⁻⁶, and the correct-stratum cost is reported as a cost whose interval contains zero.
We checked every other quoted interval in the manuscript against the records for a one-signed
discordance and found no second instance.

**R2-M2, the exchange rate does not fall monotonically.** *Accepted in full.*

The source table's ladder is 1.67, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68 from K = 2 to K = 8. It
falls once and then rises. The paper now prints the ladder and states that repeated reading on
this route buys recall at a slightly improving price rather than a worsening one, which is the
more interesting fact and the one the records support. Verified digit for digit.

**R2-M3, the coverage statement.** *Accepted in full, and measured.*

Every part of the referee's account checks out: "roughly 2 to 5 points" is a range the source
report withdrew as "a generalisation the evidence does not support"; a clustered simulation sits
in our own test suite, so "unvalidated" was wrong; and the truth is rate-dependent rather than
scalar. We have run the simulation the referee describes, at both strata's actual cluster
profiles:

| true rate | 0.03 | 0.05 | 0.10 | 0.16 | 0.30 | 0.48 | 0.60 |
|---|---|---|---|---|---|---|---|
| defect stratum, 56 clusters | **0.797** | 0.870 | 0.932 | 0.932 | 0.953 | 0.935 | 0.927 |
| correct stratum, 143 clusters | 0.887 | 0.917 | 0.938 | 0.932 | 0.943 | 0.955 | 0.965 |

Our 0.797 at 0.03 on the defect stratum sits beside the referee's independently measured 0.807
and 0.826. The table replaces the scalar range in the methods, and the 3.3% figure is marked in
place as an interval narrower than it claims. The script is committed and uses no model calls.

**R2-M4, multiplicity on intervals.** *Accepted; open.* The referee is right that the directed
conclusions in two sections are interval-based and uncorrected, and that the word "establishes"
should not attach to an interval whose relevant endpoint is 0.7 points from zero. We have not
made this change yet.

**R2-M5, the flattening statistic.** *Accepted; open.* The referee's derivation is correct — the
last-step gain is the singleton count over K·n, 17/(8·110) = 1.93 points — and the quoted
interval carries task-sampling variance while the statistic is made of reading-sampling
variance. Stating what the statistic is costs nothing and we owe it.

**R2-M6, "all 70 subsets on each side".** *Accepted in full.*

`astra` has four readings, so C(4,4) = 1. The cross-vendor arm's estimate is averaged over 70
subsets and `astra`'s is a single realisation with none of its reading-selection variance
averaged out. The source report had this right; the manuscript lost it. Corrected, with the
asymmetry stated rather than only the counts.

**R2-M7, "twenty readings".** *Accepted in full.*

Recomputed from the records: the same-vendor route gains 1.8 points from its first reading to
its eighth, against the cross-vendor route's 19.3, because it is sent temperature 0. Both the
abstract and the results now say the effective depth is nearer thirteen and that the pooled
figure is a union over three routes rather than twenty independent looks.

**Minor comments.** R2-m1's interval discrepancies led us to find and fix a cross-report
inconsistency where one estimand had been bootstrapped twice at two seeds and quoted as one
number. R2-m3, m4, m6, m7 and m8 are accepted and open; m8's seed-stability observation for the
−12.7 contrast is the one we consider most urgent among them, since an endpoint that lands on
zero for one seed in sixty is not an endpoint that excludes zero.
