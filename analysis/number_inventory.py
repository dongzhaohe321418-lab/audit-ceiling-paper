#!/usr/bin/env python3
"""Every number in the manuscript, as a multiset, so a prose rewrite can be diffed for lost or
changed numbers.

    python3 analysis/number_inventory.py > /tmp/before.txt      # before the edit
    python3 analysis/number_inventory.py --diff /tmp/before.txt  # after: what was removed / added

A rewrite may remove a number only with a stated reason (e.g. it lived in a note about an earlier
draft); it may add one only if it already appears in CLAIMS.md or a record.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "tex"
FILES = [ROOT / "paper.tex", *sorted((ROOT / "sections").glob("*.tex"))]
NUM = re.compile(r"(?<![\w.])[-+−]?\d+(?:\{,\}\d+|,\d{3})*(?:\.\d+)?(?:\\?%)?")


def inventory() -> Counter:
    c: Counter = Counter()
    for f in FILES:
        text = re.sub(r"(?<!\\)%.*", "", f.read_text(encoding="utf-8"))
        text = re.sub(r"\\(label|ref|cite[pt]?|includegraphics|input)(\[[^]]*\])?\{[^}]*\}", "", text)
        for m in NUM.finditer(text):
            tok = m.group(0).replace("{,}", ",").replace("\\%", "%").replace("−", "-").lstrip("+")
            c[(f.name, tok)] += 1
    return c


def main() -> int:
    inv = inventory()
    if len(sys.argv) == 3 and sys.argv[1] == "--diff":
        before: Counter = Counter()
        for line in Path(sys.argv[2]).read_text().splitlines():
            f, tok, n = line.split("\t")
            before[(f, tok)] = int(n)
        # compare across files too: a number moved between sections is not lost
        b_all, a_all = Counter(), Counter()
        for (f, t), n in before.items(): b_all[t] += n
        for (f, t), n in inv.items(): a_all[t] += n
        removed, added = b_all - a_all, a_all - b_all
        print("REMOVED:", sorted(removed.elements()))
        print("ADDED:  ", sorted(added.elements()))
        return 0
    for (f, t), n in sorted(inv.items()):
        print(f"{f}\t{t}\t{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
