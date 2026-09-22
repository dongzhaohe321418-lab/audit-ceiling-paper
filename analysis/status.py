#!/usr/bin/env python3
"""Regenerate STATUS.md from the live system. Run it; do not hand-edit the output.

The owner asked to be kept in sync continuously. A hand-written status page goes stale the
moment something finishes, so the volatile parts -- what is running, what the Codex allowance
says, the latest commit on each branch, what is blocked on whom -- are read from the machine
every time this runs. The narrative parts are short and dated.

    python analysis/status.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = Path.home() / "Documents" / "Crossaudit" / "codex-review-queue"
REPOS = {
    "paper": ROOT,
    "harness (fusion)": Path.home() / "Documents" / "Crossaudit" / "crossaudit_integ",
    "study/injection": Path.home() / "Documents/Crossaudit/review-worktrees/wt-inject",
    "study/ceiling4": Path.home() / "Documents/Crossaudit/review-worktrees/wt-ceiling4",
    "study/ceiling3b": Path.home() / "Documents/Crossaudit/review-worktrees/wt-ceiling3b",
    "study/testgen-val": Path.home() / "Documents/Crossaudit/review-worktrees/wt-testval",
}


def sh(*args: str, cwd: Path | None = None) -> str:
    try:
        return subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                              timeout=20).stdout.strip()
    except Exception:                                                  # noqa: BLE001
        return ""


def running() -> list[str]:
    out = []
    for pat, label in (("codex exec", "cross-vendor review"),
                       ("dispatch.sh", "review dispatcher"),
                       ("guard-all.sh", "report snapshot guard"),
                       ("third_rater", "third-rater run"),
                       ("audit2_sub", "study 23 audit"),
                       ("clarify/audit_run", "P3 audit readings"),
                       ("clarify/generate", "P3 condition generation"),
                       ("manipulation_check", "P3 manipulation check")):
        pids = sh("pgrep", "-f", pat).split()
        if pids:
            out.append(f"{label} ({len(pids)} process{'es' if len(pids) > 1 else ''})")
    return out


def codex_quota() -> str:
    """Probe the allowance LIVE.

    The first version of this read a cached probe file, and on its first run reported an
    allowance as exhausted nine hours after it had returned. A status page that serves a stale
    reading as current is worse than one that says it does not know.
    """
    import re
    try:
        r = subprocess.run(
            ["codex", "exec", "-m", "gpt-6-astra", "-c", 'model_reasoning_effort="low"',
             "--sandbox", "read-only", "--skip-git-repo-check", "-"],
            input="Reply with exactly: OK", capture_output=True, text=True, timeout=90)
    except Exception as exc:                                           # noqa: BLE001
        return f"probe failed ({type(exc).__name__})"
    blob = (r.stderr or "") + (r.stdout or "")
    if "usage limit" in blob.lower():
        m = re.search(r"try again at ([^\.]+)", blob)
        return f"exhausted, returns {m.group(1).strip()}" if m else "exhausted"
    return "available" if r.returncode == 0 else f"probe exit {r.returncode}"


def reviews() -> list[str]:
    rows = []
    for d in sorted(QUEUE.glob("codex-review-*")):
        rounds = sorted(d.glob("report-r*.md"))
        rep = d / "report.md"
        verdict = ""
        if rep.exists() and rep.stat().st_size:
            text = rep.read_text(errors="ignore")
            for line in reversed(text.splitlines()):
                if "quotable" in line.lower():
                    verdict = line.strip().strip("*")[:120]
                    break
        rows.append(f"| `{d.name}` | {len(rounds)} | {verdict or '—'} |")
    return rows


def main() -> int:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    live = running()
    lines = [
        "# Status",
        "",
        f"*Generated {now} by `analysis/status.py`. Do not hand-edit: run the script.*",
        "",
        "## Running now",
        "",
        *([f"* {x}" for x in live] or ["* nothing"]),
        "",
        f"**Codex allowance:** {codex_quota()}",
        "",
        "## Blocked on the owner",
        "",
        "* **P1, the 121-item blinded rating by a human from outside the project** —",
        "  `~/Desktop/CrossAudit-审计天花板/人类评分任务/`. The sheet was rebuilt 2026-09-22 on",
        "  mechanical evidence after its control arm was found unanswerable, and a third MODEL",
        "  has now rated it (C12). **That does not discharge this**: P1 exists to obtain a",
        "  rating by someone outside the project, and C12 says so in the claim itself.",
        "* **The Anthropic credit**, which blocks every same-vendor arm and the",
        "  temperature-matched replication.",
        "",
        "## Decided, and recorded rather than left implied",
        "",
        "* **P3 proceeds on model raters alone.** The owner delegated the decision; the",
        "  precondition was checked and holds, the registered manipulation check cleared its",
        "  bar, and the audit readings are being bought. Every step is in",
        "  `plan/P3-PREREGISTRATION.md` with the amendment that governs it.",
        "",
        "## Review rounds",
        "",
        "| queue | rounds archived | latest verdict |",
        "|---|---:|---|",
        *reviews(),
        "",
        "## Branch tips",
        "",
        "| repo | head | subject |",
        "|---|---|---|",
    ]
    for name, path in REPOS.items():
        if not path.exists():
            lines.append(f"| {name} | — | worktree missing |")
            continue
        head = sh("git", "rev-parse", "--short", "HEAD", cwd=path)
        subj = sh("git", "log", "-1", "--format=%s", cwd=path)[:90]
        dirty = sh("git", "status", "--porcelain", cwd=path)
        mark = " *(uncommitted changes)*" if dirty else ""
        lines.append(f"| {name} | `{head}` | {subj}{mark} |")
    (ROOT / "STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote STATUS.md — {len(live)} running, {len(reviews())} review queues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
