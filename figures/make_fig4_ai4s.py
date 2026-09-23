#!/usr/bin/env python3
"""Figure 4 — Act 4: what each audit tier catches on scientific code, results and data.

Every number is read from the AI4S records copied from the auditor harness into
`records/ai4s/`; nothing is transcribed. A panel whose record is absent is not drawn, so the figure
never shows a study that has not been admitted.

  (a) scientific code: union recall and false positives against K for both families (A4S-1);
  (b) scientific results: flag rate by fault type for the LLM, the deterministic science profile
      and re-execution, with the clean-item rate as the leftmost group (A4S-2);
  (c) scientific data: flag rate by fault type for the card-derived validator, the shipped
      auditor and their union, with the clean-item rate as the leftmost group (A4S-3).

Bars carry exact Clopper–Pearson 95% intervals on the item counts.

    python3 figures/make_fig4_ai4s.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import scienceplots  # noqa: F401  — registers the styles
from scipy.stats import beta

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / "records/ai4s"
OUT = Path(__file__).resolve().parent / "fig4_ai4s.pdf"
COL = plt.cm.tab10.colors
#: One meaning per colour across panels: the deterministic tier, the LLM auditor, and the third
#: series (re-execution in (b), the union in (c)).
DET, LLM, THIRD = COL[0], COL[1], COL[2]


def cp(k: int, n: int) -> tuple[float, float]:
    lo = 0.0 if k == 0 else beta.ppf(0.025, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(0.975, k + 1, n - k)
    return 100 * lo, 100 * hi


def bars(ax, groups: list[str], series: list[tuple[str, list[tuple[int, int]], tuple]], title: str):
    width = 0.8 / len(series)
    for si, (label, cells, colour) in enumerate(series):
        xs = [gi + (si - (len(series) - 1) / 2) * width for gi in range(len(groups))]
        ys, lo, hi = [], [], []
        for k, n in cells:
            p = 100 * k / n
            a, b = cp(k, n)
            ys.append(p)
            lo.append(p - a)
            hi.append(b - p)
        ax.bar(xs, ys, width * 0.92, color=colour, label=label, zorder=2)
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="none", ecolor="0.25", elinewidth=0.5,
                    capsize=0.9, zorder=3)
    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels(groups, fontsize=5.4)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(0, 124)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_ylabel("items flagged (%)")
    ax.axvline(0.5, color="0.6", lw=0.5, ls=":", zorder=1)
    ax.set_title(title, fontsize=7, loc="left")
    ax.legend(fontsize=5.8, frameon=False, loc="upper center", ncol=len(series),
              handlelength=1.0, columnspacing=0.8, borderaxespad=0.2)


def count(cell: dict) -> tuple[int, int]:
    return round(cell["pct"] * cell["n"] / 100), cell["n"]


def panel_data(ax, r: dict) -> None:
    v, c = r["validator"], r["families"]["cross"]
    faults = ["F1", "F2", "F3", "F4", "F5", "F6", "F7"]
    names = ["clean", "unit\nmix", "neg.", "dup.\nrows", "shuf.\ntarget",
             "swap\ncols", "$-999$", "round"]
    ser = []
    for label, src, colour in (("validator", v, DET), ("auditor", c["by_k"]["4"], LLM),
                               ("union", c["union_with_validator"], THIRD)):
        ser.append((label, [count(src["clean_fp"])] + [count(src["by_fault"][f]) for f in faults],
                    colour))
    bars(ax, names, ser, "(c) scientific data")


def panel_results(ax, r: dict) -> None:
    faults = ["R1", "R2", "R3", "R4", "R5", "F1", "F4"]
    names = ["clean", "scale", "sign", "other\ncase", "5%", "digit\nswap",
             "fab.\nscale", "fab.\n5%"]
    a = r["auditors"]

    def cells(name):
        src = a[name]
        return [(round(src["clean_fp"]["flagged"]), src["clean_fp"]["n"])] + \
               [(round(src["by_fault"][f]["flagged"]), src["by_fault"][f]["n"]) for f in faults]

    bars(ax, names, [("profile", cells("dcl"), DET), ("auditor", cells("llm_k4"), LLM),
                     ("re-exec.", cells("reexec"), THIRD)], "(b) scientific results")


def panel_code(ax, r: dict) -> None:
    """The shipped auditor in both registered arms; the other family is in the text."""
    ks = list(range(1, 9))
    rb = json.loads((REC / "code_results_b.json").read_text(encoding="utf-8"))["arm_b"]
    for arm, res, style in (("A: whole problem", r, "--"), ("B: step as deliverable", rb, "-")):
        f = res["families"]["cross"]
        ax.plot(ks, f["recall_curve_pct"], style + "o", ms=2.4, lw=0.8, color=LLM,
                label=f"{arm[0]}: defective")
        ax.plot(ks, f["false_positive_curve_pct"], style + "s", ms=2.2, lw=0.8, color=COL[7],
                label=f"{arm[0]}: correct")
    ax.set_xlabel("readings $K$")
    ax.set_ylabel("items flagged (%)")
    ax.set_xticks(ks)
    ax.set_ylim(0, 124)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_title("(a) scientific code", fontsize=7, loc="left")
    ax.legend(fontsize=5.2, frameon=False, loc="upper center", ncol=2, handlelength=1.6,
              columnspacing=0.8, borderaxespad=0.2)


def main() -> int:
    panels = [(name, fn) for name, fn in (("code_results.json", panel_code),
                                          ("results_results.json", panel_results),
                                          ("data_results.json", panel_data))
              if (REC / name).exists()]
    if not panels:
        print("no admitted AI4S record; nothing drawn")
        return 0
    with plt.style.context(["science", "nature", "no-latex"]):
        fig, axes = plt.subplots(1, len(panels), figsize=(min(6.75, 2.45 * len(panels) + 0.3), 2.3),
                                 squeeze=False)
        for ax, (name, fn) in zip(axes[0], panels):
            fn(ax, json.loads((REC / name).read_text(encoding="utf-8")))
        fig.tight_layout()
        fig.savefig(OUT, metadata={"CreationDate": None})
        fig.savefig(OUT.with_suffix(".png"), dpi=300)
    print(f"wrote {OUT} with {len(panels)} panel(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
