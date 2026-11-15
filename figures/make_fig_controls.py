"""Held-out estimates across the randomised-contract studies (Appendix A): the flag preference under the code-shape
controls, and what stating the requirement adds. Reads the frozen results files only.

    python figures/make_fig_controls.py ../crossaudit-harness figures/fig_controls

(a) flag rate of the program that departs from the benchmark's behaviour minus that of the program that follows it,
task alone (E6; E13 and E14 in fresh, interleaved readings); (b) verified diagnosis, sentence minus task alone and
minus the pointer control (E6, E10; E11 on edited BigCodeBench units). Points: estimates; bars: 95% problem-level
bootstrap intervals; open markers: worst-case imputation of missing units (the statistic E14's verdict uses).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

try:            # optional layout QA from the author's figure toolkit; the figure itself does not depend on it
    sys.path.insert(0, str(Path.home() / ".claude/skills/nature-figure/scripts"))
    from audit_panel_alignment import require_matplotlib_panel_alignment  # noqa: E402
except ImportError:
    def require_matplotlib_panel_alignment(*args, **kwargs):
        return None

mpl.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42, "svg.fonttype": "none", "font.size": 7,
    "axes.spines.right": False, "axes.spines.top": False, "axes.linewidth": 0.6, "legend.frameon": False,
})
INK, MUTED = "#0072B2", "#999999"


def load(root: Path, rel: str) -> dict:
    return json.loads((root / "benchmarks" / rel).read_text())


def rows(root: Path) -> tuple[list, list]:
    e6 = load(root, "code/records/icml/e6_results_v4_test.json")
    e10 = load(root, "e10/records/e10_results_test.json")
    e11 = load(root, "e11/records/e11_results_test.json")
    e13 = load(root, "e13/records/e13_results_test.json")
    e14 = load(root, "e14/records/e14_results_test.json")
    w = e14["E14_1_ma_minus_mb"]["bootstrap_with_missing"]["worst"]
    pref = [("E6: A $-$ B (exploratory)", e6["flag_pref_a_minus_b_none"], None),
            ("E13: A $-$ B, fresh", e13["flag_pref_b_fresh"], None),
            ("E13: A $-$ B with added branch", e13["E13_2_flag_pref_bprime"], None),
            ("E14: A $-$ B, fresh", e14["a_minus_b_fresh"], None),
            ("E14: matched pair", e14["E14_1_ma_minus_mb"], w)]
    req = [("E6-5: sentence $-$ task", e6["E6_5_cov_sentence_minus_none"], None),
           ("E10-1: sentence $-$ pointer", e10["E10_1_sentence_minus_pointer"], None),
           ("E10: pointer $-$ task", e10["E10_2_pointer_minus_none"], None),
           ("E11-1: sentence $-$ task (BCB)", e11["E11_1_sentence_minus_none"], None),
           ("E11-2: sentence $-$ pointer (BCB)", e11["E11_2_sentence_minus_pointer"], None)]
    return pref, req


def panel(ax, items, xlabel, letter):
    for i, (label, d, worst) in enumerate(items):
        y = len(items) - 1 - i
        ax.errorbar(d["est"], y, xerr=[[d["est"] - d["lo"]], [d["hi"] - d["est"]]], fmt="o", ms=3.2, color=INK,
                    ecolor=INK, elinewidth=0.9, capsize=0)
        if worst:
            ax.errorbar(worst["est"], y - 0.32, xerr=[[worst["est"] - worst["lo"]], [worst["hi"] - worst["est"]]],
                        fmt="o", ms=3.2, mfc="white", color=INK, ecolor=MUTED, elinewidth=0.9, capsize=0)
    ax.axvline(0, color=MUTED, lw=0.6, zorder=0)
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels([x[0] for x in reversed(items)])
    ax.set_xlabel(xlabel)
    ax.tick_params(axis="y", length=0)
    ax.text(-0.02, 1.04, letter, transform=ax.transAxes, fontweight="bold", fontsize=8, ha="right")


def main(root: str, out: str) -> None:
    pref, req = rows(Path(root))
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 1.9), gridspec_kw={"wspace": 1.15})
    panel(a, pref, "flag rate difference, task alone (points)", "a")
    panel(b, req, "verified diagnosis difference (points)", "b")
    a.set_xlim(-10, 50)
    b.set_xlim(-10, 100)
    fig.subplots_adjust(left=0.24, right=0.98, bottom=0.22, top=0.9)
    require_matplotlib_panel_alignment(fig, json_out=f"{out}.alignment.json", overlay_svg=f"{out}.alignment.svg")
    for ext in ("pdf", "png"):
        fig.savefig(f"{out}.{ext}", dpi=300)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
