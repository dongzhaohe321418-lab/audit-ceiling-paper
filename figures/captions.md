# Figure captions

Every value is read by `figures/src/make_figures.py` from a study's committed `numbers.json`;
no figure carries a number typed by hand. Substrate 1 is HumanEval+ and MBPP+ (median task 41
words of prose, 6 lines of reference code); substrate 2 is the standard-library half of
BigCodeBench (median 118 words, 41 lines).

**Figure 1. Reading again saturates, and where it saturates depends on the substrate.** Union
rate against the number of independent readings K, for two auditor families on two substrates.
Left: recall on defective increments. Right: false positives on correct increments. Bars at the
right of each panel give the 95% problem-cluster bootstrap interval of each series at K = 8,
dodged horizontally so overlapping intervals stay separable. The same-vendor auditor on substrate
2 is flat because its verdict is identical on all 250 instances across all eight readings.

**Figure 2. Recall and false positives move together, and the two substrates never meet.** Each
track is one auditor family on one substrate, walked from K = 1 to K = 8; the outlined marker is
K = 8. Shaded spans show each substrate's measured false-positive range: they do not overlap, so
no number of readings places the two substrates at a matched false-positive rate. The dotted line
marks equal recall and false-positive rates. All eight readings of the same-vendor auditor on
substrate 2 fall on one point.

**Figure 3. On defects the specification determines, one reading is almost all of it.** Left:
union recall at K = 8 of the shipped cross-vendor auditor on three populations — defects injected
so that the specification determines them, the same code with the injection removed, and the
natural residual of substrate 1. Bars carry 95% Wilson intervals; the first two populations are
the same 92 instances, so their difference is paired. Right: the recall curve on the injected
population against the natural residual, same auditor, same protocol. The injected defects are
detectably artificial — a frontier model separates them from natural ones at 96.7% — so this
figure bounds what the auditor can do, not what it does on natural defects.
