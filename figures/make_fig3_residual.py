#!/usr/bin/env python3
"""Figure 3 — the residual contrast, printed beside the instrument that produced it.

Panel (a): the share of instances a rater called specification-undetermined, missed group
against caught group, under each reading. Panel (b): the same rater's agreement with itself on
the eleven instances the sheet carries twice with identical text and identical evidence.

The two panels belong together. A twenty-point contrast read off an instrument that agrees with
itself on 7 of 11 repeats is a different object from the same contrast read off a stable one,
and the paper's claim is stated under that constraint. Every number is read from
`records/rate3/analysis.json` and the rater CSVs.

    python3 figures/make_fig3_residual.py
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import scienceplots  # noqa: F401

ROOT = Path.home() / "Documents/Crossaudit/crossaudit_integ/benchmarks/code"
REC = ROOT / "records/rate3/analysis.json"
SHEET_KEY = Path.home() / "Desktop/CrossAudit-审计天花板/人类评分任务/_items.json"
OUT = Path(__file__).resolve().parent / "fig3_residual.pdf"


def main() -> int:
    d = json.loads(REC.read_text(encoding="utf-8"))
    readings = [
        ("sheet groups",            d["sheet_groups_NOT_missed_vs_caught"], False),
        ("disjoint instances",      d["disjoint_instances_57_vs_53"],       True),
        ("disjoint, no abstention", d["secondary_cannot_tell_excluded_DISJOINT"], True),
        ("unrepaired sheet",        d["exploratory_broken_sheet"],          False),
    ]
    labels = [r[0] for r in readings]
    pts = [r[1]["diff_points"] for r in readings]
    los = [r[1]["diff_points"] - r[1]["cluster_ci95"][0] for r in readings]
    his = [r[1]["cluster_ci95"][1] - r[1]["diff_points"] for r in readings]

    items = json.loads(SHEET_KEY.read_text(encoding="utf-8"))
    lab = {r["rate_id"]: r["label"]
           for r in csv.DictReader((ROOT / "records/rate3/L3.csv").open(encoding="utf-8"))}
    dup = defaultdict(list)
    for it in items:
        dup[it["instance"]].append(it["rate_id"])
    pairs = [v for v in dup.values() if len(v) > 1]
    three = sum(1 for v in pairs if len({lab[i] for i in v}) == 1)
    binary = sum(1 for v in pairs if len({lab[i] == "undetermined" for i in v}) == 1)
    free = [v for v in pairs if all(lab[i] != "cannot-tell" for i in v)]
    free_ag = sum(1 for v in free if len({lab[i] for i in v}) == 1)

    with plt.style.context(["science", "nature", "no-latex"]):
        fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 2.35),
                                     gridspec_kw={"width_ratios": [1.75, 1]})
        y = range(len(labels))[::-1]
        for yi, (name, r, disjoint), lo, hi, pt in zip(y, readings, los, his, pts):
            c = "#c0392b" if name == "unrepaired sheet" else ("#2c6fbb" if disjoint else "#7f8c8d")
            ax.errorbar(pt, yi, xerr=[[lo], [hi]], fmt="o", ms=3.4, color=c,
                        ecolor=c, elinewidth=0.8, capsize=1.6)
            ax.text(pt, yi + 0.20, f"{pt:+.1f}", ha="center", fontsize=5.2, color=c)
        ax.axvline(0, color="0.6", lw=0.5)
        ax.set_yticks(list(y))
        ax.set_yticklabels(labels, fontsize=5.6)
        ax.set_xlabel("undetermined, missed minus caught (percentage points)")
        ax.set_xlim(-6, 80)
        ax.annotate("the same rater, on the sheet\nwhose control arm it could not answer",
                    xy=(54.2, 0), xytext=(62, 0.72), fontsize=4.8, color="#c0392b",
                    ha="center", va="center",
                    arrowprops=dict(arrowstyle="-", color="#c0392b", lw=0.4,
                                    shrinkA=0, shrinkB=3))
        ax.text(-0.19, 1.04, "a", transform=ax.transAxes, fontweight="bold", fontsize=7)

        names = ["primary\nbinary", "full\nlabel", "abstention-free\npairs"]
        got = [binary, three, free_ag]
        tot = [len(pairs), len(pairs), len(free)]
        xs = range(len(names))
        bx.bar(xs, tot, color="0.88", width=0.55)
        bx.bar(xs, got, color="#2c6fbb", width=0.55)
        for x, g, t in zip(xs, got, tot):
            bx.text(x, t + 0.25, f"{g}/{t}", ha="center", fontsize=5.4)
        bx.set_xticks(list(xs))
        bx.set_xticklabels(names, fontsize=5.2)
        bx.set_ylabel("instance pairs")
        bx.plot([], [], "s", color="#2c6fbb", ms=3, label="agree")
        bx.plot([], [], "s", color="0.88", ms=3, label="disagree")
        bx.legend(loc="upper right", frameon=False, fontsize=5.0, handlelength=0.9,
                  handletextpad=0.4)
        bx.set_ylim(0, 14.6)
        bx.text(-0.30, 1.04, "b", transform=bx.transAxes, fontweight="bold", fontsize=7)
        fig.savefig(OUT, bbox_inches="tight")
    print(f"wrote {OUT}: panel a {len(readings)} readings; panel b {binary}/{len(pairs)}, "
          f"{three}/{len(pairs)}, {free_ag}/{len(free)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
