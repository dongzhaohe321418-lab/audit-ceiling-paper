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
]),
        (axes[1], "Correct increments (false positives)",
         [("Substrate 1, cross-vendor", c1["cross"]["C"]["curve"], CROSS, "-", "o",
           c1["cross"]["C"]["curve_ci95"]),
          ("Substrate 1, same-vendor", c1["self"]["C"]["curve"], SELF, "-", "s",
           c1["self"]["C"]["curve_ci95"]),
]),
    ]
    for ax, title, series in panels:
        for index, (label, curve, colour, ls, marker, ci) in enumerate(series):
            ax.plot(list(ks), curve, ls, color=colour, marker=marker, markersize=3,
                    linewidth=1.0, label=label, clip_on=False)
            # the quoted point carries its 95% problem-cluster interval. One bar per series
            # rather than a band keeps four curves legible, and the bars are dodged in x so
            # two series with overlapping intervals stay separately readable.
            lo, hi = ci[-1]
            x_ci = 8.50 + 0.42 * index
            ax.errorbar([x_ci], [curve[-1]], yerr=[[curve[-1] - lo], [hi - curve[-1]]],
                        fmt="none", ecolor=colour, elinewidth=0.9, capsize=2.0, capthick=0.9)
            ax.plot([x_ci], [curve[-1]], marker=marker, color=colour, markersize=2.6)
        # the interval strip is fenced off so it cannot be read as data at K = 8.5
        ax.axvline(8.25, color="0.75", linewidth=0.6)
        # on the fence itself, rotated: no interval bar can reach this column
        ax.text(8.38, 0.5, "95% CI at $K=8$", fontsize=5.8, color="0.35", ha="center",
                va="center", rotation=90)
        ax.set_xlabel("Independent readings $K$")
        ax.set_title(title, fontsize=7.5, pad=4)
        ax.set_xlim(0.8, 10.3)
        ax.set_ylim(0, 1.0)
        ax.set_xticks(list(ks))
        ax.xaxis.set_minor_locator(mticker.NullLocator())
        pct(ax)
    axes[0].set_ylabel("Union rate")
    for ax, tag in zip(axes, "ab"):
        ax.text(-0.16, 1.02, f"({tag})", transform=ax.transAxes, fontsize=8, va="bottom")
    # the flat series is flat because the verdict is identical, not because the curve is smooth
    axes[0].annotate("identical verdict on all 250 instances", xy=(4.5, 0.88),
                     xytext=(4.5, 0.775), fontsize=5.8, color=SELF, ha="center",
                     arrowprops=dict(arrowstyle="-", color=SELF, linewidth=0.6, shrinkB=1))
    # One legend for both panels, placed outside so no curve is covered.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False,
               fontsize=6.5, bbox_to_anchor=(0.5, -0.12), handlelength=2.2, columnspacing=1.4)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_saturation.pdf", bbox_inches="tight")
    fig.savefig(OUT / "fig1_saturation.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def figure2(c1, s2):
    """WITHDRAWN 2026-09-15.

    This figure was the two substrates' operating-point comparison. Substrate 2's run is
    void: the visible-test text shown to its auditor and generator did not parse on any of
    its 300 tasks (substrate2 Amendment 1), so the tracks it drew are not measurements.
    It is not regenerated. If the re-run restores the substrate, restore the figure from
    git history rather than from this stub.
    """
    raise SystemExit("figure2 is withdrawn: substrate 2's run is void")

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
    ax.set_ylabel("Union flag rate at $K=8$")
    ax.set_ylim(0, 1.08)
    pct(ax)
    ax.set_title("Same auditor, same eight readings", fontsize=7.5, pad=4)
    ax.xaxis.set_minor_locator(mticker.NullLocator())

    ax2.plot(range(1, len(inj["H22d_curve"]["curve"]) + 1), inj["H22d_curve"]["curve"], "-",
             color=INJ, marker="o", markersize=3, linewidth=1.0,
             label="Injected defects", clip_on=False)
    ax2.plot(range(1, 9), c1["cross"]["P"]["curve"], "--", color=CROSS, marker="o",
             markersize=3, linewidth=1.0, label="Natural residual", clip_on=False)
    ax2.set_xlabel("Independent readings $K$")
    ax2.set_ylabel("Union recall")
    ax2.set_xlim(0.8, 8.2)
    ax2.set_ylim(0, 1.05)
    ax2.set_xticks(list(range(1, 9)))
    pct(ax2)
    ax2.legend(loc="center right", frameon=False, fontsize=6.5, handlelength=2.4)
    ax2.xaxis.set_minor_locator(mticker.NullLocator())
    for a, tag in ((ax, "a"), (ax2, "b")):
        a.text(-0.14, 1.02, f"({tag})", transform=a.transAxes, fontsize=8, va="bottom")
    ax2.set_title("One reading is almost all of it \u2014 on injected defects",
                  fontsize=7.5, pad=4)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_specification_determined.pdf", bbox_inches="tight")
    fig.savefig(OUT / "fig3_specification_determined.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    plt.style.use(STYLE)
    c1, s2, inj = load()
    figure1(c1, s2)
    # figure2 withdrawn 2026-09-15: substrate 2's run is void
    figure3(c1, inj)
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("fig*.p*"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
