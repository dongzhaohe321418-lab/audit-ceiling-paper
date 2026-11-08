You are co-editing an ICML 2027 submission with its author. Humanise the prose of these LaTeX files so that they read
as written by a careful human scientist in British academic English: vary sentence length and openings, cut
formulaic transitions and signposting, prefer concrete subjects and active verbs, remove filler and hedges that carry
no information, and keep the register plain. Hard constraints: do not change any number, interval, citation key,
label, \ref, math, claim strength or scope; do not add or remove claims; keep LaTeX valid; keep every \tbd{} as is.
Files (in audit-ceiling-paper/tex/sections/): introduction_v2.tex, e6.tex, natural.tex. In e6.tex keep the \\input line, figure environment and its caption labels unchanged.
Output, for each file, a unified diff against the current file (diff -u style, paths relative to
audit-ceiling-paper/), and after the diffs a short list of any sentence where you suspect a factual or logical problem
(do not fix those, just list them).
