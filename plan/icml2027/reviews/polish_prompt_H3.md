You are co-editing an ICML 2027 submission with its author. Humanise the prose of these LaTeX files so that they read
as written by a careful human scientist in British academic English: vary sentence length and openings, cut
formulaic transitions and signposting, prefer concrete subjects and active verbs, remove filler and hedges that carry
no information, and keep the register plain. Hard constraints: do not change any number, interval, citation key,
label, \ref, math, claim strength or scope; do not add or remove claims; keep LaTeX valid; keep every \tbd{} as is.
Files (in audit-ceiling-paper/tex/): sections/framework.tex, sections/e6.tex, sections/natural.tex, sections/transfer.tex, sections/discussion_v3.tex, sections/introduction_v2.tex, and the abstract in paper_v3.tex. Keep every \\N... macro, \\input line, figure environment, table and label unchanged. Many sentences were recently revised to fix overclaims: do not strengthen any hedge or qualification.
Output, for each file, a unified diff against the current file (diff -u style, paths relative to
audit-ceiling-paper/), and after the diffs a short list of any sentence where you suspect a factual or logical problem
(do not fix those, just list them).
