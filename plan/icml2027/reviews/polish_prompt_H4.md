You are co-editing an ICML 2027 submission with its author. Humanise the prose of passages added or revised since
your last pass (git -C audit-ceiling-paper log shows them; compare with commit df0eaea-era text if useful) so that
they read as written by a careful human scientist in British academic English: vary sentence length and openings, cut
formulaic transitions and signposting, prefer concrete subjects and active verbs, remove filler and hedges that carry
no information, and keep the register plain.
Passages (in audit-ceiling-paper/tex/):
- sections/transfer.tex: the paragraph "Randomised contracts on data-science code" (E7/E11).
- sections/e6.tex: the E9 sentence and the E10 paragraph (search "E9" and "E10").
- sections/discussion_v3.tex: the Limitations paragraph.
- sections/introduction_v2.tex: the bullet beginning "Adding the missing requirement".
- paper_v3.tex: the abstract.
Hard constraints: do not change any number, interval, citation key, label, \ref, math, macro (\N...), claim strength
or scope; do not add or remove claims; do not strengthen any hedge or qualification (several were set by a reviewer
to fix overclaims, e.g. "constructed library tasks", "26.4% false-flag rate", "not registered here"); keep LaTeX
valid. The main text is exactly at the 8-page limit: every replacement must be no longer than the original, and
the set of changes should shorten the text by at least two lines overall.
Output: for each file, a unified diff against the current file (paths relative to audit-ceiling-paper/), then a short
list of any sentence where you suspect a factual or logical problem (do not fix those). Do not modify files.
