#!/usr/bin/env python3
"""Measure the coverage of the problem-cluster percentile bootstrap under this paper's design.

A pre-submission referee observed that the manuscript reinstated a "roughly 2 to 5 points"
under-coverage range that the source report had explicitly withdrawn as an unsupported
generalisation, and called the clustered design unvalidated while a clustered simulation exists
in the paper's own test suite. Both were true. This measures it properly: the estimator is the
one the paper uses, the cluster-size profiles are the ones the paper has, and coverage is
reported per rate rather than as one scalar range, because it is strongly rate-dependent.

    python3 analysis/coverage_simulation.py            # ~2 minutes
    python3 analysis/coverage_simulation.py --reps 400 # quick

No model calls. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "records" / "coverage_simulation.json"

#: The two strata's actual cluster structure, from the frozen audit set.
#: P: 110 instances in 56 problems, 54 problems with two instances and 2 with one.
#: C: 150 instances in 143 problems, 7 with two and 136 with one.
DESIGNS = {
    "P (110 instances, 56 problems)": [2] * 54 + [1] * 2,
    "C (150 instances, 143 problems)": [2] * 7 + [1] * 136,
}
RATES = [0.03, 0.05, 0.10, 0.16, 0.30, 0.48, 0.60]
RHO = 0.5   # within-problem concordance: two instances of one problem share a generation


def cluster_bootstrap_ci(clusters: list[list[int]], reps: int, rng: random.Random):
    n_c = len(clusters)
    out = []
    for _ in range(reps):
        k = t = 0
        for _ in range(n_c):
            for v in clusters[rng.randrange(n_c)]:
                k += v
                t += 1
        if t:
            out.append(k / t)
    out.sort()
    lo = out[int(0.025 * (len(out) - 1))]
    hi = out[int(0.975 * (len(out) - 1))]
    return lo, hi


def simulate(sizes: list[int], p: float, reps: int, boots: int, seed: int) -> float:
    rng = random.Random(seed)
    hits = 0
    for _ in range(reps):
        clusters = []
        for s in sizes:
            if s == 1:
                clusters.append([1 if rng.random() < p else 0])
            else:
                # Correlated within a problem: with probability RHO both instances share one
                # draw, otherwise they are drawn independently.
                if rng.random() < RHO:
                    v = 1 if rng.random() < p else 0
                    clusters.append([v, v])
                else:
                    clusters.append([1 if rng.random() < p else 0 for _ in range(s)])
        lo, hi = cluster_bootstrap_ci(clusters, boots, rng)
        if lo <= p <= hi:
            hits += 1
    return hits / reps


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=1200)
    ap.add_argument("--boots", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260923)
    a = ap.parse_args()

    result = {"reps": a.reps, "bootstrap_resamples": a.boots, "seed": a.seed,
              "within_problem_concordance": RHO, "nominal": 0.95, "coverage": {}}
    print(f"{'design':34s} " + "".join(f"{r:>8.2f}" for r in RATES))
    for name, sizes in DESIGNS.items():
        row = {}
        cells = []
        for i, p in enumerate(RATES):
            c = simulate(sizes, p, a.reps, a.boots, a.seed + i)
            row[f"{p:.2f}"] = c
            cells.append(f"{c:>8.3f}")
        result["coverage"][name] = row
        print(f"{name:34s} " + "".join(cells))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
