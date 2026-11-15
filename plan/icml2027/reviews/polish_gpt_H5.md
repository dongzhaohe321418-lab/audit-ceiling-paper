```diff
--- a/tex/appendix/e6_protocol.tex
+++ b/tex/appendix/e6_protocol.tex
@@ -88,43 +88,58 @@
 the task leaves open is left largely to the task's author. E8 was registered after a development pilot (96.9\%
 against 88.3\%), uses one vendor for both roles and relies on a model judge; all 238 held-out readings completed.
 
-\paragraph{Do judges outside the construction accept both rules? (E9.)} Registered after the E6 results were known and
-before any held-out E9 call (after development pilots), in response to a review that named admissibility the central validity question. Two judges that
-took no part in the construction, Claude Sonnet 5.5 and GPT-5.6-terra (high budget; both also E6 auditors), read each
-held-out unit in both rule orders, not told which rule is the benchmark's nor what kind of item they read, and judged
-whether the inputs are valid and each rule compatible with the task; an exclusion had to quote the words that rule the rule out or appeal to ordinary meaning. Besides the 41 open units and 78 positive controls, 41 \emph{resolved} items appended one rule to the
-task as an ordinary requirement, so that the other rule should be excluded, an anchor that does not depend on E6's
-judges. Of 640 readings, one (a resolved item) failed. Both rules were accepted on 84.1\% [77.4, 90.3] of readings of
-open units (E9-1, lower bound $>50$: supported), and rule A was excluded on 9.1\% of them against 96.5\% of
-readings of controls: a difference of 87.3 points [81.5, 92.5] (E9-2, $>30$: supported). On resolved items the
-non-appended rule was excluded 55.0 points [47.5, 62.5] more often than on the same units without the requirement
-(E9-2b: supported). The judges differ: Claude accepted both rules on 96.3\% of open readings and GPT on 72.0\%, and
-on resolved items Claude excluded the non-appended rule in only 25.9\% of readings against GPT's 98.8\%, so Claude
-is the more permissive judge. The two rule orders gave the same judgement for 66 of 82 judge--unit pairs on open units (80.5\%); each of the 425 exclusions came with a quotation matching the task after normalisation (262; matching does not show that the words entail the exclusion) or an appeal to ordinary meaning (163). Rerun by
-the frozen E6 code on the 35 units that at least three of four readings accept, the registered criteria of E6-1, E6-2 and E6-5 hold and the flag preference stays positive:
-resolved diagnosis 91.1\% [81.4, 98.2], E6-2 +11.1 [5.0, 17.5], E6-5 +79.3 [70.0, 87.9], flag preference +22.9 [10.0,
-36.4]; so it does on the 23 units all four readings accept (E6-2 +8.7 [3.3, 15.2], E6-5 +83.7 [72.8, 92.4]). On units
-selected by one judge alone, the other vendor's auditors still show the convention advantage (selected by GPT,
-Claude auditors: +13.0 [5.4, 21.7]; selected by Claude, GPT auditors: +11.2 [5.3, 17.8]); on GPT-selected units
-GPT's own auditors give +4.3 [0.0, 9.8]. These judges are models of the same vendors, and the subset analyses are
-conditional, not independent replications; E9 does not replace human validation.
-
-\paragraph{Does the sentence add more than pointing at the behaviour? (E10.)} Registered after the E6, E8 and E9
-results were known and before any held-out E10 call (after a development pilot). On the 41 held-out open units, E6's two low-budget configurations read
-four arms afresh, interleaved within each construction attempt: the task alone; a \emph{pointer}, ``Additional note:
-pay particular attention to how the function handles the following kind of input: \dots'', naming the unit's input
-class in the constructor's words with any clause that says what is unspecified or names the alternatives removed by a
-fixed rule; and the two sentence arms. Scoring and analysis are E6's frozen code; the pointer, revealing no contract,
-is scored under both. All 1{,}312 readings are valid. Verified diagnosis is 12.2\% [7.3, 17.7] with the task alone,
-31.1\% [23.8, 38.4] with the pointer and 91.5\% [82.9, 97.6] with the sentence. The sentence exceeds the pointer by
-60.4 points [51.8, 68.9] (E10-1, lower bound $>0$: supported), and does so for each vendor (GPT +59.8, Claude +61.0)
-and without the two exception-contract units (+62.2). The pointer adds 18.9 points [12.2, 26.2] over the task alone;
-since the upper limit exceeds the registered 20-point margin, we do not claim that attention adds little. Pointing
-without a rule raises pooled recall and false-flag rate equally (from 14.0\% to 37.8\%, equal by construction), more on program A (23.2\% to 53.7\%) than on program B (4.9\% to 22.0\%), widens the flag preference for the program that departs from the benchmark (+18.3
-[6.1, 31.7] to +31.7 [12.2, 51.2]) and the convention advantage (+9.8 to +15.2): directed to the behaviour but not
-told the rule, auditors apply the benchmark's convention more often. Among flagging readings, over 90\% name an in-class witness in every arm; since this is conditional on flagging, it does not show how often each arm finds the input. The fresh sentence-minus-task
-contrast, +79.3 [69.5, 87.2], replicates E6-5 (+76.8). The pointer is one attention control, phrased as a note rather
-than a requirement, and the auditors are two of E6's configurations at the low budget.
+\paragraph{Do judges outside the construction accept both rules? (E9.)} We registered this study after
+the E6 results were known and before any held-out E9 call, following development pilots. It responds to a
+review that identified admissibility as the central validity question. Two judges uninvolved in
+construction, Claude Sonnet 5.5 and GPT-5.6-terra (high budget; both also E6 auditors), read each
+held-out unit in both rule orders. They were told neither which rule was the benchmark's nor what kind of
+item they were reading. Each judged whether the inputs were valid and each rule compatible with the task.
+To exclude a rule, they had to quote the task wording that excluded it or appeal to ordinary meaning.
+Alongside the 41 open units and 78 positive controls, 41 \emph{resolved} items appended one rule to the
+task as an ordinary requirement. The other rule should then be excluded, providing an anchor independent
+of E6's judges. Of 640 readings, one (a resolved item) failed. Both rules were accepted on 84.1\% [77.4,
+90.3] of readings of open units (E9-1, lower bound $>50$: supported). Rule A was excluded on 9.1\% of
+them against 96.5\% of readings of controls: a difference of 87.3 points [81.5, 92.5] (E9-2, $>30$:
+supported). On resolved items, the non-appended rule was excluded 55.0 points [47.5, 62.5] more often
+than on the same units without the requirement (E9-2b: supported). Claude accepted both rules on 96.3\%
+of open readings and GPT on 72.0\%. On resolved items, Claude excluded the non-appended rule in only
+25.9\% of readings against GPT's 98.8\%, making Claude the more permissive judge. The two rule orders
+gave the same judgement for 66 of 82 judge--unit pairs on open units (80.5\%). Each of the 425 exclusions
+included a quotation matching the task after normalisation (262) or an appeal to ordinary meaning (163).
+A matching quotation does not show that the words entail the exclusion. We reran the frozen E6 code on
+the 35 units that at least three of four readings accept. The registered criteria of E6-1, E6-2 and E6-5
+hold, and the flag preference stays positive. The estimates are resolved diagnosis 91.1\% [81.4, 98.2],
+E6-2 +11.1 [5.0, 17.5], E6-5 +79.3 [70.0, 87.9], flag preference +22.9 [10.0, 36.4]. The flag preference
+also stays positive on the 23 units all four readings accept (E6-2 +8.7 [3.3, 15.2], E6-5 +83.7 [72.8,
+92.4]). On units selected by one judge alone, the other vendor's auditors still show the convention
+advantage. For GPT-selected units, Claude auditors give +13.0 [5.4, 21.7]; for Claude-selected units, GPT
+auditors give +11.2 [5.3, 17.8]. On GPT-selected units, GPT's own auditors give +4.3 [0.0, 9.8]. These
+judges are models of the same vendors, and the subset analyses are conditional, not independent
+replications; E9 does not replace human validation.
+
+\paragraph{Does the sentence add more than pointing at the behaviour? (E10.)} We registered this study
+after the E6, E8 and E9 results were known and before any held-out E10 call, following a development
+pilot. On the 41 held-out open units, E6's two low-budget configurations read four arms afresh,
+interleaved within each construction attempt. The arms were the task alone, a \emph{pointer}, and the two
+sentence arms. The pointer read ``Additional note: pay particular attention to how the function handles
+the following kind of input: \dots''. It named the unit's input class in the constructor's words. A fixed
+rule removed any clause that said what was unspecified or named the alternatives. E6's frozen code
+handles scoring and analysis; the pointer reveals no contract and is scored under both. All 1{,}312
+readings are valid. Verified diagnosis is 12.2\% [7.3, 17.7] with the task alone, 31.1\% [23.8, 38.4]
+with the pointer and 91.5\% [82.9, 97.6] with the sentence. The sentence exceeds the pointer by 60.4
+points [51.8, 68.9] (E10-1, lower bound $>0$: supported). The difference is positive for each vendor (GPT
++59.8, Claude +61.0) and without the two exception-contract units (+62.2). The pointer adds 18.9 points
+[12.2, 26.2] over the task alone. Its upper limit exceeds the registered 20-point margin, so we do not
+claim that attention adds little. Pointing without a rule raises pooled recall and false-flag rate
+equally (from 14.0\% to 37.8\%, equal by construction). The rise is larger on program A (23.2\% to
+53.7\%) than on program B (4.9\% to 22.0\%). Pointing also widens the flag preference for the program
+that departs from the benchmark (+18.3 [6.1, 31.7] to +31.7 [12.2, 51.2]) and the convention advantage
+(+9.8 to +15.2). Directed to the behaviour but not told the rule, auditors apply the benchmark's
+convention more often. Among flagging readings, over 90\% name an in-class witness in every arm. This is
+conditional on flagging and does not show how often each arm finds the input. The fresh
+sentence-minus-task contrast, +79.3 [69.5, 87.2], replicates E6-5 (+76.8). The pointer is one attention
+control, phrased as a note rather than a requirement. The auditors are two of E6's configurations at the
+low budget.
 
 \subsection{Inputs, interface and red team}
 
@@ -152,18 +167,21 @@
 a model. Sensitivity analyses replace the domain predicate by the reference's own domain
 and credit witnesses outside the class.
 
-\paragraph{Exception contracts (exploratory, found after the held-out analysis).} The frozen scorer treats a
-witness on which the contract's oracle raises as outside the domain. Two held-out units have a rule A that requires
-an exception (MBPP 93: \texttt{ValueError} for zero to the power zero; MBPP 623: the same for a zero element with
-exponent zero), so under contract A their diagnosis is zero by construction, while contract B, the reference's
-behaviour, cannot be affected. The registered results are unchanged; a separate script
-(\texttt{e6\_exception\_sensitivity.py}) recomputes them. Excluding the two units gives 39 units, resolved
-diagnosis 93.3\% [84.6, 99.7] and E6-5 +78.8 [69.9, 86.5]. Crediting a flagging reading under contract A when one of
-its in-class witness calls makes the A oracle raise and the auditor's stated expectation names an exception (all 24 flagging readings
-with witnesses on these programs qualify) gives resolved diagnosis 93.6\% [86.0, 99.7] and E6-5 +79.3 [70.7, 86.6], the largest effect
-the asymmetry can have. Under recrediting, E6-2 (+11.6) and the flag preference (+23.8) are unchanged (11.5 and 23.7 without the two units), since no auditor flagged the
-contract-B program of these units in the unrevealed arm, and every registered verdict is the same under all three analyses.
-The frozen estimates therefore slightly understate verified diagnosis once the contract is stated.
+\paragraph{Exception contracts (exploratory, found after the held-out analysis).} The frozen scorer
+treats a witness on which the contract's oracle raises as outside the domain. Two held-out units have a
+rule A that requires an exception. These are MBPP 93 (\texttt{ValueError} for zero to the power zero) and
+MBPP 623 (the same for a zero element with exponent zero). Under contract A, their diagnosis is therefore
+zero by construction. Contract B, the reference's behaviour, cannot be affected. The registered results
+are unchanged; a separate script (\texttt{e6\_exception\_sensitivity.py}) recomputes them. Excluding the
+two units leaves 39 units, resolved diagnosis 93.3\% [84.6, 99.7] and E6-5 +78.8 [69.9, 86.5]. We
+recredit a flagging reading under contract A if one of its in-class witness calls makes the A oracle
+raise and the auditor's stated expectation names an exception. All 24 flagging readings with witnesses on
+these programs qualify. This gives resolved diagnosis 93.6\% [86.0, 99.7] and E6-5 +79.3 [70.7, 86.6],
+the largest effect the asymmetry can have. Under recrediting, E6-2 (+11.6) and the flag preference
+(+23.8) are unchanged (11.5 and 23.7 without the two units). This is because no auditor flagged the
+contract-B program of these units in the unrevealed arm. Every registered verdict is the same under all
+three analyses. The frozen estimates therefore slightly understate verified diagnosis once the contract
+is stated.
 
 \subsection{Statistics}
 
@@ -182,35 +200,39 @@
 required 12 held-out open units, so no audit was run. A provider outage during the first pass was handled as in E1
 Amendment 5: calls that never reached the model were archived and repeated.
 
-\paragraph{Data-science tasks by localised edits (E11).} Registered after E6 and E8--E10 were known and after E7's
-construction records had been seen; E11 reuses E7's corpus, split, hidden inputs, comparator and rule proposals, so it
-extends E7 with held-out audit outcomes rather than replicating it on unused tasks. Only the implementation stage
-changes: each implementing vendor receives the task, the reference with its docstring removed and one rule, and is
-asked to edit the reference minimally so that the inputs the rule concerns go through an explicit branch that follows
-it. Minimality is prompted, not enforced; equivalence outside the class is established, as in E6, by execution on the
-registered inputs, and edits change a median of 3.5 lines (maximum 12) of the reference; some also change code
-outside the branch. All other stages, the two
-judges, E6's second construction attempt and E7's gate of 12 units are E6's and E7's frozen code. A protocol freeze
-preceded held-out construction and a population freeze preceded any held-out audit. Funnel (held out), first attempt:
-88 proposals, 71 pre-admitted, 37 admitted, 17 past the red team, 12 past both judges; second attempt: 78 usable
-proposals, 67, 27, 10, 6. During the second attempt 81 proposal calls (69 tasks) exited with an error and no reply; under E6's rule
-(an exit without recorded usage) they did not reach the model, so they were archived and repeated with identical
-prompts (E11 amendment 1). The proposal records do not keep usage and no transport log was retained, so the
-classification rests on the exit status. Preliminary gate reports were 12 and 17; the final gate was evaluated after
-all eligible construction calls had completed.
-The 18 units come from 18 problems. Arms: the task alone, E10's note naming the input class, and E6's two sentence
-arms; GPT and Claude at the low budget, two readings per cell; 576 of 576 registered readings valid. Verified
-diagnosis: 8.3\% (task alone), 18.1\% (note), 66.7\% (sentence). E11-1, sentence minus task: +58.3 [41.7, 73.6];
-E11-2, sentence minus note: +48.6 [34.7, 62.5]; both supported, also for each vendor (GPT +55.6 and +41.7, Claude
-+61.1 and +55.6). No problem's effect is negative; the minimum leave-one-problem-out lower limits were 38.2 and 30.9
-points. The two-reading policy's sentence-arm false-flag rate was 26.4\% [11.1, 43.1] (betting upper bound
-46.0\%; 24.3\% of individual readings; 5 development units gave 25\%). Unregistered here: convention advantage +8.3 [2.8, 13.9] and flag preference
-+13.9 [$-$2.8, 30.6] with the task alone. E9's judges, prompt and code (E11-3, descriptive) accepted both rules on
-93.1\% [86.1, 98.6] of open readings and excluded the non-appended rule on 73.6\% of resolved readings (Claude 47.2\%,
-GPT 100\%); E11 has no positive controls, so E9's Disc is not estimable. On the 17 units accepted in at least three of four
-judge--order readings, E11-1 is +60.3 [42.6, 76.5] and E11-2 +50.0 [35.3, 64.7]; the code computing these subset
-contrasts (E9's own reads E6's results) was written after the held-out audits. The edited branches cue the relevant behaviour in every arm; the
-result is conditional on these constructed library tasks.
+\paragraph{Data-science tasks by localised edits (E11).} We registered the study after E6 and E8--E10
+were known and after seeing E7's construction records. E11 reuses E7's corpus, split, hidden inputs,
+comparator and rule proposals. It therefore extends E7 with held-out audit outcomes rather than
+replicating it on unused tasks. Only the implementation stage changes. Each implementing vendor receives
+the task, the reference with its docstring removed and one rule. We ask it to edit the reference
+minimally, routing inputs covered by the rule through an explicit branch that follows it. Minimality is
+prompted, not enforced. As in E6, execution on the registered inputs establishes equivalence outside the
+class. The edits change a median of 3.5 lines (maximum 12) of the reference; some also change code
+outside the branch. All other stages, the two judges, E6's second construction attempt and E7's gate of
+12 units use E6's and E7's frozen code. A protocol freeze preceded held-out construction and a population
+freeze preceded any held-out audit. Funnel (held out), first attempt: 88 proposals, 71 pre-admitted, 37
+admitted, 17 past the red team, 12 past both judges; second attempt: 78 usable proposals, 67, 27, 10, 6.
+During the second attempt, 81 proposal calls (69 tasks) exited with an error and no reply. Under E6's
+rule (an exit without recorded usage), they did not reach the model. They were therefore archived and
+repeated with identical prompts (E11 amendment 1). The proposal records do not keep usage and no
+transport log was retained, so the classification rests on the exit status. Preliminary gate reports were
+12 and 17; the final gate was evaluated after all eligible construction calls had completed. The 18 units
+come from 18 problems. The arms were the task alone, E10's note naming the input class, and E6's two
+sentence arms. GPT and Claude ran at the low budget, with two readings per cell; 576 of 576 registered
+readings were valid. Verified diagnosis was 8.3\% (task alone), 18.1\% (note), 66.7\% (sentence). E11-1,
+sentence minus task: +58.3 [41.7, 73.6]; E11-2, sentence minus note: +48.6 [34.7, 62.5]. Both are
+supported, also for each vendor (GPT +55.6 and +41.7, Claude +61.1 and +55.6). No problem's effect is
+negative; the minimum leave-one-problem-out lower limits were 38.2 and 30.9 points. The two-reading
+policy's sentence-arm false-flag rate was 26.4\% [11.1, 43.1] (betting upper bound 46.0\%; 24.3\% of
+individual readings; 5 development units gave 25\%). With the task alone, the convention advantage was
++8.3 [2.8, 13.9] and the flag preference +13.9 [$-$2.8, 30.6]; these are not registered here. E9's
+judges, prompt and code (E11-3, descriptive) accepted both rules on 93.1\% [86.1, 98.6] of open readings.
+They excluded the non-appended rule on 73.6\% of resolved readings (Claude 47.2\%, GPT 100\%); E11 has no
+positive controls, so E9's Disc is not estimable. On the 17 units accepted in at least three of four
+judge--order readings, E11-1 is +60.3 [42.6, 76.5] and E11-2 +50.0 [35.3, 64.7]. The code computing these
+subset contrasts (E9's own code reads E6's results) was written after the held-out audits. The edited
+branches cue the relevant behaviour in every arm; the result is conditional on these constructed library
+tasks.
 
 \subsection{Registered hypotheses and held-out verdicts}
 
```

Possible factual or logical issues, left unchanged:

- **E11, “they did not reach the model”:** exit status alone does not establish this; the following sentence acknowledges that usage and transport records are unavailable.
- **Exception contracts, “The frozen estimates therefore slightly understate verified diagnosis…”:** recrediting requires an expectation naming an exception, without explicitly requiring the correct exception type. Check whether this establishes verified diagnosis or only an upper-bound sensitivity estimate.