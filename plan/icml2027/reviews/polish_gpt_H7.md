```diff
--- a/tex/appendix/e6_protocol.tex
+++ b/tex/appendix/e6_protocol.tex
@@ -183,60 +183,66 @@
 three analyses. The frozen estimates may therefore slightly understate verified diagnosis once the contract
 is stated; the recrediting does not check the type of the exception.
 
-\paragraph{Code shape (exploratory).} Added after an unanchored review asked whether the flag preference reflects
-how the code looks rather than a convention (\texttt{e6\_code\_shape.py}; not registered). Program A implements the
-rule the models' own solutions rarely follow, and in 20 of the 41 held-out units its code has more conditionals than
-B's. With the task alone, the flag preference is +38.8 [20.0, 58.8] on those 20 units and +9.5 [$-$7.1, 26.2] on the
-other 21; the convention advantage is +18.1 [9.4, 27.5] and +5.4 [$-$3.0, 13.7]. The split does not separate the two
-explanations, since departing from the convention often needs extra code, but part of the preference may come from
-what the code looks like. E6-5 is +67.5 [53.8, 80.0] and +85.7 [76.2, 94.0] in the two strata.
-
-\paragraph{Shape control (E13).} Registered after the split above (\texttt{benchmarks/e13/}, reviewed before the
-held-out run, frozen before any held-out reading). For each registered unit the vendor that wrote the audited
-programs rewrote B into B$'$, which sends the class inputs through an explicit branch computing what B computes and
-keeps every other line of B. Execution checks: on every registered admission input B$'$ has B's status and value; it
-passes the visible tests, adds at least one conditional and removes no line of B. 40 of the 41 held-out units passed
-(Mbpp/93: both edits differed from B on one input; it is missing under the registered bounds). A, B and B$'$ were then
-read afresh, interleaved in a seeded random order, in the task-alone arm with E6's four configurations, prompt,
+\paragraph{Code shape (exploratory).} We added this analysis after an unanchored review asked whether the flag
+preference reflects how the code looks rather than a convention (\texttt{e6\_code\_shape.py}; not registered).
+Program A implements the rule the models' own solutions rarely follow. In 20 of the 41 held-out units, its code
+has more conditionals than B's. With the task alone, the flag preference is +38.8 [20.0, 58.8] on those 20 units
+and +9.5 [$-$7.1, 26.2] on the other 21. The convention advantage is +18.1 [9.4, 27.5] and +5.4 [$-$3.0, 13.7].
+The split does not separate the two explanations: departing from the convention often needs extra code.
+Part of the preference may nevertheless come from what the code looks like. E6-5 is +67.5 [53.8, 80.0] and
++85.7 [76.2, 94.0] in the two strata.
+
+\paragraph{Shape control (E13).} We registered this study after the split above (\texttt{benchmarks/e13/},
+reviewed before the held-out run and frozen before any held-out reading). For each registered unit, the vendor
+that wrote the audited programs rewrote B into B$'$. The rewrite sends the class inputs through an explicit
+branch computing what B computes and keeps every other line of B. Execution checks require B$'$ to have B's
+status and value on every registered admission input. It must also pass the visible tests, add at least one
+conditional and remove no line of B. 40 of the 41 held-out units passed (Mbpp/93: both edits differed from B on
+one input; the unit is missing under the registered bounds). We then obtained fresh readings of A, B and B$'$
+in the task-alone arm, interleaved in a seeded random order. These used E6's four configurations, prompt,
 rulebook and scoring; 960 of 960 readings were valid. Adding the branch changed B's flag rate by +0.6 points
-[$-$1.2, 2.5] (bounds $-$1.8, 3.0; E13-1, inside the registered $\pm$10-point margin: no shape effect detected). A was
-flagged 20.6 [6.9, 33.8] points more often than B$'$ (E13-2: supported) and 21.2 [8.1, 33.8] more often than B in the
-same fresh readings; the convention advantage was +10.6 [4.7, 16.6] with B and +10.0 [3.4, 16.2] with B$'$. The
-remaining preference is still concentrated where A has more conditionals (+34.2 [17.1, 52.6] on 19 units, +8.3
-[$-$9.5, 26.2] on 21). E13 detects little effect of adding branches to B; it does not test other features of A's code or
-distinguish a convention from the behaviour A implements. The prespecified per-vendor and between-stratum estimates
-(\texttt{e13\_secondary\_test.json}, computed after the held-out run with E6's frozen code) are: B$'$ minus B +2.5
-[$-$2.5, 7.5] for GPT and $-$1.2 [$-$3.8, 0.0] for Claude; A minus B$'$ +16.2 [2.5, 31.2] and +25.0 [8.8, 41.2]; the
-difference between the strata is $-$1.2 [$-$5.3, 2.8] for B$'$ minus B and +25.9 [0.6, 52.1] for A minus B$'$. Edits
-added a median of 1 conditional and 2.5 lines (at most 9).
-
-\paragraph{Matched pairs (E14).} Registered after E13 and reviewed twice before the held-out run (a first design,
-rewriting A with fewer conditionals, was rejected because the special case could survive as arithmetic on a
-comparison; \texttt{benchmarks/e14/}). For each unit the vendor that wrote the audited programs wrote a pair M$_A$,
-M$_B$ that agrees with A and B, respectively, in execution status and returned value under E6's comparator on
-every registered admission input and is identical except for the body of one \texttt{if}: same
-position in the syntax tree, same non-constant condition, identical trees with that body masked and identical source
-outside it; M$_A$ and M$_B$ must also differ on at least two valid class inputs, so the body runs. 38 of 41 held-out
-units passed (three gave no parseable pair in three attempts). A, B, M$_A$ and M$_B$ were read afresh, interleaved,
-in the task-alone arm with E6's four configurations; 1{,}216 of 1{,}216 readings were valid (one after a registered
-third attempt). M$_A$ was flagged more often than M$_B$: complete cases +28.9 [14.5, 42.8], $n=38$; with the three missing
-units at the worst value, +19.5 [2.4, 35.4], $n=41$ (E14-1: supported). In the same readings A was flagged 26.3 [14.5, 38.2]
-points more often than B, so matching the surrounding code changed the preference by +2.6 [$-$3.9, 9.2]. The
-preference is +40.0 [23.8, 57.5] on the 20 units whose A has more conditionals and +16.7 [$-$4.2, 36.1] on the 18 of
-21 others analysed. The pairs still differ inside the branch body (for example a loop against a single
-\texttt{return}; body spans have medians of 1 and 1 lines and maxima of 10 and 3 for M$_A$ and M$_B$, and M$_A$'s
-body is longer in 9 of 38 pairs), so E14 shows that the preference persists with identical surrounding code, not that it is
-independent of how each rule is written; it cannot separate a convention from a plain reading of the task.
+[$-$1.2, 2.5] (bounds $-$1.8, 3.0; E13-1, inside the registered $\pm$10-point margin: no shape effect detected).
+A was flagged 20.6 [6.9, 33.8] points more often than B$'$ (E13-2: supported) and 21.2 [8.1, 33.8] more often
+than B in the same fresh readings. The convention advantage was +10.6 [4.7, 16.6] with B and +10.0 [3.4, 16.2]
+with B$'$. The remaining preference is still concentrated where A has more conditionals (+34.2 [17.1, 52.6]
+on 19 units, +8.3 [$-$9.5, 26.2] on 21). E13 detects little effect of adding branches to B. It does not test
+other features of A's code or distinguish a convention from the behaviour A implements. We computed the
+prespecified per-vendor and between-stratum estimates after the held-out run with E6's frozen code
+(\texttt{e13\_secondary\_test.json}). B$'$ minus B was +2.5 [$-$2.5, 7.5] for GPT and $-$1.2 [$-$3.8, 0.0] for
+Claude. A minus B$'$ was +16.2 [2.5, 31.2] and +25.0 [8.8, 41.2]. The difference between the strata is
+$-$1.2 [$-$5.3, 2.8] for B$'$ minus B and +25.9 [0.6, 52.1] for A minus B$'$. Edits added a median of
+1 conditional and 2.5 lines (at most 9).
+
+\paragraph{Matched pairs (E14).} We registered this study after E13 and had it reviewed twice before the
+held-out run (\texttt{benchmarks/e14/}). The first design, which rewrote A with fewer conditionals, was rejected
+because the special case could survive as arithmetic on a comparison. For each unit, the vendor that wrote
+the audited programs wrote a pair M$_A$, M$_B$. They agree with A and B, respectively, in execution status and
+returned value under E6's comparator on every registered admission input. They are identical except for the
+body of one \texttt{if}: the branch has the same position in the syntax tree and the same non-constant condition.
+With that body masked, the trees are identical; the source outside it is also identical. M$_A$ and M$_B$ must
+also differ on at least two valid class inputs, so the body runs. 38 of 41 held-out units passed (three gave
+no parseable pair in three attempts). Auditors read A, B, M$_A$ and M$_B$ afresh in E6's four configurations,
+interleaved in the task-alone arm. All 1{,}216 of 1{,}216 readings were valid (one after a registered third attempt).
+M$_A$ was flagged more often than M$_B$: complete cases +28.9 [14.5, 42.8], $n=38$. With the three missing
+units at the worst value, the difference was +19.5 [2.4, 35.4], $n=41$ (E14-1: supported).
+In the same readings, A was flagged 26.3 [14.5, 38.2] points more often than B. Matching the surrounding code
+therefore changed the preference by +2.6 [$-$3.9, 9.2]. The preference is +40.0 [23.8, 57.5] on the 20 units
+whose A has more conditionals and +16.7 [$-$4.2, 36.1] on the 18 of 21 others analysed.
+The pairs still differ inside the branch body, for example a loop against a single \texttt{return}.
+Body spans have medians of 1 and 1 lines and maxima of 10 and 3 for M$_A$ and M$_B$.
+M$_A$'s body is longer in 9 of 38 pairs. E14 therefore shows that the preference persists with identical
+surrounding code, not that it is independent of how each rule is written. It cannot separate a convention
+from a plain reading of the task.
 
 \begin{figure}[h]
 \centering
 \includegraphics[width=\textwidth]{fig_controls.pdf}
 \caption{Held-out estimates across the randomised-contract studies (points; 95\% problem-level bootstrap intervals).
 (a) Flag rate of the program that departs from the benchmark's behaviour minus that of the program that follows it,
-task alone: E6, and E13 and E14 in fresh interleaved readings, with B given a behaviour-preserving branch (E13) or both
-programs sharing all code outside one branch body (E14; open marker: missing units at the worst value, the statistic
-the verdict uses). (b) Verified diagnosis, the sentence against the task alone and against the pointer (E6, E10) and
-on the edited BigCodeBench units (E11).}
+with the task alone. E6 is shown alongside fresh interleaved readings from E13 and E14. B has a behaviour-preserving
+branch (E13), or both programs share all code outside one branch body (E14; open marker: missing units at the worst
+value, the statistic the verdict uses). (b) Verified diagnosis: the sentence against the task alone and against the
+pointer (E6, E10), and on the edited BigCodeBench units (E11).}
 \label{fig:controls}
 \end{figure}
 
@@ -355,13 +361,14 @@
 \section{The data study's voided runs}
 \label{app:e3}
 
-\paragraph{Design.} Twelve public regression tables were each delivered with a data card and either left clean or
-given one injected fault (mixed units, negated values, duplicated rows, a shuffled target, swapped columns, sentinel
-values, rounding); four tables were used for development (84 faulty and 84 clean items) and eight held out (266 and
-266). A profile validator built from the card and from thresholds against a clean reference sample was combined with
-a model auditor (GPT-5.6-terra or Claude Sonnet 5.5, with a shell on the full table or reading 120 rows). Localisation
-counts only when a blocking finding names the injected fault type and column, scored by code against the injection
-manifest. This study (E3) differs from the earlier four-table study in Appendix~\ref{app:earlier}.
+\paragraph{Design.} Each of twelve public regression tables came with a data card. We either left the table
+clean or injected one fault (mixed units, negated values, duplicated rows, a shuffled target, swapped columns,
+sentinel values, rounding). We used four tables for development (84 faulty and 84 clean items) and held out
+eight (266 and 266). We combined a profile validator built from the card and from thresholds against a clean
+reference sample with a model auditor. The auditor was GPT-5.6-terra or Claude Sonnet 5.5, with a shell on the
+full table or reading 120 rows. Localisation counts only when a blocking finding names the injected fault type
+and column. Code scores the finding against the injection manifest. This study (E3) differs from the earlier
+four-table study in Appendix~\ref{app:earlier}.
 
 \paragraph{Voided runs.} The data study (Section~\ref{sec:transfer}) was registered with its hypotheses, validators
 and scoring before any reading. Its first agentic runs used a command filter that discarded readings in which the auditor tried to reach the
```

No specific sentence flagged as factually incorrect.