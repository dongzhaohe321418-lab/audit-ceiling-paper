```diff
--- a/tex/paper_v3.tex
+++ b/tex/paper_v3.tex
@@ -36,5 +36,5 @@
 
 \twocolumn[
-\icmltitle{What Moves the Ceiling on Automated Code Audit:\\
+\icmltitle{What Limits Automated Code Audit?\\
            Separating Convention Agreement from Defect Detection}
 
@@ -54,18 +54,18 @@
 
 \begin{abstract}
-Audit benchmarks grade automated code auditors against a hidden reference. Where the task leaves a behaviour open,
-the evidence an auditor sees can be equally consistent with the program and the reference, and recall minus
-false-flag rate is then bounded by how well that evidence separates the two; a benchmark that fixes one contract
-cannot show how much of a score this explains. We introduce a randomised-contract evaluation: execution-checked
-pairs of programs, built from HumanEval+ and MBPP+ tasks, that differ only on a behaviour the task leaves open,
-graded against a contract drawn at random and revealed in different ways. With the contract withheld on 41
-held-out units, auditors from two vendors flag the program that departs from the benchmark's behaviour
-\NSixFlagPref{} points more often than the one that follows it (exploratory; registered convention advantage
-\NSixTwo), and 28.9 points more often among 38 of 41 units in a preregistered control where the two programs share
-all code outside one branch body. The models' own task-only solutions follow the benchmark's behaviour 89\% of the
-time, so on these units the benchmark rewards agreement with a convention the models share. One sentence stating the
-missing requirement adds \NSixFive{} points to verified diagnosis, and 58.3 on 18 reference-edited BigCodeBench
-data-science tasks. In only 34 of 150 natural hidden-test failures do two model classifiers agree that the task's
-words single out the expected value. Confirmatory analyses were preregistered; deviations are disclosed.
+Audit benchmarks grade automated code auditors against a hidden reference. When a task leaves a behaviour open,
+the evidence an auditor sees can fit the program and the reference equally well. Recall minus false-flag rate
+is then bounded by how well that evidence separates them. A benchmark with one fixed contract cannot show how
+much of its score this explains. We introduce a randomised-contract evaluation using execution-checked program
+pairs built from HumanEval+ and MBPP+ tasks. The programs differ only on a behaviour the task leaves open and are graded
+against a randomly drawn contract revealed in different ways. With the contract withheld on 41 held-out units,
+auditors from two vendors flag the program that departs from the benchmark's behaviour \NSixFlagPref{} points
+more often than the one that follows it (exploratory; registered convention advantage \NSixTwo).
+The difference is 28.9 points among 38 of 41 units in a preregistered control with all code shared outside one branch body.
+The models' task-only solutions follow the benchmark's behaviour 89\% of the time; on these units, the benchmark
+therefore rewards agreement with a convention the models share. One sentence stating the missing requirement
+adds \NSixFive{} points to verified diagnosis, and 58.3 on 18 reference-edited BigCodeBench data-science tasks.
+In only 34 of 150 natural hidden-test failures do two model classifiers agree that the task's words single out the
+expected value. Confirmatory analyses were preregistered; we disclose deviations.
 \end{abstract}
 
--- a/tex/sections/introduction_v2.tex
+++ b/tex/sections/introduction_v2.tex
@@ -9,11 +9,11 @@
 this program as defective. By that measure, an automated auditor that reads and passes it has missed a defect.
 
-Models increasingly check what other models write. Audit benchmarks score them as in this example, against a hidden
-reference. We argue that these scores conflate two kinds of case. In some, the evidence available to the auditor
-determines the correct behaviour, and a miss is the auditor's failure. In others, such as the example above, the
-evidence is equally consistent with the program and the reference; where the evidence is moreover identically
-distributed under both behaviours, as our construction guarantees, no auditor, whatever its capacity, can tell which
-of the two is wanted without being told. A ``detection'' in these cases amounts to agreement with the
-benchmark's convention; it would be a false accusation had the convention gone the other way.
+Models increasingly check what other models write. Benchmarks score these audits against a hidden reference,
+as in the example above. We argue that these scores conflate two kinds of case. In some, the evidence available
+to the auditor determines the correct behaviour, so a miss is the auditor's failure. In others, including the
+example above, the evidence fits the program and the reference equally well. If it also has the same distribution
+under both behaviours, as our construction guarantees, no auditor, however capable, can tell which is wanted
+without being told. A ``detection'' in these cases amounts to agreement with the benchmark's convention;
+had the convention gone the other way, it would be a false accusation.
 
 This distinction is classical. For any flagging rule, recall minus false-flag rate is bounded by the total
@@ -28,19 +28,20 @@
 \textbf{Findings.} Across \NSixUnits{} held-out units and auditors from two vendors at two reasoning budgets:
 \begin{itemize}\itemsep1pt
-\item With the contract withheld, flagging cannot track which program is wrong: the same readings are scored under
-  both contracts, so recall equals the false-flag rate (\NSixNoneFlag\%) by construction. The informative difference
-  is which program is flagged. The one that departs from the benchmark's behaviour is flagged \NSixFlagPref{} points
-  [\NSixFlagPrefLo, \NSixFlagPrefHi] more often than the one that follows it (exploratory), and diagnosed more often too (the registered convention advantage, half
-  the difference between the two diagnosis rates, is \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi]).
-\item The models' own solutions written from the task alone follow the benchmark's behaviour on these units 89\%
-  of the time. The models share the benchmark's convention; flagging departures becomes a false accusation when
-  the other rule is intended.
-\item One ordinary sentence stating the missing requirement raises verified diagnosis (a flag whose executed
+\item With the contract withheld, flags cannot track which program is wrong: we score the same readings under
+  both contracts, so recall equals the false-flag rate (\NSixNoneFlag\%) by construction. What differs is which
+  program auditors flag. They flag the program that departs from the benchmark's behaviour \NSixFlagPref{} points
+  [\NSixFlagPrefLo, \NSixFlagPrefHi] more often than the one that follows it (exploratory), and diagnose it more often too.
+  The registered convention advantage, half the difference between the two diagnosis rates, is
+  \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi].
+\item From the task alone, the models write solutions that follow the benchmark's behaviour on these units 89\%
+  of the time. They share the benchmark's convention; when the other rule is intended, flagging departures
+  becomes a false accusation.
+\item Stating the missing requirement in one ordinary sentence raises verified diagnosis (a flag whose executed
   witness shows the program breaking the contract) by \NSixFive{} points
   [\NSixFiveLo, \NSixFiveHi] over the task alone. No correct program was flagged in that arm (\NSixResolveFpr\% when the contract is
-  stated as a choice between the two rules). On 18 BigCodeBench data-science tasks with edited references, the
+  stated as a choice between the two rules). On 18 reference-edited BigCodeBench data-science tasks, the
   sentence adds 58.3 points [41.7, 73.6] (Section~\ref{sec:transfer}).
 \item Told only that the choice is open, one vendor passes almost every program; the other asks for clarification.
-\item On positive controls, where the task's words rule out one program, the same auditors separate the programs
+\item On positive controls, the task's words rule out one program. The same auditors separate the programs
   without being told (recall minus false-flag rate \NSixFourJ{} points).
 \end{itemize}
--- a/tex/fig_design.tex
+++ b/tex/fig_design.tex
@@ -33,8 +33,8 @@
   node[midway, below=2pt, font=\tiny, align=center] {$H$ revealed:\\ separable};
 \end{tikzpicture}
-\caption{Randomised-contract evaluation (an illustrative unit). Either program can be correct, depending on the
-contract, which is drawn at random and then withheld or stated. Withheld, recall equals the false-flag rate by design;
-which program is flagged, and what stating the contract adds, are empirical. A diagnosis counts only with a witness
-on which program and oracle disagree under the benchmark's comparator.}
+\caption{Randomised-contract evaluation (illustrative unit). We draw the contract at random, then withhold or
+state it; either program can be correct. With the contract withheld, recall equals the false-flag rate by design.
+Which program auditors flag and what stating the contract adds are empirical questions. A diagnosis requires a
+witness on which program and oracle disagree under the benchmark's comparator.}
 \label{fig:design}
 \end{figure}
--- a/tex/sections/e6.tex
+++ b/tex/sections/e6.tex
@@ -99,8 +99,8 @@
 more likely when the contract is the benchmark's rule: the registered convention advantage, half the difference
 between the two diagnosis rates, is \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi] (E6-2). We cannot say whether this
-reflects memory of the benchmark or the most natural reading of the task. The preference is larger where A has more
-conditionals than B, but it survives two preregistered controls (Appendix~\ref{app:e6}): a behaviour-preserving
-branch added to B changed its flag rate by +0.6 points [$-$1.2, 2.5] (E13), and with both programs rewritten to share
-all code outside one branch body, A's version was still flagged 28.9 [14.5, 42.8] points more often among 38 of 41 units (E14).
+reflects memory of the benchmark or the most natural reading of the task. The preference is larger when A has more
+conditionals than B, but persists in two preregistered controls (Appendix~\ref{app:e6}). Adding a behaviour-preserving
+branch to B changed its flag rate by +0.6 points [$-$1.2, 2.5] (E13). With both programs rewritten to share
+all code outside one branch body, auditors flagged A's version 28.9 [14.5, 42.8] points more often among 38 of 41 units (E14).
 The models' own solutions written from the task alone follow the benchmark's rule on these units 89\% of the time
 (Appendix~\ref{app:e6}). A hidden-test ``detection'' here therefore credits agreement with a shared convention, and
```

Potentially overbroad sentence, unchanged and outside the requested edits (`tex/sections/e6.tex`):

> All hypotheses, intervals and the order in which claims are tested were registered before the first held-out call.

The appendix places E13/E14 registration after earlier held-out analyses. This statement needs checking unless its scope is exclusively the original E6 tests.