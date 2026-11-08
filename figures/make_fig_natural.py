"""Natural hidden-test failures (Section 4): classes and what independent task-only solutions return.

    python figures/make_fig_natural.py figures/data/natural_v4.json figures/fig_natural

(a) the 150 failures by taxonomy-v4 class (two classifiers, identical evidence pooled);
(b) per class, the share of the generators' other solutions (passing the visible tests; the failing program itself is
excluded) that return the defective program's result, the reference's result, or neither, on the failing input;
intervals: bootstrap over problems (10,000 draws), since items of the same problem share solutions.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path.home() / ".claude/skills/nature-figure/scripts"))
from audit_panel_alignment import require_matplotlib_panel_alignment  # noqa: E402

mpl.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42, "svg.fonttype": "none", "font.size": 7,
    "axes.spines.right": False, "axes.spines.top": False, "axes.linewidth": 0.6, "legend.frameon": False,
})
CLASSES = [("DETERMINED", "determined"), ("OPEN", "open"), ("AT_ODDS", "at odds"),
           ("OUT_OF_DOMAIN", "out of domain"), ("DISPUTED", "disputed")]
DEF, REF, OTH = "#D55E00", "#0072B2", "#BBBBBB"


def boot_share(items: list, b: int = 10000, seed: int = 20261113) -> tuple[float, float]:
    rng = random.Random(seed)
    groups: dict = {}
    for x in items:                      # cluster by problem
        groups.setdefault(x[0], []).append(x)
    keys = sorted(groups)
    draws = []
    for _ in range(b):
        s = [x for k in (rng.choice(keys) for _ in keys) for x in groups[k]]
        tot = sum(x[1] + x[2] + x[3] for x in s)
        draws.append(100 * sum(x[2] for x in s) / tot if tot else 0.0)
    draws.sort()
    return draws[int(0.025 * b)], draws[int(0.975 * b)]


def main(path: str, stem: str) -> None:
    d = json.loads(Path(path).read_text())
    by = {c: [] for c, _ in CLASSES}
    for k, v in d["behaviour"].items():
        # the failing program is one of its problem's generations: remove it from the defective count
        by[d["taxonomy"][k]].append((k.split("|")[1], v["n_defective"] - 1, v["n_reference"], v["n_other"]))
    fig = plt.figure(figsize=(3.3, 1.75))
    gs = fig.add_gridspec(1, 2, width_ratios=[0.8, 1.2], wspace=0.15)
    ax_a, ax_b = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    ys = range(len(CLASSES))
    ax_a.barh(list(ys), [len(by[c]) for c, _ in CLASSES], color="0.35", height=0.6)
    for y, (c, _) in zip(ys, CLASSES):
        ax_a.text(len(by[c]) + 1, y, str(len(by[c])), va="center", fontsize=6)
    ax_a.set_yticks(list(ys), [lab for _, lab in CLASSES])
    ax_a.invert_yaxis()
    ax_a.set_xlim(0, 48)
    ax_a.set_xlabel("failures (of 150)")
    for y, (c, _) in zip(ys, CLASSES):
        tot = sum(x[1] + x[2] + x[3] for x in by[c])
        df, rf = 100 * sum(x[1] for x in by[c]) / tot, 100 * sum(x[2] for x in by[c]) / tot
        ax_b.barh(y, rf, color=REF, height=0.6, label="reference's result" if y == 0 else None)
        ax_b.barh(y, df, left=rf, color=DEF, height=0.6, label="defective program's result" if y == 0 else None)
        ax_b.barh(y, 100 - rf - df, left=rf + df, color=OTH, height=0.6, label="neither" if y == 0 else None)
        lo, hi = boot_share(by[c])
        ax_b.errorbar(rf, y, xerr=[[rf - lo], [hi - rf]], color="black", lw=0.6, capsize=1.2)
    ax_b.set_yticks(list(ys), [""] * len(CLASSES))
    ax_b.tick_params(axis="y", length=0)
    ax_b.invert_yaxis()
    ax_b.set_xlim(0, 100)
    ax_b.set_xlabel("other solutions (%)")
    ax_b.legend(loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=2, fontsize=5.5, handlelength=0.9,
                columnspacing=0.7, borderaxespad=0.2)
    for ax, letter in ((ax_a, "a"), (ax_b, "b")):
        ax.text(-0.02, 1.02, letter, transform=ax.transAxes, fontsize=8, fontweight="bold", ha="right", va="bottom")
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=f"{stem}.alignment.json", overlay_svg=f"{stem}.alignment.svg",
                                       tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True, panel_ids=["a", "b"],
                                       exemptions=[{"panels": ["a", "b"], "checks": ["panel-width"],
                                                    "reason": "count panel narrower than share panel by design"}])
    fig.savefig(f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(f"{stem}.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
