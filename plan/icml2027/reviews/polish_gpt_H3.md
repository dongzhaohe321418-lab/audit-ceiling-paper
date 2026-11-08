Proposed diffs below; files remain unchanged. Protected LaTeX, numbers and intervals were checked against the current files.

```diff
--- tex/sections/framework.tex
+++ tex/sections/framework.tex
@@ -3,7 +3,7 @@
 \label{sec:framework}
 
 \paragraph{Setting.}
-An audit case consists of a program $X$, the evidence $E$ shown to the auditor (the task text, the visible tests,
+An audit case comprises a program $X$, the evidence $E$ shown to the auditor (the task text, the visible tests,
 any added text, and anything the auditor can compute from these, including by executing $X$), and a hidden
 contract $H$ that defines the ground truth. The program is defective, $D=1$, if it violates $H$. An auditor is any
 measurable, possibly randomised, map from $E$ to a flag; we write $\phi(e)=\Pr(\text{flag}\mid E=e)\in[0,1]$.
@@ -38,13 +38,13 @@
 bound on any test's power minus its size; \citealp{neyman1933efficient}). We claim no novelty for them. The
 component bound requires a false-flag constraint on the component itself. Under an overall false-flag rate $\alpha$
 alone, with $q$ the share of correct programs in the component, the bound is only $(1-\pi)+\pi\min(1,\alpha/q)$.
-We use these statements to separate two causes of missed defects that audit evaluations conflate.
-An auditor that operates below the likelihood-ratio ROC of its evidence loses recall to \emph{capacity}: some
+These statements separate two causes of missed defects that audit evaluations conflate.
+An auditor operating below the likelihood-ratio ROC of its evidence loses recall to \emph{capacity}: another
 auditor with the same evidence attains higher recall at the same false-flag rate. Recall lost because the ROC itself
-is low is lost to \emph{information}; in the extreme of an indistinguishable component, any auditor buys recall there
-only with an equal rise in false flags, and no auditor does better without different evidence. Where the two laws
+is low is lost to \emph{information}. In the extreme case of an indistinguishable component, any gain in recall requires
+an equal rise in false flags; no auditor does better without different evidence. Where the two laws
 overlap only partly, even the optimal test misses some defects, so not every miss on a distinguishable case is a
-capacity miss. By definition, only a change in $E$ moves the ceiling; the empirical questions are how far real auditors sit
+capacity miss. By definition, only a change in $E$ moves the ceiling. The empirical questions are how far real auditors fall
 below it and which changes in $E$ matter.
 
 \paragraph{Contract randomisation makes the component observable.}
@@ -68,15 +68,16 @@
 
 Revealing $H$ in the evidence (stating the requirement) breaks the premise of Lemma~\ref{lem:symmetric}; text that
 draws attention to the input class, or lists both behaviours without choosing, does not. The experiment in
-Section~\ref{sec:e6} measures how far real auditors sit below the ceiling once the requirement is revealed, and how
-often, before it is revealed, their detections agree with the benchmark's convention, detections that would be false
-flags had the convention gone the other way. The propositions leave both questions open.
+Section~\ref{sec:e6} measures how far real auditors fall below the ceiling once the requirement is revealed.
+Before the reveal, it measures how often their detections agree with the benchmark's convention.
+Those detections would be false flags had the convention gone the other way. The propositions leave both questions open.
 
 \paragraph{What we do not claim.}
 The ceiling is relative to the evidence, which includes what a model brings with it.
 A model that has memorised a benchmark's reference sees more than the task text. Contract randomisation
 neutralises this on the constructed units because the memorised convention is equally likely to be wrong.
-On natural units we cannot observe the counterfactual contract. Section~\ref{sec:natural} therefore reports
-which failures the task's words determine, as judged by two models and checked against what the generators' own solutions do.
+On natural units we cannot observe the counterfactual contract. Section~\ref{sec:natural} therefore describes
+which failures the task's words determine, using two models' judgements and checking them against the behaviour of
+the generators' own solutions.
 This describes a benchmark; it does not estimate an information-limited share. A task's logical ambiguity is
 not the same as equality of the two evidence laws, and nothing here rules out computation helping on natural programs.
```

```diff
--- tex/sections/e6.tex
+++ tex/sections/e6.tex
@@ -4,8 +4,8 @@
 
 Section~\ref{sec:framework} states that computation cannot repair a miss on an indistinguishable case.
 In a natural benchmark, we never observe the counterfactual contract. We construct it for each experimental unit:
-a real benchmark task that leaves one behaviour open. We write two programs that differ only in that behaviour
-and draw the contract used to grade the auditor independently of what it sees. We then either reveal or withhold the contract.
+a real benchmark task that leaves one behaviour open. We write two programs that differ only in that behaviour.
+We draw the contract used to grade the auditor independently of what it sees, then either reveal or withhold it.
 
 \subsection{Construction}
 \label{sec:e6-construction}
@@ -18,8 +18,8 @@
 first'' versus ``\dots the last''). Appendix~\ref{app:e6} groups the registered units by the kind of
 behaviour left open (ties, readings of a phrase, Unicode conventions, repeated items, numeric types, degenerate
 inputs). Two vendors then implement each rule from the task and the rule alone,
-using the same prompt; no implementation sees the reference. Auditors read one vendor's A and B implementations,
-which therefore share provenance and style. The vendor alternates across units.
+using the same prompt; neither vendor sees the reference when implementing the rules. Auditors read one vendor's
+A and B implementations, which therefore share provenance and style. The vendor alternates across units.
 
 \paragraph{Admission by execution.} An independent model writes a domain predicate \texttt{valid} and 16--24 probe
 inputs; the proposer writes a class predicate \texttt{in\_class}. The checks cover the hidden suite, the proposer's
@@ -33,18 +33,18 @@
 inputs, and every implementation must pass the visible tests. Each construction stage is attempted once per problem
 (the red team may make a second call if the first yields fewer than ten usable inputs); problems without a
 first-attempt primary unit received one second, independent attempt, fixed before any held-out audit. The models
-that judge the rules (Claude Opus, GPT-6.1-sol) also implement them, Claude Opus writes the probes and GPT-6.1-sol the
-red-team inputs, so construction and judging are separate calls, not independent validators. These checks reject, for example, a ``correct'' B program whose integer summation silently
-became floating point.
+that judge the rules (Claude Opus, GPT-6.1-sol) also implement them. Claude Opus writes the probes and GPT-6.1-sol the
+red-team inputs. Construction and judging thus use separate calls, not independent validators.
+These checks reject, for example, a ``correct'' B program whose integer summation silently became floating point.
 
 \paragraph{Judging without human raters.} Two models that neither proposed the rules nor serve as auditors (Claude Opus,
 GPT-6.1-sol) judge whether the inputs are valid and each rule is compatible with the task's words and visible tests.
 They are blind to which rule is the benchmark's and are instructed that a missing example is not permission.
-The primary population comprises admitted units for which both judges accept the domain and both rules. We call these
-\emph{execution-validated, two-model-compatible contract pairs}. They are not human-validated ambiguities, and we make
+The primary population comprises admitted units for which both judges accept the domain and both rules:
+\emph{execution-validated, two-model-compatible contract pairs}. These are not human-validated ambiguities, and we make
 no claim about how common such ambiguity is.
 
-\paragraph{Positive controls.} The same pipeline yields units whose evidence distinguishes the programs by asking
+\paragraph{Positive controls.} To obtain units whose evidence distinguishes the programs, the same pipeline asks
 the proposer for a plausible \emph{misreading} that passes the visible tests but that the task's words rule out.
 Both judges must call the misreading incompatible and the required rule compatible.
 
@@ -67,7 +67,7 @@
 whose arguments have the benchmark's own types, that satisfies \texttt{valid} and lies in the class. On that call
 the two contract oracles must differ, the program must disagree with the contract's oracle (the reference for B, the
 other vendor's implementation for A) under the benchmark's own comparator, and the value the auditor says the call
-should return must equal the oracle's. All of this is checked by execution. A unit's value is the mean over
+should return must equal the oracle's. Execution checks all these conditions. A unit's value is the mean over
 configurations; intervals are problem-level bootstraps. We test the false-flag budget after resolution (10\%)
 separately with a betting confidence bound \citep{waudbysmith2024betting}, which does not gate the other claims.
 
@@ -81,24 +81,24 @@
 \paragraph{Adding the requirement turns agreement into diagnosis.} One ordinary sentence stating the contract
 raises verified diagnosis by \NSixFive{} points [\NSixFiveLo, \NSixFiveHi] over the task alone (E6-5). A menu of both
 rules followed by a choice does about as well: \NSixResolveCov\%, against \NSixMenuCov\% with the undecided menu (E6-1:
-+\NSixOne{} [\NSixOneLo, \NSixOneHi]). Because the undecided menu itself suppresses flagging, E6-5 is the contrast
-that measures what a stated requirement adds to the plain task. The menu doubles as an attention control. It is
-longer than the sentence, names the input class and states both rules, yet it yields almost no verified diagnosis;
-the gain is consistent with knowing which rule holds rather than being pointed at the right place, though the menu
++\NSixOne{} [\NSixOneLo, \NSixOneHi]). The undecided menu itself suppresses flagging, so E6-5 measures what a stated
+requirement adds to the plain task. The menu also serves as an attention control: it is longer than the sentence,
+names the input class and states both rules, yet yields almost no verified diagnosis.
+The gain is consistent with knowing which rule holds rather than being pointed at the right place, though the menu
 is also a strong cue of uncertainty and the arms do not rule out every prompting effect. Once the contract is
 stated, the flag rate on correct programs is \NSixResolveFpr\%, with a betting upper bound of \NSixResolveFprUp\%
 against the registered 10\% budget (E6-1b, \NSixOneBVerdict).
 
 \paragraph{Without the contract, auditors side with the benchmark.} In the \textsc{none} arm recall equals the
-false-flag rate (\NSixNoneFlag\%) by construction, since the same readings are scored under both contracts. What
-carries information is which program gets flagged. The program that departs from the benchmark's behaviour is
+false-flag rate (\NSixNoneFlag\%) by construction, since the same readings are scored under both contracts. The informative
+difference is which program gets flagged. The program that departs from the benchmark's behaviour is
 flagged \NSixFlagPref{} points [\NSixFlagPrefLo, \NSixFlagPrefHi] more often than the one that follows it; the frozen
-code computes this, though the registration does not list it as a hypothesis. Verified diagnoses, likewise, are
+code computes this, though the registration does not list it as a hypothesis. Verified diagnoses are also
 more likely when the contract is the benchmark's rule: the registered convention advantage, half the difference
-between the two diagnosis rates, is \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi] (E6-2). Whether this
-reflects memory of the benchmark or the most natural reading of the task we cannot say, and for an evaluation it
-makes no difference. The models' own solutions written from the task alone follow the benchmark's rule on these units 89\% of the
-time (Appendix~\ref{app:e6}). A hidden-test ``detection'' here therefore credits agreement with a shared convention, and
+between the two diagnosis rates, is \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi] (E6-2). We cannot say whether this
+reflects memory of the benchmark or the most natural reading of the task. For an evaluation, it makes no difference.
+The models' own solutions written from the task alone follow the benchmark's rule on these units 89\% of the time
+(Appendix~\ref{app:e6}). A hidden-test ``detection'' here therefore credits agreement with a shared convention, and
 it would be a false accusation had the task's author meant the other rule.
 
 \paragraph{Reasoning budget.} After the contract is stated, the high budget changes verified diagnosis by
```

```diff
--- tex/sections/natural.tex
+++ tex/sections/natural.tex
@@ -2,10 +2,10 @@
 \section{What natural audit failures are made of}
 \label{sec:natural}
 
-The randomised experiment isolates the information limit on constructed units. Here we describe an ordinary audit
-benchmark through the same lens, without claiming to estimate how much of it is information-limited: classifying a
-program's first failing input does not establish that a defective and a correct program are indistinguishable. We use
-150 programs written by two generator models for 97 HumanEval+ and MBPP+ problems \citep{liu2023evalplus}; each passes
+The randomised experiment isolates the information limit on constructed units. We use the same distinction to
+describe an ordinary audit benchmark, without claiming to estimate how much of it is information-limited.
+Classifying a program's first failing input does not establish that a defective and a correct program are
+indistinguishable. We use 150 programs written by two generator models for 97 HumanEval+ and MBPP+ problems \citep{liu2023evalplus}; each passes
 its visible tests but fails the hidden suite and is paired with a control that passes the hidden suite. Of the 150,
 43 are development and 107 held-out items.
 
@@ -14,7 +14,7 @@
 reference's output acceptable (\textsc{determined}); both acceptable (\textsc{open}); only the program's acceptable
 (\textsc{at odds}); or neither. Identical evidence is pooled so that it cannot receive two labels. On the 107 held-out
 items, both classifiers agree on \textsc{determined} for 26, \textsc{open} for 21, \textsc{at odds} for 22 and out of
-domain for 13, and disagree on 25 (Cohen's $\kappa=0.71$; 0.78 on development items). Over all 150, both agree that
+domain for 13, and disagree on 25 (Cohen's $\kappa=0.71$; 0.78 on development items). Across all 150, both agree that
 the words single out the hidden suite's value for 34 (23\%). Disputed items are not evidence of ambiguity, only of
 disagreement between the classifiers.
 
@@ -22,8 +22,8 @@
 classifier judgement. For each failure we run the problem's other generations that pass the visible tests (up to
 eleven, from the same two generators, excluding the failing program itself) on its first failing input. They return
 the defective program's result 930 times and the reference's 559 times (71 neither); for 90 failures more of them return
-the defective program's result than the reference's, for 57 the reverse (an absolute majority: 85 against 55). Because the solutions come from the generators that wrote the
-failing programs, this measures what these models take the task to mean, not what independent programmers would do.
+the defective program's result than the reference's, for 57 the reverse (an absolute majority: 85 against 55). These solutions come from the generators that wrote the
+failing programs, so the check measures what these models take the task to mean, not what independent programmers would do.
 It also checks the classification (Figure~\ref{fig:natural}b): where the classifiers judge that only the program's
 output fits the words (\textsc{at odds}), 89\% of the other solutions return it; on \textsc{determined} and
 \textsc{open} failures the solutions split roughly evenly.
@@ -41,7 +41,7 @@
 \paragraph{What auditors verify.} With the original task text, four readings per program and two auditors, verified
 diagnosis on the held-out failures is \NOneVdDetermined\% on \textsc{determined} failures and \NOneVdOpen\% on
 \textsc{open} ones. The registered contrast (H6) is \NOneHSix{} points [\NOneHSixLo, \NOneHSixHi]: we could not detect
-a difference, and the interval allows a sizeable one in either direction (the development estimate, from 13 items,
+a difference, but the interval allows a sizeable one in either direction (the development estimate, from 13 items,
 was 50 points). Of the \NOneBridgeItems{} held-out programs with a verified diagnosis, \NOneBridgeDetermined{} have at
 least one witness that both classifiers label \textsc{determined}; among the four \textsc{open} failures with a
 verified diagnosis, two do. The classification concerns the first failing input only, so a program may have
@@ -52,6 +52,6 @@
 length-matched placebo, or a pointer naming the input class without resolving it. The \NOneItems{} held-out items
 (\NOneProblems{} problems) give a small replication of Section~\ref{sec:e6}: the clause raises verified diagnosis by
 \NOneHOne{} points [\NOneHOneLo, \NOneHOneHi] over the placebo (H1) and by \NOneHFive{} points [\NOneHFiveLo,
-\NOneHFiveHi] over the pointer (H5). The placebo left verified diagnosis where the original task had it (11.1\% in both; H4 passes its
-registered rule, but with seven problems its exact upper bound is 34.8\%), and whether the clause changes flags on the
-test-passing controls could not be settled (H2: $-$5.6 points [$-$33.3, 22.2]).
+\NOneHFiveHi] over the pointer (H5). Verified diagnosis was the same under the placebo and the original task (11.1\% in both; H4 passes its
+registered rule, but with seven problems its exact upper bound is 34.8\%). We could not settle whether the clause
+changes flags on the test-passing controls (H2: $-$5.6 points [$-$33.3, 22.2]).
```

```diff
--- tex/sections/transfer.tex
+++ tex/sections/transfer.tex
@@ -4,46 +4,47 @@
 
 Section~\ref{sec:framework} separates capacity misses, where the evidence decides the case but the auditor does
 not use it, from information misses, where the evidence does not decide the case. Three preregistered studies of
-scientific work are consistent with this distinction. They preceded the experiment above, are reported in full in
-Appendix~\ref{app:earlier}, and use ground truth that no model supplies; none of them randomised the contract, so
-they illustrate the distinction rather than test it.
+scientific work are consistent with this distinction. They preceded the experiment above and use ground truth that no
+model supplies. Appendix~\ref{app:earlier} reports them in full. None randomised the contract, so they illustrate the
+distinction rather than test it.
 
 \paragraph{Code: what the auditor is told it is reviewing.} SciCode \citep{tian2024scicode} splits research problems
 into steps with tests written by scientists. We label generated steps that pass the tests correct and those that fail defective (the tests can themselves
 reject correct code; \citealp{hu2026scicodeverified}) (81 defective, 150 correct instances). The auditor sees the step's text and code but no tests.
 Given the whole problem as the task, a cross-vendor auditor at eight readings flagged 87.7\% [72.7, 98.6] of
-defective and 68.7\% [56.6, 79.7] of correct steps. Some objections concerned a single step's failure to implement
+defective and 68.7\% [56.6, 79.7] of correct steps. The auditor sometimes objected that a single step failed to implement
 the whole problem. A second registered arm changed only the task text to name the step as the deliverable;
 the program bytes were identical. Flags on correct code fell by 32.7 points [22.4, 42.8], and flags on defective code
-by 14.8 points [2.7, 28.6]. What the auditor was told it was reviewing moved its operating point more than reading
-more often did.
+by 14.8 points [2.7, 28.6]. Changing what the auditor was told it was reviewing moved its operating point more than
+increasing the number of readings did.
 
 \paragraph{Results: where the evidence decides, computation helps.} For 74 correct SciCode programs we built a run
 log, a results file and a report in which every number cites its source. We injected either a reporting fault
 (the artefacts disagree) or a fabrication written consistently into all of them. A deterministic provenance
 check flagged all 49 reporting faults and none of the 25 fabrications, whose artefacts all agreed.
-The model auditor flagged 23 of the 25 (exact McNemar $p=2.4\times10^{-7}$), 21 of them with a finding about the
-fault itself on our post hoc reading, usually after recomputing the result from the code and inputs. Re-execution uses the same information and flagged 70 of the 74 faulty items.
+The model auditor flagged 23 of the 25 (exact McNemar $p=2.4\times10^{-7}$). On our post hoc reading, 21 had a
+finding about the fault itself, usually after recomputing the result from the code and inputs.
+Re-execution uses the same information and flagged 70 of the 74 faulty items.
 It missed four whose change fell inside the default numerical tolerance. The evidence here determines the
-right value, so a miss is a capacity miss. More capacity, through a model that computes or simply running the
-code, removes most of them.
+right value, so a miss is a capacity miss. More capacity, supplied by a model that computes or by simply running the
+code, removes most of these misses.
 
 \paragraph{Data: what a deterministic profile already captures.} We gave each of twelve public regression tables a
 data card. Each table was either left clean or given one injected fault (mixed units, negated values, duplicated
 rows, a shuffled target, swapped columns, sentinel values, rounding). Eight tables were held out (266 faulty and 266
-clean items). A profile validator, built from the card and from thresholds against a clean reference sample of the
-same table, was combined with a model auditor (GPT or Claude, with a shell on the full table or reading 120 rows).
+clean items). We combined a profile validator, built from the card and from thresholds against a clean reference sample of the
+same table, with a model auditor (GPT or Claude, with a shell on the full table or reading 120 rows).
 Adding the model raised correct localisation, scored by code against the injection manifest, by 2.3 points
 [0.4, 4.8], and flags on clean items by 16.0 points [3.2, 31.4]. Against a weaker validator (the card's ranges and units with
 simple checks against the reference sample), which localises 67.7\% of faults against the profile's 91.0\%, the
 model's gain is 23.3 points [13.2, 33.3]. On the 42 faulty items with a full 12{,}000-row table, adding the model
 to the profile changed localisation by 0.0, and agentic over reading-only configurations, which also differ in the
-number of readings, by +1.3 [$-$2.7, 5.8]. Earlier runs of this study were voided: in them one auditor searched the
+number of readings, by +1.3 [$-$2.7, 5.8]. Earlier runs of this study were voided. In those runs, one auditor searched the
 disk and the web for the original files, and several readings found and read the clean source files kept for item
-construction; held-out results under those runs (localisation gain +1.5 [0.0, 3.4], clean-flag increase +19.2) had
+construction. Held-out results from those runs (localisation gain +1.5 [0.0, 3.4], clean-flag increase +19.2) had
 been computed before the registered amendment that introduced an operating-system sandbox and replaced them
-(Appendix~\ref{app:e3}). In the reported run, 57\% of
-that auditor's held-out readings still attempted out-of-scope access; the attempts were logged and returned nothing.
+(Appendix~\ref{app:e3}). In the reported run, 57\% of that auditor's held-out readings still attempted out-of-scope
+access; the attempts were logged and returned nothing.
 An earlier study on four tables, at a clean-flag budget fixed in advance, found a gain of 10.7 points [6.0, 15.9] in
 findings naming the faulty column over a card validator. Where a strong profile from a clean reference is available,
 the model adds little localisation and many false flags.
```

```diff
--- tex/sections/discussion_v3.tex
+++ tex/sections/discussion_v3.tex
@@ -3,11 +3,11 @@
 
 \paragraph{Interpretation.} On units where the task leaves a behaviour open, a hidden-test ``detection'' is
 agreement with the benchmark's behaviour, a convention the models' own task-only solutions also follow (89\% on
-held-out units): auditors flag the program that departs from it far more often (Section~\ref{sec:e6}). Whether
-this convention is a natural reading of the task or one the models share with the benchmark, we cannot separate.
+held-out units): auditors flag the program that departs from it far more often (Section~\ref{sec:e6}). We cannot
+separate a natural reading of the task from a convention the models share with the benchmark.
 Adding one sentence that states the requirement turns that agreement into verified diagnosis; we could not resolve
 whether a larger reasoning budget changes the result once it is stated. Natural failures are observational and
-classified by models, but they point the same way: both classifiers agree that the task's words settle fewer than
+classified by models, but point in the same direction: both classifiers agree that the task's words settle fewer than
 a quarter of failures, and the generators' other solutions often behave like the ``defective'' program
 (Section~\ref{sec:natural}). The earlier scientific studies are consistent with the distinction without testing it
 (Section~\ref{sec:transfer}): naming the deliverable cut false flags on correct scientific code from 69\% to 36\%,
@@ -17,21 +17,21 @@
 \paragraph{Practical consequences.} Alongside recall, an audit benchmark should report which of its cases the
 task determines. It should not count agreement with an unstated convention as detection. An auditor that is
 unsure whether a behaviour is required should be scored for asking, not only for flagging or passing.
-For deployment, an auditor's value on such behaviour depends on whether the requirement is written down;
-discovering requirements that nobody wrote down, which we did not measure, is the harder problem.
+In deployment, an auditor's value on such behaviour depends on whether the requirement is written down.
+Discovering requirements that nobody wrote down, which we did not measure, is the harder problem.
 
 \paragraph{Limitations.}\label{sec:limits} \emph{Constructed units.} The randomised-contract units are execution-validated;
-two models, rather than people, judge them admissible, and the same two models implement the rules, so construction
+two models, rather than people, judge them admissible. The same two models implement the rules, so construction
 and judging are not independent. We make no claim about how often such ambiguity occurs. The 41 held-out units are
-selected (from 406 problems) and concentrated: 37 come from MBPP+, and on only two do the models' task-only solutions
-follow both rules.
+selected (from 406 problems) and concentrated: 37 come from MBPP+. The models' task-only solutions
+follow both rules on only two units.
 \emph{Benchmarks.} All randomised-contract and natural-failure units come from HumanEval+ and MBPP+, short functions with small specifications.
 Whether the size of the convention advantage carries over to larger programs, where more behaviour is
 unstated, remains untested. \emph{Auditors.} We tested two vendors' models at two reasoning budgets with one rulebook.
 Other auditors, agent scaffolds or execution-based test generation may sit closer to the ceiling before the
 reveal, although Lemma~\ref{lem:symmetric} bounds what any of them can do on the unrevealed arms.
 \emph{Verification.} A verified diagnosis requires a witness whose disagreement with the contract's oracle the
-benchmark's own comparator confirms by execution, with the auditor's stated expected value correct. We do not credit diagnoses stated only in prose, which can understate auditors whose
+benchmark's own comparator confirms by execution, with the auditor's stated expected value correct. We do not credit diagnoses stated only in prose. This can understate the performance of auditors whose
 findings are correct but unexecutable. \emph{Natural failures.} Models classify the natural failures
 (Cohen's $\kappa$ 0.71 on held-out items), and the behavioural check reuses the generators' own solutions.
 \emph{Data.} The data study injects one fault per item into twelve public tables; its conclusion is specific to
@@ -41,5 +41,5 @@
 selectivity of 16.8 points [10.5, 23.2], above zero but not resolved against the registered 20-point threshold for
 substantial selectivity, so the question largely returns to the task's author. \emph{Amendments.} Two
 infrastructure rules were registered during the held-out runs, before any held-out analysis (attempt accounting
-for calls that never reached the model; terminal treatment of reference timeouts); Appendix~\ref{app:e6} lists them. \emph{Earlier studies} of the shipped configuration
+for calls that never reached the model; terminal treatment of reference timeouts). Appendix~\ref{app:e6} lists them. \emph{Earlier studies} of the shipped configuration
 (Appendix~\ref{app:earlier}) are reported as registered and are not re-analysed here.
```

```diff
--- tex/sections/introduction_v2.tex
+++ tex/sections/introduction_v2.tex
@@ -6,7 +6,7 @@
 gives three ordinary examples. A generated function splits on underscores, capitalises each word and passes
 all three. The hidden suite then passes \verb|___python_program| and expects \verb|___PythonProgram|; the function
 returns \verb|PythonProgram|. The task says nothing about how to handle leading underscores. The benchmark treats
-this program as defective, so an automated auditor that reads and passes it has missed a defect.
+this program as defective. By that measure, an automated auditor that reads and passes it has missed a defect.
 
 Models increasingly check what other models write. Audit benchmarks score them as in this example, against a hidden
 reference. We argue that these scores conflate two kinds of case. In some, the evidence available to the auditor
@@ -19,16 +19,16 @@
 variation between the evidence a defective and a correct program produce. The best attainable recall at a given
 false-flag rate is the Neyman--Pearson power of that evidence (Section~\ref{sec:framework}). Audit evaluations have
 lacked a way to observe this distinction because a benchmark fixes one contract and hides the counterfactual.
-Our experiment constructs that counterfactual (Section~\ref{sec:e6}). For each unit, we take a real benchmark task
-that leaves one behaviour open and build two programs that differ only there. We grade the auditor against a
+We construct that counterfactual experimentally (Section~\ref{sec:e6}). Each unit starts with a real benchmark task
+that leaves one behaviour open; we build two programs that differ only in that behaviour. We grade the auditor against a
 contract drawn independently of what it sees, then reveal the contract in different ways. Execution validates the
 programs, oracles and boundaries of the open behaviour; two independent models judge whether both rules are admissible.
 
 \textbf{Findings.} Across \NSixUnits{} held-out units and auditors from two vendors at two reasoning budgets:
 \begin{itemize}\itemsep1pt
 \item With the contract withheld, flagging cannot track which program is wrong: the same readings are scored under
-  both contracts, so recall equals the false-flag rate (\NSixNoneFlag\%) by construction. Which program is flagged
-  is telling. The one that departs from the benchmark's behaviour is flagged \NSixFlagPref{} points
+  both contracts, so recall equals the false-flag rate (\NSixNoneFlag\%) by construction. The informative difference
+  is which program is flagged. The one that departs from the benchmark's behaviour is flagged \NSixFlagPref{} points
   [\NSixFlagPrefLo, \NSixFlagPrefHi] more often than the one that follows it, and diagnosed more often too (the registered convention advantage, half
   the difference between the two diagnosis rates, is \NSixTwo{} points [\NSixTwoLo, \NSixTwoHi]).
 \item The models' own solutions written from the task alone follow the benchmark's behaviour on these units 89\%
```

```diff
--- tex/paper_v3.tex
+++ tex/paper_v3.tex
@@ -53,18 +53,18 @@
 \printAffiliationsAndNotice{}
 
 \begin{abstract}
-Audit benchmarks grade an automated auditor against a hidden reference, but the evidence an auditor sees is often
-equally consistent with the program and with that reference. In such cases recall minus false-flag rate is bounded by
-how well the evidence separates defective from correct programs. The bound is a classical fact about tests, yet
-audit evaluations cannot observe it, because a benchmark fixes a single contract. We make it observable. From
-HumanEval+ and MBPP+ tasks we build pairs of programs, checked by execution, that differ only on a behaviour the task
-leaves open; we grade auditors from two vendors against a contract drawn at random and vary how that contract is
-revealed. On 41 held-out units with the contract withheld, auditors flag the program that departs from the
+Audit benchmarks grade automated auditors against a hidden reference, yet the evidence an auditor sees is often
+equally consistent with the program and the reference. In such cases recall minus false-flag rate is bounded by
+how well the evidence separates defective from correct programs. The bound is a classical fact about tests, but
+audit evaluations cannot observe it because a benchmark fixes a single contract. To make it observable, we build pairs of programs
+from HumanEval+ and MBPP+ tasks, checked by execution, that differ only on a behaviour the task leaves open.
+We grade auditors from two vendors against a contract drawn at random and vary how that contract is revealed.
+On 41 held-out units with the contract withheld, auditors flag the program that departs from the
 benchmark's behaviour \NSixFlagPref{} points more often than the one that follows it. The models' own solutions written from
-the task alone follow the benchmark's behaviour on 89\% of occasions, so what the benchmark rewards is agreement with
+the task alone follow the benchmark's behaviour on 89\% of occasions. The benchmark thus rewards agreement with
 a convention the models share. One added sentence stating the missing requirement raises verified diagnosis by \NSixFive{} points.
-Among 150 natural hidden-test failures, two model classifiers agree that the task's words single out the expected
-value in only 34. Three earlier preregistered studies of scientific code, results and data fit the same distinction:
+Of 150 natural hidden-test failures, only 34 are cases where two model classifiers agree that the task's words
+single out the expected value. Three earlier preregistered studies of scientific code, results and data fit the same distinction:
 false flags on correct scientific code halve when the task names the deliverable, and recomputation catches
 fabricated results where code and inputs determine them. Held-out analyses were preregistered; deviations are disclosed.
 \end{abstract}
```

Possible factual or logical issues, left unchanged:

- **`introduction_v2.tex`**, “No auditor, whatever its capacity, can tell them apart…”: compatibility with two behaviours does not itself establish equality of evidence distributions, as `framework.tex` explicitly acknowledges.
- **`introduction_v2.tex`**, “…two independent models judge whether both rules are admissible”: “independent” could imply independence from construction, whereas `e6.tex` says the same models implement and judge the rules.
- **`e6.tex`**, “computation cannot repair a miss on an indistinguishable case”: the result constrains recall relative to false flags; it does not prohibit correcting an individual miss.
- **`framework.tex`**, proof beginning “With $X$ uniform…”: the proof assumes uniform program sampling, which the lemma does not state. The lemma may still hold more generally, but this proof establishes the stated mixture only under that additional assumption.

