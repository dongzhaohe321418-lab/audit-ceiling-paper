You are co-editing an ICML 2027 submission with its author. Humanise these appendix paragraphs so they read as written
by a careful human scientist in British academic English: vary sentence length and openings, cut formulaic
transitions, prefer concrete subjects and active verbs, split overlong sentences, remove filler. They are dense
protocol descriptions; clarity for a reviewer matters more than brevity, but do not lengthen them by more than 10%.
File: audit-ceiling-paper/tex/appendix/e6_protocol.tex. Paragraphs: "Exception contracts (exploratory...)", the E9
paragraph, the E10 paragraph, and "Data-science tasks by localised edits (E11)". Leave tables untouched.
Hard constraints: do not change any number, interval, label, \ref, citation, math or macro; do not add or remove
claims; do not strengthen any hedge or qualification (several were set by a reviewer: "policy" false-flag rate,
"constructed library tasks", "the classification rests on the exit status", "written after the held-out audits",
"not registered here", "conditional on flagging"); keep LaTeX valid.
Output: one unified diff against the current file (path relative to audit-ceiling-paper/), then a short list of any
sentence where you suspect a factual or logical problem (do not fix those). Do not modify files.
