The numerical result reproduces, and the replacement readings audit the correct candidates. **The report is not ready for quotation because the intervention is not consistently the addition of the hidden oracle’s missing rule.** Several additions instead contradict that rule.

I reviewed `38480a3` read-only. No files were modified.

**R1-M1 — Blocking. The causal interpretation misdescribes the manipulation.**

The [generator](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/generate.py:178) receives failing **inputs**, without their expected outputs. Its additions sometimes endorse the candidate’s wrong behavior or invent another rule. Examples from the frozen conditions and witnesses:

| Instance | Added rule implies | Hidden oracle expects |
|---|---|---|
| `b2:Mbpp/137`, all-zero array | `0.0` | `inf` |
| `b1:Mbpp/278`, tuple `(1,2,3,4,5,6)` | Count all elements, therefore `6` | `5` |
| `b1:Mbpp/102`, `___python_program` | Discard leading separators | Preserve them: `___PythonProgram` |
| `b2:Mbpp/559`, all-negative list | Greatest negative element | `0` |

These are verifiable contradictions, not merely an imprecisely measured increase in determinacy. I also executed the reference programs: all **84 displayed expected outputs** reproduce.

One successful instance, [`b2:Mbpp/597`](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/records/clarify/conditions.json:462), changes “two sorted arrays” into “arrays are not required to be sorted.” That broadens an explicit input precondition rather than settling something the original prose left open.

Consequently, the [closing interpretation](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/RESULTS-CLARIFY.md:85) and CLAIMS’ proposed “causal reading of C4” exceed what this intervention establishes. The registered numerical criterion can pass while this interpretation fails. The report needs to distinguish oracle-consistent additions, contradictory additions, and changes to existing requirements, without retrospectively replacing the primary population with favorable survivors.

The manipulation-check contrast **+18.8 points [−9.4, +45.2]** reproduces, but its uncertainty belongs beside the main interpretation. The assertion that the audit result “is not subject to that ambiguity” is defensible only for the observed diagnosis contrast. Zero placebo diagnoses do not validate the proposed mechanism.

**R1-M2 — Blocking for the blinding assurance. Neither the quotation metric nor its input extraction measures what the report says.**

In [`overlap()`](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/adjudication_sheet.py:56), `if w in fw` checks whether a word occurs anywhere in the finding. It checks neither ordering nor adjacency and also permits substring matches. An added sentence `alpha beta gamma delta epsilon` scores **1.0** against the reversed finding `epsilon delta gamma beta alpha`.

There is a second defect. `added_sentences()` includes unchanged visible assertions in the supposed addition for **21/31 clarified specifications**, because an appended sentence becomes attached to the original’s final, unpunctuated assertion. That contaminates both metrics’ denominators.

Thus:

- **4/83** reproduces the implemented function, but does not mean four contiguous quotations.
- The archived vocabulary count is **11/83**, omitted from the report.
- As a diagnostic recomputation, removing the original lines before measuring actual additions gives **39/83** above the vocabulary threshold and **1/83** above the contiguous-match threshold, using the existing content-word convention.

Those replacement counts are not proof of leakage either. They demonstrate that the published measurement is wrong. The heading “The clarification is not being read back” is unsupported; lexical overlap cannot exclude paraphrase or establish successful blinding.

**R1-M3 — The candidate repair works on the retained run, but its additional exclusion is falsely attributed to hidden-test leakage.**

All **31 candidates exactly match their frozen batch solutions**. Across all **372 successful readings**, I independently reconstructed the complete prompts and matched their archived hashes. Candidate and visible-suite bytes are constant across conditions; each condition’s full specification reaches the prompt. All **84 displayed actual outputs** reproduce, and all **87 sheet items** match their keyed candidate, witness, and finding. There are four failed attempts, followed by successful replacements, with no missing or duplicate successful cells.

The void archive contains **384 successful readings**, all matching canonical candidates and none matching the corresponding frozen batch candidate. The new source-identity check therefore closes the actual defect for this run. Its broader claim that different programs cannot reproduce the same outputs is false; finite witness agreement establishes consistency, while the frozen-source comparison establishes identity.

However, the [repair record](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/records/clarify/conditions.json:2) drops `b1:Mbpp/427` for three allegedly hidden assertions. All three already occur in the original specification and visible tests. They enter `hidden_program` through the replacement candidate’s embedded tests. The [gate](/Users/ericdong/Documents/Crossaudit/crossaudit_integ/benchmarks/code/clarify/gates.py:72) scans the whole assembled program and mistakes those public assertions for hidden leakage.

The 31-instance result remains reproducible, but this exclusion’s explanation needs correction and its population consequence needs explicit resolution. The manipulation check concerns **32 instances/19 problems**, not the final **31/18**.

**R1-M4 — Required registered reporting is missing.**

[Amendment 2](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/P3-PREREGISTRATION.md:256) requires the consensus-undetermined secondary beside the primary, “always.” It is absent from both the report and `h3.json`.

Intersecting that registered subgroup with the retained population gives **22 instances on 14 problems**:

- Original **0/22**, clarified **8/22**, placebo **0/22**.
- Clarified minus original **+36.4 points**, problem-cluster interval **[+12.0, +63.6]**.

Its direction agrees with the primary; omission is still a registration departure. Amendment 9 also requires the generation-run yields together: **25/44, 29/44, 32/44**, followed by the repair’s **31**.

The central arithmetic otherwise checks out:

| Quantity | Independent result |
|---|---:|
| Correct diagnosis, original / clarified / placebo | **0/31 / 9/31 / 0/31** |
| Clarified minus original | **+29.0323 points** |
| Problem-cluster bootstrap, 10,000 draws, seed `20260921` | **[+9.0909, +51.7241]** |
| Exact McNemar | **0.00390625** |
| Problem-level sign-flip, 10,000 draws | **0.06149385** |
| Agreement | **80/87**, κ **0.84420568** |

The Wilson intervals also reproduce. Placebo-minus-original is zero with both p-values equal to one; clarified-minus-placebo reproduces the primary contrast.

The sign-flip correctly flips **per problem**, not per instance. The nine successes occupy `391`, `556`, `559`, `576`, and `597`, with counts **2,2,2,2,1**. Exact enumeration gives **0.0625**; the reported **0.0615** is its seeded Monte Carlo estimate. The explanation of the McNemar discrepancy is substantively correct. I would not invent a new significance requirement to overturn the registered bootstrap criterion.

The ladder is genuinely flat under the recorded adjudication: nine clarified instances have flags **1111**, the other 22 have **0000**, and both other arms are entirely zero. Exact subset averaging does not manufacture this result. “Whatever this auditor does … it does on the first reading” should nevertheless be restricted to these observed draws.

The adjudication correctly requires both raters’ `yes`. Its contingency counts are **46 yes/yes, 34 no/no, three yes/no, and four no/cannot-tell**. The author-independence disclosure is adequate and matches the amended registration. Some item judgments deserve qualification: `P0001` accepts a docstring-only complaint where three closely equivalent findings are rejected by L2; `P0052` contains a false subsequence example. Other jointly accepted findings preserve the affected instance/draw diagnoses, so these observations do not overturn 9/31.

Two smaller corrections matter:

- The registration’s claimed absence of repeatability evidence is overstated. Its manipulation sheet contains **13 exact duplicate original specifications**, with agreement on **12/13**. `M004` and `M051` disagree on identical `Mbpp/391` prose. This measures repeatability on originals, not accuracy or repeatability on edited arms.
- **$3.94** is cumulative recorded audit spending, including the void run. The replacement readings cost **$1.747908**. Amendment 13’s commit precedes those replacement calls; I found no chronology contradiction in the examined history.

Validation used independent in-memory recomputation and the read-only candidate, specification-routing, gate, and overlap proof programs. Their existing tests pass, including the overlap proof that fails to detect the metric defect. I did not run the full application suite.

**not quotable — the intervention frequently adds rules that contradict the hidden oracle, so the reproduced diagnosis increase does not establish the report’s claimed causal mechanism.**
