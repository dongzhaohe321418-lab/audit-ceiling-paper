Reviewed `77dbade`, the full manuscript, `fb400e3..77dbade`, all three earlier manuscript reviews, and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its ranking, residual labels, clarification adjudication and earlier reviews are conflicted. This review is independent of the author’s account, but **does not provide independent-family validation** of those results.

The principal repairs and calculations hold. Some qualifications still fail to propagate, and the fresh reading identifies a substantive misrepresentation of prior work.

1. **R4-1 — Major, new. The claimed gap in consensus-validation research is contradicted by both cited papers.**

   [related.tex:54](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:54) says neither paper supplies the quantity needed to assess these filters, “how many wrong assertions survive it.”

   **Contradicting sources:** ConVerTest explicitly measures validity among retained tests. Its Table II reports post-filter precision/validity of 84–91%, corresponding to 9–16% invalid retained tests. Its evaluation defines validity by execution against the ground-truth implementation. [ConVerTest, §IV-C and §V-B](https://arxiv.org/html/2602.10522v1#S5.SS2)

   CANDOR explicitly measures correct assertions divided by all assertions in the resulting suite. It reports oracle correctness of .910, .930 and .894 on correct-code benchmarks and evaluates the contribution of panel discussion. These quantities directly describe remaining incorrect oracles. [CANDOR, §4.3 and §5.2](https://arxiv.org/html/2506.02943v7#S5.SS2)

   Your experiment has a narrower, defensible distinction: its primary denominator is **retained failing test–candidate applications**, as [RESULTS-TESTGEN-VAL.md:25](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:25) specifies. That differs from retained tests or assertions. Explain that distinction and the registered 2% criterion; do not claim the cited work omitted residual-error evaluation.

2. **R4-2 — Moderate, residual R3-2. C15 is repaired, but the manuscript still assigns its simulation results directly to production intervals.**

   [results.tex:91](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:91) says the reported interval occupies a range “where that interval covers about 0.89.” [discussion.tex:102](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:102) likewise says the primary single-rate intervals’ coverage was measured.

   **Contradicting implementation:** [coverage_simulation.py:36](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/analysis/coverage_simulation.py:36) tests 600-resample, integer-index percentile intervals under an assumed correlation model. C15 now correctly disclaims validation of the analyses’ 10,000-resample interpolating implementation.

   There is also a parameter-versus-estimate distinction: .8875 is simulated coverage **at true rate .03**, not coverage established for an individual interval because its observed estimate is 3.3%. Report this as evidence of potential undercoverage from analogous simulations.

   The supporting [RESULTS-DERIVED.md:50](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-DERIVED.md:50) also retains “at true rates of 0.10 and above,” although C15 correctly restricts that statement to the five tested rates through .60.

   No new simulation is necessary to retain these useful results. Their actual scope needs to govern every description.

3. **R4-3 — Moderate, residual R3-5 and earlier causal-allocation concern. Sampling remains an asserted explanation in unrepaired locations.**

   [results.tex:53](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:53) attributes the same-vendor route’s small gain to its temperature setting. The Figure 1 caption at [line 72](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:72) concludes that its flatness “is a property of how it is sampled.” The heading at [discussion.tex:23](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:23) still says repeated reading buys coverage “only where the decision is marginal.”

   **Contradicting scope:** [RESULTS-SWEEP.md:163](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-SWEEP.md:163) says model identity and sampling configuration are not isolated. The repaired [discussion.tex:41](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/discussion.tex:41) correctly acknowledges that decision-boundary distance was never measured.

   The records establish little observed verdict variation **under this configuration**. They do not identify temperature’s contribution or establish marginality as the mechanism. Preserve the sampling confound and observed gains; make the caption and heading obey the repaired body text.

4. **R4-4 — Moderate, new. The generated-test comparator conclusion is stronger than the record permits.**

   [results.tex:325](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:325) says neither paid rule “beats the free within-draw comparator.”

   **Contradicting record:** [RESULTS-TESTGEN-VAL.md:33](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:33) gives A **11/90 = 12.2%**, versus C′ **11/86 = 12.8%**. A retains the same wrong applications and four additional correct applications, with identical retention of the seven designated instances. At [line 48](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:48), the report explicitly says the study cannot settle whether the extra draws improve on the free comparator.

   Failure of the absolute 2% requirement is established under the registered rule. Absence of comparative benefit is not. Say **superiority was not established**, while preserving A’s small observed advantage.

5. **R4-5 — Minor. The author’s additional rater-role correction leaves its opposite in the heading.**

   [results.tex:241](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:241) still introduces Luna as “A rater that audited nothing.” The following paragraph now correctly acknowledges its earlier audit role.

   **Contradicting record:** [PREREGISTRATION-explore.md:63](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/PREREGISTRATION-explore.md:63) identifies `cheap-cross` as Luna; [manifest.json:68](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/explore/manifest.json:68) records its audit draws. I also read the first draw’s 290 successful records.

   “Outside the families defining this residual” is supported. “Audited nothing” is not. This matters specifically to the claimed independence of the check.

6. **R4-6 — Minor, residual R3-6. The promised paired p-value reporting remains incomplete.**

   [results.tex:25](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:25) promises both McNemar and cluster sign-flip values wherever a p-value appears.

   The repaired pass-rate contrast now supplies both. But the pooled flag contrast at [line 185](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:185) still prints only \(3.0\times10^{-6}\).

   **Contradicting record:** [numbers.json:2218](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/records/code/ceiling/numbers.json:2218) gives McNemar **\(2.9802\times10^{-6}\)** and cluster sign-flip **\(1.0014\times10^{-5}\)**. Both clear the threshold; the conclusion does not change. The correct-stratum passage also names only McNemar, although both tests equal .015625 there.

7. **R4-7 — Minor, new. SWR-Bench’s aggregation is not the same operation as a Boolean union.**

   [related.tex:18](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:18) calls its multi-review strategy “the same mechanical move as our union-of-K.”

   **Contradicting source:** SWR-Bench uses an additional LLM call to synthesize the sampled reports. Your union counts an instance whenever any reading flags it. The sampling motivation is shared; the aggregation and resulting estimands differ. [SWR-Bench, Multi-Review description](https://arxiv.org/html/2509.01494v2)

The disposition of every round-3 finding is:

| Finding | Ruling at `77dbade` |
|---|---|
| **R3-1**, clarification mechanism | **Fixed.** The repaired passage identifies post-hoc classification and possible problem difficulty without withdrawing the observed intervention contrast. |
| **R3-2**, statistical scope | **Partly fixed.** C15, final Limitations, C3’s approximate unconditional interval and Monte Carlo errors are corrected. Remaining scope failures are R4-2. |
| **R3-3**, pooled flags versus FP constraint | **Fixed.** The introduction now uses the correct-stratum observed rate, 10/56 versus 3/56, and distinguishes it from uncertainty in the difference. |
| **R3-4**, “partly definitional” association | **Fixed.** The empirical +23.3-point contrast and its interval are restored without causal attribution. |
| **R3-5**, general resampling mechanism | **Partly fixed.** The proportional law is removed and diminishing increments are correctly identified as arithmetic. The heading and sampling attribution remain, R4-3. |
| **R3-6**, statistical reporting policy | **Partly fixed.** Multiplicity is now study-specific, and the cited pass-rate p-value is repaired. Other omissions remain, R4-6. |
| **R3-7**, C14 “pending” label | **Fixed**, including the generator and compiled table. |

The earlier findings round 3 left partial follow the same disposition. **R2-1**’s clarification mechanism is repaired, but the broader causal-allocation problem remains in the locations identified above. **R2-2/R1-8**’s coverage problem is partly repaired. **R1-1’s C15 admission scope is now satisfied by C15 itself.** The corrections round 3 accepted for R2-3 through R2-8 remain intact.

**C14 and C15 retain their scoped admission.** C14 supports a descriptive comparison, not population stability. C15 now faithfully states the tested rates, assumed correlation, 400 datasets, 600 resamples, integer-index percentiles and limits on transfer to other procedures. Its admission does not extend to the broader surviving manuscript statements.

Independent checks recovered:

- All fourteen committed coverage cells exactly.
- C14’s **68** consensus-undetermined instances, **25/32** remaining and **43** flagged.
- Clarification **0/32, 9/32, 0/32**, five informative problems, interval **[7.6852, 51.4286]**, 27 zero bootstrap resamples and exact cluster **\(p=.0625\)**.
- Adjudicator agreement **84/91**, **κ=.85203**.
- Table 1 byte-identically, and equality of all three figure/compiled-copy pairs.

The manuscript checker passes despite these findings. I did not run the file-writing reproduction script.

The paper offers useful descriptive evidence for evaluation researchers, especially its separation of flagging from diagnosis. The remaining problems do not justify dismissing those measurements or demanding an entirely new programme. They require accurate positioning and consistent limits on interpretation.

**not submittable — most importantly, the paper claims an evidential gap in consensus validation that its own cited prior work already addresses.**
