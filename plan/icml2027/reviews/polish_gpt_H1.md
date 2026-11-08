```diff
--- tex/sections/framework.tex
+++ tex/sections/framework.tex
@@ -35,19 +35,20 @@
 \end{corollary}
 
 Both statements are textbook facts about hypothesis testing (the Neyman--Pearson lemma and the total-variation
-bound on any test's power minus its size; \citealp{neyman1933efficient}); we claim no novelty for them. Note that the
-component bound needs the false-flag constraint on the component itself: under an overall false-flag rate $\alpha$
+bound on any test's power minus its size; \citealp{neyman1933efficient}). We claim no novelty for them. The
+component bound requires a false-flag constraint on the component itself. Under an overall false-flag rate $\alpha$
 alone, with $q$ the share of correct programs in the component, the bound is only $(1-\pi)+\pi\min(1,\alpha/q)$.
-Their use here is to separate two causes of a missed defect that audit evaluations conflate. A miss on a distinguishable case is a \emph{capacity} miss: some auditor with the same evidence could do
+We use these statements to separate two causes of missed defects that audit evaluations conflate.
+A miss on a distinguishable case is a \emph{capacity} miss: some auditor with the same evidence could do
 better. A miss on an indistinguishable case is an \emph{information} miss: no auditor can do better without
 different evidence. Only interventions that change $E$ move the ceiling.
 
 \paragraph{Contract randomisation makes the component observable.}
-On a natural benchmark the hidden contract is fixed to the benchmark's reference behaviour, so indistinguishability
-is a counterfactual: we cannot see the auditor's response under the other admissible contract. We construct it.
-Take a discrepancy unit: an input class on which two behaviours, $A$ and $B$, are both admissible under the task
-text and the visible tests. Build two programs that differ only on that class, $X_A$ and $X_B$, and draw
-$H\in\{A,B\}$ independently of everything the auditor sees.
+A natural benchmark fixes the hidden contract to its reference behaviour. Indistinguishability is therefore
+counterfactual: we cannot see the auditor's response under the other admissible contract. We construct this
+counterfactual using a discrepancy unit, an input class on which two behaviours, $A$ and $B$, are both admissible
+under the task text and the visible tests. We build two programs that differ only on that class, $X_A$ and $X_B$,
+and draw $H\in\{A,B\}$ independently of everything the auditor sees.
 
 \begin{lemma}
 \label{lem:symmetric}
@@ -63,16 +64,17 @@
 
 Revealing $H$ in the evidence (stating the requirement) breaks the premise of Lemma~\ref{lem:symmetric}; text that
 draws attention to the input class, or lists both behaviours without choosing, does not. The experiment in
-Section~\ref{sec:e6} therefore measures three things that the propositions leave open: how far real auditors sit
-below the ceiling once the requirement is revealed, whether additional computation helps more before or after
-the reveal, and how much of the recall measured on natural benchmarks is agreement with the benchmark's convention
-on indistinguishable units, which would be false flags had the convention gone the other way.
+Section~\ref{sec:e6} measures how far real auditors sit below the ceiling once the requirement is revealed and
+whether additional computation helps more before or after the reveal. It also measures how much of the recall
+on natural benchmarks reflects agreement with the benchmark's convention on indistinguishable units.
+Those detections would be false flags had the convention gone the other way. The propositions leave these
+three questions open.
 
 \paragraph{What we do not claim.}
-The ceiling is relative to the evidence, and the evidence includes what a model brings with it: a model that has
-memorised a benchmark's reference sees more than the task text. Contract randomisation neutralises this on the
-constructed units, because the memorised convention is equally likely to be wrong. On natural units we cannot
-observe the counterfactual contract, so Section~\ref{sec:natural} reports which failures the task's words determine,
-as judged by two models and checked against what independent programmers do; that is a description of a benchmark,
-not an estimate of an information-limited share. Logical ambiguity of a task is not the same as equality of the two
-evidence laws, and nothing here says that computation cannot help on natural programs.
+The ceiling is relative to the evidence, which includes what a model brings with it.
+A model that has memorised a benchmark's reference sees more than the task text. Contract randomisation
+neutralises this on the constructed units because the memorised convention is equally likely to be wrong.
+On natural units we cannot observe the counterfactual contract. Section~\ref{sec:natural} therefore reports
+which failures the task's words determine, as judged by two models and checked against what independent programmers do.
+This describes a benchmark; it does not estimate an information-limited share. A task's logical ambiguity is
+not the same as equality of the two evidence laws, and nothing here rules out computation helping on natural programs.
```

```diff
--- tex/sections/transfer.tex
+++ tex/sections/transfer.tex
@@ -2,38 +2,39 @@
 \section{Transfer: scientific code, results and data}
 \label{sec:transfer}
 
-Section~\ref{sec:framework} separates two kinds of miss: a capacity miss, where the evidence decides the case and
-the auditor does not use it, and an information miss, where the evidence does not decide it. Three preregistered
-studies of scientific work, run before the experiment above and reported in full in Appendix~\ref{app:earlier}, fall
-on either side of that line. Each uses ground truth no model supplies.
+Section~\ref{sec:framework} separates capacity misses, where the evidence decides the case but the auditor does
+not use it, from information misses, where the evidence does not decide the case. Three preregistered studies of
+scientific work fall on either side of this distinction. They preceded the experiment above and are reported in
+full in Appendix~\ref{app:earlier}. Each uses ground truth that no model supplies.
 
 \paragraph{Code: what the auditor is told it is reviewing.} SciCode \citep{tian2024scicode} splits research problems
 into steps with tests written by scientists. Generated steps that pass are correct and those that fail are
-defective (81 defective, 150 correct instances); the auditor sees the step's text and code, no tests. Given the whole
-problem as the task, a cross-vendor auditor at eight readings flagged 87.7\% [72.7, 98.6] of defective and 68.7\%
-[56.6, 79.7] of correct steps, some of its objections being that one step did not implement the whole problem. A second registered arm
-changed only the task text, naming the step as the deliverable; the program bytes were identical. Flags on correct
-code fell by 32.7 points [22.4, 42.8]. As on the constructed units, the largest change came from telling the
-auditor what was required, not from reading more.
+defective (81 defective, 150 correct instances). The auditor sees the step's text and code but no tests.
+Given the whole problem as the task, a cross-vendor auditor at eight readings flagged 87.7\% [72.7, 98.6] of
+defective and 68.7\% [56.6, 79.7] of correct steps. Some objections concerned a single step's failure to implement
+the whole problem. A second registered arm changed only the task text to name the step as the deliverable;
+the program bytes were identical. Flags on correct code fell by 32.7 points [22.4, 42.8]. As on the constructed
+units, telling the auditor what was required produced the largest change, rather than reading more.
 
 \paragraph{Results: where the evidence decides, computation helps.} For 74 correct SciCode programs we built a run
-log, a results file and a report whose every number cites its source, and injected either a reporting fault (the
-artefacts disagree) or a fabrication written consistently into all of them. A deterministic provenance check flagged
-all 49 reporting faults and none of the 25 fabrications, because everything agreed with everything else. The model
-auditor flagged 23 of the 25, usually by recomputing the result from the code and inputs (exact McNemar
-$p=2.4\times10^{-7}$); re-execution, which uses the same information, flagged 70 of the 74 faulty items, missing four
-whose change fell inside the default numerical tolerance. Here the evidence determines the
-right value, so a miss is a capacity miss, and more capacity, a model that computes or simply running the code,
-removes it.
+log, a results file and a report in which every number cites its source. We injected either a reporting fault
+(the artefacts disagree) or a fabrication written consistently into all of them. A deterministic provenance
+check flagged all 49 reporting faults and none of the 25 fabrications, whose artefacts all agreed.
+The model auditor flagged 23 of the 25, usually by recomputing the result from the code and inputs (exact McNemar
+$p=2.4\times10^{-7}$). Re-execution uses the same information and flagged 70 of the 74 faulty items.
+It missed four whose change fell inside the default numerical tolerance. The evidence here determines the
+right value, so a miss is a capacity miss. More capacity, through a model that computes or simply running the
+code, removes it.
 
-\paragraph{Data: where the documentation carries the information.} Twelve public regression tables were each given a
-data card and either left clean or given one injected fault (mixed units, negated values, duplicated rows, a shuffled
-target, swapped columns, sentinel values, rounding); eight tables (266 items) were held out. A validator written
-mechanically from the card was combined with a model auditor (GPT or Claude, with a shell on the full table or reading
-120 rows). Adding the model raised correct localisation, scored by code against the injection manifest, by 2.3 points
-[0.4, 4.8] and flags on clean items by 16.0 points [3.2, 31.4]; neither the full table nor tool use helped. Every
-reading ran in an operating-system sandbox, after an unsandboxed pilot in which one auditor searched the disk and the
-web for the original files; inside it, 57\% of that auditor's held-out readings still attempted out-of-scope access,
-which was logged and returned nothing. An earlier study on four tables, at a clean-flag budget fixed in advance, found
-a larger gain in findings naming the faulty column (10.7 points [6.0, 15.9]) over a simpler validator. Either way, where the documentation already states
-what valid data look like, a check written from it finds most of the faults that it and the model find together.
+\paragraph{Data: where the documentation carries the information.} We gave each of twelve public regression tables a
+data card. Each table was either left clean or given one injected fault (mixed units, negated values, duplicated
+rows, a shuffled target, swapped columns, sentinel values, rounding). We held out eight tables (266 items) and
+combined a validator written mechanically from the card with a model auditor (GPT or Claude, with a shell on the
+full table or reading 120 rows). Adding the model raised correct localisation, scored by code against the injection manifest, by 2.3 points
+[0.4, 4.8] and flags on clean items by 16.0 points [3.2, 31.4]. Neither the full table nor tool use helped.
+In an unsandboxed pilot, one auditor searched the disk and the web for the original files. Every subsequent
+reading ran in an operating-system sandbox. Even there, 57\% of that auditor's held-out readings attempted
+out-of-scope access; these attempts were logged and returned nothing. An earlier study on four tables, at a clean-flag budget fixed in advance, found
+a larger gain in findings naming the faulty column (10.7 points [6.0, 15.9]) over a simpler validator.
+In both studies, where the documentation already states what valid data look like, a check written from it
+finds most of the faults that it and the model find together.
```

```diff
--- tex/sections/related_v3.tex
+++ tex/sections/related_v3.tex
@@ -1,38 +1,38 @@
 \section{Related work}
 \label{sec:related}
 
-\textbf{Critics and repeated reading.} Trained critics catch more bugs in model-written code than unaided humans
-and hallucinate some \citep{mcaleese2024critics}; aggregating review passes raises review F1 on real pull requests
-\citep{zeng2025swrbench}; coverage under repeated sampling grows roughly log-linearly in the number of samples
-\citep{brown2024monkeys}; and self-correction without external feedback does not reliably help
-\citep{huang2024selfcorrect}. These results vary the auditor while holding the evidence fixed. We vary the evidence
-while holding the auditor fixed, and show that on the cases we construct the second moves performance and the first
-does not.
+\textbf{Critics and repeated reading.} Trained critics catch more bugs in model-written code than unaided humans,
+but also hallucinate some \citep{mcaleese2024critics}. Aggregating review passes raises review F1 on real pull
+requests \citep{zeng2025swrbench}, and coverage under repeated sampling grows roughly log-linearly in the number
+of samples \citep{brown2024monkeys}. Self-correction without external feedback does not reliably help
+\citep{huang2024selfcorrect}. These studies vary the auditor while holding the evidence fixed. We hold the auditor
+fixed and vary the evidence. On the cases we construct, changing the evidence moves performance; changing the
+auditor does not.
 
 \textbf{What the hidden suite decides.} EvalPlus rebuilt HumanEval and MBPP with larger suites
-\citep{liu2023evalplus}; models collapse onto one reading of an underspecified task \citep{richter2026collapse};
-generated tests err mostly in the expected value \citep{xiong2023testing}; and generated oracles capture what a
+\citep{liu2023evalplus}. Models collapse onto one reading of an underspecified task \citep{richter2026collapse},
+and generated tests err mostly in the expected value \citep{xiong2023testing}. Generated oracles capture what a
 program does rather than what was intended \citep{konstantinou2024oracles}. Label errors in test sets bound and
-reorder what benchmarks can measure \citep{northcutt2021labelerrors, gema2025mmlu}. Our setting differs: the
-reference is not wrong, it is one of several behaviours the task admits, so the right correction is neither
-relabelling nor discarding but stating the contract, and we measure what stating it does.
+reorder what benchmarks can measure \citep{northcutt2021labelerrors, gema2025mmlu}. In our setting, the reference
+is not wrong: it is one of several behaviours the task admits. The appropriate correction is to state the
+contract, rather than relabel or discard the case. We measure the effect of stating it.
 
 \textbf{Clarification.} Code generators can be made to ask clarifying questions when a task is ambiguous
 \citep{mu2024clarifygpt, wu2025humanevalcomm}, or to formalise intent as tests confirmed by a user
-\citep{lahiri2022ticoder}; abstaining when evidence is insufficient is the classical reject option
-\citep{chow1970reject}. We study the auditing side: we score a request for clarification as a separate outcome,
-neither a detection nor a pass, and find % CHECK against held-out routing result
- that the two vendors' auditors differ sharply in how often they make one.
+\citep{lahiri2022ticoder}. Abstaining when evidence is insufficient is the classical reject option
+\citep{chow1970reject}. We study auditing and score a request for clarification as a separate outcome,
+neither a detection nor a pass. We find % CHECK against held-out routing result
+ that the two vendors' auditors differ sharply in how often they request clarification.
 
 \textbf{Auditing scientific work.} Models detect a minority of errata-grade errors in manuscripts
-\citep{son2025spot} and of paper--code discrepancies \citep{baumgartner2026scicoqa}; an auditor of AI-scientist
-projects detects pitfalls far better with logs and code than with the paper alone \citep{luo2025pitfalls}; cleaning
-agents miss errors that span rows \citep{bendinelli2025cleaning}; and an expert audit of SciCode
-\citep{tian2024scicode} found specifications and tests that reject correct solutions \citep{hu2026scicodeverified},
-which it repairs by rewriting the specification. Our randomised contracts are the experimental counterpart of that
-repair: they measure how much of an auditor's apparent miss rate a repaired specification would remove.
+\citep{son2025spot} and of paper--code discrepancies \citep{baumgartner2026scicoqa}. An auditor of AI-scientist
+projects detects pitfalls far better with logs and code than with the paper alone \citep{luo2025pitfalls}.
+Cleaning agents miss errors that span rows \citep{bendinelli2025cleaning}. An expert audit of SciCode
+\citep{tian2024scicode} found specifications and tests that reject correct solutions \citep{hu2026scicodeverified}
+and repairs them by rewriting the specification. Our randomised contracts are the experimental counterpart
+of that repair. They measure how much of an auditor's apparent miss rate a repaired specification would remove.
 
-\textbf{Statistics.} The ceiling is the Neyman--Pearson bound \citep{neyman1933efficient}; the false-flag budget is
-tested with a betting confidence sequence \citep{waudbysmith2024betting}, which is valid at any sample size.
+\textbf{Statistics.} The ceiling is the Neyman--Pearson bound \citep{neyman1933efficient}. We test the false-flag
+budget with a betting confidence sequence \citep{waudbysmith2024betting}, which is valid at any sample size.
 Preregistration of evaluations is beginning to appear in machine learning \citep{vaccaro2026prereg,
-thomas2026phacking}; here it is method, not contribution.
+thomas2026phacking}. We use it as a method and do not claim it as a contribution.
```

```diff
--- tex/sections/discussion_v3.tex
+++ tex/sections/discussion_v3.tex
@@ -1,34 +1,35 @@
 \section{Discussion and limitations}
 \label{sec:discussion}
 
-\paragraph{What the results say.} On units where the task leaves a behaviour open, a hidden-test ``detection'' is
+\paragraph{Interpretation.} On units where the task leaves a behaviour open, a hidden-test ``detection'' is
 agreement with the benchmark's convention, and the auditors we tested agree with it more often than chance
-(Section~\ref{sec:e6}). One added sentence that states the convention turns that agreement into verified diagnosis;
-a larger reasoning budget does not. On natural failures the same pattern appears without construction: most
-failures are ones the task's words do not settle, independent programmers mostly behave like the ``defective''
-program, and the diagnoses auditors do verify concern what the words settle (Section~\ref{sec:natural}). In
-scientific work the same line holds in both directions (Section~\ref{sec:transfer}): naming the deliverable cut
-false flags on correct scientific code from 69\% to 36\%; where code and inputs determine a reported value, recomputation by
-the model, or by re-execution, catches fabrications that consistency checks cannot; and where documentation states
-what valid data look like, a validator written from it already finds most faults. Computation helps where the
-evidence decides; elsewhere the ceiling moves with what the auditor is told.
+(Section~\ref{sec:e6}). Adding one sentence that states the convention turns that agreement into verified
+diagnosis. A larger reasoning budget does not. Natural failures show the same pattern without construction.
+The task's words do not settle most failures, and independent programmers mostly behave like the ``defective''
+program. The diagnoses auditors do verify concern what the words settle (Section~\ref{sec:natural}).
+Scientific work shows both sides of this distinction (Section~\ref{sec:transfer}). Naming the deliverable cut
+false flags on correct scientific code from 69\% to 36\%. Where code and inputs determine a reported value,
+recomputation by the model, or by re-execution, catches fabrications that consistency checks cannot.
+Where documentation states what valid data look like, a validator written from it already finds most faults.
+Computation helps where the evidence decides; elsewhere the ceiling moves with what the auditor is told.
 
-\paragraph{Practical consequences.} An audit benchmark should report, beside recall, which of its cases the task
-determines, and should not count agreement with an unstated convention as detection. An auditor that is unsure
-whether a behaviour is required should be scored for asking, not only for flagging or passing. For deployment,
-the cheapest improvement we measured is to write the missing requirement down.
+\paragraph{Practical consequences.} Alongside recall, an audit benchmark should report which of its cases the
+task determines. It should not count agreement with an unstated convention as detection. An auditor that is
+unsure whether a behaviour is required should be scored for asking, not only for flagging or passing.
+Writing down the missing requirement is the cheapest deployment improvement we measured.
 
-\paragraph{Limitations.}\label{sec:limits} \emph{Constructed units.} The randomised-contract units are execution-validated and judged
-admissible by two models, not by people; we make no claim about how often such ambiguity occurs, and two models
-agreeing that a rule is compatible with a task is weaker than expert agreement. \emph{Benchmarks.} All code units
-come from HumanEval+ and MBPP+, short functions with small specifications; whether the size of the convention
-advantage carries over to larger programs, where more behaviour is unstated, is untested. \emph{Auditors.} Two
-vendors' models at two reasoning budgets, with one rulebook; other auditors, agent scaffolds or execution-based
-test generation may sit closer to the ceiling before the reveal, although Lemma~\ref{lem:symmetric} bounds what any
-of them can do on the unrevealed arms. \emph{Verification.} A verified diagnosis requires a witness that the
-benchmark's own comparator confirms and two judges accept; diagnoses stated only in prose are not credited, which
-can understate auditors whose findings are correct but unexecutable. \emph{Natural failures.} The classification
-of natural failures is model-made, with Cohen's $\kappa$ of 0.78 on development items, and the behavioural check
-uses solutions from two generators only. \emph{Data.} The data study injects one fault per item into twelve public
-tables; its conclusion is specific to faults that documentation describes. \emph{Earlier studies} of the shipped
-configuration (Appendix~\ref{app:earlier}) are reported as they were registered and are not re-analysed here.
+\paragraph{Limitations.}\label{sec:limits} \emph{Constructed units.} The randomised-contract units are execution-validated;
+two models, rather than people, judge them admissible. We make no claim about how often such ambiguity occurs.
+Agreement between two models that a rule is compatible with a task is weaker than expert agreement.
+\emph{Benchmarks.} All code units come from HumanEval+ and MBPP+, short functions with small specifications.
+Whether the size of the convention advantage carries over to larger programs, where more behaviour is
+unstated, remains untested. \emph{Auditors.} We tested two vendors' models at two reasoning budgets with one rulebook.
+Other auditors, agent scaffolds or execution-based test generation may sit closer to the ceiling before the
+reveal, although Lemma~\ref{lem:symmetric} bounds what any of them can do on the unrevealed arms.
+\emph{Verification.} A verified diagnosis requires a witness that the benchmark's own comparator confirms and
+two judges accept. We do not credit diagnoses stated only in prose, which can understate auditors whose
+findings are correct but unexecutable. \emph{Natural failures.} Models classify the natural failures, with
+Cohen's $\kappa$ of 0.78 on development items. The behavioural check uses solutions from two generators only.
+\emph{Data.} The data study injects one fault per item into twelve public tables; its conclusion is specific to
+faults that documentation describes. \emph{Earlier studies} of the shipped configuration
+(Appendix~\ref{app:earlier}) are reported as registered and are not re-analysed here.
```

Suspected factual or logical problems, left unresolved:

- **`framework.tex` — “A miss on a distinguishable case is a … capacity miss” and “no auditor can do better without different evidence.”** Distributional distinguishability does not make every individual miss avoidable. Under indistinguishability, recall can increase if false flags increase too; the latter claim needs an operating-point qualification.
- **`transfer.tex` — “Generated steps that pass are correct and those that fail are defective.”** This equates test outcomes with correctness, while `related_v3.tex` reports that SciCode tests can reject correct solutions. The intended ground-truth definition needs checking.
- **`transfer.tex` — “More capacity … removes it.”** This categorical statement sits uneasily with the reported residual misses: the model flags 23 of 25 fabrications, and re-execution flags 70 of 74 faulty items.
- **`discussion_v3.tex` — “All code units come from HumanEval+ and MBPP+.”** Read literally, this conflicts with the SciCode transfer studies. Its intended scope may be only the main experiments.

