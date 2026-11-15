# Cold audits of the humanisation passes (2026-11-15)
Prompted by pass H6 having changed the main title unannounced (restored in 51bc338). Two unanchored Claude subagents
diffed every pass for unannounced meaning changes (claim strength, hedges, scope, causal words, who-did-what,
citations, headings).

H4-H7 (e3c2f2c, 5ed0a47, 6caefdc, a659d8e): besides the title, one sentence needed fixing: H5 made the flag
preference the subject of the E9 23-unit sentence while citing E6-2/E6-5 numbers; corrected in 5ec2096 (registered
criteria hold; flag preference +17.4 [5.4, 31.5], checked against e9_results_test.json). Announced hedge and scope
changes were reviewed and kept.

H1-H3 and the Claude pass (2a1426d, e071cce, 673afbf, 054b5d2): the two problems that changed meaning (a removed
"check, not a finding" hedge and a garbled convention sentence in 054b5d2) had already been rewritten by later
revisions. Still present and checked: the SciCode-Verified citation added by H1 (accurate: tests that reject correct
solutions); the heading "Interpretation."; "does about as well" (sentence minus resolved menu +1.2 [0.0, 3.0]). No
further change needed.

Practice from now on: titles are excluded from polishing scope unless the author asks, and every pass is diffed for
meaning, not only for numbers and hedge words.
