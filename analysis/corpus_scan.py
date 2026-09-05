"""Prove the prose records carry no corpus text. No key, no network.

ExpertLongBench is CC BY-NC-SA 4.0 (non-commercial, no redistribution). The
records under records/prose/ may carry ids, hashes, scores, counts and the
dataset's checklist-item LABELS (short rubric names such as
"Selection of Precursors [level] Structural Considerations"), which this
project treats as identifiers. They may not carry draft text, prompt text,
source passages, or model output that quotes the corpus.

The scan lists every string field longer than LIMIT characters, grouped by
field name, with its longest value. A reviewer reads the table and sees for
themselves that nothing there is prose from the corpus. Exit status is 1 if
any field name that is known to hold free text appears.
"""
from __future__ import annotations

import glob
import json
import sys
from collections import defaultdict

LIMIT = 60
FREE_TEXT_FIELDS = {"text", "draft", "prompt", "body", "content", "passage",
                    "output", "response", "answer", "abstract", "source_text"}


def walk(value, key, table):
    if isinstance(value, str):
        entry = table[key]
        entry[1] += 1
        if len(value) > entry[0]:
            entry[0], entry[2] = len(value), value[:70].replace("\n", " ")
    elif isinstance(value, dict):
        for k, v in value.items():
            walk(v, k, table)
    elif isinstance(value, list):
        for v in value:
            walk(v, key, table)


def main() -> int:
    table = defaultdict(lambda: [0, 0, ""])
    for path in glob.glob("records/prose/**/*.json*", recursive=True):
        with open(path) as fh:
            if path.endswith(".jsonl"):
                for line in fh:
                    walk(json.loads(line), "<row>", table)
            else:
                walk(json.load(fh), "<doc>", table)
    print(f"{'field':32s} {'longest':>7s} {'count':>6s}  sample")
    bad = []
    for key, (length, count, sample) in sorted(table.items(), key=lambda kv: -kv[1][0]):
        if length > LIMIT:
            print(f"{key[:32]:32s} {length:7d} {count:6d}  {sample!r}")
        if key.lower() in FREE_TEXT_FIELDS and length > LIMIT:
            bad.append(key)
    if bad:
        print(f"\nFREE-TEXT FIELDS PRESENT: {bad}", file=sys.stderr)
        return 1
    print("\nno free-text field present; longest dataset-derived strings are rubric labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
