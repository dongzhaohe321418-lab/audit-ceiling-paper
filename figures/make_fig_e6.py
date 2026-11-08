"""Figure for the randomised-contract experiment (Section 3), read from one analyse_e6 results file.

    python figures/make_fig_e6.py <e6_results_v4_{split}.json> <out stem>

(a) flag rate on defective and on correct programs and verified diagnosis, per arm, pooled over configurations;
(b) verified diagnosis after resolution at the low and high reasoning budget, per vendor;
(c) what the auditor does in the menu arm (pass, ask for clarification, block), per configuration.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path.home() / ".claude/skills/nature-figure/scripts"))
from audit_panel_alignment import require_matplotlib_panel_alignment  # noqa: E402

mpl.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42, "svg.fonttype": "none", "font.size": 7,
    "axes.spines.right": False, "axes.spines.top": False, "axes.linewidth": 0.6,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6, "legend.frameon": False,
})
# Okabe-Ito subset: colour-blind safe and distinct in greyscale by lightness
TPR, FPR, COV = "#0072B2", "#E69F00", "#009E73"
PASS, ESC, BLOCK = "#BBBBBB", "#56B4E9", "#D55E00"
VENDOR = {"gpt": ("aud-gpt-terra", "GPT-5.6-terra"), "claude": ("aud-claude-sonnet", "Claude Sonnet 5.5")}
ARMS = [("none", "all|none", "none"), ("menu", "all|menu", "menu"),
        ("sentence", "sentence-configs|sentence", "sentence"), ("resolve", "all|resolve", "resolve")]


def err(m: dict) -> tuple[float, float]:
    if m.get("est") is None:
        return 0.0, 0.0
    return m["est"] - m["lo"], m["hi"] - m["est"]


def est(m: dict) -> float:
    return m["est"] if m.get("est") is not None else float("nan")      # missing: no bar or marker is drawn


def main(path: str, stem: str) -> None:
    d = json.loads(Path(path).read_text())
    fig = plt.figure(figsize=(6.75, 2.15))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.55, 0.8, 1.0], wspace=0.55)
    ax_a, ax_b, ax_c = (fig.add_subplot(gs[0, i]) for i in range(3))

    # (a) per arm: three bars
    w = 0.26
    for i, (_name, key, label) in enumerate(ARMS):
        lv = d["levels"][key]
        for j, (metric, col) in enumerate((("tpr", TPR), ("fpr", FPR), ("cov", COV))):
            m = lv[metric]
            lo, hi = err(m)
            ax_a.bar(i + (j - 1) * w, est(m), w, color=col, yerr=[[lo], [hi]], error_kw={"lw": 0.6, "capsize": 1.2},
                     label=("flag | defective", "flag | correct", "verified diagnosis")[j] if i == 0 else None)
    ax_a.set_xticks(range(len(ARMS)), [a[2] for a in ARMS])
    ax_a.set_ylim(0, 105)
    ax_a.set_ylabel("rate (%)")
    ax_a.legend(loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=3, fontsize=6, handlelength=0.9,
                columnspacing=0.8, borderaxespad=0.2)
    tr = mpl.transforms.blended_transform_factory(ax_a.transData, ax_a.transAxes)
    for x0, x1, lab in ((-0.4, 1.4, "contract withheld"), (1.6, 3.4, "contract stated")):
        ax_a.plot([x0, x1], [-0.2, -0.2], transform=tr, color="0.45", lw=0.6, clip_on=False)
        ax_a.text((x0 + x1) / 2, -0.23, lab, transform=tr, ha="center", va="top", fontsize=6, color="0.35")

    # (b) low vs high budget after resolution
    for k, (v, (route, name)) in enumerate(VENDOR.items()):
        ys = [d["levels"][f"{route}-{b}|resolve"]["cov"] for b in ("low", "high")]
        xs = [0 + 0.06 * (k - 0.5), 1 + 0.06 * (k - 0.5)]
        ax_b.errorbar(xs, [est(y) for y in ys], yerr=[[err(y)[0] for y in ys], [err(y)[1] for y in ys]],
                      marker="os"[k], ms=3.2, lw=0.9, capsize=1.2, color=("0.15", "0.55")[k], label=name)
    ax_b.set_xticks([0, 1], ["low", "high"])
    ax_b.set_xlim(-0.4, 1.4)
    ax_b.set_ylim(0, 105)
    ax_b.set_xlabel("reasoning budget")
    ax_b.set_ylabel("verified diagnosis (%)")
    ax_b.set_title("contract stated", fontsize=6, color="0.35", pad=3)
    ax_b.legend(loc="lower center", fontsize=6, handlelength=1.2, borderaxespad=0.1)

    # (c) routing in the menu arm
    cfgs = [f"{VENDOR[v][0]}-{b}" for v in ("gpt", "claude") for b in ("low", "high")]
    names = [f"{('GPT', 'Claude')[i // 2]} {('low', 'high')[i % 2]}" for i in range(4)]
    rt = d["routing_menu"]
    for i, c in enumerate(cfgs):
        left = 0.0
        for key, col, lab in (("pass", PASS, "pass"), ("escalate", ESC, "ask to clarify"), ("block", BLOCK, "block")):
            val = 100 * rt[c][key]
            ax_c.barh(i, val, left=left, color=col, height=0.62, label=lab if i == 0 else None)
            left += val
    ax_c.set_yticks(range(4), names)
    ax_c.invert_yaxis()
    ax_c.set_xlim(0, 100)
    ax_c.set_xlabel("readings in menu arm (%)")
    ax_c.spines["left"].set_visible(False)
    ax_c.tick_params(axis="y", length=0)
    ax_c.legend(loc="lower left", bbox_to_anchor=(-0.05, 1.0), ncol=3, fontsize=6, handlelength=0.9,
                columnspacing=0.8, borderaxespad=0.2)

    for ax, letter in zip((ax_a, ax_b, ax_c), "abc"):
        ax.text(-0.02, 1.13, letter, transform=ax.transAxes, fontsize=8, fontweight="bold", ha="right", va="bottom")
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=f"{stem}.alignment.json", overlay_svg=f"{stem}.alignment.svg",
                                       tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True,
                                       panel_ids=["a", "b", "c"],
                                       exemptions=[{"panels": ["a", "b", "c"], "checks": ["panel-width", "horizontal-gutter"],
                                                    "reason": "unequal widths by design: (a) has four grouped arms, (b) two budgets"}])
    fig.savefig(f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(f"{stem}.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
