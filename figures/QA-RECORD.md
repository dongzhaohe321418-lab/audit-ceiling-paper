# Figure QA, 2026-09-23

Both figures audited with `nature-figure`'s scripts before delivery.

## Minimum font size (`audit_pdf_text.py`, floor 5 pt)

| figure | before | after | verdict |
|---|---|---|---|
| `fig2_sweep.pdf` | 4.6 pt | 5.2 pt | **PASS** |
| `fig3_residual.pdf` | 4.8 pt | 5.0 pt | **PASS** |

Both failed on first audit. The rule legend and the diagonal annotation in figure 2, and the
red annotation in figure 3, were below the floor.

## Collisions (`audit_figure_collisions.py`)

| figure | first audit | after repair |
|---|---|---|
| `fig2_sweep.pdf` | 1 fail, 4 warn — **FIX BEFORE DELIVERY** | 0 fail, 4 warn |
| `fig3_residual.pdf` | 1 fail — **FIX BEFORE DELIVERY** | **0 fail, 0 warn, PASS** |

Two real defects, both invisible at screen size and both caught by the audit:

* **Figure 3**: the `+54.2` value label was crossed by its own error bar's stroke. Value labels
  now sit below their markers, clear of the whiskers.
* **Figure 2**: the rotated `recall = false positives` annotation lay on the diagonal and was
  crossed by **four** error bars. It moved to the empty lower-right corner, unrotated. The rule
  legend also sat inside the axes touching a plotted region; it moved below the axes.

## The four remaining warnings, inspected at final size

All four are the same finding: a legend marker glyph touching the edge of its own text's fill
region in the decision-rule legend. Inspected at 260 dpi. This is ordinary legend rendering, not
an overlap of two pieces of information, and it is accepted rather than suppressed.

## What the audit does not cover, and was checked by hand

* **Colour accessibility.** Five families use matplotlib's `tab10`, which is not
  colourblind-safe end to end. Marker shape carries the decision rule independently of colour,
  so every point remains identifiable by shape plus position, but **family identity is
  colour-only**. A reader with deuteranopia can distinguish the points but may not separate
  `self` from `astra`. Recorded as a known limitation rather than fixed, because switching to a
  Paul Tol palette would change all three figures and figure 1 is already published in the
  record.
* **Whether the figures claim more than the data.** Figure 2's dotted guides join a family's
  four reachable points and could be read as an interpolated curve; the caption says in its
  second sentence that they are guides and that only four points exist. Figure 3's panel labels
  still use the superseded word "disjoint" for what the ledger now calls a definitional overlap,
  which a referee flagged and which is **open**.
