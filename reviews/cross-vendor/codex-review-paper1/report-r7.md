Reviewed `87c8db7`, the full manuscript, `18fe530..87c8db7`, the archived findings and supporting records. **No files modified.**

I share the measured `gpt-6-astra` family. My judgments about its comparative performance, residual labels, clarification adjudication and the effectiveness of earlier reviews are conflicted. This review checks the author’s account independently, but **does not provide independent-family validation** of those judgments.

The principal round-6 repairs hold. The remaining problem is an overcorrection in the interpretation of the generated-test results.

1. **R7-1 — Moderate, introduced by the R6-3 repair. One rule’s inconclusive interval is used to dismiss evidence concerning both rules.**

   [results.tex:334](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:334) now correctly reports the visible-passing population’s counts and intervals, but concludes that “no separate failure on that population is established” because the **first** interval contains zero and 2%. [CLAIMS.md:201](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:201) repeats that conclusion.

   **Contradicting record.** [RESULTS-TESTGEN-VAL.md:164](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-TESTGEN-VAL.md:164) distinguishes:

   | Rule | Visible-passing candidates | Problem-cluster interval |
   |---|---:|---:|
   | A | 6/33 = 18.2% | [0.0%, 44.8%] |
   | B | 10/43 = 23.3% | [6.8%, 47.1%] |

   I independently recovered both counts and intervals. **A’s interval leaves its relationship to 2% unresolved; B’s unadjusted exploratory interval lies entirely above 2%.** A’s uncertainty cannot erase B’s evidence.

   There are also two different meanings of “failure” here. The [registered kill rule:138](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/plan/studies/testgen-PREREGISTRATION-VAL.md:138) uses a **point estimate**, not exclusion of 2% by an interval, and applies to the registered mixed population. The visible-passing analysis is post hoc and cannot become a new confirmatory H17 decision.

   State these distinctions explicitly: A is unresolved against the threshold under its exploratory interval; B supplies exploratory evidence of exceeding it; neither analysis constitutes a separately preregistered product-population test. Round 6’s warning against promoting exploratory point estimates should not become a blanket withdrawal of the evidence now reported.

2. **R7-2 — Minor, newly identified. C8’s heading asserts absence of an effect that its own paragraph correctly leaves unresolved.**

   [CLAIMS.md:120](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/manuscript/CLAIMS.md:120) says the referent rule moves the family “and the grading rule does not.”

   **Contradicting record.** [RESULTS-CEILING3B.md:123](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/reports/RESULTS-CEILING3B.md:123) gives **+0.9 points [−1.8, +4.5]**, explicitly distinguishing no demonstrated improvement from no effect. The ledger’s following sentences and [results.tex:290](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/results.tex:290) already preserve that distinction.

   Change the heading to “the grading rule shows no demonstrated BLOCKER-recall improvement.” This is a local propagation error; the underlying result remains usable.

3. **R7-3 — Minor, newly identified. The self-assessment literature is summarized more categorically than the cited evidence permits.**

   [related.tex:31](/Users/ericdong/Documents/Crossaudit/audit-ceiling-paper/tex/sections/related.tex:31) introduces it as establishing that models are poor judges of their own output, with self-preference as one supporting direction.

   **Contradicting source scope.** Chen et al. explicitly distinguish legitimate preference for better outputs from harmful self-preference. They find stronger generators generally make better evaluators, while harmful self-preference persists particularly on instances they answer incorrectly. Preference for one’s own output alone therefore does not establish poor judgment. [Chen et al., abstract and §§3–4](https://arxiv.org/html/2504.03846v1)

   Describe the conditional failure mode. This correction does **not** remove this programme’s evaluator conflicts or validate its adjudications.

The disposition of every round-6 finding is:

| Finding | Ruling at `87c8db7` |
|---|---|
| **R6-1**, categorical interval undercoverage | **Fixed.** Methods and Limitations now describe potential undercoverage suggested by analogous simulations. |
| **R6-2**, matching allegedly requiring new calls | **Fixed substantively.** The claim is restricted to evaluated deterministic rules, and an unbuilt post-hoc randomized policy is acknowledged. |
| **R6-3**, missing product-population denominators and uncertainty | **Numbers fixed; interpretation overcorrected**, R7-1 above. |
| **R6-4**, retained recall interval’s provenance | **Fixed.** It is the complement of ceiling 1’s residual interval at seed **20260912**, imported by study 21. |
| **R6-5**, universal detector claim | **Fixed.** The statement now concerns the methods evaluated by Tan et al., consistent with their study. [Tan et al., §3](https://arxiv.org/html/2505.17656v2#S3) |

The remaining coverage issue inherited through **R5-2 → R4-2 → R3-2 → R2-2 → R1-8 is now closed**. All fourteen simulation cells reproduce, and the text no longer treats them as measured coverage of the production intervals. **C14 and C15 retain their scoped admission.**

I found no regression in the previously accepted pooled-cost, sampling-confound, recurrence, paid-comparator, Luna-role, paired-test or clarification-mechanism repairs. The fourth- and eighth-reading increments reproduce as **2.892857** and **1.931818** percentage points.

**Explicit ruling on `RESULTS-DERIVED.md`, section 3: QUOTABLE.** Its revised provenance and stated inferential scope faithfully preserve round 6’s ruling.

Using the archived readings through the harness loader, I recovered:

| Stratum | Pooled union | Newly computed cluster interval |
|---|---:|---:|
| Defective | **53/110 = 48.2%** | **[36.4%, 59.8%]** |
| Correct | **54/150 = 36.0%** | **[28.2%, 44.2%]** |

The computation matches the committed pooled record exactly. Separately, bootstrapping the residual at **20260912** recovers the retained recall interval **[36.7%, 60.0%]** by complementation. Both recall and its price may remain. Admission supports this **descriptive operating point**, without establishing superiority at matched cost.

Table 1 regenerates byte-identically in memory, all three figure copies match their manuscript copies, and the manuscript checker passes. I did not execute the file-writing reproduction script.

The paper retains a useful descriptive contribution about audit operating points and the distinction between flagging and diagnosis. I found no new computational defect in the quantities checked. The remaining corrections concern what those quantities permit the manuscript to say.

**not submittable — most importantly, the uncertainty repair now uses rule A’s inconclusive result to discount rule B’s distinct exploratory evidence on the product population.**
