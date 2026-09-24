"""The paper's figures, drawn from the studies' committed records only.

    python figures/src/make_figures.py

Every number is read from a `numbers.json` written by a study's own report script and mirrored
into records/code/; nothing is retyped here. Runs from a clean checkout.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scienceplots  # noqa: F401  registers the styles

# Inputs are read from this repository's own mirror of the records (records/code/, provenance
# in records/PROVENANCE.md), so the figure regenerates from a clean checkout (R3-M3). It read a
# harness review worktree under ~/Documents until 2026-09-23.
REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1]
STYLE = ["science", "nature", "no-latex"]

# Paul Tol bright, chosen for grayscale separation as well as hue.
CROSS, SELF, INJ, TWIN = "#4477AA", "#EE6677", "#228833", "#BBBBBB"


def load():
    c1 = json.loads((REPO / "records/code/ceiling/numbers.json")
                    .read_text())["ceiling1"]["families"]
    # figure2 (substrate 2) and figure3 (injection) are withdrawn; their records are not read.
    return c1, None, None


def pct(ax):
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))


def figure1(c1, s2):
    """Union recall and false positives against the number of independent readings."""
    fig, axes = plt.subplots(1, 2, figsize=(6.9, 2.7))
    ks = range(1, 9)
    panels = [
        (axes[0], "Defective increments (recall)",
         [("cross-vendor (shipped)", c1["cross"]["P"]["curve"], CROSS, "-", "o",
           c1["cross"]["P"]["union_at_kmax_block"]["cluster_ci95"]),
          ("same-vendor, temperature 0", c1["self"]["P"]["curve"], SELF, "-", "s",
           c1["self"]["P"]["union_at_kmax_block"]["cluster_ci95"]),
]),
        (axes[1], "Correct increments (false positives)",
         [("cross-vendor (shipped)", c1["cross"]["C"]["curve"], CROSS, "-", "o",
           c1["cross"]["C"]["union_at_kmax_block"]["cluster_ci95"]),
          ("same-vendor, temperature 0", c1["self"]["C"]["curve"], SELF, "-", "s",
           c1["self"]["C"]["union_at_kmax_block"]["cluster_ci95"]),
]),
    ]
    for ax, title, series in panels:
        for index, (label, curve, colour, ls, marker, ci) in enumerate(series):
            ax.plot(list(ks), curve, ls, color=colour, marker=marker, markersize=3,
                    linewidth=1.0, label=label, clip_on=False)
            # the quoted point carries its 95% problem-cluster interval. One bar per series
            # rather than a band keeps four curves legible, and the bars are dodged in x so
            # two series with overlapping intervals stay separately readable.
            # the same K=8 interval Table 1 and the text quote (union_at_kmax_block)
            lo, hi = ci
            x_ci = 8.50 + 0.42 * index
            ax.errorbar([x_ci], [curve[-1]], yerr=[[curve[-1] - lo], [hi - curve[-1]]],
                        fmt="none", ecolor=colour, elinewidth=0.9, capsize=2.0, capthick=0.9)
            ax.plot([x_ci], [curve[-1]], marker=marker, color=colour, markersize=2.6)
        # the interval strip is fenced off so it cannot be read as data at K = 8.5
        ax.axvline(8.25, color="0.75", linewidth=0.6)
        # on the fence itself, rotated: no interval bar can reach this column
        ax.text(8.38, 0.505, "95% CI at $K=8$", fontsize=5.8, color="0.35", ha="center",
                va="center", rotation=90)
        ax.set_xlabel("Independent readings $K$")
        ax.set_title(title, fontsize=7.5, pad=4)
        ax.set_xlim(0.8, 10.3)
        ax.set_ylim(0, 0.6)
        ax.set_xticks(list(ks))
        ax.xaxis.set_minor_locator(mticker.NullLocator())
        pct(ax)
    axes[0].set_ylabel("Union rate")
    for ax, tag in zip(axes, "ab"):
        ax.text(-0.16, 1.02, f"({tag})", transform=ax.transAxes, fontsize=8, va="bottom")
    # Until 2026-09-23 this read "identical verdict on all 250 instances" and pointed at empty
    # space: 250 was substrate 2's count and its curve had been withdrawn beneath the label. On
    # this substrate the same-vendor verdict varies across readings on a few instances, counted
    # here from the record rather than typed.
    def varying(s):
        return sum(v for k, v in c1["self"][s]["counts_k"].items() if k not in ("0", "8"))
    n_p = sum(c1["self"]["P"]["counts_k"].values())
    axes[0].annotate(f"verdict varies across readings\non {varying('P')} of {n_p} instances",
                     xy=(6.0, c1["self"]["P"]["curve"][5]), xytext=(5.6, 0.07), fontsize=5.8,
                     color=SELF, ha="center",
                     arrowprops=dict(arrowstyle="-", color=SELF, linewidth=0.6, shrinkB=1))
    # One legend for both panels, placed outside so no curve is covered.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False,
               fontsize=6.5, bbox_to_anchor=(0.5, -0.12), handlelength=2.2, columnspacing=1.4)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_saturation.pdf", bbox_inches="tight", metadata={"CreationDate": None})
    fig.savefig(OUT / "fig1_saturation.png", dpi=400, bbox_inches="tight", metadata={"Software": None})
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
    """WITHDRAWN 2026-09-16.

    This figure plotted the injected population against the natural residual. Study 22's
    headline is withdrawn (inject Amendment 7): the construction never enforced
    specification-determinedness -- F6 checked that the injector wrote a non-empty string
    and nothing more -- so the population is "small injected edits", and its edits are
    separable from natural code at 96.7%. The figure is not regenerated. If a construction
    that enforces the property is built, draw it from that, not from this stub.
    """
    raise SystemExit("figure3 is withdrawn: study 22's headline is withdrawn")

def main() -> int:
    plt.style.use(STYLE)
    c1, s2, inj = load()
    figure1(c1, s2)
    # figure2 withdrawn 2026-09-15: substrate 2's run is void
    # figure3 withdrawn 2026-09-16: study 22's headline is withdrawn
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("fig*.p*"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
