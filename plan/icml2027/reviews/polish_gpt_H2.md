```diff
--- tex/sections/introduction_v2.tex
+++ tex/sections/introduction_v2.tex
@@ -2,52 +2,52 @@
 \section{Introduction}
 \label{sec:intro}
 
-MBPP+ problem 102 \citep{liu2023evalplus} asks for a function that converts a snake-case string to camel case, and
-shows three ordinary examples. A generated function splits on underscores and capitalises each word, and it passes
+MBPP+ problem 102 \citep{liu2023evalplus} asks for a function that converts a snake-case string to camel case and
+gives three ordinary examples. A generated function splits on underscores, capitalises each word and passes
 all three. The hidden suite then passes \verb|___python_program| and expects \verb|___PythonProgram|; the function
-returns \verb|PythonProgram|. Nothing in the task says what leading underscores should become. On a benchmark this
-program is defective, and an automated auditor that reads it and passes it has missed a defect.
+returns \verb|PythonProgram|. The task says nothing about how to handle leading underscores. The benchmark treats
+this program as defective, so an automated auditor that reads and passes it has missed a defect.
 
-Models increasingly check what other models write, and audit benchmarks score them the way this example is scored:
-against a hidden reference. We argue that such scores mix two things that should be kept apart. On some cases the
-evidence the auditor sees determines the correct behaviour, and a miss is a failure of the auditor. On others, like
-the one above, the evidence is equally consistent with the program and with the reference, and no auditor of any
-capacity can tell them apart without being told which behaviour is wanted. On those cases a ``detection'' is
-agreement with the benchmark's convention, and it would be a false accusation had the convention gone the other way.
+Models increasingly check what other models write. Audit benchmarks score them as in this example, against a hidden
+reference. We argue that these scores conflate two kinds of case. In some, the evidence available to the auditor
+determines the correct behaviour, and a miss is the auditor's failure. In others, such as the example above, the
+evidence is equally consistent with the program and the reference. No auditor, whatever its capacity, can tell them
+apart without being told which behaviour is wanted. A ``detection'' in these cases amounts to agreement with the
+benchmark's convention; it would be a false accusation had the convention gone the other way.
 
-The separation is a classical one. For any flagging rule, recall minus false-flag rate is bounded by the total
-variation between the evidence a defective and a correct program produce, and the best attainable recall at a given
-false-flag rate is the Neyman--Pearson power of that evidence (Section~\ref{sec:framework}). What has been missing is a
-way to observe it in audit evaluations, because a benchmark fixes one contract and hides the counterfactual. We
-construct it. Each unit of our experiment (Section~\ref{sec:e6}) takes a real benchmark task with one behaviour the
-task leaves open, builds two programs that differ only there, grades the auditor against a contract drawn
-independently of what it sees, and then reveals the contract in different ways. Programs, oracles and the boundaries
-of the open behaviour are validated by execution; admissibility of both rules is judged by two independent models.
+This distinction is classical. For any flagging rule, recall minus false-flag rate is bounded by the total
+variation between the evidence a defective and a correct program produce. The best attainable recall at a given
+false-flag rate is the Neyman--Pearson power of that evidence (Section~\ref{sec:framework}). Audit evaluations have
+lacked a way to observe this distinction because a benchmark fixes one contract and hides the counterfactual.
+Our experiment constructs that counterfactual (Section~\ref{sec:e6}). For each unit, we take a real benchmark task
+that leaves one behaviour open and build two programs that differ only there. We grade the auditor against a
+contract drawn independently of what it sees, then reveal the contract in different ways. Execution validates the
+programs, oracles and boundaries of the open behaviour; two independent models judge whether both rules are admissible.
 
 \textbf{Findings.} Across \tbd{N} units and two auditor families at two reasoning budgets:
 \begin{itemize}\itemsep1pt
-\item Without the contract, auditors flag the two programs equally often (\tbd{x}\%), as the construction forces,
-  but they diagnose the program that departs from the benchmark's convention more often than the reverse: a
+\item Without the contract, auditors flag the two programs equally often (\tbd{x}\%), as the construction forces.
+  Yet they diagnose the program that departs from the benchmark's convention more often than the reverse: a
   benchmark-convention advantage of \tbd{y} points.
 \item Stating the contract, either as a choice between the two rules or as one ordinary requirement, raises verified
   diagnosis to \tbd{z}\% at a false-flag rate under \tbd{f}\%. A higher reasoning budget changes verified diagnosis by
   no more than \tbd{e} points, before or after the contract is stated.
-\item When told the task leaves the choice open, the two vendors route differently: one passes almost every program,
-  the other asks for clarification.
-\item On positive controls, where the task's words do rule out one program, the same auditors separate the programs
+\item When told that the task leaves the choice open, the two vendors respond differently: one passes almost every
+  program, while the other asks for clarification.
+\item On positive controls, where the task's words rule out one program, the same auditors separate the programs
   without being told (recall minus false-flag rate \tbd{j} points).
 \end{itemize}
-On the natural failures we audited earlier (Section~\ref{sec:natural}), most hidden-test failures are ones the task's
-words do not determine, and the verified diagnoses auditors do produce mostly concern defects the words determine.
+Among the natural failures we audited earlier (Section~\ref{sec:natural}), most hidden-test failures concern behaviour
+that the task's words do not determine. Most verified diagnoses, however, concern defects that the words determine.
 Three earlier preregistered studies of scientific code, results and data (Section~\ref{sec:transfer}) fall on either
-side of the same line: telling the auditor what the deliverable is nearly halves its false flags on correct
-scientific code, recomputation catches consistently fabricated results because code and inputs determine them, and
-on data a validator written from the documentation finds most of what a model auditor finds.
+side of the same distinction. Telling the auditor what the deliverable is nearly halves its false flags on correct
+scientific code. Recomputation catches consistently fabricated results because code and inputs determine them.
+For data, a validator written from the documentation finds most of what a model auditor finds.
 
 \textbf{Contributions.} (i) A randomised-contract design that makes the information limit of an audit observable and
 separates convention agreement, unjustified accusation, requests for clarification and verified diagnosis, with
-execution-validated programs and oracles. (ii) Evidence, preregistered, that on such cases clarification moves audit
+execution-validated programs and oracles. (ii) Preregistered evidence that, on such cases, clarification moves audit
 performance from the convention baseline to near the ceiling while additional computation does not. (iii) A bridge to
-natural audits showing how hidden-test recall decomposes into determined and undetermined failures, and a reading of
-scientific code, results and data audits through the same distinction between capacity and information misses.
+natural audits showing how hidden-test recall decomposes into determined and undetermined failures, and an
+interpretation of scientific code, results and data audits using the same distinction between capacity and information misses.
 Code, records and preregistrations are released.
```

```diff
--- tex/sections/e6.tex
+++ tex/sections/e6.tex
@@ -2,97 +2,98 @@
 \section{A randomised-contract audit experiment}
 \label{sec:e6}
 
-Section~\ref{sec:framework} says that a miss on an indistinguishable case cannot be repaired by computation, but
-on a natural benchmark we never observe the counterfactual contract. This section builds it. Each unit is a real
-benchmark task with one behaviour the task leaves open; we write two programs that differ only there, draw the
-contract the auditor is graded against independently of what it sees, and then reveal the contract, or not.
+Section~\ref{sec:framework} states that computation cannot repair a miss on an indistinguishable case.
+In a natural benchmark, we never observe the counterfactual contract. We construct it for each experimental unit:
+a real benchmark task that leaves one behaviour open. We write two programs that differ only in that behaviour
+and draw the contract used to grade the auditor independently of what it sees. We then either reveal or withhold the contract.
 
 \subsection{Construction}
 \label{sec:e6-construction}
 \input{fig_design}
 
 \paragraph{Contracts first.} For each of the 542 HumanEval+ and MBPP+ problems \citep{liu2023evalplus}, a proposer
-model names one kind of valid input on which the task text and the visible tests leave the behaviour open, and states
-two rules for it as requirements a task author could add: \emph{B}, the behaviour the benchmark reference follows,
-and \emph{A}, an alternative of equal specificity (for example, ``if several sublists are equally short, return the
-first'' against ``\dots the last''). Each rule is then implemented from the task and the rule alone, by two vendors
-with the same prompt; no implementation sees the reference. The programs an auditor reads are one vendor's A and B
-implementations, so the two share provenance and style; the vendor alternates across units.
+model identifies one kind of valid input for which the task text and visible tests leave the behaviour open.
+It states two rules as requirements a task author could add: \emph{B}, the benchmark reference's behaviour,
+and \emph{A}, an equally specific alternative (for example, ``if several sublists are equally short, return the
+first'' versus ``\dots the last''). Two vendors then implement each rule from the task and the rule alone,
+using the same prompt; no implementation sees the reference. Auditors read one vendor's A and B implementations,
+which therefore share provenance and style. The vendor alternates across units.
 
 \paragraph{Admission by execution.} An independent model writes a domain predicate \texttt{valid} and 16--24 probe
-inputs; the proposer writes a class predicate \texttt{in\_class}. A unit is admitted only if, on every valid input
-among the hidden suite, the proposer's inputs, the probes, up to 300 seeded stress mutations (unusual whitespace,
-combining marks and other Unicode, complex values equal to integers, negative indices, extreme and cancelling
-floating-point values, empty and duplicated collections) and up to 40 inputs from a red-team model that sees all
-implementations and both predicates and tries to break these conditions, both B implementations agree with the reference; outside
-the class all four implementations agree with the reference; inside it the two A implementations agree; A and B
-differ on at least two valid class inputs; and every implementation passes the visible tests. Each stage is attempted
-once per problem; problems without a first-attempt primary unit received one second, independent attempt, fixed
-before any held-out audit. These checks reject,
-for example, a ``correct'' B program whose integer summation silently became floating point.
+inputs; the proposer writes a class predicate \texttt{in\_class}. The checks cover the hidden suite, the proposer's
+inputs, the probes, up to 300 seeded stress mutations (unusual whitespace, combining marks and other Unicode,
+complex values equal to integers, negative indices, extreme and cancelling floating-point values, empty and
+duplicated collections) and up to 40 inputs from a red-team model. That model sees all implementations and both
+predicates and tries to break the admission conditions. Admission requires both B implementations to agree with
+the reference on every valid input in these sets. Among these valid inputs, all four implementations must agree
+with the reference outside the class; inside it, the two A implementations must agree. A and B must differ on at
+least two valid class inputs, and every implementation must pass the visible tests. Each stage is attempted once
+per problem; problems without a first-attempt primary unit received one second, independent attempt, fixed before
+any held-out audit. These checks reject, for example, a ``correct'' B program whose integer summation silently
+became floating point.
 
-\paragraph{Judging without human raters.} Two models that neither proposed the rules nor audit (Claude Opus,
-GPT-6.1-sol) judge, blind to which rule is the benchmark's, whether the inputs are valid and whether each rule is
-compatible with the task's words and visible tests, with the instruction that a missing example is not permission.
-The primary population is the admitted units on which both judges accept the domain and both rules. We call these
+\paragraph{Judging without human raters.} Two models that neither proposed the rules nor serve as auditors (Claude Opus,
+GPT-6.1-sol) judge whether the inputs are valid and each rule is compatible with the task's words and visible tests.
+They are blind to which rule is the benchmark's and are instructed that a missing example is not permission.
+The primary population comprises admitted units for which both judges accept the domain and both rules. We call these
 \emph{execution-validated, two-model-compatible contract pairs}. They are not human-validated ambiguities, and we make
 no claim about how common such ambiguity is.
 
-\paragraph{Positive controls.} The same pipeline, with a proposer prompt asking for a plausible \emph{misreading}
-that passes the visible tests but that the words rule out, yields units on which the evidence does distinguish the
-programs. Both judges must call the misreading incompatible and the required rule compatible.
+\paragraph{Positive controls.} The same pipeline yields units whose evidence distinguishes the programs by asking
+the proposer for a plausible \emph{misreading} that passes the visible tests but that the task's words rule out.
+Both judges must call the misreading incompatible and the required rule compatible.
 
 \subsection{Arms, auditors and scoring}
 \label{sec:e6-arms}
 
-Each open unit is audited under six arms that append text to the task: nothing (\textsc{none}); both rules as a
-numbered menu with the statement that the task does not say which applies (\textsc{menu}); the same menu plus
+Each open unit is audited under six arms defined by the text appended to the task: nothing (\textsc{none}); both rules
+as a numbered menu stating that the task does not say which applies (\textsc{menu}); the same menu plus
 ``the function must follow rule ($k$)'' (\textsc{resolve}); and one rule stated as an ordinary requirement with no
-menu (\textsc{sentence}). Menu order is fixed per unit and independent of the contract. Auditors are GPT-5.6-terra and
-Claude Sonnet 5.5, each at a low and a high reasoning budget, with the shipped rulebook and two readings per cell
+menu (\textsc{sentence}). Menu order is fixed per unit and independent of the contract. GPT-5.6-terra and
+Claude Sonnet 5.5 each audit at a low and a high reasoning budget, using the shipped rulebook and two readings per cell
 (\tbd{N} readings in all).
 
-Under contract $X$, program $X$ is correct and the other is defective. In \textsc{none} and \textsc{menu} the evidence
-does not depend on the contract, so the same readings are scored under both contracts (Lemma~\ref{lem:symmetric}
-then forces flag recall to equal the false-flag rate; we report it as a check). A cell flags if either reading
-reports a blocking finding. A diagnosis is \emph{verified} only if a flagging reading supplies a witness call that
-satisfies \texttt{valid}, lies in the class, and on which the program and the contract's oracle disagree under the
-benchmark's own comparator (the reference for B, the other vendor's implementation for A), and both judges confirm
-that the witness exercises the disagreement. A unit's value is the mean over configurations; intervals are
-problem-level bootstraps, and the false-flag budget after resolution (10\%) is tested separately with a betting
-confidence bound \citep{waudbysmith2024betting}, which does not gate the other claims.
+Under contract $X$, program $X$ is correct and the other is defective. In \textsc{none} and \textsc{menu}, the evidence
+does not depend on the contract, so we score the same readings under both contracts. Lemma~\ref{lem:symmetric}
+then forces flag recall to equal the false-flag rate; we report this equality as a check. A cell flags if either
+reading reports a blocking finding. A diagnosis is \emph{verified} only if a flagging reading supplies a witness call
+that satisfies \texttt{valid} and lies in the class. On that call, the program and the contract's oracle
+(the reference for B, the other vendor's implementation for A) must disagree under the benchmark's own comparator,
+and both judges must confirm that the witness exercises the disagreement. A unit's value is the mean over
+configurations; intervals are problem-level bootstraps. We test the false-flag budget after resolution (10\%)
+separately with a betting confidence bound \citep{waudbysmith2024betting}, which does not gate the other claims.
 
 \subsection{Results}
 \label{sec:e6-results}
 
-The held-out population has \tbd{40} units from \tbd{40} problems (\tbd{32} from the first construction attempt and
-\tbd{8} from the second) and \tbd{3{,}200} readings; the positive-control population has \tbd{54} units. All
-hypotheses, intervals and the order in which claims are tested were registered before the first held-out call.
+The held-out population contains \tbd{40} units from \tbd{40} problems (\tbd{32} from the first construction attempt
+and \tbd{8} from the second) and \tbd{3{,}200} readings; the positive-control population contains \tbd{54} units.
+All hypotheses, intervals and the order in which claims are tested were registered before the first held-out call.
 
-\paragraph{Without the contract, auditors side with the convention.} In the \textsc{none} arm the two flag rates are
-equal by construction (\tbd{x}\% each), so flagging carries no information about which program is wrong. The
-diagnoses are not symmetric: a verified diagnosis is \tbd{y} points [\tbd{lo}, \tbd{hi}] more likely when the
-contract is the benchmark's own rule than when it is the alternative (E6-2). An auditor that ``detects'' the program
-departing from the reference is, on these units, reporting the convention it expects.
+\paragraph{Without the contract, auditors side with the convention.} In the \textsc{none} arm, the two flag rates
+are equal by construction (\tbd{x}\% each), so flagging carries no information about which program is wrong.
+Verified diagnoses are asymmetric: they are \tbd{y} points [\tbd{lo}, \tbd{hi}] more likely when the contract is
+the benchmark's own rule than when it is the alternative (E6-2). On these units, an auditor that ``detects'' the
+program departing from the reference reports the convention it expects.
 
 \paragraph{Stating the contract moves the ceiling.} Resolving the menu raises verified diagnosis from \tbd{c0}\%
-to \tbd{c1}\% (E6-1: +\tbd{d} [\tbd{lo}, \tbd{hi}]), and one ordinary sentence without a menu does nearly as well
-(E6-5: +\tbd{d5} over \textsc{none}). After resolution the flag rate on correct programs is \tbd{f}\%; its betting
+to \tbd{c1}\% (E6-1: +\tbd{d} [\tbd{lo}, \tbd{hi}]). One ordinary sentence without a menu does nearly as well
+(E6-5: +\tbd{d5} over \textsc{none}). After resolution, the flag rate on correct programs is \tbd{f}\%; its betting
 upper bound is \tbd{u}\% against the registered 10\% budget (E6-1b, \tbd{met / not met}).
 
-\paragraph{More reasoning does not.} After resolution the high reasoning budget changes verified diagnosis by
+\paragraph{More reasoning does not.} After resolution, the high reasoning budget changes verified diagnosis by
 \tbd{e} points (bootstrap [\tbd{lo}, \tbd{hi}]; betting [\tbd{lo}, \tbd{hi}]). The registered equivalence claim
-(margin 10) is \tbd{inconclusive}: at this sample size the betting interval is wider than the margin. Before
-resolution the budget changes neither the flag rates nor the diagnoses by more than \tbd{e0} points.
+(margin 10) is \tbd{inconclusive}: at this sample size, the betting interval is wider than the margin. Before
+resolution, the budget changes neither the flag rates nor the diagnoses by more than \tbd{e0} points.
 
-\paragraph{The vendors differ in what they do with an open question.} Told that the task leaves the choice open,
+\paragraph{The vendors respond differently to an open question.} When told that the task leaves the choice open,
 GPT passes \tbd{p}\% of readings and Claude asks for clarification in \tbd{q}\% (Figure~\ref{fig:e6}c). Neither
-flags. Both behaviours are defensible; only one is visible to a benchmark that scores flag or pass.
+flags. Both behaviours are defensible, but only one is visible to a benchmark that scores flag or pass.
 
-\paragraph{Positive controls.} Where the task's words do rule one program out, the same auditors separate the two
+\paragraph{Positive controls.} Where the task's words rule out one program, the same auditors separate the two
 programs without any added text: flag recall minus false-flag rate is \tbd{j} points [\tbd{lo}, \tbd{hi}] (E6-4).
-The flat \textsc{none} arm of the open units is therefore not an auditor that cannot read; it is evidence that does
-not decide.
+The flat \textsc{none} arm of the open units therefore reflects evidence that does not decide, rather than an
+auditor that cannot read.
 
 \begin{figure*}[t]
 \centering
```

```diff
--- tex/sections/natural.tex
+++ tex/sections/natural.tex
@@ -2,34 +2,34 @@
 \section{What natural audit failures are made of}
 \label{sec:natural}
 
-The randomised experiment isolates the information limit on constructed units. Here we ask how much of an ordinary
-audit benchmark sits behind that limit. We use 150 programs written by two generator models for HumanEval+ and MBPP+
-problems that pass their visible tests and fail the hidden suite, each paired with a test-passing control
+The randomised experiment isolates the information limit on constructed units. We ask how much of an ordinary audit
+benchmark is subject to that limit. We use 150 programs written by two generator models for HumanEval+ and MBPP+
+problems. Each program passes its visible tests but fails the hidden suite and is paired with a test-passing control
 \citep{liu2023evalplus}.
 
-\paragraph{Most hidden-test failures are not determined by the task.} Two models, blind to which output is the
-benchmark's (order randomised by evidence), classify each program's first failing input: the input is outside the
-task's domain, only the reference's output is acceptable (\textsc{determined}), both are (\textsc{open}), only the
-program's is (\textsc{at odds}), or neither. Identical evidence is pooled so that it cannot receive two labels. Of the
-150 failures, 34 are \textsc{determined}, 26 \textsc{open}, 37 \textsc{at odds}, 21 out of domain and 32 disputed
-(Cohen's $\kappa=0.78$ on the 43 development items). On roughly three failures in four, then, the task's words do not
-single out the value the hidden suite expects.
+\paragraph{Most hidden-test failures are not determined by the task.} Two models classify each program's first failing
+input, blind to which output is the benchmark's (order randomised by evidence). The categories are: the input is
+outside the task's domain, only the reference's output is acceptable (\textsc{determined}), both are
+(\textsc{open}), only the program's is (\textsc{at odds}), or neither. Identical evidence is pooled so that it cannot
+receive two labels. Of the 150 failures, 34 are \textsc{determined}, 26 \textsc{open}, 37 \textsc{at odds},
+21 out of domain and 32 disputed (Cohen's $\kappa=0.78$ on the 43 development items). For roughly three failures
+in four, the task's words do not single out the value expected by the hidden suite.
 
 \paragraph{Independent programmers mostly side with the ``defective'' program.} A behavioural check avoids model
-judgement altogether. For each failure we run the twelve solutions that two generators wrote from the task alone and
-that pass the visible tests on the same first failing input. They return the defective program's result 1{,}080 times
-and the reference's result 559 times (71 neither). On the inputs that define these programs as defective, most
-readers of the task do what the defective program does; the benchmark's expected value is the minority reading.
+judgement altogether. For each failure, we take the twelve solutions written by two generators from the task alone
+that pass the visible tests and run them on the same first failing input. They return the defective program's result
+1{,}080 times and the reference's result 559 times (71 neither). On the inputs that define these programs as defective,
+most readers of the task do what the defective program does; the benchmark's expected value is the minority reading.
 
-\paragraph{Auditors find what the words determine.} On the original task text, four readings per program and two
+\paragraph{Auditors find what the words determine.} With the original task text, four readings per program and two
 auditors, verified diagnosis is \tbd{a}\% on \textsc{determined} failures and \tbd{b}\% on \textsc{open} ones
-(preregistered H6: \tbd{difference}). When an auditor does produce a verified diagnosis, its witness usually targets a
-behaviour the words determine: of the \tbd{n} programs with a verified diagnosis, \tbd{m} have at least one witness
+(preregistered H6: \tbd{difference}). When an auditor produces a verified diagnosis, its witness usually targets a
+behaviour the words determine. Of the \tbd{n} programs with a verified diagnosis, \tbd{m} have at least one witness
 that the classifiers label \textsc{determined}; the rest are not established as contract-independent (development
 pilot: 5 of 6). Hidden-test recall on such a benchmark is therefore bounded by its share of determined failures, and
 the misses concentrate where Section~\ref{sec:framework} says no auditor can do better without being told more.
 
 \paragraph{Clarifying the missing requirement.} For the 13 failures that remain \textsc{open} after reclassification
 and whose added sentences pass a neutrality recheck, we appended the missing requirement as one sentence, a
-length-matched placebo, or a pointer that names the input class without resolving it. On the \tbd{9} test items
-(\tbd{7} problems) this is a small replication of Section~\ref{sec:e6}: \tbd{H1, H5}.
+length-matched placebo, or a pointer naming the input class without resolving it. The \tbd{9} test items
+(\tbd{7} problems) provide a small replication of Section~\ref{sec:e6}: \tbd{H1, H5}.
```

Suspected factual or logical problems, left unresolved:

- **`introduction_v2.tex`, “auditors flag the two programs equally often … as the construction forces”:** scoring identical readings under both contracts forces aggregate recall to equal the false-flag rate; it does not necessarily force equal flagging frequencies for the A and B programs.
- **`e6.tex`, auditors “each at a low and a high reasoning budget”:** this appears to cover every arm, whereas the unchanged caption specifies “sentence: low budget only”.
- **`introduction_v2.tex`, contribution (ii), “while additional computation does not”:** the unqualified conclusion appears stronger than the inconclusive equivalence result reported in `e6.tex`.
- **`natural.tex`, “roughly three failures in four”:** this apparently counts the 32 disputed cases as established cases in which the task does not determine the expected value. Disagreement between judges does not establish that conclusion.
- **`natural.tex`, “They return … 1{,}080 times … 559 times (71 neither)”:** these counts total 1,710, whereas twelve solutions for each of 150 failures implies 1,800 evaluations. The missing 90 are unexplained.
- **`natural.tex`, “Hidden-test recall … is therefore bounded by its share of determined failures”:** this bound does not follow without further assumptions about false flags and convention-based detections. Classifying only the first failing input also does not exclude determined defects elsewhere in the same program.

