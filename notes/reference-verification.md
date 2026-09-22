# Reference verification, 2026-09-23

Every entry in `tex/paper.bib` checked against the arXiv API (`export.arxiv.org/api/query`)
by id, with titles and complete author lists compared field by field.

**14 entries. All 13 arXiv ids resolve to a real paper, and no entry is fabricated.** Three
carried errors serious enough to correct, and four understated their author lists.

## ❌ Corrected

| entry | what was wrong |
|---|---|
| `tan2025consistent` | listed **4 authors of 11**, with no `and others` — a reader would take those four for the whole list. Now complete. |
| `zeng2025swrbench` | title truncated: "…Real-World Code Review" for "…Real-World Code Review **Comment Generation**" |
| `xu2025consensus` | title carried a clause the paper does not have: "…Test Generation **with Accurate Oracles**" |

## ⚠️ Improved

`zeng2025swrbench`, `xu2025consensus`, `chen2025selfpreference` and `taherkhani2026consistency`
used `and others` where the full list is 4, 5, 5 and 10 names. All are now complete: at this
length there is no reason to elide.

## ⚠️ Noted, not changed

`vaccaro2026prereg` has id `2606.11217` — June 2026 by arXiv's numbering — while the API reports
a published date of 2026-05-03. Both were recorded; the entry cites the id, which resolves to
the right paper.

## Machine-checkable from the bibliography itself

Every arXiv entry now carries `eprint` and `archivePrefix` fields, so a reader can resolve each
id without parsing the `journal` string. 13 of 14 entries have them; the fourteenth is a NeurIPS
paper.

## One method note worth keeping

The script that added those fields first used `"eprint" not in block` to decide whether the
field was already present. **Every arXiv entry contains "arXiv pr*eprint*"**, so the test was
true for all of them and nothing was added. A substring test standing in for a field test — the
same shape as the defects this programme keeps finding in its own checks, at a smaller scale.
The fix matches `^\s*eprint\s*=` as a field.
