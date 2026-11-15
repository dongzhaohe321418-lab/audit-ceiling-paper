No files changed. Every replacement is shorter in source. In-memory paragraph typesetting with the current style saves **five lines overall**, with no passage growing.

```diff
--- a/tex/sections/transfer.tex
+++ b/tex/sections/transfer.tex
@@ -9,19 +9,18 @@
 distinction rather than test it.
 
-\paragraph{Randomised contracts on data-science code.} A first attempt to carry the experiment of
-Section~\ref{sec:e6} to 121 deterministic BigCodeBench tasks that use pandas, numpy, scipy or scikit-learn (E7)
-stopped at construction: programs written from scratch kept disagreeing with the reference elsewhere, and only 5
-held-out units survived a registered gate of 12. A second preregistered study (E11)
-changed only construction: each implementing vendor edited the reference to follow one rule in an explicit branch
-(median 3.5 changed lines). It yielded 18 held-out units from 18
-problems; all 576 registered readings were valid (Appendix~\ref{app:e6}). Stating the requirement in one
-sentence increased verified diagnosis by 58.3 points [41.7, 73.6] over the task alone (66.7\% versus 8.3\%) and by
-48.6 [34.7, 62.5] over a note naming the input class; the note added 9.7 [2.8, 16.7]. Both registered hypotheses
-hold. No problem has a negative effect, and omitting any one problem leaves both lower limits above 30. Without the
-contract, the convention advantage was 8.3 [2.8, 13.9] (not registered here). Unlike on HumanEval+ and MBPP+, the
-sentence arm had a 26.4\% false-flag rate. Judges outside the construction accepted both
-rules on 93\% of readings. The edited branches cue the
-relevant behaviour in every arm: the sentence effect extends to these constructed library tasks, and its
-applicability to ordinary library code remains untested.
+\paragraph{Randomised contracts on data-science code.} We first tried extending the experiment in
+Section~\ref{sec:e6} to 121 deterministic BigCodeBench tasks using pandas, numpy, scipy or scikit-learn (E7).
+Construction stopped: programs written from scratch kept disagreeing with the reference elsewhere; only 5
+held-out units survived a registered gate of 12. A second preregistered study (E11) changed only construction:
+each implementing vendor edited the reference to follow one rule in an explicit branch (median 3.5 changed lines).
+It yielded 18 held-out units from 18 problems; all 576 registered readings were valid (Appendix~\ref{app:e6}).
+One sentence stating the requirement raised verified diagnosis by 58.3 points [41.7, 73.6] over the task alone
+(66.7\% versus 8.3\%) and by 48.6 [34.7, 62.5] over a note naming the input class.
+The note added 9.7 [2.8, 16.7]. Both registered hypotheses hold. No problem's effect is negative;
+omitting any one keeps both lower limits above 30. Without the contract, the convention advantage was
+8.3 [2.8, 13.9] (not registered here). Unlike on HumanEval+ and MBPP+, the sentence arm had a 26.4\% false-flag rate.
+Judges outside the construction accepted both rules on 93\% of readings. The edited branches cue the relevant
+behaviour in every arm. The sentence effect extends to these constructed library tasks;
+transfer to ordinary library code remains untested.
 
 \paragraph{Code: what the auditor is told it is reviewing.} SciCode \citep{tian2024scicode} splits research problems
```

```diff
--- a/tex/sections/e6.tex
+++ b/tex/sections/e6.tex
@@ -44,7 +44,7 @@
 The primary population comprises admitted units for which both judges accept the domain and both rules:
 \emph{execution-validated, two-model-compatible contract pairs}. These are not human-validated ambiguities, and we make
-no claim about how common such ambiguity is. In a later preregistered check (E9, Appendix~\ref{app:e6}), two judges outside the
-construction, blind to which rule is the benchmark's, accepted both rules on 84\% of readings of these units yet
-excluded the misreading on 96\% of control readings, and E6-1, E6-2 and E6-5 hold on the 35 units most of them accept.
+no claim about how common such ambiguity is. A later preregistered check (E9, Appendix~\ref{app:e6}) used two judges outside the
+construction, blind to which rule is the benchmark's. They accepted both rules on 84\% of readings of these units
+and excluded the misreading on 96\% of control readings. E6-1, E6-2 and E6-5 hold on 35 units most of them accept.
 
 \paragraph{Positive controls.} To obtain units whose evidence distinguishes the programs, the same pipeline asks
@@ -86,7 +86,7 @@
 rules followed by a choice does about as well: \NSixResolveCov\%, against \NSixMenuCov\% with the undecided menu (E6-1:
 +\NSixOne{} [\NSixOneLo, \NSixOneHi]). The undecided menu itself suppresses flagging, so E6-5 measures what a stated
-requirement adds to the plain task. A later preregistered attention control (E10, Appendix~\ref{app:e6}) appends only a note naming the input class:
-it raises verified diagnosis by 18.9 points [12.2, 26.2] over the task alone, and flags on correct programs from 14\%
-to 38\%, while the sentence adds a further 60.4 points [51.8, 68.9]. The sentence improves diagnosis substantially beyond this pointer. Once the contract is
+requirement adds to the plain task. A later preregistered attention control (E10, Appendix~\ref{app:e6}) adds only a note naming the input class.
+It raises verified diagnosis by 18.9 points [12.2, 26.2] over the task alone and flags on correct programs
+from 14\% to 38\%. The sentence adds a further 60.4 points [51.8, 68.9], a substantial improvement beyond this pointer. Once the contract is
 stated, the flag rate on correct programs is \NSixResolveFpr\%, with a betting upper bound of \NSixResolveFprUp\%
 against the registered 10\% budget (E6-1b, \NSixOneBVerdict).
```

```diff
--- a/tex/sections/discussion_v3.tex
+++ b/tex/sections/discussion_v3.tex
@@ -22,22 +22,24 @@
 
 \paragraph{Limitations.}\label{sec:limits} \emph{Constructed units.} The randomised-contract units are execution-validated;
-two models, rather than people, judge them admissible. The same two models implement the rules, so construction
-and judging are not independent; judges outside the construction agree (E9), but they too are models of the same vendors. We make no claim about how often such ambiguity occurs. The 41 held-out units are
-selected (from 406 problems) and concentrated: 37 come from MBPP+. The models' task-only solutions
-follow both rules on only two units.
-\emph{Benchmarks.} The natural failures and 41 of the 59 randomised-contract units come from HumanEval+ and MBPP+;
-the 18 BigCodeBench units are edits of the reference (Section~\ref{sec:transfer}). Whether the convention advantage
-carries over to unedited library code, where more behaviour is unstated, remains untested. \emph{Auditors.} We tested two vendors' models at two reasoning budgets with one rulebook.
+two models, rather than people, judge them admissible. Both models also implement the rules, so construction and
+judging are not independent. Model judges outside construction agree (E9) but share the same vendors.
+We make no claim about the frequency of such ambiguity. The 41 held-out units, selected from 406 problems,
+are concentrated in MBPP+ (37). The models' task-only solutions follow both rules on only two units.
+\emph{Benchmarks.} HumanEval+ and MBPP+ supply the natural failures and 41 of the 59 randomised-contract units;
+the 18 BigCodeBench units are reference edits (Section~\ref{sec:transfer}). The convention advantage remains
+untested on unedited library code, where more behaviour is unstated. \emph{Auditors.} We tested two vendors' models at two reasoning budgets with one rulebook.
 Other auditors, agent scaffolds or execution-based test generation may sit closer to the ceiling before the
-reveal, although Lemma~\ref{lem:symmetric} bounds what any of them can do on the unrevealed arms.
-\emph{Verification.} A verified diagnosis requires a witness whose disagreement with the contract's oracle the
-benchmark's own comparator confirms by execution, with the auditor's stated expected value correct. We do not credit diagnoses stated only in prose. This can understate the performance of auditors whose
-findings are correct but unexecutable. Nor does the frozen scorer credit a witness on which the oracle raises; crediting the two
-units whose rule A requires an exception raises E6-5 from 76.8 to 79.3 and changes no verdict (Appendix~\ref{app:e6}). \emph{Natural failures.} Models classify the natural failures
-(Cohen's $\kappa$ 0.71 on held-out items), and the behavioural check reuses the generators' own solutions.
+reveal, although Lemma~\ref{lem:symmetric} bounds them on the unrevealed arms.
+\emph{Verification.} To verify a diagnosis, execution must confirm a witness's disagreement with the contract's oracle
+using the benchmark's own comparator. The auditor's stated expected value must also be correct.
+We exclude diagnoses stated only in prose, which can understate performance for auditors with correct but
+unexecutable findings. The frozen scorer also gives no credit when the oracle raises. Crediting the two units whose
+rule A requires an exception raises E6-5 from 76.8 to 79.3 and changes no verdict (Appendix~\ref{app:e6}).
+\emph{Natural failures.} Models classify the natural failures (Cohen's $\kappa$ 0.71 on held-out items);
+the behavioural check reuses the generators' own solutions.
 \emph{Data.} The data study injects one fault per item into twelve public tables; its conclusion is specific to
-faults that a clean reference sample reveals. \emph{Discovering requirements.} Our registered arms state the requirement or list both candidates. In a
-registered follow-up (E8, Appendix~\ref{app:e6}), an auditor asked to list unspecified behaviours named the open
-behaviour in 97.6\% of held-out readings but also the decided behaviour of positive controls in 80.8\% (selectivity
-16.8 points [10.5, 23.2], not resolved against the registered 20-point threshold), so the question largely returns
-to the task's author. \emph{Amendments} to infrastructure rules were registered before any held-out analysis (Appendix~\ref{app:e6}).
+faults that a clean reference sample reveals. \emph{Discovering requirements.} Our registered arms state the requirement or list both candidates.
+In a registered follow-up (E8, Appendix~\ref{app:e6}), an auditor asked to list unspecified behaviours named the open
+behaviour in 97.6\% of held-out readings but also the decided behaviour of positive controls in 80.8\%.
+Selectivity was 16.8 points [10.5, 23.2], not resolved against the registered 20-point threshold, so the question
+largely returns to the task's author. \emph{Amendments} to infrastructure rules were registered before any held-out analysis (Appendix~\ref{app:e6}).
```

```diff
--- a/tex/sections/introduction_v2.tex
+++ b/tex/sections/introduction_v2.tex
@@ -36,6 +36,6 @@
   of the time. The convention the benchmark rewards is one the models share, and rewarding it would be a false
   accusation had the task's author meant the other rule.
-\item Adding the missing requirement as one ordinary sentence raises verified diagnosis by \NSixFive{} points
-  [\NSixFiveLo, \NSixFiveHi] over the task alone, with no correct program flagged in that arm (\NSixResolveFpr\% when the contract is
+\item One ordinary sentence stating the missing requirement raises verified diagnosis by \NSixFive{} points
+  [\NSixFiveLo, \NSixFiveHi] over the task alone. No correct program is flagged in that arm (\NSixResolveFpr\% when the contract is
   stated as a choice between the two rules). On 18 BigCodeBench data-science tasks with edited references, the
   sentence adds 58.3 points [41.7, 73.6] (Section~\ref{sec:transfer}).
```

```diff
--- a/tex/paper_v3.tex
+++ b/tex/paper_v3.tex
@@ -54,16 +54,16 @@
 
 \begin{abstract}
-Audit benchmarks grade automated auditors against a hidden reference, yet the evidence an auditor sees is often
-equally consistent with the program and the reference. In such cases recall minus false-flag rate is bounded by
-how well the evidence separates defective from correct programs. The bound is a classical fact about tests, but
-audit evaluations cannot observe it because a benchmark fixes a single contract. To make it observable, we build pairs of programs
-from HumanEval+ and MBPP+ tasks, checked by execution, that differ only on a behaviour the task leaves open.
-We grade auditors from two vendors against a contract drawn at random and vary how that contract is revealed.
-On 41 held-out units with the contract withheld, auditors flag the program that departs from the
-benchmark's behaviour \NSixFlagPref{} points more often than the one that follows it. The models' own solutions written from
-the task alone follow the benchmark's behaviour on 89\% of occasions. The benchmark thus rewards agreement with
-a convention the models share. One sentence stating the missing requirement adds \NSixFive{} points to verified diagnosis, and 58.3 on 18 reference-edited BigCodeBench data-science tasks.
-Of 150 natural hidden-test failures, only 34 are cases where two model classifiers agree that the task's words
-single out the expected value. Three earlier preregistered studies of scientific code, results and data fit the same distinction:
+Audit benchmarks grade automated auditors against a hidden reference, yet auditors' evidence is often equally
+consistent with the program and the reference. Recall minus false-flag rate is then bounded by how well that
+evidence separates defective from correct programs. Audit evaluations cannot observe this classical testing
+bound because a benchmark fixes a single contract. To make it observable, we build execution-checked program
+pairs from HumanEval+ and MBPP+ tasks. The programs in each pair differ only on a behaviour the task leaves open.
+We grade auditors from two vendors against a randomly drawn contract and vary how we reveal it.
+With the contract withheld on 41 held-out units, auditors flag the program that departs from the benchmark's
+behaviour \NSixFlagPref{} points more often than the one that follows it. The models' own task-only solutions
+follow the benchmark's behaviour 89\% of the time. The benchmark thus rewards agreement with a convention the models share.
+One sentence stating the missing requirement adds \NSixFive{} points to verified diagnosis, and 58.3 on 18 reference-edited BigCodeBench data-science tasks.
+Two model classifiers agree that the task's words single out the expected value in only 34 of 150 natural hidden-test failures.
+Three earlier preregistered studies of scientific code, results and data fit the same distinction:
 false flags on correct scientific code halve when the task names the deliverable, and recomputation catches
 fabricated results where code and inputs determine them. Held-out analyses were preregistered; deviations are disclosed.
```

Possible factual or logical issues, left unresolved:

- **E9:** “35 units most of them accept” suggests a majority of judges. The appendix specifies acceptance in at least three of four judge–order readings.
- **Limitations:** “Amendments to infrastructure rules were registered before any held-out analysis” appears accurate for the cited E6 amendments, but could be read across all studies. The data study’s Amendment 3 followed an earlier held-out analysis.