#!/usr/bin/env python3
"""Figure 2 — the severity-threshold sweep on the recall/false-positive plane.

Every number is read from `records/threshold_sweep.json`; nothing is transcribed. Each family
appears once per decision rule, with problem-cluster 95% intervals on both axes, so the figure
shows what the sweep's table shows and what the table cannot: that the families do not lie on
one curve, and that no same-vendor family has a reachable point near the cross-vendor auditor's
false-positive rate.

    python3 figures/make_fig2_sweep.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import scienceplots  # noqa: F401  — registers the styles

REC = Path(__file__).resolve().parents[1] / "records/code/threshold_sweep.json"
OUT = Path(__file__).resolve().parent / "fig2_sweep.pdf"

RULE_MARKER = {
    "blocker>=1 (shipped)": ("o", "BLOCKER $\\geq$ 1 (shipped)"),
    "blocker>=2":           ("s", "BLOCKER $\\geq$ 2"),
    "any finding>=1":       ("^", "any finding $\\geq$ 1"),
    "any finding>=2":       ("D", "any finding $\\geq$ 2"),
}
FAMILY_ORDER = ["cross", "astra", "self", "self-strong", "self-frontier"]


def main() -> int:
    d = json.loads(REC.read_text(encoding="utf-8"))
    rows = d["rows"]
    fams = [f for f in FAMILY_ORDER if any(r[0] == f for r in rows)]
    colours = plt.cm.tab10.colors

    with plt.style.context(["science", "nature", "no-latex"]):
        fig, ax = plt.subplots(figsize=(3.4, 3.05))
        for fi, fam in enumerate(fams):
            pts = [r for r in rows if r[0] == fam]
            pts.sort(key=lambda r: r[6])
            c = colours[fi % len(colours)]
            # A family's four rules are four operating points, not a measured curve.
            # They are joined by a faint dotted guide only, so the eye can group them without
            # reading an interpolation that was never measured.
            ax.plot([r[6] for r in pts], [r[3] for r in pts], ":", color=c, lw=0.5,
                    alpha=0.45, zorder=1)
            for r in pts:
                _fam, rule, _k, rec, rlo, rhi, fp, flo, fhi = r
                m, _lab = RULE_MARKER[rule]
                ax.errorbar(fp, rec, xerr=[[fp - flo], [fhi - fp]],
                            yerr=[[rec - rlo], [rhi - rec]],
                            fmt=m, ms=3.2, color=c, ecolor=c, elinewidth=0.5,
                            capsize=1.1, alpha=0.95, zorder=3)
        for fi, fam in enumerate(fams):
            ax.plot([], [], ":o", color=colours[fi % len(colours)], ms=3.2, lw=0.5,
                    label=fam)
        ax.plot([0, 48], [0, 48], "-", color="0.72", lw=0.5, zorder=0)
        # The rotated label on the diagonal was crossed by four error bars; a collision audit
        # caught it. It sits in the empty lower-right corner instead, unrotated.
        ax.text(43.5, 3.0, "recall = false positives", fontsize=5.2, color="0.45",
                ha="right", va="bottom")
        ax.set_xlabel("false positives on correct code (%)")
        ax.set_ylabel("union recall on defective code (%)")
        ax.set_xlim(-1.5, 45)
        ax.set_ylim(-2, 74)
        # Two legends: adding the second replaces the first unless the first is kept
        # explicitly as an artist. The first version of this figure lost its family legend
        # exactly that way.
        fam_leg = ax.legend(loc="upper left", frameon=False, handlelength=1.5,
                            fontsize=5.2, title="auditor family", title_fontsize=5.2)
        ax.add_artist(fam_leg)
        h = [plt.Line2D([], [], marker=m, ls="none", color="0.25", ms=3.2)
             for m, _ in RULE_MARKER.values()]
        # The rule legend sat inside the axes and its last entry touched a plotted region;
        # a collision audit caught it. It moves below the axes, where nothing is drawn.
        ax.legend(h, [lab.replace("$\\geq$", "\u2265") for _, lab in RULE_MARKER.values()],
                  loc="upper center", bbox_to_anchor=(0.5, -0.155), ncol=4, frameon=False,
                  handlelength=1.0, fontsize=5.2, columnspacing=1.0,
                  title="decision rule", title_fontsize=5.2)
        fig.savefig(OUT, bbox_inches="tight", metadata={"CreationDate": None})
    print(f"wrote {OUT}  ({len(rows)} points from {REC.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
