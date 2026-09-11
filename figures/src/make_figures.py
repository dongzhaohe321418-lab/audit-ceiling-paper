"""The paper's figures, drawn from the studies' committed records only.

    python figures/src/make_figures.py

Every number is read from a `numbers.json` written by a study's own report script; nothing is
retyped here. Run from the paper repository root with the harness worktrees present.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scienceplots  # noqa: F401  registers the styles

W = Path("/private/tmp/claude-501/-Users-ericdong/e8f80e28-bc0c-43ea-845e-513b702467fc/scratchpad")
OUT = Path(__file__).resolve().parents[1]
STYLE = ["science", "nature", "no-latex"]

# Paul Tol bright, chosen for grayscale separation as well as hue.
CROSS, SELF, INJ, TWIN = "#4477AA", "#EE6677", "#228833", "#BBBBBB"


def load():
    c1 = json.loads((W / "wt-inject/benchmarks/code/records/ceiling/numbers.json")
                    .read_text())["ceiling1"]["families"]
    s2 = json.loads((W / "wt-sub2/benchmarks/code/records/substrate2/numbers.json").read_text())
    inj = json.loads((W / "wt-inject/benchmarks/code/records/inject/numbers.json").read_text())
    return c1, s2, inj


def pct(ax):
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))


def figure1(c1, s2):
    """Union recall and false positives against the number of independent readings."""
    fig, axes = plt.subplots(1, 2, figsize=(6.9, 2.7))
    ks = range(1, 9)
    panels = [
        (axes[0], "Defective increments (recall)",
         [("Substrate 1, cross-vendor", c1["cross"]["P"]["curve"], CROSS, "-", "o",
           c1["cross"]["P"]["curve_ci95"]),
          ("Substrate 1, same-vendor", c1["self"]["P"]["curve"], SELF, "-", "s",
           c1["self"]["P"]["curve_ci95"]),
          ("Substrate 2, cross-vendor", s2["H23b_curve"]["P"]["curve"], CROSS, "--", "^",
           s2["H23b_curve"]["P"]["curve_cluster_ci95"]),
          ("Substrate 2, same-vendor", s2["self_family_curve"]["P"]["curve"], SELF, "--", "v",
           s2["self_family_curve"]["P"]["curve_cluster_ci95"])]),
        (axes[1], "Correct increments (false positives)",
         [("Substrate 1, cross-vendor", c1["cross"]["C"]["curve"], CROSS, "-", "o",
           c1["cross"]["C"]["curve_ci95"]),
          ("Substrate 1, same-vendor", c1["self"]["C"]["curve"], SELF, "-", "s",
           c1["self"]["C"]["curve_ci95"]),
          ("Substrate 2, cross-vendor", s2["H23b_curve"]["C"]["curve"], CROSS, "--", "^",
           s2["H23b_curve"]["C"]["curve_cluster_ci95"]),
          ("Substrate 2, same-vendor", s2["self_family_curve"]["C"]["curve"], SELF, "--", "v",
           s2["self_family_curve"]["C"]["curve_cluster_ci95"])]),
    ]
    for ax, title, series in panels:
        for index, (label, curve, colour, ls, marker, ci) in enumerate(series):
            ax.plot(list(ks), curve, ls, color=colour, marker=marker, markersize=3,
                    linewidth=1.0, label=label, clip_on=False)
            # the quoted point carries its 95% problem-cluster interval. One bar per series
            # rather than a band keeps four curves legible, and the bars are dodged in x so
            # two series with overlapping intervals stay separately readable.
            lo, hi = ci[-1]
            ax.errorbar([8.28 + 0.16 * index], [curve[-1]],
                        yerr=[[curve[-1] - lo], [hi - curve[-1]]],
                        fmt="none", ecolor=colour, elinewidth=0.8, capsize=1.6,
                        capthick=0.8, clip_on=False, alpha=0.95)
        ax.set_xlabel("Independent readings $K$")
        ax.set_title(title, fontsize=7, pad=4)
        ax.set_xlim(0.8, 9.0)
        ax.set_ylim(0, 1.0)
        ax.set_xticks(list(ks))
        pct(ax)
    axes[0].set_ylabel("Union rate")
    # One legend for both panels, placed outside so no curve is covered.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False,
               fontsize=6.5, bbox_to_anchor=(0.5, -0.12), handlelength=2.2, columnspacing=1.4)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_saturation.pdf", bbox_inches="tight")
    fig.savefig(OUT / "fig1_saturation.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def figure2(c1, s2):
    """The operating points: recall against false positives as readings accumulate.

    The point of the panel is that the two substrates' false-positive ranges do not overlap,
    so the shaded spans are drawn first and labelled, and the same-vendor track on substrate 2
    is annotated because all eight of its readings fall on one point.
    """
    fig, ax = plt.subplots(figsize=(3.6, 3.0))
    tracks = [
        ("Substrate 1, cross-vendor", c1["cross"]["C"]["curve"], c1["cross"]["P"]["curve"],
         CROSS, "-", "o"),
        ("Substrate 1, same-vendor", c1["self"]["C"]["curve"], c1["self"]["P"]["curve"],
         SELF, "-", "s"),
        ("Substrate 2, cross-vendor", s2["H23b_curve"]["C"]["curve"],
         s2["H23b_curve"]["P"]["curve"], CROSS, "--", "^"),
        ("Substrate 2, same-vendor", s2["self_family_curve"]["C"]["curve"],
         s2["self_family_curve"]["P"]["curve"], SELF, "--", "v"),
    ]
    # the two substrates' measured false-positive ranges, which do not meet
    s1_fp = c1["cross"]["C"]["curve"] + c1["self"]["C"]["curve"]
    s2_fp = s2["H23b_curve"]["C"]["curve"] + s2["self_family_curve"]["C"]["curve"]
    ax.axvspan(min(s1_fp), max(s1_fp), color="0.88", zorder=0)
    ax.axvspan(min(s2_fp), max(s2_fp), color="0.94", zorder=0)
    ax.text((min(s1_fp) + max(s1_fp)) / 2, 0.955, "substrate 1", fontsize=5.4, color="0.35",
            ha="center", va="top")
    ax.text(min(s2_fp) + 0.055, 0.955, "substrate 2", fontsize=5.4, color="0.35",
            ha="center", va="top")

    for label, fp, rec, colour, ls, marker in tracks:
        ax.plot(fp, rec, ls, color=colour, marker=marker, markersize=3, linewidth=1.0,
                label=label, clip_on=False, zorder=3)
        ax.plot(fp[-1], rec[-1], marker=marker, color=colour, markersize=5.5,
                markeredgecolor="black", markeredgewidth=0.45, clip_on=False, zorder=4)

    ax.plot([0, 0.92], [0, 0.92], ":", color="0.55", linewidth=0.8, zorder=1)
    ax.text(0.345, 0.345, "recall = false positives", fontsize=5.4, color="0.45",
            rotation=41, rotation_mode="anchor", ha="center", va="bottom", zorder=2)

    # all eight readings of the same-vendor auditor on substrate 2 land on one point
    fx, fy = s2["self_family_curve"]["C"]["curve"][-1], s2["self_family_curve"]["P"]["curve"][-1]
    ax.annotate("all 8 readings identical", xy=(fx, fy), xytext=(-38, 13),
                textcoords="offset points", fontsize=5.4, color=SELF, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="-", color=SELF, linewidth=0.6,
                                shrinkA=0, shrinkB=4))
    ax.annotate("$K=1$", xy=(c1["cross"]["C"]["curve"][0], c1["cross"]["P"]["curve"][0]),
                xytext=(7, -7), textcoords="offset points", fontsize=5.6, color=CROSS)
    ax.annotate("$K=8$", xy=(c1["cross"]["C"]["curve"][-1], c1["cross"]["P"]["curve"][-1]),
                xytext=(6, 2), textcoords="offset points", fontsize=5.6, color=CROSS)

    ax.set_xlabel("Union false-positive rate on correct work")
    ax.set_ylabel("Union recall on defects")
    ax.set_xlim(0, 0.86)
    ax.set_ylim(0, 1.0)
    pct(ax)
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))
    ax.legend(loc="lower right", frameon=False, fontsize=5.6, handlelength=2.0,
              borderaxespad=0.3, labelspacing=0.32)
    fig.tight_layout()
    fig.savefig(OUT / "fig2_operating_points.pdf", bbox_inches="tight")
    fig.savefig(OUT / "fig2_operating_points.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def figure3(c1, inj):
    """Recall on defects the specification determines, against the natural residual."""
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.6),
                                  gridspec_kw={"width_ratios": [1.25, 1.0]})
    a, b = inj["H22a_primary"]["a"], inj["H22a_primary"]["b"]
    paired = inj["H22b_paired"]
    bars = [
        ("Injected defects\n(specification\ndetermines them)", a["k"] / a["n"],
         a["wilson95"], INJ),
        ("The same code\nwith the injection\nremoved", paired["twin"]["k"] / paired["n"],
         paired["twin"]["wilson95"], TWIN),
        ("Natural residual\n(substrate 1)", b["k"] / b["n"], b["wilson95"], CROSS),
    ]
    xs = range(len(bars))
    for x, (label, value, ci, colour) in zip(xs, bars):
        ax.bar(x, value, width=0.55, color=colour, edgecolor="black", linewidth=0.4,
               yerr=[[value - ci[0]], [ci[1] - value]], ecolor="black",
               error_kw=dict(elinewidth=0.7, capsize=2.0, capthick=0.7))
        ax.text(x, ci[1] + 0.03, f"{value:.0%}", ha="center", fontsize=6.5)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([b[0] for b in bars], fontsize=6)
    ax.set_ylabel("Union recall at $K=8$")
    ax.set_ylim(0, 1.12)
    pct(ax)
    ax.set_title("Same auditor, same eight readings", fontsize=7, pad=4)

    ax2.plot(range(1, len(inj["H22d_curve"]["curve"]) + 1), inj["H22d_curve"]["curve"], "-",
             color=INJ, marker="o", markersize=3, linewidth=1.0,
             label="Injected defects", clip_on=False)
    ax2.plot(range(1, 9), c1["cross"]["P"]["curve"], "-", color=CROSS, marker="^",
             markersize=3, linewidth=1.0, label="Natural residual", clip_on=False)
    ax2.set_xlabel("Independent readings $K$")
    ax2.set_ylabel("Union recall")
    ax2.set_xlim(0.8, 8.2)
    ax2.set_ylim(0, 1.05)
    ax2.set_xticks(list(range(1, 9)))
    pct(ax2)
    ax2.legend(loc="center right", frameon=False, fontsize=6.2, handlelength=2.0)
    ax2.set_title("One reading is almost all of it", fontsize=7, pad=4)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_specification_determined.pdf", bbox_inches="tight")
    fig.savefig(OUT / "fig3_specification_determined.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    plt.style.use(STYLE)
    c1, s2, inj = load()
    figure1(c1, s2)
    figure2(c1, s2)
    figure3(c1, inj)
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("fig*.p*"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
