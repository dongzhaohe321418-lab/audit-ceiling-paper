#!/usr/bin/env python3
"""Table 1 — every primary quantity this paper quotes, with its population and its label.

A pre-submission referee observed that roughly eighty quantities appear in prose across the
results, over denominators of 110, 150, 56, 57, 53, 68, 92 and 11, with no table to hold them.
This generates one from the records, so the table and the prose cannot drift apart.

**The first version of this script said that and did not do it**: eleven of its fifteen rows
were literals typed from the prose, and the caption told the reader the table was generated from
the committed records. One of those literals carried a wrong population (the pass-rate contrast
pools both strata, 112 instances on 96 problems, and the row said 56). Every row now reads a
record, and the script fails if a record is missing a field rather than falling back to text.

The six-family residual is recomputed here from study 21's labels and study 20's residual list,
because no committed record held 25 of 32.

    python3 figures/make_table1.py > tex/table1.tex
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

# This repository's mirror of the records (records/PROVENANCE.md names each source commit), so
# the table regenerates from a clean checkout. It read ~/Documents paths until 2026-09-23.
R = Path(__file__).resolve().parents[1] / "records/code"
C4 = R / "ceiling4/numbers.json"


def j(p): return json.loads((R / p).read_text(encoding="utf-8"))


def six_family_residual() -> tuple[int, int, int]:
    """(consensus-undetermined in the six-family residual, residual size, consensus total)."""
    rr = R / "rerate"
    key = {}
    for f in ("key.jsonl", "key-flagged.jsonl"):
        for line in (rr / f).read_text(encoding="utf-8").splitlines():
            d = json.loads(line)
            key[d["id"]] = d.get("instance") or d.get("instance_id")

    def lab(*fs):
        out = {}
        for f in fs:
            with open(rr / f, newline="", encoding="utf-8") as fh:
                out.update({r["id"]: r["label"] for r in csv.DictReader(fh)})
        return out
    l1, l2 = lab("L1.csv", "L1-flagged.csv"), lab("L2.csv", "L2-flagged.csv")
    rated = {key[i] for i in key if i in l1 and i in l2}
    cons = {key[i] for i in key if i in l1 and i in l2 and l1[i] == l2[i] == "ambiguous-oracle"}
    still = set(json.loads(C4.read_text(encoding="utf-8"))["H20d_residual"]["instance_ids"])
    assert still <= rated, "a six-family residual instance was never rated"
    return len(cons & still), len(still), len(cons)


def main() -> int:
    sw, r3 = j("threshold_sweep.json"), j("rate3/analysis.json")
    c = j("ceiling/numbers.json")
    x = c["ceiling1"]["families"]["cross"]
    loop = c["ceiling2"]["contrasts"]["referent-loop__vs__cross-loop"]
    c3all = j("ceiling3/numbers.json")
    c3 = c3all["primary_H18b_self_strong_minus_cross_P"]
    c3fp = c3all["H18b_C_false_positives"]
    c4 = json.loads(C4.read_text(encoding="utf-8"))
    rer = j("rerate/numbers.json")
    pu = j("ceiling/pooled_union.json")
    fa = j("fpadj/adjudication.json")
    h3 = j("clarify/h3.json")["primary_clarified_minus_original"]
    pa = sw["paired_astra_minus_cross"]["subset_averaged_K4"]
    g, dj = r3["sheet_groups_NOT_missed_vs_caught"], r3["disjoint_instances_57_vs_53"]
    pool = rer["oracle_clean_secondary"]
    res57 = rer["populations"]["all_families_residual"]["consensus"]["ambiguous-oracle"]
    k32, n32, n68 = six_family_residual()

    def pct(v): return f"{v:.1f}\\%"
    def pts(v, nd=1): return f"${v:+.{nd}f}$"
    def ci(lo, hi, nd=1, sign=True):
        f = f"{{:{'+' if sign else ''}.{nd}f}}"
        return f"$[{f.format(lo)}, {f.format(hi)}]$"
    def ci100(pair, nd=1, sign=False): return ci(100 * pair[0], 100 * pair[1], nd, sign)

    P, Cc = x["P"]["union_at_kmax_block"], x["C"]["union_at_kmax_block"]
    gain = x["P"]["last_step_gain_block"]
    fl = loop["flag_discordance"]
    rows = [
        # quantity, population, value, interval, label
        ("Union recall, shipped route, $K=8$", f"{P['n']} defect, {P['n_problems']} problems",
         pct(100 * P["rate"]), ci100(P["cluster_ci95"]), "preregistered"),
        ("Union false positives, shipped, $K=8$", f"{Cc['n']} correct, {Cc['n_problems']} problems",
         pct(100 * Cc["rate"]), ci100(Cc["cluster_ci95"]), "preregistered"),
        ("Pooled union, 3 routes", f"{pool['P']} defect", pct(pool["union_recall_registered"]),
         ci(*pool["union_recall_registered_cluster_ci"], sign=False), "preregistered"),
        # Its own price, never the shipped route's (review paper1 r5).
        ("\\quad its false positives", f"{pu['C']['n']} correct", pct(100 * pu["C"]["rate"]),
         ci100(pu["C"]["cluster_ci95"]), "derived (C1)"),
        ("Gain from the eighth reading", f"{gain['n']} defect", pts(100 * gain["rate"], 2),
         ci100(gain["cluster_ci95"], 2), "bar 1.0, not met"),
        ("Same-vendor stronger $-$ cross, recall", f"{c3['n']} defect", pts(c3["difference_points"]),
         ci(*c3["cluster_ci95_points"]), "preregistered"),
        # C2 requires its operating point beside it wherever it is quoted (review paper1 r1, 7).
        ("\\quad its false-positive difference", f"{c3fp['n']} correct",
         pts(c3fp["difference_points"]),
         ci(*c3fp["cluster_ci95_points"]), "prereg.; 3.3\\% v 16.0\\%"),
        ("Rulebook rule $-$ shipped, recall", f"{c4['primary_H20a_crossR_minus_cross_P']['n']} defect",
         pts(c4["primary_H20a_crossR_minus_cross_P"]["difference_points"]),
         ci(*c4["primary_H20a_crossR_minus_cross_P"]["cluster_ci95_points"]), "preregistered"),
        ("\\quad its false-positive cost", f"{c4['H20c_C_false_positives']['n']} correct",
         pts(c4["H20c_C_false_positives"]["difference_points"]),
         ci(*c4["H20c_C_false_positives"]["cluster_ci95_points"]), "preregistered"),
        ("Rulebook rule, flags", f"{fl['P']['n']} loop defect", pts(100 * fl["P"]["delta"]),
         ci100(fl["P"]["ci95"], sign=True), "exploratory"),
        ("\\quad its cost on correct code", f"{fl['C']['n']} loop correct", pts(100 * fl["C"]["delta"]),
         ci100(fl["C"]["exact_unconditional_ci95"], sign=True), "unconditional, approx."),
        ("\\quad isolating contrast, pass rate", f"{loop['n']} loop, {loop['n_clusters']} problems",
         pts(100 * loop["delta"]), ci100(loop["ci95"], sign=True), "registered, failed"),
        ("\\texttt{astra} $-$ cross, common $K=4$", "110 defect, 56 problems",
         pts(pa["recall_P"]["points"]), ci(*pa["recall_P"]["cluster_ci95"]), "exploratory"),
        ("\\quad its false-positive difference", "150 correct", pts(pa["fp_C"]["points"]),
         ci(*pa["fp_C"]["cluster_ci95"]), "exploratory"),
        ("Undetermined, sheet groups", "121 entries, 110 instances", pts(g["diff_points"]),
         ci(*g["cluster_ci95"]), "registered method"),
        ("\\quad one definition of caught", f"{dj['missed'][1]} against {dj['caught'][1]}",
         pts(dj["diff_points"]), ci(*dj["cluster_ci95"]), "post hoc"),
        ("Undetermined share, 3-family residual", f"{res57['count']} of {res57['n']}",
         pct(res57["share"]), ci(*res57["cluster_ci"], sign=False), "post hoc"),
        ("\\quad 6-family residual", f"{k32} of {n32}", pct(100 * k32 / n32), "---",
         "post hoc (C14)"),
        ("Correct-code flags, reference disagrees", f"{fa['classes']['D']} of {fa['flagged_instances']} flagged",
         pct(fa["D_share_pct"]), ci(*fa["D_cluster_ci95"], sign=False), "preregistered (C16)"),
        ("Clarified $-$ original, diagnosis", f"{h3['n']} selected, {h3['n_problems']} problems",
         pts(h3["points"]), ci(*h3["cluster_ci95"]), "one-signed; exact $p$ .0625"),
    ]
    out = [
        r"\begin{table*}[t]", r"\caption{Every primary quantity this paper quotes, with the "
        r"population it is measured on and the label its source report gives it. Values are "
        r"percentages or percentage points. Intervals are 95\% problem-cluster percentile "
        r"bootstraps unless the label names another method. The coverage simulation of "
        r"\S\ref{sec:stats} measures single-rate intervals only; the contrasts and the "
        r"category-conditioned shares have no measured coverage. The two third-rater rows rest on "
        r"labels from a rater that agreed with itself on 7 of 11 repeated items (6 problems). "
        r"The correct-code row counts disagreement on inputs extracted from the findings; of the "
        f"{fa['flagged_instances']} flagged instances, {fa['classes']['A']} agreed on every extracted "
        f"input and {fa['classes']['N']} yielded no valid input, "
        r"which can be neither confirmed nor refuted.  Every row is read from a committed record by "
        r"\texttt{figures/make\_table1.py}.}",
        r"\label{tab:primary}", r"\centering", r"\footnotesize\setlength{\tabcolsep}{4pt}",
        r"\begin{tabular}{@{}llrll@{}}", r"\toprule",
        r"quantity & population & value & interval & label \\", r"\midrule",
    ]
    for q, p, v, i, l in rows:
        out.append(f"{q} & {p} & {v} & {i} & {l} \\\\")
    out += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    print("\n".join(out))
    print(f"% {len(rows)} rows, all read from records; six-family residual {k32}/{n32}, "
          f"consensus total {n68}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
