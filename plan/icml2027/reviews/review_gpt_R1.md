I found several substantive reporting errors, although **`numbers.tex` exactly matches regenerated output from the final E6/E1 JSON files**. No files were changed.

References below use manuscript filenames under `audit-ceiling-paper/tex` and the supplied harness filenames.

**1. Numerical, factual and registered-verdict mismatches**

- **E6-2 is described at twice its registered scale.** `sections/introduction_v2.tex:32–33` and `sections/e6.tex:93` describe **11.6 points** as the difference between diagnosis rates. The registered estimand is **half that difference**, `(r_B − r_A)/2`. The full difference is **23.2 points [10.4, 36.0]**. The macro is correct; its verbal interpretation is not. Source: `PREREGISTRATION-E6.md:199–200`.

- **“Neither flags” is false.** `sections/e6.tex:106`: GPT blocks **7/164 low-budget readings and 2/164 high-budget readings**, or **9/328 overall**; Claude blocks none. Zero verified diagnosis is not zero flagging. Source: `e6_results_v4_test.json:1596–1619`.

- **The OPEN-subgroup conclusion uses the wrong denominator.** `sections/natural.tex:46–48`: **17/19** diagnosed programs overall have a determined witness, but among diagnosed **OPEN** programs this is **2/4**, not “usually”. Source: `e1_taxonomy_test.json:289–312`.

- **The introduction attaches the resolved-arm false-flag rate to the sentence intervention.** `sections/introduction_v2.tex:37–39` juxtaposes the sentence gain with **2.1%** false flags. That rate pools the four **resolve** configurations; the two low-budget **sentence** configurations have **0%** observed false flags. Identify the arm explicitly. Source: `e6_results_v4_test.json:622`.

- **E3’s held-out sample size is understated.** `sections/transfer.tex:33`: there are **266 faulty plus 266 clean items**, hence **532 total**, not 266 total. Source: `icml_e3/e3_results_test.json:3–4`.

- **E3’s comparator is misidentified.** `sections/transfer.tex:34–35,41–42` attributes the **+2.3-point** gain to a validator derived mechanically from the card. It is the **profile validator**, which additionally uses a clean reference sample and distributional thresholds. Against the card-only validator, the reported gain is **23.3 points [13.2, 33.3]**. Source: `PREREGISTRATION-E3.md:19,27–34`; `e3_results_test.json`, `card_instead`.

- **The admission description differs from the final protocol.** `sections/e6.tex:29–33` restricts agreement checks to “valid” inputs and says every stage is attempted once. Final admission checks interface-conforming inputs on which the reference runs **whether or not `valid` accepts them**; red-teaming permits a conditional second call. Source: `PREREGISTRATION-E6.md:63–77`.

- **The verification limitation misstates scoring.** `sections/discussion_v3.tex:30–31` says verified diagnosis requires a witness “two judges accept”. E6 witness credit is executable scoring; the two models adjudicate contract compatibility. E1 witness classification is a separate descriptive analysis. This also contradicts `appendix/e6_protocol.tex:108–112`.

The **ordered E6 family is correctly reported**: E6-1 → E6-2 → E6-5 are claimed; E6-3 is inconclusive; E6-1b fails its compliance criterion but does not gate that family; E6-4 is separate. E1 H4 also formally passes its registered rule—the concern below is its interpretation, not a misreported Boolean verdict.

**2. Overclaims**

- **Inconclusive H6 becomes a null conclusion.** `sections/natural.tex:43–45`: “does not predict” exceeds **+6.0 points [−20.2, 28.3]**. This interval permits substantial differences in either direction.

- **“The placebo does nothing” overstates H4.** `sections/natural.tex:58`: its bootstrap interval collapses to **[0,0]** across only seven problems. The registered sensitivity reports an exact upper bound of **34.8%**, which is omitted. Preserve the formal H4 verdict while reporting its fragility. Sources: `e1_results_test.json:33–39`; `PREREGISTRATION-E1.md:269–272`.

- **E8 does not establish “little selectivity” against its registered threshold.** `sections/discussion_v3.tex:37–38`: selectivity is **16.8 points [10.5, 23.2]**—above zero, but unresolved relative to the registered **20-point** substantial-selectivity threshold. The appendix gives the interval but omits that threshold interpretation. Sources: `PREREGISTRATION-E8.md:25–27`; `e8_results_test.json:98–104`.

- **“Neither the full table nor tool use helped” is unsupported as a general null.** `sections/transfer.tex:36`: the tool/configuration contrast is **+1.3 [−2.7, 5.8]**, not an equivalence result. The 12,000-row analysis tests incremental model value on that subset, not the causal effect of providing more rows. Sources: `PREREGISTRATION-E3.md:62–65`; `e3_results_test.json:26–38`.

- **The natural analysis cannot estimate an information-limited share.** `sections/natural.tex:5–6,10,48–50` and `sections/framework.tex:70–71` imply such a decomposition. First-failure classifications do not establish whole-program indistinguishability; disputed labels are not evidence of ambiguity. This conflicts with the appropriate qualification at `framework.tex:79–82`.

- **The capacity/information dichotomy is mathematically too strong.** `sections/framework.tex:41–45`: distinguishability does not imply every miss is reducible at the same false-positive rate. An optimal likelihood-ratio test can still miss cases when distributions overlap. Capacity loss should mean a gap below the attainable ROC, not every miss outside an identical-distribution component.

- **“Default reading” is stronger than the behavioural evidence.** `paper_v3.tex:64–65`, `sections/introduction_v2.tex:34–36`, and `sections/discussion_v3.tex:4–6`: agreement may reflect benchmark memorisation or shared model conventions, as `e6.tex:94–95` acknowledges. Held-out behavioural agreement is **89.1%**, versus **98.4%** on development—not an independently established natural interpretation.

- **Mechanistic attribution exceeds the controls.** `sections/e6.tex:82–84,108–111`: the menu is a strong uncertainty cue, and positive controls are conspicuous misreadings, not difficulty-matched cases. These support the specific intervention effects; they do not eliminate all prompting, attention or difficulty explanations. These limitations were registered at `PREREGISTRATION-E6.md:247–248`.

**3. Missing or misleading disclosures**

- **Separate pooled descriptive data from held-out data.** `sections/natural.tex:14–15,20–22`: the 150-item summaries combine **43 development and 107 test items**. Held-out taxonomy counts are **26 determined, 21 open, 22 at odds, 13 out of domain and 25 disputed**. Report held-out agreement too: **κ = 0.714**, rather than only development κ = 0.78. Source: `e1_taxonomy_test.json:3–30`.

- **The behavioural check reuses the selected generation pool.** `sections/natural.tex:19–27,36` and `sections/framework.tex:80` call these “other”, “independent” solutions or “independent programmers”. They are existing E1 generations, including the selected failing solution itself—not fresh independent validation. The 150 items cover **97 problems**, reusing solutions across items; the item-level bootstrap ignores that clustering. Sources: `icml/e1.py:1421–1452`; `figures/make_fig_natural.py:31–40`.

- **Disclose construction–judging role overlap explicitly.** `sections/e6.tex:20–40` distinguishes judges from proposers/auditors but omits that **the judges also implement the contracts**; Claude supplies probes, and GPT supplies red-team inputs. Separate calls and vendor diversity do not establish independent semantic validation. Source: `PREREGISTRATION-E6.md:39–43,74,244–248`.

- **Report the concentrated and highly selected population.** `sections/e6.tex:74–76`: the 41 primary units comprise **37 MBPP and four HumanEval problems**. Only **two** units have task-only solutions exhibiting both rules. These materially qualify generalisation beyond model-compatible alternative contracts. Source: `e6_results_v4_test.json:1246–1290`.

- **The protocol history omits amendments made during held-out execution.** `appendix/e6_protocol.tex:124–134` should disclose E1 Amendments 5–6, also applied to E6: revised attempt accounting and the **10-second → 60-second reference-timeout rule**, followed by no credit if timeout persists. Distinguish changes made before outcome analysis from changes made before any held-out call. Source: `PREREGISTRATION-E1.md:288–315`.

- **E3’s contamination history is materially compressed into a “pilot”.** `sections/transfer.tex:37–39`: earlier production runs included held-out readings, some accessed clean source files, and **test results had been analysed before Amendment 3**. The required side-by-side Amendment-2 results are absent from the included appendix. This also qualifies “All held-out analyses were preregistered” at `paper_v3.tex:69`. Source: `PREREGISTRATION-E3.md:118–146`.

- **Keep endpoint qualifications beside transfer claims.** `sections/transfer.tex:25–29` gives 23/25 fabrication flags, but only **21** had sound fault-related findings, assessed post hoc. `sections/natural.tex:59` calls H2 controls “correct programs”, although registration explicitly calls them **test-passing controls**. Sources: `appendix/ai4s_full.tex:97–101`; `PREREGISTRATION-E1.md:191–194`.

**4. Three principal acceptance weaknesses and feasible six-week fixes**

1. **Semantic validity lacks an independent anchor.** The main population and natural taxonomy depend on overlapping model roles.  
   **Fix:** obtain blinded ratings from two independent programmers for all 41 E6 units, matched controls and a stratified natural-failure sample; adjudicate disagreements; report sensitivity to human-supported labels. Keep original registered analyses intact.

2. **The bridge from an imposed information limit to real auditing remains unproven.** The theorem is classical, unrevealed equality is constructed, and H6 is inconclusive.  
   **Fix:** preregister a fresh, modest cohort of unfamiliar or repository-level tasks with author-confirmed contracts. Compare task-only auditing, auditor-generated clarification, author answers and direct specification disclosure; include difficulty-matched determined controls. Measure verified diagnoses and false flags together.

3. **Statistical interpretation and provenance are not yet reliable enough.** Null overinterpretation, collapsed intervals, reused behavioural samples and incompletely disclosed reruns weaken confidence.  
   **Fix:** produce one claim-to-estimand/verdict table; automate checks of prose values and arm labels; report registered sensitivities and amendment timelines; use problem-clustered behavioural analyses. Design any fresh confirmation around precision for the false-flag and equivalence targets, without changing the completed studies’ margins.

