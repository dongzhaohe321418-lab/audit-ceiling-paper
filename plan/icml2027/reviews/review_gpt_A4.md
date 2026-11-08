**No. The test split should remain closed.** The implementation is substantially improved, but semantic admission, control validity, H6 interpretation and completeness checks still require changes.

This review covered all **38 admitted constructions**, all **150 taxonomy items with both classification reasons**, and all development records. All **236 construction cases** replayed successfully. There are **904 valid development readings and no test readings**.

The code changed externally during review. References below use the final inspected commit **`e1c89af`**, including `judge-v3.1`. Its `None` fix and development rescoring are acknowledged below; they are not outstanding blockers. Paths are relative to `benchmarks/code/`.

**Status of the seven A3 blockers**

| A3 blocker | Assessment under the inspected code |
|---|---|
| 1. Contradictions and reference quirks admitted | **Partly fixed.** Stronger instructions and dual approval exist at `icml/e1.py:540–586,763–841`, but problematic admissions remain. See B1. |
| 2. Placebo cannot distinguish information from diagnostic prompting | **Partly fixed.** The constructor omits candidate code/output (`e1.py:717–719`), and H5 exists (`analyse_e1.py:127`). It still sees the selected failing input and reference output. Several controls are not demonstrably non-resolving. See B2. |
| 3. Incorrect ground-truth comparison | **Main comparator repairs work; error handling remains defective.** Original assertions/tolerances are preserved (`e1.py:241–285`); fresh argument copies and fixed hash seed are implemented. `judge-v3.1` fixes expected `None`. Comparator exceptions and result framing remain problematic. See B4. |
| 4. Lost argument types and inadequately checked controls | **Principal repair implemented.** Literal tuples, control agreement and output variation are checked at `e1.py:663–705`. All admitted cases reproduce; the previously defective Terra Mbpp/223 control is no longer admitted. However, `type_sig` examines only the first container element, to limited depth (`619–660`), and is a type proxy rather than semantic domain validation. |
| 5. Incorrect missing-data rule | **Arithmetic fixed.** Valid-reading unions, complete-subset O2 averaging and available-auditor pooling match Amendment 2 (`analyse_e1.py:51–84`). Effective reading/auditor counts by contrast still need explicit reporting. |
| 6. Incomplete or stale scoring silently becomes negative | **Partly fixed.** Current witness hashes and infrastructure exclusion work (`e1.py:1059–1083`), but schedule completeness can be bypassed and important cache dependencies remain unhashed. See B5. |
| 7. Missing secondary analyses | **H1–H5 repaired** (`analyse_e1.py:157–198`), with the E2 interpretation explicitly narrowed. Amendment 3 introduces another incomplete secondary matrix (`265–270`). See B6. |

**(a) BLOCKERS before test audits**

**B1. Semantic admission remains inconsistent, including clear reference quirks.**

Seven admitted items receive unanimous subsequent taxonomy judgements of **DETERMINED** or **AT_ODDS**. This is not automatically grounds for exclusion, since taxonomy concerns a particular failure, but these cases directly challenge the intended intervention.

Here, **H** means `gen-claude-haiku45` and **T** means `gen-gpt-terra`.

| Admitted item | Concern |
|---|---|
| **H and T · Mbpp/294** | The clauses exclude floats from “maximum value”. Returning `False` rather than the available `7.5` codifies the reference’s integer filter. Both taxonomy judges subsequently classify both items AT_ODDS. |
| **T · Mbpp/410** | The corresponding integer-only minimum rule excludes `2.5` and returns `5`. The task does not impose that restriction. Both taxonomy judges say AT_ODDS. |
| **H · Mbpp/759** | Rejecting `"-123.11"` adds an unsigned-only restriction to checking a decimal number with precision two. Both taxonomy judges identify this as a reference-pattern quirk. |
| **H · HumanEval/86** | The clause substantially restates the explicit space-delimited, ASCII-ordering reading. Both taxonomy judges subsequently call the behaviour DETERMINED. The admission’s alternative reading needs a consistent justification. |
| **H · HumanEval/125** | Admission permits empty strings in a “list of words”; both taxonomy judges subsequently reject that interpretation. This is a material unresolved semantic judgement, not clean evidence of missing information. |
| **H · Mbpp/99** | The selected candidate returns `"b101"` for `-5`. That is already invalid binary output. Detecting this defect does not require choosing between legitimate negative-number representation conventions. |

**Concrete fix:** archive the existing decisions and conduct one consistent, audit-outcome-blind semantic reconciliation. Reject the integer-filter and signed-decimal quirks unless a defensible specification basis can be established. For every retained item, document two genuinely permissible behaviours and explain why the intervention resolves their difference. Distinguish a novel clause from a defect that already violates the original task.

The disputed admissions **H·Mbpp/558, T·Mbpp/576 and T·Mbpp/780** also need explicit resolutions. Do not silently remove them merely because the taxonomy disagrees.

**B2. Some placebos and pointers change the permitted behaviour; H5 therefore needs a narrower interpretation or revised materials.**

The strongest placebo counterexample is **H·Mbpp/125**, `constructions_v3.jsonl:21`.

- Its first failure is empty input, reference `0`, candidate `-inf`.
- Both taxonomy judges call those outputs permissible under the original task.
- Its placebo requires the function to return **“a single integer”**.

That placebo excludes `-inf`. Either `-inf` was already impermissible, undermining the OPEN classification, or the placebo supplies consequential behavioural information. Both claims cannot stand.

Related concerns:

- **H·Mbpp/433** and **H·Mbpp/445** have placebos promising Boolean/tuple results, while their adjudication accepts exceptions as alternative original-task behaviours.
- **H·HumanEval/86** has a placebo reminding the auditor that ordering applies to letters, digits and punctuation. This is related behavioural guidance, although less serious than the Mbpp/125 contradiction.
- **T·Mbpp/780:** the pointer explicitly admits tuples longer than two elements. Combined with the task’s tuple-summing requirement, this strongly implies retaining and summing the additional coordinates.
- **H·Mbpp/433 and /445:** pointers admitting empty arrays or unequal tuple lengths narrow the domain-based justification for accepting exceptions. They are not merely attention cues under the admission’s own reasoning.

**What H5 identifies:** a contrast between these particular clause and pointer texts. It does **not**, without additional assumptions, isolate a pure effect of behavioural information holding attention constant. The texts differ in diagnostic specificity, domain commitments and how directly they suggest a witness.

**Concrete fix:** replace non-neutral placebos; reconcile domain assumptions; and ensure both clause and pointer arms share the same explicit domain statement and input-class wording. Independently verify that the pointer preserves the relevant alternative behaviours. Freeze the interpretation as **“benefit beyond the specified pointer control”**, rather than a general identification of information beyond attention.

The constructor is candidate-code-blind, but remains **failure-informed**. Amendment 2 correctly acknowledges this.

**B3. The taxonomy is not yet suitable for the proposed interpretation of H6.**

Reading all 150 items exposed several concrete problems.

1. **Comparator-irrelevant ordering is mistaken for the failure.**  
   **H·Mbpp/579** (`taxonomy_v3.jsonl:115,118`) and **H·Mbpp/769** (`:156–157`) are unanimously AT_ODDS because reference ordering is arbitrary. Their candidates actually raise `TypeError`, and both benchmark helpers compare **sets**. Ordering does not explain the observed failure.

2. **OPEN mixes in-domain ambiguity with violated input conditions.**  
   **H·Mbpp/597** uses an unsorted array despite “sorted arrays”; **H·Mbpp/622** uses unequal lengths despite “same size”. Both generators’ **Mbpp/785** cases use malformed tuple strings. These are different from genuinely unspecified duplicate handling or signed-versus-absolute differences.

3. **The three definitions are not exhaustive or cleanly exclusive.**  
   A candidate can be unquestionably wrong while the task permits several correct outputs. **T·Mbpp/564**, whose candidate returns a negative pair count, illustrates the difficulty. “Reference implementation artefact” also overlaps with unconstrained out-of-domain behaviour.

4. **Identical evidence receives different final classes.**  
   Identical taxonomy prompt hashes produce different generator-specific classifications for **Mbpp/119, /311, /468 and /771**. For **Mbpp/468**, the DETERMINED rationale also overlooks visible-test evidence favouring contiguous increasing runs over arbitrary subsequences.

5. **H6 labels one failure but credits any discrepancy.**  
   Taxonomy uses the first failing input (`e1.py:885–889`); diagnosis can credit any witness (`1033–1056`). For example, **H·HumanEval/91** is AT_ODDS on `is_bored("I")`, while credited original-arm witnesses concern `is_bored("I'm bored")`. The endpoint need not measure the classified behavioural distinction.

**Concrete fix:** separate domain validity from determinacy; provide comparator semantics and explicit exception status; establish canonical decisions for identical evidence; and resolve ambiguous/conflicting specifications under a frozen rule.

Then choose, before test audits:

- retain H6 explicitly as a **programme-level observational association with first-failure labels**; or
- add independently assessed witness-to-classified-failure correspondence to measure detection of the classified defect.

H6 is mathematically computable now. It is not yet a clean test of an information-limited recall ceiling.

**B4. Finish the judge’s failure handling before freezing it.**

Two executable failures remain.

- **Result framing crashes on legitimate content**, `e1.py:270–273`:

  ```python
  judge_witness(
      p_for_Mbpp_465,
      selected_haiku_defective,
      'drop_empty({"JUDGE ": 0})',
      '{"JUDGE ": 0}',
  )
  # Uncaught JSONDecodeError
  ```

  `rfind("JUDGE ")` selects the marker inside the result’s JSON string.

  **Fix:** use a dedicated framed result channel/line and convert malformed transport into an explicit infrastructure result.

- **Every comparator exception becomes disagreement**, `e1.py:219–224,1053–1056`. A helper raising `RuntimeError` on equal outputs produces `agree=False`. Equal NumPy arrays also produce false agreement because the benchmark helper raises an ambiguous-truth `ValueError`.

  **Fix:** distinguish ordinary assertion rejection, unsupported-output rejection and unexpected comparator failure. Preserve the benchmark’s intentional semantics, but do not silently call helper failures output disagreements. Bound comparator execution as well as function execution.

These are prospective robustness failures. Neither explains an observed change in the admitted development scores.

**B5. Completeness and provenance are still insufficient.**

`e1.py:1098–1099` loads only schedule files that exist. Consequently, on the actual unaudited test split:

```python
completeness("test")
# {"scheduled": 0, "valid": 0, "missing": []}
```

More seriously, an in-memory simulation omitting the original-only development schedule accepted **360/360** readings and produced **H6 +100 [100,100]** from the admitted subset. The complete development result is **+66.67 [33.33,100]**.

**Concrete fix:** reconstruct and verify the exact required key universe, rather than trusting existing schedules. Require complete taxonomy coverage and reject missing schedules, duplicate/unexpected keys and mismatched prompt hashes. Under the current population, test coverage should be:

- **1,160** intervention readings;
- **1,248** original-only readings;
- **2,408 total**.

Witness keys bind the scorer-version string, solution, reference and witness text (`1059–1061`), but not the comparator/helper/tolerance bytes or scorer implementation automatically. Hash those dependencies, or enforce them through a verified immutable manifest.

The promised **checksummed pre-test bundle still does not exist**. The latest commit contains the revised scorer, development summaries and witness records, but construction/adjudication/taxonomy inputs remain untracked, and both test schedules are absent. Freeze and verify the complete bundle before any test call.

**B6. Complete the newly registered analysis outputs.**

`analyse_e1.py:265–270` implements only part of Amendment 3’s natural secondary matrix. Missing combinations include flag DETERMINED-minus-AT_ODDS and the corresponding per-auditor contrasts.

**Concrete fix:** enumerate and implement the exact H6 matrix before seeing test outcomes. Add effective reading, auditor, item and problem counts for each contrast. Require two successful taxonomy classifications per selected item; currently `analyse_e1.py:236` silently removes items absent from the taxonomy.

The quantiles are correct for the registered settings. The general bootstrap function’s `int` versus `ceil` upper-rank discrepancy does not affect fixed `B=10,000`.

**B7. Freeze a defensible precision and claim plan for the small sample.**

The intervention sample is **29 items across 22 problems**, not 29 independent problems. It contains **13 reference controls and 16 generated controls**.

This can support a narrow study of large effects in a selected population. It is weak support for broad ceiling claims, ±5-point equivalence, reassurance under the +10-point H2 margin, or generator-specific conclusions.

There is also a concrete boundary problem: the current percentile bootstrap returns **[0,0]** when all sampled contrasts are zero. That mechanically satisfies H2/H4 without accounting for unseen discordant cases. For perspective, even a simplified calculation with 22 independent binary clusters and zero events has a one-sided 95% upper event-probability bound of **12.7%**. That is illustrative, not a substitute interval for the actual weighted contrast.

**Concrete fix before test:** register prospective precision/power simulations using the actual cluster structure, and add a defensible boundary-sensitive interval or sensitivity decision rule for H2/H4. Preserve the original analysis transparently.

Additional independent eligible problems should be obtained **now**, through an explicitly frozen extension, if precise margin claims are central. Otherwise retain the 29-item sample and narrow the claims beforehand. More readings or more candidates from the same problems do not provide equivalent independent information.

**(b) Disclosures and reassuring findings**

- **Execution:** all 236 construction cases reproduced, with control agreement and separation retained. Mutable arguments were independently deserialised; nested tuples survived; Mbpp/233 tolerance and Mbpp/579 order-insensitive comparison worked.
- **Judge stress tests:** large outputs were compared in full despite truncated displays. A generator worked under the set comparator; exceptions during generator consumption were collapsed into comparison rejection. No selected reference contains `yield`, and no selected programme uses NumPy.
- **The original `None` bug is fixed:** current scoring correctly credits legitimate `None` expectations. External rescoring appended 214 `judge-v3.1` records; development results were unchanged.
- **Development completeness:** 906 attempts yielded 904 valid readings; two malformed replies succeeded on retry. Both saved analysis JSON files reproduce exactly.
- **Blinding:** all construction, adjudication and taxonomy prompt hashes reproduced. Taxonomy prompts contain neither programme text nor audit outcomes. Classification records do not retain raw route transcripts, limiting independent verification of runtime isolation.
- **Raw audit provenance:** Codex event streams are present; no recognised tool-call events were found in the 452 Codex development attempts.
- **Development results remain pilot evidence:**

  | Contrast | Estimate, percentage points | 95% interval |
  |---|---:|---:|
  | H1 | +77.78 | [50.00, 100.00] |
  | H2 | +5.56 | [0.00, 18.75] |
  | H3 | +88.89 | [62.50, 100.00] |
  | H4 | +12.04 | [0.00, 30.77] |
  | H5 | +44.44 | [16.67, 72.22] |

  H2 and H4 do not meet their criteria. This neither proves harm nor proves non-equivalence. Keep the registered margins.

- The admitted test population currently contains **19 OPEN, two DETERMINED, four AT_ODDS and four DISPUTED** items. Report the full funnel and every pre-test correction.
- H2 measures flags on test-passing controls, not known-correct-programme false positives. H3 is not an equal-total-cost comparison. H6 is observational. Four readings do not establish an asymptotic recall ceiling.

**(c) Verdict: no test audits yet.** Resolve semantic admission and control neutrality, freeze H6’s target, repair judge/completeness handling, complete the analysis contract, and commit the verified pre-test bundle. The development arithmetic is credible; the intended scientific interpretation is not yet secure.

