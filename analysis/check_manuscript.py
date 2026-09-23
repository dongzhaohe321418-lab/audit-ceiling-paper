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
#: `paper.tex` was excluded until 2026-09-23, and it holds the abstract and the Limitations
#: section: the forbidden-claims check never read the most-quoted paragraph of the paper. Every
#: file is scanned now; `paper.tex` only `\input`s the others, so nothing is read twice.
SECTIONS = sorted((ROOT / "tex" / "sections").glob("*.tex")) + [
    f for f in sorted((ROOT / "tex").glob("*.tex")) if f.is_file()
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
    # Admitted claims carry prohibitions of their own; the list above had none of them, and the
    # abstract that quoted the forbidden interval passed this check (found 2026-09-23).
    # Review paper1 r1 (2026-09-23): five sentences the ledger now forbids.
    "study 23's substrate-dependent direction":
        r"direction is\s+substrate-dependent|substrate-dependent direction",
    "astra ranked on both axes":
        r"beats both on recall|dominating the shipped auditor on both",
    "no measurement moved":
        r"no measurement (?:ever )?moved",
    "the sweep read as recognition or cause":
        r"writes down\s+more of what is wrong|fact about severity\s+calibration",
    # gpt-5.6-luna was cheap-cross in the explore study; written as roleless on 2026-09-23.
    # Review paper1 r4: prior work misrepresented; luna's heading; comparator superiority.
    "consensus-validation work said to omit residual error":
        r"in neither paper could we find",
    "SWR-Bench aggregation equated with union":
        r"same mechanical move",
    "luna said to have audited nothing":
        r"rater that audited nothing",
    "comparator superiority asserted":
        r"neither beats the\s+free",
    # Review paper1 r6.
    "operating-point matching said impossible from archived findings":
        r"only that can place|no reachable point",
    "coverage asserted of reported intervals":
        r"intervals are narrower than they claim|read\s+as narrower than they claim",
    # Review paper1 r9: the rulebook contrast is recall at K = 1, not "not recall".
    "rulebook contrast denied to be recall":
        r"counts flags, not\s+union recall",
    # L1 was Claude, the agent that ran the programme, not a human (found 2026-09-23).
    "L1 described as a human author":
        r"one an author|by an author|an author and|human judgement|was the author, who",
    "luna called roleless":
        r"no audit role",
    # Review paper1 r3: the post-hoc oracle-agreement split read as a mechanism.
    "P3 split read as mechanism":
        r"what moved diagnosis was",
    "P3 read as unselected":
        r"not conditioned on being\s+missed",
    "C1: the curve saturates (the flattening bar was not met)":
        r"\bsaturates\b|reaches saturation|has saturated|curve saturat",
    "C2 read as auditing ability":
        r"is a worse auditor|stronger model is (?:a )?worse",
    "C13: a causal verb on the clarification result":
        r"(?:underdetermination|ambiguity|incompleteness) (?:causes|caused|explains)",
    "study 22 licensing a bound on the ceiling":
        r"construction licenses is a bound",
}


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def main() -> int:
    body = " ".join(flat(f.read_text(encoding="utf-8")) for f in SECTIONS)
    failures: list[str] = []

    # A forbidden sentence may be named in order to deny it ("the evidence does not support `a
    # stronger model is a worse auditor'"). A hit counts unless the 70 characters before it carry
    # a negation or an opening quotation mark; the pre-54a5802 abstract, which asserted two of
    # these, still fails.
    for name, pattern in FORBIDDEN.items():
        hits = [m.group(0) for m in re.finditer(pattern, body, flags=re.I)
                if not re.search(r"\bnot\b|\bno\b|``", body[max(0, m.start() - 70):m.start()])]
        if hits:
            failures.append(f"forbidden claim present -- {name}: {hits[:2]}")

    # The percentile bootstrap's interval on the one-signed C-stratum cost may appear only where
    # the text says it is forbidden -- which is how the historical correction names it.
    for m in re.finditer(r"5\.17, 21\.82", body):
        if "forbidden" not in body[max(0, m.start() - 80):m.start()]:
            failures.append(f"forbidden interval quoted: ...{body[max(0, m.start() - 80):m.end() + 10]}...")

    # The pooled recall never without its own price (review paper1 r5): 48.2% came beside the
    # shipped route's 16.0% for four rounds.
    for m in re.finditer(r"48\.2\\?%", body):
        near = body[max(0, m.start() - 300): m.end() + 300]
        if "36.0" not in near and "forbidden" not in near:
            failures.append(f"pooled recall without its false-positive rate: ...{body[m.start()-60:m.end()+60]}...")

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
