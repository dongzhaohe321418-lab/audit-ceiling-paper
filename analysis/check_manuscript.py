#!/usr/bin/env python3
"""Mechanical checks on the manuscript, run before any submission.

Why this exists. Twice in one week a study's own correction failed to reach the paper, and
both times the gap was found by a reviewer rather than by us:

  * Study 23 closed without a quotable number. CLAIMS.md recorded that `tex/` carried none of
    its figures, because the check had been a grep for `76.8`, `46.8`, `substrate 2` and
    `BigCodeBench`. Three of its conclusions were in the text, written out in words -- "more
    than twice the recall", "the two substrates' false-positive intervals never meet", and "a
    study on a second substrate reverses that sign", the last of which its own clean run had
    contradicted.
  * Study 22 withdrew its causal reading of the separability probe at review round 7. The
    introduction still called the probe result "the same fact from the other side" and the
    discussion still said the construction licenses a bound on the measured ceiling.

A grep for numerals does not find a claim written as a sentence. These checks look for the
CLAIMS of the forbidden list and for the shape of an unqualified figure, and they are
deliberately crude: they are a floor under the reading, not a substitute for it.

    python analysis/check_manuscript.py        # non-zero exit on any failure
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
#: Every .tex the manuscript actually compiles, not only the ones under `sections/`. A generated
#: table lived at `tex/table1.tex` and the checker reported its label as undefined -- the
#: checker's blind spot, not the paper's error. Anything `\input` from the body counts.
SECTIONS = sorted((ROOT / "tex" / "sections").glob("*.tex")) + [
    f for f in sorted((ROOT / "tex").glob("*.tex"))
    if f.name not in {"paper.tex"} and f.is_file()
]

#: Sentences CLAIMS.md's "must not appear" list forbids, as patterns a reader would recognise
#: rather than as the numbers behind them.
FORBIDDEN = {
    "the ceiling is set by unexercised edges":
        r"ceiling is set by unexercised|set by unexercised edges",
    "the ceiling is set by oracle-defined failures":
        r"ceiling is set by oracle|oracle-defined failures set",
    "CrossAudit finds most defects":
        r"finds most defects|most of the defects are found",
    "the auditor cannot see these defects":
        r"cannot see these defects|auditor cannot see",
    # Study 23, closed without a quotable number. Its conclusions, not its numerals.
    "substrate 2's recall comparison":
        r"more than twice the recall|three times as much correct work",
    "substrate 2's matched-operating-point claim":
        r"intervals never meet|no reading count offers a matched",
    "substrate 2's same-vendor sign reversal":
        r"reverses that sign(?!\.\s*\\emph\{That is withdrawn\})|"
        r"direction\s+reverses on a second substrate(?!;)",
    # Study 22, whose causal reading of the probe was withdrawn at round 7.
    "study 22's probe identifying edit salience":
        r"same fact\s+from the other side|probe shows that salience is detectable|"
        r"detectably artificial",
    "study 22 licensing a bound on the ceiling":
        r"construction licenses is a bound",
}


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def main() -> int:
    body = " ".join(flat(f.read_text(encoding="utf-8")) for f in SECTIONS)
    failures: list[str] = []

    for name, pattern in FORBIDDEN.items():
        hits = re.findall(pattern, body, flags=re.I)
        if hits:
            failures.append(f"forbidden claim present -- {name}: {hits[:2]}")

    # Every asymptote must be qualified where the flattening bar was not met.
    for m in re.finditer(r"asymptote", body, flags=re.I):
        near = body[max(0, m.start() - 220) : m.end() + 280]
        if not re.search(r"extrapolation|not met|does not establish|would be quotable",
                         near, flags=re.I):
            failures.append(f"asymptote without its qualification: ...{near[200:320].strip()}...")

    # A number split by an insertion: "reach 48. <inserted text> looks.2% [36.7, 60.0]". The
    # fragment glued onto a word is what survives; it read cleanly enough to pass two builds.
    for m in re.finditer(r"[a-z]{2}\.[0-9]", body):
        failures.append(f"number fragment glued to a word: ...{body[max(0, m.start() - 40):m.end() + 30]}...")

    # Every label is referenced, and every reference has a label.
    labels = set(re.findall(r"\\label\{([a-z]+:[a-z0-9-]+)\}", body))
    refs = set(re.findall(r"\\ref\{([a-z]+:[a-z0-9-]+)\}", body))
    for missing in sorted(refs - labels):
        failures.append(f"reference to a label that does not exist: {missing}")
    for orphan in sorted(labels - refs):
        failures.append(f"label never referenced: {orphan}")

    if failures:
        print(f"{len(failures)} manuscript check(s) failed:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"manuscript checks pass ({len(SECTIONS)} sections, {len(labels)} labels)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
