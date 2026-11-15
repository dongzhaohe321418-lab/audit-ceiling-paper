**I retain 7/10.** The framing is clearer, and E15’s negative registered verdict is reported honestly. E15 does not resolve the remaining implementation-form concern. No files changed.

**A. E15 verification**

I reproduced the estimates from the 1,152 recorded readings, checked their prompt hashes against the freeze, and verified construction and programme hashes.

| Quantity | Verified result, percentage points |
|---|---:|
| Construction; valid readings | 36/41 units; 1,152/1,152 |
| Complete-case preference | +34.0 [18.8, 48.6] |
| Registered worst-case analysis, n=41 | **+17.7 [−1.2, 36.0]: not supported** |
| Fresh original A−B preference | **+25.7 [11.8, 39.6]** |
| More-conditionals stratum, 18/20 units | +47.2 [30.6, 65.3] |
| Other stratum, 18/21 units | +20.8 [−1.4, 43.1] |
| Body lengths | 29 equal; A longer in six |

Corrections in [appendix/e6_protocol.tex](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/tex/appendix/e6_protocol.tex:237>):

| File:line | Finding and exact correction |
|---|---|
| `appendix/e6_protocol.tex:245` | **Numerical error:** replace `25.7 [11.8, 38.2]` with **`25.7 [11.8, 39.6]`**. |
| `appendix/e6_protocol.tex:239` | **Overstated matching guarantee:** replace “statements, nesting, operators and names match” with **“non-expression syntax matches; operators and names inside masked expressions may differ”**. The checker accepts `return x + 1` versus `return y * 2`; accepted experimental pairs also differ in expression names. |
| `appendix/e6_protocol.tex:246–247` | Supply registered denominators: **“18 of 20”** and **“18 of 21”**. Replace “the development pilot’s equal strata did not replicate” with **“Pilot stratum estimates were +41.7 and +36.1; held-out estimates were +47.2 and +20.8. Equality was not established in the pilot.”** |
| `appendix/e6_protocol.tex:256` | Caption omission: replace “E13 and E14” with **“E13, E14 and E15”**. |

The E15 figures in `sections/e6.tex:106–107`, the verdict table at `appendix/e6_protocol.tex:356`, and the plotted complete-case/worst-case intervals are correct. “Inconclusive” and “not supported” appropriately describe the registered result; neither establishes absence of preference.

**Additional reporting bug:** [`e15.py:153`](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/crossaudit-harness/benchmarks/e15/e15.py:153>) can count an earlier, unchanged branch. Correct per-body counts for MBPP /602, /576, /74, /778, /395 and /730 are respectively **2/2, 6/6, 5/5, 5/5, 5/5 and 5/5**, rather than 4/4, 3/3, 2/2, 10/10, 26/26 and 54/54. Select the actual differing branch when reporting tokens. The paper’s aggregate counts and primary verdict remain unchanged.

**B. Abstract, introduction and related work**

The instrument-first framing improves the paper. The headline numerical claims check out, including the pointer comparison and the restriction of 89% to two generator models. Remaining corrections:

- **`paper_v3.tex:60`:** qualify “the task leaves open” as **“two model judges deem compatible with both rules”**. Execution checks do not independently establish semantic admissibility.
- **`paper_v3.tex:64`:** the positive E14 summary would be better balanced by adding: **“A stricter symmetric-body control was inconclusive under its registered missing-unit analysis.”**
- **`sections/introduction_v2.tex:21–23`:** “Audit evaluations have lacked a way” is an unsupported field-wide novelty claim. Replace with **“A fixed-contract benchmark does not supply this counterfactual.”**
- **`sections/introduction_v2.tex:34–35`:** write **“half the difference between the two diagnosis rates”** to avoid ambiguity about the factor of one-half.

The additions citing [Orchid](https://arxiv.org/abs/2604.21505), [ClarEval](https://arxiv.org/abs/2603.00187) and [ClarifyCodeBench](https://arxiv.org/abs/2607.00711) accurately describe ambiguity and clarification research. These reinforce that the contribution is the controlled audit evaluation, rather than discovering that clarification helps.

At **`sections/related_v3.tex:8–9`**, distinguish c-CRAB from direct reference-answer scoring: **“CriticBench scores against reference answers; c-CRAB evaluates whether review-guided code revisions pass tests derived from human review comments.”** That is its actual evaluation mechanism. [c-CRAB methodology](https://arxiv.org/html/2603.23448v3)

**C. Scores**

| Soundness | Presentation | Significance | Originality | Overall | Confidence |
|---:|---:|---:|---:|---:|---:|
| 3/4 | 3/4 | 3/4 | 3/4 | **7/10** | 4/5 |

The controlled design, reproducible estimates and transparent negative result support acceptance. Model-dependent admissibility, the small selected population and unresolved expression-level implementation differences prevent an upgrade.