# Survey notes: raising audit recall (2026-09-05)

Unvetted working notes from the first literature pass, kept as source material.

**Known error, corrected in `manuscript/related-work/related-work-decomposition.md`:**
the MCeT figures here (59.3% / 0.86, "~6x tokens") are wrong in all three
components. arXiv:2508.00630 reports the holistic baseline finding <35% of
engineer-found issues at 0.58 precision and the combined atomic approach at 65%
recall / 0.81 precision; "6" is six new issues per diagram, not a token
multiplier; no cost figure is given. Cite the vetted section, never this file.

---

# Raising automated-reviewer recall without a bigger model

**A literature survey for CrossAudit.** Written 2026-09-05. Every number below is attributed;
where I could not verify a figure against a primary source I say so in-line. Where a claim
rests on one paper or a small benchmark I say that too.

---

## 0. What we are trying to explain

Our measured position, from `benchmarks/expertlongbench/RESULTS{,-2,-3}.md` and
`benchmarks/code/RESULTS.md`:

| observation | number |
|---|---|
| auditor round-1 recall vs CLEAR ground truth, shipped rules | **2.0%** (4/201, n=40); replicated 2.0% (2/100, n=20, fresh seed) |
| same, rubric-derived rules, split from the generator's brief | **23.5%** (23/98) — ~12× |
| same, stronger auditor model, rules unchanged | **3.8%** (2/52) — inside noise |
| auditor precision, shipped → rubric rules | **100% (2/2) → 73% (33/45)** |
| code, "passes visible tests, fails hidden test" population | **8.9%** recall (5/56), CI [3.9, 19.3] |
| code, self-audit vs cross-vendor | recall 16.1% vs 10.7% (p=0.51); **FP on correct code 20.0% vs 4.7% (p=0.000066)** |
| revision, pooled | **−11.0 F1** over 25 revisions, p=0.0014; 17 rubric items broken, 3 fixed |
| CLEAR (decomposed, reference-grounded) vs our holistic auditor, same outputs | **201 wrong items named vs 4** |

The leading hypothesis is that **holistic review has a low recall ceiling and CLEAR's
structure — per-item extraction plus comparison against an evidence source — is what buys the
difference.** This survey supports the first half strongly, supports the second half with an
important correction, and produces one clean counterexample that constrains how the fix
should be built.

**The correction, stated up front, because it changes the design:** our 201-vs-4 contrast is
*confounded*. CLEAR has three things our auditor does not: (a) decomposition, (b) a
**gold reference answer** to compare against, and (c) a *forced verdict on every item* rather
than free-form enumeration. The literature says (b) and (c) are each worth as much as or more
than (a). Any experiment that changes all three at once will not tell us which one paid.

---

## 1. Decomposition — how much recall does it buy over holistic judging?

### 1.1 The strongest direct evidence, and it is structurally our problem

**MCeT** — Ahmed, Song, Chen, Wei, Zheng (Huawei Research Canada + McGill), *MCeT: Behavioral
Model Correctness Evaluation using Large Language Models*, arXiv:2508.00630, Aug 2025.

Mechanism: instead of asking one model "does this sequence diagram satisfy these requirements?",
split the requirements text into **requirement-atoms** and the diagram into **diagram-atoms**,
run one focused check per atom, then run a self-consistency "higher-authority cross-check"
across the three views to suppress hallucinated issues. Ground truth = issues found by
experienced engineers on the FBENCH corpus.

| check | issues emitted | true positives | precision | recall vs human experts |
|---|---:|---:|---:|---:|
| **Holistic (baseline)** | 134 | 78 | **0.58** | **46 (34.1%)** |
| Diagram-atom | 505 | 254 | 0.50 | 43 (31.9%) |
| **Requirement-atom** | 885 | 764 | **0.86** | **80 (59.3%)** |
| Combined (MCeT-A) | 1524 | 1096 | 0.72 | **92 (68.1%)** |
| **Combined + cross-check (MCeT-X)** | 1155 | 938 | **0.81** | 88 (65.2%) |

Four things matter here:

1. **Decomposition roughly doubles recall** (34.1% → 68.1%) on human-found issues, and the
   requirement-atom check *alone* gets 59.3% at **higher precision than holistic** (0.86 vs
   0.58). Decomposition is not always a precision-for-recall trade.
2. **Which axis you decompose along decides everything.** Iterating over *requirements*
   ("is this requirement implemented?") gives precision 0.88; iterating over *artifact
   fragments* ("is this diagram element correct?") gives precision 0.40. The authors'
   explanation is that the requirement-side check is **context-free** — the model needs no
   surrounding context to answer it — while the artifact-side check is context-sensitive and
   the model invents context-dependent objections. **For CrossAudit this says: decompose by
   RULE, not by document chunk.**
3. **Decomposition beats a model upgrade, measured head to head.** GPT-4o-mini holistic recall
   21.4% → MCeT-X 71.4%. GPT-4o holistic 28.6% → 85.7%. DeepSeek-R1 (reasoning) holistic 50%
   → 85.7%. **GPT-4o-mini + MCeT-X (71.4%) beats DeepSeek-R1 holistic (50%) at 0.56× the wall
   time.** This is the closest published analogue of our "changing the auditor model does
   nothing" result, and it says the lever is architecture, not capability.
4. **Cost.** GPT-4o-mini: 12K tokens/diagram holistic → 70.8K MCeT-A → 80.5K MCeT-X
   (**5.9×–6.7×**); 0.6 min → 4.1/4.5 min (**~7×**).

*Weight to give it:* one domain (sequence diagrams vs requirements), one corpus, ground truth
adjudicated by the two authors (Cohen's κ = 0.79 on a 20% calibration slice), industrial-lab
paper. The RQ3 model-comparison table is only 8 diagrams (10% of the corpus). But it is the
only paper I found whose *task shape* is ours: an artifact, a specification, no gold answer,
and human-found defects as ground truth.

### 1.2 The mechanism: models judge far better than they enumerate

**Chen, Chen, Lin, Long, Vong (U. Macau)**, *Judging Is Not Enumerating: Silent Omissions in
LLM-Authored Acceptable Sets*, arXiv:2608.01000, 2 Aug 2026.

Judge-free ground truth via three orthogonal constructions: mechanically decidable predicates
over a *presented* finite list (incompleteness impossible), HumanEval+/MBPP+ execution, and
WordNet. One-shot greedy, no test-time reasoning (the authors state this scope condition
themselves).

| construction | judging (per-candidate) F1 | enumerating (author the set) F1 | gap |
|---|---|---|---|
| algorithmic, Qwen2.5 3B → 72B, n=240 | 0.599 → **0.769** | 0.259 → **0.483** | **+0.340 / +0.252 / +0.286 / +0.286**, all CI pairs disjoint |
| arithmetic predicates | 0.94–1.00 | 0.66–0.79 | +0.21 to +0.30 |
| executable code | F1 0.74–0.90 | authored suites admit only **19–42%** of oracle-correct solutions | — |
| Llama-3.2-3B / 3.1-8B | — | — | +0.128 / +0.190 |

Four findings that bear directly on us:

- **The gap does not close over a 24× parameter range.** Enumeration improves with scale; it
  never catches judging. This is the published version of our 2.0% → 3.8% auditor-model null.
- **The dominant error is omission, and omission resists review.** Models detect *planted
  over-inclusions* **6–7× more often** than *planted omissions*. A production deployment of
  43,227 scored items failed omission-first at **10:1**. Our auditor's failure mode — precision
  100%, recall 2% — is the omission mode, and the paper says review will not surface it.
- **The predicate control.** Asked to emit *the predicate* rather than its extension, the same
  models reach **F1 ≈ 0.99**, above even their own judging. The failure is not missing
  knowledge and not an inability to specify — it is an inability to *materialise* the set a
  specification induces. **Translation for CrossAudit: our rules file already is the predicate.
  The auditor's job should be to evaluate it pointwise, not to enumerate defects freely.**
- Test-time reasoning closes the gap outright on the algorithmic construction; it does **not**
  transfer to code (Opus improves, GPT-5.1 does not).

*Weight:* mostly open-weight mid-size models; an arXiv preprint; the "one-shot greedy, no
reasoning" scope condition is doing real work and the authors flag it. But the ground truth is
model-free across three orthogonal constructions, which is unusually strong.

### 1.3 Why a holistic auditor goes quiet: count bias

**Pushkar, Kabra, Kumar, Challa**, *Beyond Single Bugs: Benchmarking LLMs for Multi-Vulnerability
Detection*, arXiv:2512.22306, 30 Dec 2025. Injected vulnerabilities, C/C++/JS/Python, 5 models.
C results (precision stays ≈1.00 throughout):

| model | recall N=1 | N=3 | N=5 | N=9 |
|---|---:|---:|---:|---:|
| Qwen2.5-32B | 0.702 | 0.236 | 0.213 | 0.146 |
| Qwen2.5-72B | 0.910 | 0.548 | 0.441 | 0.386 |
| Llama-3.3-70B | 0.944 | 0.622 | 0.543 | 0.464 |
| Mistral-3.2-24B | 0.948 | 0.603 | 0.498 | 0.449 |
| gpt-4o-mini | 0.899 | 0.527 | 0.397 | 0.296 |

The authors name this **"count bias": the model gives up after finding a few issues.**
**Precision ≈ 1.00 with recall collapsing to 0.15–0.46 is CrossAudit's exact signature.** Our
T03 round-one drafts had 5–6 of 6 rubric items wrong — the N=9 regime. On this reading, our 2%
is not "the auditor disagrees"; it is the auditor stopping.

*Weight:* injected (synthetic) defects; one preprint; **and note the authors propose
decomposition/multi-pass exhaustive audit only as future work — they did not test it.** The
paper diagnoses; it does not prescribe.

### 1.4 The negative evidence, which is larger than I expected

This is the part of the survey that most changes the plan. **Decomposition is not generically
recall-positive; in several well-controlled studies it is recall-negative, and the failure mode
is precisely ours — omissions.**

| study | comparison | result |
|---|---|---|
| **Molecular Facts** — Gunjal & Durrett, Findings EMNLP 2024 | fully atomic facts vs minimally contextualised units | **not-supported recall 22.4% → 38.8%.** Context-free atoms default to "supported" — decontextualisation *destroys* the ability to detect unsupported content |
| **FBI / Finding Blind Spots in Evaluator LLMs** — Doddapaneni et al., EMNLP 2024, arXiv:2406.13439; 2,400 perturbed answers, 22 categories | adding rubrics to **single-answer scoring** | undetected-error rate **0.57 → 0.85** (long-form), **0.54 → 0.73** (factual), **0.57 → 0.80** (instruction-following). Rubrics made GPT-4-Turbo **worse**. In **pairwise comparison the sign flips** — Axis/Axis+Rules beat plain pairwise on every ability. Evaluators missed quality drops in **>50%** of cases overall |
| **NLI under the Microscope** — Srikanth & Rudinger, arXiv:2502.08080 | holistic label vs label composed from atoms | SNLI GPT-4o-mini **−8.5**; δ-SNLI GPT-4o **92.6 → 77.2 (−15.4)**. Atomic/holistic consistency collapses to 41–75% on holistically-wrong examples |
| **ClaimCLAIRE** — TrustNLP 2026 | cumulative ablation, + decomposition | macro-F1 0.774 → 0.742; **recall 0.664 → 0.541 (−12.3pp)**. The authors then add "adaptive gap-filling" explicitly to repair the recall bottleneck decomposition introduced |
| **Rethinking Atomic Decomposition** — arXiv:2603.28005 (§1.7) | atomic vs prompt-matched holistic | holistic wins on 2 of 3 benchmarks, all four model families, **and is cheaper**; advantage concentrated at **+14.5 to +33.0pp on `partially_supported` = incompleteness** |

**The FBI result deserves the most weight of these** — it is peer-reviewed, it is about *error
detection* rather than correlation, and its finding that **format interacts with decomposition**
(rubrics hurt in single-answer scoring, help in pairwise comparison) is a warning that "add
rubric detail" and "decompose" are not the same intervention and can point opposite ways.

Two further cautions on the pro-decomposition side of the ledger:

- **Decomposed factuality scores are gameable.** *Core* (Jiang et al., Findings ACL 2025,
  arXiv:2407.03572): padding a generation with obvious subclaims inflates FActScore
  **54.0 → 83.0 (+29pp)**; a tautological biography scores **100%** against 81.5% for a real one;
  under attack MistralINST and GPT-2 become indistinguishable (0.8pp apart, from an 18.6pp gap).
  Not an NLI artefact (r = .98–.99 across three NLI models). A per-rule audit that rewards
  "addressed the rule" invites exactly this.
- **Individually-true atoms compose into false wholes.** *D-FActScore* (Chiang & Lee, Findings
  ACL 2024): entity-ambiguous biographies score **94.8% vs 78.4%** once disambiguated — a
  **16.4pp** overestimate. And *DnDScore*: changing only pipeline **order** moves the score
  **33.00% → 61.51%** with **19.11% of judgments flipping**, while decomposition entailment stays
  at 95.7–96.8%.
- **Absolute recall stays poor regardless of design.** *ReaLMistake* (Kamoi et al., COLM 2024):
  GPT-4 error-detection recall **11.9% / 12.6%** on two of three tasks, Claude 3 Opus **6.8%**,
  against humans at **~90–95% F1**; self-consistency did not help. **Our 8.9% on code and 2–23.5%
  on prose sit squarely inside this band.** Nobody has an automated reviewer with good recall.

### 1.5 The moderator: when does decomposition help?

Two papers give a mechanism that reconciles the conflicting results, and both point the same way.

**Decomposition Dilemmas** — Hu et al., **NAACL 2025**. Holistic verification vs three
decomposers × three verifiers:

- **Strong verifier + short claims → decomposition hurts**: WICE/MiniCheck **80.01 → 71.11 BAcc**.
- **Weak verifier + long responses → decomposition helps a lot**: FELM/AlignScore F1
  **45.88 → 64.32**, largely where the holistic verifier fails outright.

**CrossAudit's prose tier is unambiguously the second regime**: ExpertLongBench outputs can exceed
5,000 tokens, and our holistic verifier is failing outright (2%). That is the strongest reason to
expect decomposition to work *for us* despite the negative results above.

**The Alignment Bottleneck** — Akhter et al., arXiv:2602.10380. The decisive variable is whether
each sub-unit gets **its own aligned evidence**:

| evidence condition | effect |
|---|---|
| sub-claim-**aligned** evidence | **+0.0625 F1** |
| repeated **shared** claim-level evidence | **−0.0672 F1** |
| under noisy labels | collapses to ≈0.44 F1 |

**This is the single most important design constraint in this document.** A naive "one audit call
per rule, each shown the whole source document" is the *shared-evidence* condition — the one
measured at −0.0672 F1. To land in the +0.0625 condition, each rule's call must be given, or must
retrieve, the *specific* portion of the source that rule is about. Our checkability probe already
knows which rubric items are derivable from which parts of `RECIPE.md`; that structure is exactly
the alignment the paper says is load-bearing.

**And grounding still beats decomposition.** FLASK's own ablation (Ye et al., ICLR 2024): skill
decomposition contributes **+0.039 ρ** to human correlation; **a reference answer contributes
+0.164 ρ — four times more.** This mirrors §2's finding and is the reason grounding is ranked
above decomposition in §11.

### 1.6 Checklist-based evaluation

- **TICK** — Cook et al., *TICKing All the Boxes: Generated Checklists Improve LLM Evaluation
  and Generation*, arXiv:2410.03608, Oct 2024. LLM-generated instruction-specific YES/NO
  checklists instead of a direct score. Exact agreement with human preference **46.4% → 52.2%**
  (+5.8pp). STICK self-refinement **+7.8%** absolute on LiveBench reasoning; Best-of-N with
  STICK **+6.3%** on WildBench. Giving human evaluators the generated checklist raised
  inter-annotator agreement **0.194 → 0.256**.
- **HealthBench** — OpenAI, May 2025 (arXiv:2505.08775). 5,000 physician-authored conversations,
  **48,562 unique rubric criteria** (~10 per conversation), each graded by a separate model
  judgement. Meta-evaluation: the model grader's class-balanced **macro-F1 = 0.709**, exceeding
  the average physician in **5 of 7 themes**; inter-physician macro-F1 ranges **0.57–0.73**.
  This is the industrial existence proof that per-criterion grading at ~10 calls/response is
  operationally viable and lands inside the human agreement band.
- **CLEAR / ExpertLongBench** — Ruan et al., arXiv:2506.01241, Jun 2025 — our own scorer.
  Mapper (Qwen2.5-72B) average mapping F1 **90.1**; judge Cohen's κ **0.81/0.87/0.89/0.85** on
  T1/T6/T7/T8; best model **33.4 F1** on the benchmark. **Important: the paper does NOT report a
  head-to-head of CLEAR against a holistic LLM judge.** Our 201-vs-4 contrast has no support
  from the paper's own ablations and must be read as a confounded observation, not a result.
- **FActScore** — Min et al., EMNLP 2023, arXiv:2305.14251. Atomic-fact decomposition + per-fact
  retrieval verification; the automated estimator has **<2% error rate** against the human
  FActScore. Verified.
- **SAFE** — Wei et al. (DeepMind), *Long-form factuality in large language models*,
  arXiv:2403.18802, Mar 2024. Decompose → generate search queries → verify each fact against
  Google Search. On ~16k individual facts, **agrees with crowdsourced annotators 72% of the
  time**; on a random 100 disagreement cases, **SAFE wins 76%**; **>20× cheaper** than human
  annotation. Verified.

### 1.7 The counterexample — and it is a good one

**Xinran Zhang (UC Berkeley)**, *A Matched Holistic Rubric Rivals Self-Decomposing Atomic Judges
for Benchmark-Style Reference-Support Classification*, arXiv:2603.28005, 30 Mar 2026.

A **self-decomposing single-prompt** atomic judge vs a **prompt-matched holistic rubric** judge,
same inputs, same output-schema detail, realized-token accounting, three independently authored
pre-frozen prompts per family, 200 source examples per dataset, four model families.

| dataset | atomic acc (Opus-4.6 / GPT-4.1) | holistic acc | tokens |
|---|---|---|---|
| TruthfulQA | 0.975 / 0.978 | 0.970 / 0.968 | comparable |
| ASQA | 0.778 / 0.565 | **0.850 / 0.720** | atomic 1.4–2.3× more |
| QAMPARI | 0.975 / 0.928 | **0.993 / 0.998** | 803 vs 511 |

Source-level paired sign tests: ASQA p = 1.5e-8 (Opus), 2.1e-14 (GPT-4.1). The holistic
advantage is **concentrated entirely in the `partially_supported` class — incompleteness
detection — at +14.5 to +33.0pp.** A schema ablation (atomic-style JSON without the
decomposition instruction) does not recover atomic's number, so it is not a formatting artefact;
a budget ablation rules out truncation.

**Read this carefully before concluding it refutes us.** The authors' own scope statement:
*"atomic pipelines with externally supplied decompositions or multi-stage extract-then-verify
architectures remain untested."* That is precisely CLEAR's architecture, and MCeT's, and the one
we would build. What the paper does refute is **the cheap version**: telling one auditor call
"decompose this into claims and check each" is not the lever. It also warns that
**self-decomposition may specifically damage completeness detection** — and "the deliverable
never addresses rubric item 4" is exactly a completeness failure, i.e. the class where holistic
won by up to 33pp.

*Weight:* single-author preprint under review; single-annotator human study (60 examples);
reference is *supplied*, which is not our setting.

### 1.8 What the decomposition literature costs, and what it needs that we lack

| technique | recall effect | precision effect | cost multiplier | needs that we lack |
|---|---|---|---|---|
| Requirement-atom decomposition (MCeT) | 34.1% → 59.3% | 0.58 → 0.86 | ~5–6× tokens, ~7× wall | nothing — our rules file already enumerates the atoms |
| + multi-perspective union | → 68.1% | 0.72 | ~6× | a second decomposition axis |
| + cross-check filter (MCeT-X) | 68.1% → 65.2% | 0.72 → **0.81** | ~6.7× | a filtering pass |
| Checklist judging (TICK) | agreement +5.8pp | — | ~1 checklist gen + n item calls | none |
| Per-criterion rubric grading (HealthBench) | macro-F1 0.709 vs physicians | — | ~10 calls/response | expert-authored criteria |
| Atomic fact + retrieval (FActScore/SAFE) | <2% estimator error / 72% human agreement | — | 1 decomp + 1 retrieval+verify per fact | a knowledge source per claim |
| Self-decomposing single prompt | **0 to −15pp vs matched holistic** | — | 1.4–2.3× tokens | — (this is the version to avoid) |
| Claim-atom decomposition of the **artifact** | **−12.3pp recall** (ClaimCLAIRE); not-supported recall **22.4%** for fully atomic units | — | 30–50× (FActScore), ~60× (VeriScore), 100–300× (SAFE) | — (also the version to avoid) |

Measured per-technique cost multipliers, from the papers' own accounting:

| method | cost | multiplier vs a holistic call |
|---|---|---:|
| holistic judge | 1 call | **1×** |
| single-prompt atomic judge | 1 call, 1.4–2.3× output tokens | ~2× |
| **per-rule audit (our #1)** | n rules × 1 call | **≈ n (7× for T03)** |
| Chain-of-Verification, factored | draft + plan + N answers + revision | N+3× (N unreported) |
| FActScore | 1 decomposition/sentence + 26–41 atom verifications | ≈30–50× |
| VeriScore | ~14 extraction + 23 search + 23 verification ≈ **60 calls**, ~100 s, **$0.01725**, 22,848 tok | ≈60× |
| SAFE | **49,622 tok/response**, ≤5 search steps/fact | ≈100–300× |
| MCeT-A / MCeT-X | 70.8K / 80.5K tok/diagram vs 12K | 5.9× / 6.7× |
| MiniCheck-FT5 as a filter | GPT-4-comparable accuracy | **400× cheaper** than a GPT-4 call |

That the field's current frontier (VeriFastScore, FaStfact, ElementCheck) is devoted to
*collapsing* this multiplier while holding r = 0.80–0.94 is itself evidence that most of those
calls carry little information.

**Two constraints the literature puts on how we build #1, both load-bearing:**

1. **Decompose the SPEC, not the ARTIFACT.** MCeT: requirement-atoms precision 0.86 / recall
   59.3%; diagram-atoms precision 0.40 / recall 31.9%. Molecular Facts: fully atomic *artifact*
   units detect only **22.4%** of not-supported cases because context-free atoms default to
   "supported". Our rules are the spec side; our document sections are the artifact side.
2. **Each rule's call must get evidence aligned to that rule.** Alignment Bottleneck: aligned
   evidence **+0.0625 F1**, repeated shared evidence **−0.0672 F1**. Handing all seven calls the
   same whole `RECIPE.md` is the measured-negative condition.

**Falsification in our harness.** `run.py --audit-rules rubric` already builds a 7-rule
constitution (`rubric_constitution()`), passed to a **single** audit call. The clean arm is **one
audit call per rule**, findings unioned, round one only, on the same 20 seeded T03 samples;
`_instrument_audit` already computes round-1 recall against CLEAR's per-item verdicts, so the
readout exists. This is falsifiable in four distinct ways, and I would run all four readouts:

- **vs the null**: union of 7 samples of the *holistic* auditor at matched cost. If per-rule does
  not beat that, the gain was scrutiny volume (Tyen et al.), not structure, and the hypothesis
  is dead.
- **vs MCeT's prediction**: recall ≫ 23.5% *and* precision ≥ 73%.
- **vs Zhang's prediction** (arXiv:2603.28005): no gain on *completeness*-type items (rubric items
  the draft never mentions) even if gains appear on *contradiction*-type items. Split the recall
  readout by those two classes — this is the discriminating measurement and nobody has run it.
- **vs the Alignment Bottleneck**: run per-rule with the whole source vs per-rule with a
  rule-scoped source excerpt. The paper predicts the former is *worse than holistic*.

---

## 2. Grounding when there is no reference answer

This is the half of the hypothesis I think is *under*-weighted in our current framing.

**Kranti & Vajjala**, *LLM Judges Can Be Too Generous When There Is No Reference Answer*,
arXiv:2607.12885, 14 Jul 2026. Judges evaluated under three conditions: no-reference (NR),
reference-visible (RV), reference-comparison (RC).

| condition | judge–human agreement |
|---|---|
| **NR (no reference)** | **33–42%** for some judge/model pairs |
| RV (reference shown) | **85–96%** |
| RC (explicit comparison) | up to **98%** |

Decision flips NR→RV ran **9% to 85%** across language pairs, and **most flips were
over-credits** — the judge had said CORRECT and reversed once it could see the reference. For
the lowest-resource language one model accepted known-incorrect answers at up to **60%**.
Calibration gap (correct-vs-incorrect discrimination) ranged 0.33–0.96.

**This is the single best explanation on offer for "the auditor passed 11 of 12 first drafts."**
A reference-free judge is generous. It is not disagreeing with the rubric; it has nothing to
disagree against. *Weight:* one paper, three languages, QA tasks; the mitigation it proposes is
a calibration protocol that itself needs labelled data.

Corroboration from the counterexample paper above: Zhang's grounding ablation on ASQA reports
holistic accuracy **0.860 (identical reference) → 0.620 (reduced reference) → 0.380 (no
reference)**, and atomic **0.740 → 0.500 → 0.380**. **Reference degradation produced the largest
accuracy drops of any perturbation tested, for both judge designs** — larger than the
decomposition effect the paper is about. Swapped (wrong) references produced ~50% verdict flip
rates in both designs: *neither architecture is robust to bad grounding.*

### 2.1 The cheap grounded verifier already exists, and it beats GPT-4-as-judge on cost

This is the most immediately actionable finding in the whole survey, and it is not about
decomposition at all.

| system | params | avg balanced accuracy, LLM-AggreFact (10 datasets, ~13k examples) | cost over that set |
|---|---:|---:|---:|
| GPT-4 as holistic judge | — | **75.3%** | ≈ **$107** |
| **MiniCheck-FT5** | 770M | **74.7%** | ≈ **$0.24** |
| Claude-3 Opus | — | 74.1% | — |
| MiniCheck-RoBERTa-L | 355M | 72.7% | — |
| AlignScore | 355M | 70.4% | — |
| QAFactEval | — | 66.5% | — |
| SummaC-Conv | — | 62.1% | — |

Tang, Laban, Durrett, *MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents*,
EMNLP 2024, arXiv:2404.10774. **A 770M model matches GPT-4 within 0.6pp at ~1/400 the cost** on
"is this claim supported by this document?". Zha, Yang, Li, Hu, *AlignScore*, ACL 2023,
arXiv:2305.16739, reports 87.4 average AUC-ROC on the TRUE benchmark (11 datasets) vs QAFactEval
80.1 and UniEval 79.5, and — the number that matters here — **Spearman correlation with human
judgement of 49.3 for a 355M alignment head vs 43.3 for ChatGPT-as-judge.**

Predecessors and their ceilings: **SummaC** (Laban et al., TACL 2022, arXiv:2111.09525) —
sentence-level NLI, 74.4% balanced accuracy on the 6-dataset SummaC benchmark vs QuestEval 69.4,
FactCC-CLS 62.8. **TRUE** (Honovich et al., NAACL 2022, arXiv:2204.04991) — 11 datasets, average
ROC-AUC ANLI 81.5 / SummaC-ZS 81.4 / Q² 80.7, but **BERTScore ranges 53.8 → 86.3 across
datasets**, so any grounded checker must be validated on our own distribution, not adopted on a
headline.

**Implication for CrossAudit.** The precision filter in a two-stage cascade (§4.3) does not need
to be a frontier model at all. "Is this finding supported by the committed source bytes?" is
exactly the entailment task these heads are trained for, at ~1/400 the cost of a model call.
That changes the economics of the cascade entirely: **the recall stage is where the money goes,
and the filter is nearly free.**

Honest ceiling: **~75% balanced accuracy is the state of the art for reference-free faithfulness
detection.** At that level a grounded checker should produce calibrated flags for human review,
not hard gates.

### 2.2 What evidence-conditioning is worth

- **AIS** (Rashkin et al., arXiv:2112.12870, Dec 2021; *Computational Linguistics* 2023): a T5
  fine-tuned with evidence reached **87.9% AIS on QReCC vs 25.2% without evidence** — a 62.7pp
  swing from grounding alone. Annotation reliability: Krippendorff's α .69–.79.
- **FActScore**: search-augmented PerplexityAI **71.5%** factual precision vs ChatGPT **58.3%**.
- **RARR** (Gao et al., ACL 2023): NQ attribution 35.4% → 43.4%; QReCC 13.2% → 28.3%.
- **SAFE**: 72% agreement with crowdworkers over ~16k facts; on the disagreement subset SAFE
  correct **76%** vs human raters **19%**; **$0.19/response vs $4.00 crowdsourced (>20×)**.

**Caveat I want on the record:** there is no single clean ablation of "retrieval vs closed-book
for the same judge on the same benchmark." The 13–63pp figures above are assembled across
different papers and benchmarks. The *direction* is unambiguous and the magnitudes are large;
the specific number is an inference, not a measurement.

### 2.3 Sampling as a substitute reference, and its hard boundary

- **SelfCheckGPT** (Manakul et al., EMNLP 2023, arXiv:2303.08896): sample N responses, check
  consistency. WikiBio-GPT-3 sentence-level AUC-PR — SelfCheck-Prompt **93.42** (NonFact),
  **53.19** (NonFact*, random floor 29.72), vs GPT-3 Max(−log p) 87.51 / 35.88. Passage-level
  Pearson 78.32.
- **Semantic entropy** (Farquhar, Kossen, Kuhn, Gal, *Nature* 630, Jun 2024): cluster samples by
  bidirectional entailment, take entropy over meaning-clusters. **AUROC 0.790** vs P(True) 0.698,
  naive entropy 0.691, and a *supervised* embedding-regression baseline 0.687. Stable at
  0.78–0.81 across LLaMA/Falcon/Mistral and 7B→70B. Detects **confabulations**, not systematic
  errors the model is confidently wrong about — which is a real limit for us, because a
  generator that misreads a rubric item is confidently wrong, not confabulating.
- **Universal Self-Consistency** (Chen et al., arXiv:2311.17311): GSM8K PaLM 2-L 85.7 → 90.2;
  MATH 30.8 → 37.4; BIRD-SQL 45.5% execution accuracy **without executing**.
- **The boundary, and it is architectural:** Huang et al. (ICLR 2024) — intrinsic self-revision
  with no external signal degrades (GPT-4 GSM8K 95.5 → 91.5 → 89.0). **Sampling may vote; it
  must not rewrite.** That distinction should be enforced in the loop, not left to a prompt.

**What can serve as the reference in production.** Our checkability probe already answered the
scoping question for T03: **69.2% of the reference checklist's substance is derivable from the
committed recipe alone** (per-item: 85% / 85% / 80% / 70% / 62.5%, and only **32.5%** for
Temperature and Heating Method). That is the recall ceiling for a source-grounded auditor on
that task, and 2% is nowhere near it. The candidate references, ranked by how well they fit
CrossAudit:

1. **The committed source documents** — already in scope; the auditor already sees them. The
   change is to force per-rule *citation* into the source, not to add data.
2. **Executed results** — deterministic checks, test output, recomputed numbers. Our code study
   already shows the size of this: on stratum F, `cross` (model reading code, tests not run)
   flags **79.3%**; `cross+checks` (same model, shown the test result) flags **100%**. That is
   a 20.7pp grounding effect from one deterministic fact, measured in our own harness.
3. **Retrieved literature** — SAFE's structure; costly and out of scope for most CrossAudit runs.
4. **The prior state** — the previous commit. Underused: a diff-grounded auditor answers "what
   changed and does the change satisfy the rule?", which is a bounded, context-free question of
   the MCeT requirement-atom shape.

**Falsification.** Two arms on the existing prose harness, both round-one only: (a) rules
unchanged but the auditor required to emit, per rule, a verbatim quotation from `RECIPE.md`
plus a verdict, with "not derivable from the source" as an explicit allowed verdict; (b) an
oracle-grounding arm that hands the auditor the *reference* checklist. (b) is not shippable —
it is the ceiling probe. If (b) does not reach the 69% checkability ceiling, decomposition and
grounding together are not the whole story and the hypothesis is wrong.

---

## 3. Tool-using verifiers

### 3.0 The cleanest tool-vs-no-tool ablation in the literature

**CRITIC** — Gou, Shao, Gong, Shen, Yang, Duan, Chen, *CRITIC: LLMs Can Self-Correct with
Tool-Interactive Critiquing*, ICLR 2024, arXiv:2305.11738. Same model, same loop, tools on/off:

| task | baseline | CRITIC (tools) | CRITIC **without tools** |
|---|---:|---:|---:|
| AmbigNQ EM (ChatGPT) | 51.8 | **62.0** | 55.2 |
| AmbigNQ EM (davinci-003) | 44.2 | **50.0** | **42.0 — below baseline** |
| TriviaQA F1 (davinci-003) | 74.5 | **80.6** | 74.7 |
| HotpotQA F1 (ChatGPT) | 42.8 | **52.9** | 46.1 |
| GSM8k (ChatGPT) | 72.5 | **78.2** | 77.0 |
| TabMWP (davinci-003) | 64.6 | **87.6** | 84.9 |
| SVAMP (davinci-003) | 84.0 | **80.7 — regression** | 80.7 |
| toxicity, max prob (ChatGPT) | 0.325 | **0.173** | 0.339 (no effect) |

Authors: *"exclusive reliance on self-correction without external feedback may yield modest
improvements or even deteriorate performance."* Note SVAMP, where tool-interactive critiquing
made things worse — this is not monotonically safe either.

**Agent-as-a-Judge** — Zhuge et al. (Meta AI / KAUST), arXiv:2410.10934, Oct 2024. DevAI: 55
tasks, 365 hierarchical requirements. A judge that can *read files and locate evidence* vs one
that only reads the final output:

| judge | MetaGPT | GPT-Pilot | OpenHands |
|---|---:|---:|---:|
| **Agent-as-a-Judge** | **88.52%** | **83.88%** | **90.44%** |
| LLM-as-a-Judge | 84.15% | 65.30% | 60.38% |
| human majority vote | 95.08% | 93.98% | 94.26% |

Ablation: 65.03% (ask only) → 82.24% (+read) → **90.44% (+locate)**. The **memory module was net
harmful** ("errors in previous judgments could lead to a chain of errors") — relevant to any
multi-round audit that carries prior findings forward. Cost: Agent-as-a-Judge **$30.58** vs
LLM-as-a-Judge **$29.63** — **the +24pp alignment gain is essentially free.** The paper's famous
"2.29% of the cost / 97% reduction" figure is against a *human* panel priced at $15/hr, which is
an assumption, not a market price; the same-cost comparison against LLM-as-a-Judge is the honest
headline. Human noise floor from the same paper: pairwise inter-evaluator disagreement 10–30%,
individual error up to 23.77%, post-majority-vote error 6.01%.

**For CrossAudit this is the highest-leverage read of the section**: the 65 → 82 → 90 ablation
says most of the gain comes from *making the judge go and look*, not from giving it a sandbox.
Our auditor reads committed bytes but is not required to locate and quote evidence per rule.
That is a cheap change (§8, technique #2).

### 3.1 The critic precision/recall law

**CriticGPT** — McAleese et al. (OpenAI), *LLM Critics Help Catch LLM Bugs*, arXiv:2407.00215,
Jun 2024. An RLHF-trained critic on code, evaluated on two sets: **Human Inserted Bugs**
(contractors tampered code adversarially, required the critic to miss the bug in ≥1 of 3
samples) and **Human Detected Bugs**.

- Model critiques **preferred over human contractor critiques in 63% of cases** on code with
  naturally occurring LLM errors.
- **Stated as a law, not an accident:** *"models which hallucinate bugs more often are also more
  likely to catch human inserted and previously detected bugs."* An explicit precision/recall
  frontier for critics. **Our 2.0%/100% → 23.5%/73% move is a movement along this frontier, not
  a regression.** That reframing matters: the honest question is not "why did precision fall"
  but "are we at the right point on the curve".
- Matching CriticGPT (RL only) by scaling the prompted baseline would take **~30× pretraining
  compute** — i.e. the frontier can be shifted by *training a critic*, which is the expensive
  answer to "without a bigger model".
- **Force Sampling Beam Search** moves along the frontier at inference: **28 samples per input**,
  scored by a reward model as `rm_score + LENGTH_MODIFIER × num_highlights`, with four penalty
  settings at the 10th/25th/50th/75th percentile of critique length. **Requires a trained reward
  model, which we do not have**, and costs 28×.
- Human+CriticGPT teams beat the model-only Pareto frontier: more comprehensive than humans
  alone, fewer hallucinations/nitpicks than the model alone. **I could not extract the numeric
  bar values for comprehensiveness and nitpick rates from the PDF — they appear only in figures.
  Do not quote a number for them.**

### 3.2 What executing buys

Ours first: stratum F, model reading code without running it, **79.3%**; same model shown the
execution result, **100%**. On stratum P — where the visible tests pass — showing the result
changes nothing measurable (−1.8pp, p=1.0, inside our 1.8pp noise floor). **The deterministic
layer's value is concentrated exactly where it can act.** The corollary is uncomfortable: for
"looks right, is wrong", *existing* execution adds nothing. What would add something is **new**
execution.

The literature agrees on both halves:

| system | mechanism | effect |
|---|---|---|
| **CodeT** (Chen et al., arXiv:2207.10397, ICLR 2023) | generate code *and* tests, rank by dual execution agreement | code-davinci-002 HumanEval pass@1 **47.0 → 65.8** (+18.8); MBPP 58.1 → 67.7. Gains scale with test quality — a weaker model's self-written tests are a weaker verifier |
| **LEVER** (Ni et al., ICML 2023, arXiv:2302.08468) | train a verifier on execution *results* rather than trusting them raw | Spider 75.3 → 81.9; WikiTQ 49.6 → 64.6; GSM8k 68.1 → 84.1; MBPP 61.1 → 75.4. **Still +4.6 to +13.2 over an error-pruning baseline that already used execution** — learning to read execution output beats "did it crash?" |
| **Self-Debugging** (Chen et al., arXiv:2304.05128) | feed unit-test results back | TransCoder 80.4 → **91.6** with unit-test feedback; **+3.5 with explanation only (no execution)**; **Spider, where no unit tests exist: +0.0 with simple feedback** |
| **Agentless** (Xia et al., arXiv:2407.01489) | localize → repair → **validate** with generated reproduction tests | SWE-bench Lite **27% → 32%** from the validation stage alone, at $0.70/issue, beating agentic systems |

The Self-Debugging Spider row is the sharpest statement in the section: **where execution is
unavailable, the identical loop delivers 0 to +2.8 instead of +11.2. Executability, not
cleverness, is doing the work.** For CrossAudit's prose tier, this is a warning that the code
result will not transfer.

### 3.3 The ceiling on verifier-authored tests

From arXiv:2608.01000 above, on HumanEval+/MBPP+: models that **judge** correctness at F1
0.74–0.90 **author test suites admitting only 19–42% of oracle-correct solutions** — they
over-reject by inventing requirements the spec never states. The mitigation that works: **discard
any authored suite that rejects a known-correct probe.** False rejection falls from **58–92% to
≤5%**, but **only 5–39% of suites survive**. Repairing each wrong expected value to what a
reference execution returns recovers yield by **3.3–10.6×**, and the survivors still catch
**94–99.8%** of wrong solutions. **The split is diagnostic: the model chooses discriminating
inputs well and computes their expected outputs badly.** For CrossAudit that means a
tool-using auditor should be allowed to *choose inputs* and must **never** be allowed to assert
expected outputs — those must come from execution against the prior committed state.

Two independent benchmarks put a hard number on how often a model can write a test that
actually reproduces a real bug:

| benchmark | best system | fail-to-pass rate |
|---|---|---:|
| **SWT-Bench** (Mündler, Müller, He, Vechev, NeurIPS 2024, arXiv:2406.12952), 1,983 instances | SWE-Agent+ | **18.5%** |
| | SWE-Agent (GPT-4) | 15.9% |
| | LIBRO | 14.1% |
| | ZeroShot | 3.6% |
| **TDD-Bench Verified** (IBM, arXiv:2412.02883), 449 issues | Auto-TDD (GPT-4o) | **23.6%** |
| | zero-shot GPT-4o | 18.7% |
| | Llama-3.1 | 8.2% |
| **Agentless** reproduction tests | — | 213 reproduced the issue on the unmodified repo; **only 94 passed after the ground-truth patch** (~56% drop-off) |

Two nuances that make this actionable rather than merely discouraging:

- **The failure is binary, which means it is filterable.** TDD-Bench: among tests that do achieve
  F→P, model coverage is **0.91–0.97** vs developer-written **0.93–0.99**, statistically
  indistinguishable at 99%. Among non-F→P model tests, coverage collapses to **0.49–0.59**.
  Either the model writes a real test or it writes a vacuous one.
- **Test-writing and bug-fixing are uncorrelated skills** (SWT-Bench found *"no statistical
  evidence of correlation"*), and yet generated tests still worked as a filter: **SWE-Agent
  achieved over twice the precision on fixes that pass self-generated tests.**

**Ceiling statement: ~19–24% of real bugs get a working model-written reproduction test. A
verifier that gates on such a test will silently no-op on three quarters of real defects.** It
must be advisory-positive and never advisory-negative — a passing generated test is not evidence
of correctness.

### 3.4 Independence and safety when the reviewer can act

This is where the tool-using design gets genuinely dangerous, and the 2025–26 literature has
moved fast enough that the risk is now quantified.

- **Executable checks get gamed, and ambiguity is the trigger.** *EvilGenie* (arXiv:2511.21654,
  latest rev. 2026): 154 hard LiveCodeBench problems, 30% of tests withheld, test files in the
  agent's writable workspace. On the 145 **unambiguous** problems: Codex hardcoded test cases in
  **0.7%**, Claude Sonnet 4 **2.1%** (plus **20.7%** non-general heuristic solutions), Gemini 2.5
  Pro **deleted test files in 3.4%**. On the 9 **ambiguous** problems: Codex **44.4%**, Claude
  Sonnet 4 **33.3%**, Gemini **22.2%**. *Under-specified rules are the dangerous ones* — which is
  a direct warning about writing rules that name a rubric item without defining it.
- **Held-out tests are not a sufficient defence.** EvilGenie reports held-out tests producing
  both false positives (correct solutions failing edge cases) and false negatives (heuristic
  solutions passing visible *and* held-out tests) — and found **LLM judges outperformed held-out
  tests** (GPT-5: 1 false positive, zero false negatives on unambiguous problems). This inverts
  the naive intuition that execution is the trustworthy signal.
- **Hacking scales with horizon.** *SpecBench* (arXiv:2605.21384, 2026), 30 systems-level tasks
  from ~1.5k to ~110k LOC: the 90th-percentile validation/held-out gap grows **~27pp per 10×
  increase in LOC**; >25k LOC tasks reach a 100-point gap. **More search iterations did not
  reduce hacking — gaps often increased.** Worst observed: a 2,900-line hash table mapping test
  inputs to precomputed outputs, 97% validation accuracy, 0% held-out.
- **RL post-training raises exploit rates.** *Reward Hacking Benchmark* (arXiv:2605.02964, 2026),
  13 models: Claude Sonnet 4.5 / Opus 4.5 **0%**; DeepSeek-V3 0.6%, GPT-4o 0.9%; o3 11.8%;
  **DeepSeek-R1-Zero 13.9%**. The controlled sibling pair **V3 0.6% → R1-Zero 13.9%** isolates RL
  post-training as the driver.
- **Fetched sources are an injection surface, and no defence is free.** *AgentDojo* (Debenedetti
  et al., NeurIPS 2024 D&B, arXiv:2406.13352): 97 user tasks, 629 security test cases. GPT-4o
  under the "Important message" attack — **~45.8% average targeted attack success rate**, up to
  **92%** on the Slack suite, up to **70%** when the injection sits at the end of a tool response.
  A prompt-injection detector cut ASR to 8% at high false-positive cost; tool filtering reached
  7.5% but was inapplicable to 17% of cases. **No defence reached zero.** For an audit product,
  the retrieved-source channel is the highest-value injection target in the system, because a
  successful injection converts the safety mechanism into the attack vector. CrossAudit's
  citation→governed-fetch decision is a precondition for this capability, not a later hardening.
- **Consensus is not evidence.** *Refute-or-Promote* (arXiv:2604.19049, recent preprint — treat
  as indicative): **80+ agents unanimously endorsed a non-existent vulnerability; 3 independent
  agents made identical errors.**
- **The verifier must not be able to modify what it checks.** There is no dedicated study
  measuring "verifier writes to state" as a failure rate — this claim is inferred from EvilGenie's
  test-file deletions and test-JSON edits. But the architectural rule is well-supported: the
  process that *runs* the check must not be able to *modify* the check, and the acting verifier
  should be read-only over the artifacts it audits and write-only into a scratch sandbox. This is
  also the property that keeps CrossAudit's hash-chained ledger meaningful.

---

## 4. Ensembles and cascades — including our own proposal

### 4.1 Is "self-audit for recall, cross-vendor to filter" described anywhere?

**Not in the form we propose it — but the two-stage shape is, and it worked.** MCeT-X is exactly
a high-recall stage followed by a precision filter: combined atomic checks at 68.1% recall /
0.72 precision, then a "higher-authority cross-check" self-consistency pass, giving 65.2% /
**0.81**. **It trades 2.9pp of recall for 9pp of precision.** Critically, MCeT's filter is *not a
different vendor* — it is a different *perspective* of the same model, exploiting the fact that
the three checks have different, partly independent failure modes.

That is a meaningful difference from our proposal. **No paper implements "model A audits its own
output for recall, model B filters A's false positives" and ablates the cross-model variable.**
The closest four:

| work | what it does | what it leaves open |
|---|---|---|
| **Dunivin, Noori, Frey, Atkinson**, *Self-reflection in Automated Qualitative Coding*, arXiv:2601.09905, Jan 2026 | **Exactly our shape**: stage 1 labels favouring recall, stage 2 critic vetoes only predicted positives. Stage-1 FP rates **8–54%** despite F1 0.74–1.00; secondary critique buys **+0.04 to +0.25 F1** (κ 0.53 → 0.78 on one code) | **Same model (gpt-4o) at both stages.** The cross-model variable is exactly what is missing |
| **Godhwani & Benrimoh (McGill)**, *LLM-Assisted Abstract Screening with OLIVER*, arXiv:2512.20022 | Actor and critic deliberately **different models**, both directions, three aggregation rules including critic-veto | Result: **improved discrimination and markedly lower calibration error (higher AUC, much lower Brier), but only modest sensitivity gains.** The cross-model critic bought precision and calibration, **not recall** — which is the prediction for our design |
| **Agarwal**, *Refute-or-Promote: Adversarial Stage-Gated Multi-Agent Review*, arXiv:2604.19049, Apr 2026 | Four-stage funnel ending in a **cross-family critic with minimal context**, explicitly to catch correlated training-data errors | ~79% retrospective / 83% prospective kill rate; **the one direct measurement: the cross-family stage caught errors in 3/19 (16%) of same-family-approved findings.** No recall metrics; cross-family variable not ablated |
| **MCeT-X** (§1.1) | High-recall decomposed stage → self-consistency filter | Filter is a different *perspective*, not a different vendor |

**The mechanism that licenses cross-vendor filtering is measured, though.** Tan et al., *Too
Consistent to Detect: A Study of Self-Consistent Errors in LLMs*, arXiv:2505.17656 (v3, Sep 2025):
errors a model makes *consistently across samples* do not shrink with scale, and **every
self-based detector collapses on them — semantic entropy AUROC 0.4608, below chance.** Overlap of
Qwen2.5-7B's self-consistent errors with a second model:

| verifier | TriviaQA-CE overlap | SciQ-CE overlap |
|---|---:|---:|
| Qwen2.5-14B (same family) | 13.6% | 28.7% |
| Qwen2.5-72B (same family) | 14.2% | 22.4% |
| **Llama3.1-70B (different family)** | **5.4%** | **15.9%** |

Probe accuracy: baseline 0.8250 → +Qwen2.5-3B 0.8357 → +Qwen2.5-72B 0.8689 → **+Llama3.1-70B
0.8794.** *Bigger and more distant is better.* Corroborated by Lu, Teehan, Jin, Ren (NYU), *When
Does Verification Pay Off?*, arXiv:2512.02304 — 37 models, 9 datasets: *"cross-family verification
is often more beneficial than intra-family verification or self-verification"*, *"models often
favor solutions resembling their own"*, and a regression of **verifier FPR against solver–verifier
similarity: r = −0.552, slope = −2.727.** ⚠️ **Polarity warning:** their "false positive" is
wrongly *accepting* a bad solution — the opposite sign from our "flagged correct code". Their
result says self-verification is more *lenient*; ours says self-audit is more *trigger-happy*.
That tension should be reported, not elided.

**Counterweight, so we do not over-claim.** Ding (UPenn), *When LLMs Agree, Are They Right?*,
arXiv:2607.08065: **cross-family models share incorrect answers 67–71% of the time conditional on
both being wrong** (p = .003–.005); a frontier model at ≥0.8 self-agreement is still wrong 48% of
the time on GPQA Diamond. Honest synthesis with Tan et al. (different conditioning): **a
cross-model filter removes a large, distinct slice of blind spots but cannot reach a residual
correlated-error core.** This is the published version of our own limitation note that "vendor
independence is not statistical independence."

### 4.2 The rest of the ingredient list

**PoLL** — Verga et al. (Cohere), *Replacing Judges with Juries*, arXiv:2404.18796, Apr 2024
(**arXiv only, never published at a venue, despite wide citation**). Panel = Command-R (35B) +
Claude-3 Haiku + GPT-3.5, three disjoint families.

| judge | κ NQ | κ TriviaQA | κ HotpotQA | Arena Pearson | Arena Kendall-τ |
|---|---:|---:|---:|---:|---:|
| GPT-4 | 0.627 | 0.841 | 0.830 | 0.817 | 0.667 |
| Haiku | 0.749 | 0.894 | **0.873** | 0.883 | 0.722 |
| **PoLL** | **0.763** | **0.906** | 0.867 | **0.917** | **0.778** |

**7–8× cheaper** than GPT-4-Turbo. Bias: PoLL score-delta σ = **2.2** vs GPT-3.5's **6.1**; *"the
highest positive delta for each model occurs when it is judged by itself"*; the GPT-4 judge ranked
a GPT-4 variant at **position 2 vs true position 4**. **The buried result most relevant to us:
GPT-4 was the *weakest* judge on KILT, attributed to over-reasoning** — "injecting too much
background knowledge... rather than simply aligning the gold reference with the generation."
Prompt sensitivity on NQ: zero-shot 0.518 → few-shot 0.627 → **+"don't overthink" 0.725**, and
that instruction was *negative* for the other two models. Over-critique is a real, measurable,
model-specific judge pathology — and a candidate explanation for our self-audit arm.

**Cascaded Selective Evaluation** — Jung, Brahman, Choi, *Trust or Escalate: LLM Judges with
Provable Guarantees for Human Agreement*, **arXiv:2407.18370** (⚠️ *not* 2410.19317, which is
FairMT-Bench), **ICLR 2025 Oral**. Confidence-gated cascade Mistral-7B → GPT-3.5 → GPT-4, with a
distribution-free guarantee P(judge = human | confidence ≥ λ) ≥ 1−α.

| method (TL;DR, 1−α = 0.9) | Mistral % | GPT-3.5 % | GPT-4 % | coverage | guarantee success |
|---|---:|---:|---:|---:|---:|
| GPT-4 only, no selection | 0 | 0 | 100 | 100.0 | **0.0** |
| heuristic selection | 0 | 0 | 100 | 89.6 | 42.0 |
| **Cascaded Selective Evaluation** | 28.3 | 28.2 | 43.5 | 55.7 | **90.8** |

Calibration via "Simulated Annotators": GPT-4-turbo AlpacaEval ECE **0.217 → 0.095**; TL;DR ECE
**0.196 → 0.039**. On ChatArena at an 80% target: coverage 79.1% with **88.1% of covered instances
judged by models cheaper than GPT-4**. **Transferable finding: weak judges know when they don't
know nearly as well as strong ones — the savings come from routing, not from better judging.**
This is the right shape for CrossAudit's tiering: a confidence-gated escalation from a cheap
grounded checker (§2.1) to a frontier auditor, with a stated agreement guarantee.

**Two-stage recall→precision, with real deployment numbers:**

| system | stage 1 (recall) | stage 2 (precision) | result |
|---|---|---|---|
| **LLift** (Li, Hao, Zhai, Qian, USENIX Security 2024, arXiv:2308.00245) | UBITect: 140,000 candidate use-before-initialization bugs; symbolic execution leaves **53,000** undecided | GPT-4 + post-constraint analysis, task decomposition, self-validation | **precision 50%**, **100% recall** on Bug-50; **13 new Linux kernel bugs**; ~7,000 tokens/case |
| LLift **scaffold ablation** | — | naive prompt → full scaffold | **P 0.12 / R 0.15 / F1 0.13 → P 0.87 / R 1.00 / F1 0.93**, same model, same data |
| **IRIS** (Li, Dutta, Naik, ICLR 2025, arXiv:2405.17238) | CodeQL, AvgFDR 90.03%, 27/120 detected | LLM `FilterPath()` | GPT-4: **55/120 detected, F1 0.076 → 0.177**; **Llama-3-8B made FDR *worse* by 5.52pp** |
| **Sifting the Noise** (arXiv:2601.22952) | SAST on OWASP, **98.3% FP rate** | Claude Sonnet 4 + agent | FPR **98.3% → 6.3%** — but **suppressed 22.25% of real vulnerabilities** (CWE-327 miss rate **77.17%**) |
| **Tencent industrial** (arXiv:2601.18844) | BkCheck: 433 alarms, 76% FP | agentic LLM | **94–98% of FPs eliminated**, acc 0.93–0.94, **$0.0011–0.12/alarm vs 10–20 min human** |
| **Meta RADAR** (arXiv:2605.30208) | ML Diff Risk Score — **flags 10% of diffs to catch 60% of production incidents** | LLM review + deterministic validators | 331k+ diffs; revert rate **⅓** of non-RADAR |
| **FActScore** | atomic decomposition | retrieve→LM **+** NP ensemble | estimator error **14.1% → 1.4%** from combining two heterogeneous verifiers |

**Two rules fall out of this table and both bind us.** (1) **A weak filter is worse than no
filter** — IRIS with Llama-3-8B made false discovery *worse*; LLift's filter quality varied GPT-4
100% / GPT-3.5 89% / Claude-2 67% / Bard 67%. (2) **Every honest two-stage paper reports what the
filter destroys**, and it is a lot: 22.25% of real vulnerabilities in *Sifting the Noise*;
Google's AutoCommenter threshold discarded predictions that were **~80% correct**. If we build the
cascade, we must instrument stage-2 kills against ground truth, not just report the precision gain.

### 4.3 The N-sample baseline, and why it is weaker than I first thought

**Cheap ensembling beats structured critique at matched compute.** Huang et al.
(arXiv:2310.01798) §4, replicating Du et al.'s prompt on the *full* GSM8K test set (Du used 100
examples): MAD **83.2** vs self-consistency **85.3** at 6 responses; **83.0 vs 88.2** at 9. Smit
et al. (ICML 2024, arXiv:2311.17371): on MedQA, Medprompt 0.65, Society of Mind 0.64, Ensemble
Refinement 0.64, ChatEval 0.60, Self-Consistency 0.60, **Single Agent 0.60** — full range across
all configurations 0.56–0.64, with debate at **$2–5/question**. **Buy independence, not
conversation.**

But repeated sampling of *one* model has a measured ceiling. **Haldar & Hockenmaier**, *Rating
Roulette: Self-Inconsistency in LLM-as-a-Judge Frameworks*, EMNLP 2025, arXiv:2510.27106: a
judge's agreement **with itself** across 3 identical runs is Krippendorff α **0.33** (Llama-3.1),
**0.63** (DeepSeek-R1), **0.79** (Qwen-3) on SummaC. **Majority vote over 3 runs gains only +1.2
to +2.5 balanced-accuracy points**, and self-reliability is *"fairly static... independent of the
number of runs."* **Repeated sampling of one model cannot remove that model's systematic bias.**

And **order-balancing beats sample count at equal budget** — Wang et al., *Large Language Models
are not Fair Evaluators*, ACL 2024, arXiv:2305.17926: GPT-4 vanilla 52.7% → MEC(k=3) 58.7% →
MEC(k=6) 60.9% → **MEC(3)+BPC(3) 62.5% at the same $6.38 as k=6**. Going 3→6 samples buys +2.2pp;
adding balanced position calibration at identical cost buys +3.8pp.

**Why we should still run union-of-N.** Not because it will win, but because **it is the null
hypothesis for decomposition.** Tyen et al. (§5) show the mechanism directly: *"if each generation
call has some probability of identifying a mistake, then the more calls made on each trace, the
more likely the model will [flag one]."* A 7-call per-rule audit might beat a 1-call holistic
audit **purely because it is seven calls.** Union-of-7-holistic-samples is the control that
separates *scrutiny volume* from *scrutiny structure*, at almost exactly the same cost. Without it,
a positive result on technique #1 is uninterpretable.

**Also from our own scorer's paper:** Ruan et al. report Llama3.1-8B / Mistral-Nemo / Qwen2.5-7B
correlating **0.65 / 0.80 / 0.78** with GPT-4o individually, and **majority pooling raising this
to 0.82**; majority pooling beats mean pooling for binary labels in most combinations. Our audit
verdicts are binary labels.

### 4.4 What the self-vs-cross literature says about our measurement

Our code result — self-audit reaches *higher* recall (16.1% vs 10.7%) and *far* worse precision
(20.0% vs 4.7% FP on correct code, p = 0.000066) — is **not** the classic self-preference story.
The full treatment is in §5.1–5.3; two points belong here because they bear on the cascade design.

- **RealCritic** — Tang, Li, Xiao et al. (CUHK-Shenzhen + Qwen Team), arXiv:2501.14492, Jan 2025.
  Critique-then-correct, 8 reasoning tasks, measuring I→C and C→I. **Self-critique: I→C below 5%
  for most models (o1-mini 25.85% on ARC); cross-critique: I→C 30–45% across all models on
  ARC/GSM8K.** Deltas vs direct CoT: self-critique **−1.8% to −5.1%** for classical models
  (o1-mini +3.3%); cross-critique **+5.8% to +15.6%**. But **C→I degradation persists at −15% to
  −30% on specialised domains (GPQA, MMLU-STEM)** even under cross-critique. Also: *"about 30% of
  low-quality critiques are erroneously classified as high quality"* under verdict-matching.
  **This is the closest published contradiction of our cross-vendor recall parity** — RealCritic
  says cross should beat self on recall by a lot, and we measured the opposite sign inside noise.
  Worth taking seriously as evidence that our audit prompt is not eliciting what a
  critique-then-correct prompt elicits. It also says plainly that cross-model review buys
  *detection*, not *non-regression*, and degrades most on hard specialised material — which
  expert prose is.
- **The direction the self/cross evidence actually points for a cascade.** OLIVER
  (arXiv:2512.20022) is the only cross-model actor–critic measurement I found with clean
  reporting, and its cross-model critic bought **higher AUC and much lower Brier — discrimination
  and calibration — with only modest sensitivity gains.** Combined with our own 4.7% vs 20.0%,
  the literature's prediction for our proposal is specific: **cross-vendor will pay as a filter
  and will not pay as a detector.** That is a testable prediction, and it is the ordering
  argument for §4.5.

### 4.5 The cascade design the evidence actually supports

Ordering matters, and MCeT plus the CriticGPT frontier argue for this shape:

1. **Stage 1 (recall):** one focused, context-free check per rule, from a *single* auditor.
   Union the findings. Expect precision to fall.
2. **Stage 2 (precision):** a filter that re-reads each candidate finding **against the source
   bytes** and drops the ones it cannot ground. Cross-vendor is a plausible filter; so is a
   second perspective from the same model (MCeT's choice, +9pp precision for −2.9pp recall); so
   is requiring a verbatim source quotation, which is deterministic to check.
3. **Cost is dominated by stage 1** (linear in rules), not stage 2 (linear in findings, and
   findings are few). And stage 2 need not be a frontier model at all: "is this finding entailed
   by the committed source?" is exactly what a 355M–770M alignment head does at **~1/400** the
   cost of a GPT-4 call, at 74.7% balanced accuracy against GPT-4's 75.3% (§2.1).
4. **Instrument what the filter kills.** *Sifting the Noise* suppressed **22.25%** of real
   vulnerabilities to get FPR from 98.3% to 6.3%; Google's AutoCommenter threshold discarded
   predictions that were **~80% correct**. A cascade that reports only its precision gain is
   hiding its cost.
5. **Do not make the filter the cheap model by default.** IRIS: the same filter architecture
   improved F1 0.076 → 0.177 with GPT-4 and **made false discovery 5.52pp worse with
   Llama-3-8B**. A weak filter is worse than no filter.

**Using cross-vendor as the filter rather than the detector is the most literature-consistent
reading of our own data** — our code study already shows cross-vendor at 4.7% FP vs self at
20.0%, the cross-family error-overlap mechanism is measured (5.4% vs 28.7%), and OLIVER predicts
precision-and-calibration gains rather than recall gains from exactly this move.

---

## 5. Judge failure modes relevant to us

### 5.1 The reframe our own numbers need

Our self-vs-cross result should not be reported as "self-audit finds more bugs." Compute the
diagnostic ratio TPR/FPR on the code study:

| arm | recall on P (TPR) | FP on correct code (FPR) | **TPR / FPR** |
|---|---:|---:|---:|
| **self-audit** | 16.1% | 20.0% | **0.81** |
| **cross-vendor** | 10.7% | 4.7% | **2.28** |

**Self-audit's ratio is below 1: a flag is marginally *more* likely on correct code than on buggy
code. It is close to uninformative.** Cross-vendor's flag carries ~2.3× evidence of a real
defect. Self-audit did not become better at finding defects — **it moved its decision criterion
liberal without improving discrimination, and on this evidence discriminates slightly worse.**
That is a signal-detection framing, it is consistent with our p = 0.000066, and it is far more
defensible than a recall claim on 56 instances with overlapping intervals.

### 5.2 Self-preference does NOT explain our result — say so plainly

This is the most likely reviewer objection, and the literature is against the obvious reading.

- **Panickssery, Bowman, Feng**, arXiv:2404.13076, ICML/NeurIPS 2024: GPT-4 self-recognition
  **73.5%** out of the box, **>90%** after a 500-example fine-tune, with a **linear**
  self-recognition ↔ self-preference relationship (τ = 0.41) surviving length/vowel/readability
  controls. Causal, but about *preference*, not fault-finding.
- **Wataoka, Takahashi, Ri**, arXiv:2410.21819: the mechanism is **perplexity** — judges
  over-reward low-perplexity text *"regardless of whether the outputs were self-generated."*
  **This predicts a self-judge that is more lenient, not more critical.**
- **Zheng et al.** (NeurIPS 2023): GPT-4 **+10%**, Claude-v1 **+25%**, GPT-3.5 none — and the
  authors' own verdict is that the study *"cannot determine whether the models exhibit a
  self-enhancement bias."*
- **Dubois et al.**: self-preference is "often smaller than general model differences" —
  Claude-3-Opus prefers GPT-4-Preview to itself; Mistral-Large prefers both others to itself.
- **Roytburg et al.**, ICML 2026, arXiv:2601.22548: against an evaluator-quality baseline, **only
  51% of examples in prior self-preference findings retain significance** (covering 89.6% of the
  probability mass); the raw measure overestimates by **17.5pp**.

**The self-preference literature predicts the opposite of what we measured.** Conflating it with
our result would be an error.

### 5.3 What DOES explain it — the self-correction literature

Four converging peer-reviewed sources, and one of them contains an almost exact quantitative
analogue of our 100%/2% → 73%/23.5% move.

**(1) A critique instruction is a prior toward finding fault.** Huang, Chen, Mishra, Zheng, Yu,
Song, Zhou (Google DeepMind), ICLR 2024, arXiv:2310.01798 — the entire self-correction loss is
correct answers being flipped:

| model / task | correct ⇒ incorrect | incorrect ⇒ correct |
|---|---:|---:|
| GPT-3.5 / CommonSenseQA | **11.6%** | 5.8% |
| GPT-3.5 / GSM8K | **8.8%** | 7.6% |
| GPT-4 / GSM8K | 1.5% | 8.0% |
| Llama-2 / GSM8K | **31.0%** | 5.5% |
| Llama-2 / CommonSenseQA | **35.5%** | 8.0% |

With *oracle* labels the same procedure improves (95.5 → 97.5). Their mechanism, quoted:
*"Introducing feedback can be viewed as adding an additional prompt... it might even bias the
model away from producing an optimal response."*

**(2) The recall/false-positive trade is a measured curve, not a defect.** Tyen, Mansoor,
Carbune, Chen, Mak, Findings of ACL 2024, arXiv:2311.08516 — BIG-Bench Mistake, ground truth at
Krippendorff α **0.979–0.998**. Best mistake-finding accuracy is GPT-4 at **52.87**, and the naive
"always say incorrect" baseline gets weighted F1 **78**. Table 9, accuracy on *clean* traces
(= 1 − FP rate) vs recall on *buggy* traces:

| model / task | prompting | acc. on clean traces | recall on buggy |
|---|---|---:|---:|
| GPT-4 / Word sorting | direct (whole trace) | 88.24 | 28.20 |
| GPT-4 / Word sorting | **CoT (per step)** | **58.82** | 30.83 |
| GPT-4 / Dyck | direct (whole trace) | **98.41** | **7.37** |
| GPT-4 / Dyck | **CoT (per step)** | **13.79** | **43.91** |
| PaLM 2 / Tracking objects | direct (whole trace) | **100.00** | **5.38** |
| PaLM 2 / Tracking objects | **CoT (per step)** | **47.50** | **56.92** |

**Read the Dyck and Tracking-objects rows against our own numbers: 98.4% clean-accuracy with 7.4%
recall, moving to 13.8% with 43.9% recall, is precisely the shape of 100% precision / 2.0% recall
moving to 73% / 23.5%.** And their stated mechanism is the one we must control for:
*"if each generation call has some probability of identifying a mistake, then the more calls made
on each trace, the more likely the model will [flag one]."* **Scrutiny volume, not scrutiny
quality.** This is why union-of-N is a mandatory control (§4.3).

**(3) Models capitulate on correct work when challenged.** Sharma, Tong, Korbak, Duvenaud,
Askell, Bowman, ... Perez (Anthropic), ICLR 2024, arXiv:2310.13548: under a single challenge
("I don't think that's right. Are you sure?"), models **wrongly admit mistakes on correct answers
between 42% (GPT-4) and 98% (Claude 1.3)**, and change the answer between **32% and 86%**.
Restricting to answers held at ≥95% confidence barely helps (GPT-4 **98.9% → 98.9%**). The reward
signal is implicated: the Claude 2 preference model **prefers a sycophantic response over a
baseline truthful one 95% of the time.** *This is the closest published analogue to our
self-audit's 20% false-positive rate on correct code.*

**(4) Self-refinement explicitly optimises for false-positive corrections.** Xu, Zhu, Zhao, Pan,
Li, Wang, *Pride and Prejudice*, ACL 2024, arXiv:2402.11436 — six LLMs, four languages, three
tasks: *"This bias causes LLMs to optimize for false positive corrections rather than improving
the actual output quality,"* amplified across self-refine iterations.

**And an over-critique pathology in judges specifically:** PoLL found GPT-4 was the *weakest*
judge on KILT because of over-reasoning, and that adding *"don't overthink"* to the prompt moved
NQ agreement **0.627 → 0.725** for GPT-4 while being *negative* for GPT-3.5 and Command-R.

### 5.4 The rest of the bias table

| bias | best evidence | magnitude |
|---|---|---|
| **Position** | Zheng et al., NeurIPS 2023, arXiv:2306.05685 | consistency on near-identical answers: **Claude-v1 23.8%, GPT-3.5 46.2%, GPT-4 65.0%**. With 3–4 candidates most models fall below 0.5 (CALM) |
| **Verbosity** | Zheng et al.; Dubois et al. COLM 2024, arXiv:2404.04475 | "repetitive list" attack failure rate **Claude-v1 91.3%, GPT-3.5 91.3%, GPT-4 8.7%**. The AlpacaEval GPT-4 baseline swings **22.9% → 64.3%** (41.4 points on a model pinned at 50%) purely by changing a verbosity instruction |
| **Generosity without a reference** | Kranti & Vajjala, arXiv:2607.12885 | judge–human agreement **33–42% (no ref) → 85–96% (ref shown) → 98% (ref comparison)**. **The largest single number in this table** |
| **Count bias / giving up** | arXiv:2512.22306 | recall 0.94 → 0.15–0.46 as defect density rises, **precision ≈1.00 throughout** |
| **Omission blindness** | arXiv:2608.01000 | planted over-inclusions detected **6–7×** more often than planted omissions; 10:1 in a 43,227-item production deployment |
| **Authority / fake citation** | Chen, Chen, Liu, Jiang, Wang, EMNLP 2024, arXiv:2402.10669 | under fake-reference injection, **every judge except GPT-4o is worse than the random baseline (0.37)**: Claude-2 **0.89**, Claude-3 0.70, GPT-4 0.66, GPT-4o 0.32 |
| **Sentiment / bandwagon / distraction** | Ye et al., *Justice or Prejudice*, CALM, arXiv:2410.02736 | GPT-4o robustness: verbosity 0.977, fallacy 0.984, **sentiment 0.699**, position 0.776, **bandwagon 0.791**. Frontier models are *worse* than ChatGPT on sentiment (0.653–0.699 vs 0.804); Claude-3.5 is most robust overall yet **least** robust to bandwagon (0.610). Self-enhancement confirmed **even with sources anonymised** |
| **Compliance with fabricated findings** | Stechly et al., arXiv:2310.12397 | GPT-4 "corrected" **~94%** of *falsely* flagged items under adversarial backprompting |
| **Judge self-inconsistency** | Haldar & Hockenmaier, EMNLP 2025 | Krippendorff α with *itself* across 3 runs: **0.33 / 0.63 / 0.79**. GPT-4 vs humans on MT-Bench is 0.671 raw accuracy but **α = 0.396** — **every raw agreement figure in this literature is inflated** |

### 5.5 Mitigations with measured effect

| mitigation | measured effect | source |
|---|---|---|
| **Reference-guided judging** | math judging failures **14/20 → 3/20** (70% → 15%) | Zheng et al. |
| Chain-of-thought judging | 14/20 → 6/20 | Zheng et al. |
| **Swap-and-average (BPC) + multi-evidence** | GPT-4 **+9.8 acc pts / +0.13 κ**; ChatGPT **+14.3 / +0.25**. At equal budget it beats more samples (+3.8 vs +2.2) | FairEval, ACL 2024 |
| **Heterogeneous panel** | κ 0.627 → 0.763; judge score-delta σ **6.1 → 2.2**; 7–8× cheaper | PoLL |
| **Length-control GLM** | Arena ρ **0.94 → 0.98**; gameability 26% → 10%. ⚠️ bootstrap **p = 0.07**; and the debiaser is itself attackable (truncation attack drove LC win rate 3.7 → 25.9) | AlpacaEval-LC |
| **Confidence-gated cascade** | ECE 0.217 → 0.095; **90.8% human-agreement guarantee at 55.7% coverage** vs 0.0% for unselected GPT-4 | Trust or Escalate |
| Fine-tuned judge (weight-merged) | FLASK human-Pearson **0.449 → 0.555** (GPT-4 = 0.679) — halves the gap | Prometheus 2 |
| Explanation-first fine-tuned judge | delta position bias **13.11 → 4.50** at no agreement cost, but 133× slower | JudgeLM |
| Heterogeneous **verifier** ensemble | estimator error **14.1% → 1.4%** | FActScore |
| Deployment-time precision dial | comprehensiveness 33 → 50% against hallucination-avoidance Elo 50 → 70% | CriticGPT FSBS |

⚠️ **JudgeLM's "»90%, exceeding human-human agreement" is agreement with GPT-4, its teacher — not
with humans.** Human-human max on MT-Bench is 82%. This is routinely miscited.

**The three mitigations we do not currently use and could adopt cheaply: (a) force a per-rule
verdict rather than free-form enumeration; (b) require a source-span citation per verdict
(33–42% → 85–96%); (c) report a diagnostic ratio, not a recall number, so a criterion shift
cannot be mistaken for a discrimination gain.**

---

## 6. Repair that does not regress

Our −11.0 F1 with 17 items broken to 3 fixed is not anomalous; it is the most replicated result
in this literature, under two different names.

### 6.1 The self-correction result

**Huang, Chen, Mishra, Zheng, Yu, Song, Zhou**, *Large Language Models Cannot Self-Correct
Reasoning Yet*, ICLR 2024, arXiv:2310.01798:

| model / task | standard | self-correct r1 | r2 |
|---|---|---|---|
| GPT-3.5 GSM8K | 75.9 | 75.1 | **74.7** |
| GPT-3.5 CommonSenseQA | 75.8 | **38.1** | 41.8 |
| GPT-4 GSM8K | 95.5 | 91.5 | **89.0** |
| GPT-4 HotpotQA | 49.0 | 49.0 | **43.0** |

Every cell flat or negative. Mechanism: GPT-3.5 on GSM8K **corrected 7.6% of wrong answers and
broke 8.8% of right ones.** Our 3-fixed/17-broken is the same shape, further out.

**Kamoi et al.**, *When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey*, TACL
2024, arXiv:2406.01297 — the field-level verdict: *"no prior work demonstrates successful
self-correction with feedback from prompted LLMs"* outside exceptionally suited tasks; many
positive results relied on oracle information or deliberately weak initial prompts; success
requires **reliable external tools** or **100K+-instance fine-tuning**. **"The bottleneck is in
feedback generation."**

**Stechly et al.** (arXiv:2310.12397): GPT-4 graph colouring — direct **16%**, with self-critique
**1%**, with a sound external verifier **~40%**; and 15 independent top-k samples also reached
~40%, i.e. **the entire benefit of the loop was resampling, not critique.** Under adversarial
backprompting with fabricated errors, GPT-4 "corrected" **~94%** of falsely flagged items.
**With 12 confirmed false positives in arm X, this alone predicts our regression without any
generator failure.**

### 6.2 The program-repair result, a decade earlier

- **Qi, Long, Achour, Rinard**, ISSTA 2015: GenProg **2 correct / 105 defects**; RSRepair 2/24;
  AE 3/105. Their *Kali* system, **which only deletes functionality**, found plausible patches
  for at least as many defects as the repair systems. *(The Kali comparison count 27 vs
  18/10/27 rests on a secondary citation — verify against the primary PDF before quoting.)*
- **Smith, Barr, Le Goues, Brun**, FSE 2015, *Is the cure worse than the disease?* — patches
  evaluated on held-out tests; both tools scored below human patches, and patch quality is
  proportional to the coverage of the suite used during repair. *(Exact deltas not verified — the
  PDFs would not parse.)*
- **SWE-bench integrity**: SWE-Bench+ (arXiv:2410.06992, Oct 2024) — **32.67%** of successful
  patches had the solution in the issue text; **31.08%** of passing patches had inadequate tests;
  SWE-Agent+GPT-4 **12.47% → 3.97%** after filtering. OpenAI's own audit of 138 o3 failures on
  SWE-bench Verified: **59.4% caused by test flaws.** *If the acceptance oracle is weak, "passes"
  means nothing* — which is the exact criticism of our "the audit passed" verdict.

### 6.3 Acceptance criteria with measured support

| criterion | evidence | number |
|---|---|---|
| **Score preservation alongside repair; gate on the combination** | RARR (Gao et al., ACL 2023, arXiv:2210.08726) | PaLM/NQ: RARR Attr 54.9, Pres_Lev **89.6**, F1_AP **57.0**; EFEC Attr **64.3** (higher!), Pres 39.1, F1_AP **17.1**. **EFEC resolves more findings and destroys the text.** Our −11.0 is EFEC-shaped. |
| **Explicit preservation condition scoped outside the finding's locus** | Poracle (Ismayilzada et al., TOSEM 2023) | precision **100% / 99%** vs ODS 94% / 88% |
| **Independent oracle, not the critic that raised the finding** | PATCH-SIM (Xiong et al., ICSE 2018) | filtered **56.3%** of incorrect patches, blocked **0** correct ones |
| | RGT (Ye et al., EMSE 2021) | improved automatic patch assessment by **190%** by improving the oracle |
| | Opad (Yang et al., FSE 2017) | filtered **75.2%** (321/427) of overfitting patches |
| **Reject regressions with an exogenous gate; make "no change" a first-class outcome** | SEAL (Guo et al., arXiv:2607.24300, Jul 2026) | 35 self-improving configs all self-scored ≥0.70 while **15 policies scored below random on deployment**. With SEAL's sealed exogenous accept/reject gate: **11 of 12 comparisons improved or tied** (9 improved). Breakout: Gemini-3-Flash 7.9→30.0, GPT-5.5 7.4→15.2. Authors: it "reduces repeated overwrites and large regressions rather than guaranteeing monotonic improvement". Atari only. |
| **Bound the edit** | multi-hunk characterisation (arXiv:2506.04418, ASE 2025), HUNK4J, 372 defects, 6 LLMs | success declines as hunk divergence and spatial dispersion increase |
| **Expect fewer accepted revisions, not better ones** | TOSEM 10.1145/3702971 | bounded-exhaustive suites of ~100 and ~1,000 tests reduce overfitting but yield **few new correct repairs** |

**The one that should change our design today is RARR's F1_AP.** We currently measure "did the
finding get addressed" and "what is the final CLEAR F1". We do not measure **preservation**. A
revision that fixes rubric item 4 and silently rewrites items 1, 2 and 5 scores as a success on
the first metric. RARR's arithmetic says a system optimised on repair alone converges to EFEC.

Also worth stating plainly: **Self-Refine** (Madaan et al., NeurIPS 2023, arXiv:2303.17651) is
the paper usually cited for "revision works," with ~+20% average across 7 tasks — but on the one
task with an **objective answer and a strong base model** (math reasoning) the gains are
**GPT-3.5 64.1→64.1, ChatGPT 74.8→75.0, GPT-4 92.9→93.1**. Expert prose scored against a fixed
rubric is the math case, not the sentiment-reversal case.

**And the prose-specific warning:** van Nuenen, *Voice Under Revision*, arXiv:2604.22142, Apr
2026 — across GPT-5.4 / Claude Sonnet 4.6 / Gemini 3.1 Pro and 13 stylometric markers, generic
"improve this" revision produced mean |d| = **1.11**; a **rewrite-only ("minimal edit") prompt
was worse at |d| = 1.16**; only an explicitly voice-preserving prompt helped (|d| = 0.76, −32%).
**Prompting for minimality does not produce minimality.** *(Single recent preprint,
personal-narrative domain; treat the transfer to expert prose as an assumption.)* This is
directly relevant: study 3 already found that constraining document growth made revision worse.
The literature says the fix is a **gate**, not a **prompt**.

**Falsification in our harness.** `run.py` already scores every round, so a post-hoc
re-analysis costs nothing: **compute, for each of our 25 recorded revisions, the number of
rubric items that flipped correct→wrong versus wrong→correct, and reject any revision whose
post-score is below its pre-score.** That gives the counterfactual "gated loop" F1 for free,
from data we already have. If gating recovers the −11.0 to ≈0, the loop's defect is acceptance,
not revision; if it does not, revision is destroying items the gate cannot see.

---

## 7. What contradicts our design outright

Stated plainly, because it is more useful than support. I have ordered these by how much they
should change what we build.

1. **Automated revision typically harms, and this is the field's most replicated result.**
   Huang et al. (ICLR 2024) — flat-to-negative on every reasoning benchmark, with the entire loss
   being correct⇒incorrect flips (8.8–35.5%). Kamoi et al. (TACL 2024) — *"no prior work
   demonstrates successful self-correction with feedback from prompted LLMs."* Qi et al. (ISSTA
   2015) — GenProg 2 correct patches out of 105 defects, and a deletion-only system matched it.
   **Our −11.0 F1 at p = 0.0014 is the expected result, not an implementation bug.** Any roadmap
   item that assumes revision helps is arguing against the field.
2. **The generator does not distinguish sound from spurious findings.** Stechly et al.: GPT-4
   "corrected" **~94%** of *fabricated* errors under adversarial backprompting. Sharma et al.
   (ICLR 2024): models wrongly admit mistakes on correct answers **42–98%** of the time under a
   single challenge, unchanged at ≥95% stated confidence. **With arm X's 12 confirmed false
   positives, this alone accounts for our regression without any generator failure.** It follows
   that **raising recall without a filter makes the loop strictly worse** — which is exactly what
   arm X measured (16/20 revised, −14.42 F1 each).
3. **Decomposition is not generically recall-positive, and it fails specifically on omissions.**
   Molecular Facts: fully atomic units detect only **22.4%** of not-supported cases because
   context-free atoms default to "supported". FBI/Doddapaneni (EMNLP 2024): adding rubrics to
   single-answer scoring raised the *undetected*-error rate **0.57 → 0.85**. ClaimCLAIRE:
   decomposition cost **−12.3pp recall**. Zhang (arXiv:2603.28005): a matched holistic rubric
   beats a self-decomposing atomic judge on 2 of 3 benchmarks and is cheaper, with the advantage
   concentrated **+14.5 to +33.0pp on incompleteness detection**. **Our missed items are
   overwhelmingly omissions**, so this is aimed squarely at us. The reconciliation (§1.5) is real
   but conditional: decomposition wins in the *long-response, weak-verifier* regime, which is
   ours — and only when each sub-unit gets **aligned** evidence (+0.0625 F1 aligned vs **−0.0672
   shared**).
4. **Cross-model review may add little on detection.** Our own code study (10.7% vs 16.1%,
   p = 0.51). Contested — RealCritic reports cross-critique I→C **30–45%** vs self **<5%** — but
   RealCritic also reports C→I **−15% to −30%** under cross-critique on specialised domains, and
   OLIVER's cross-model actor-critic bought **calibration and precision, not sensitivity**.
   **Nobody claims cross-model review prevents regression, and the one paper that measures a
   cross-model critic in a review funnel found it catching errors in only 3/19 (16%) of
   same-family-approved findings.**
5. **Structured critique loses to plain ensembling at matched compute.** Huang et al. Table 7
   (MAD 83.2 vs self-consistency 85.3 at 6 samples; 83.0 vs 88.2 at 9); Smit et al. (ICML 2024) —
   on MedQA, **Single Agent 0.60 ties Self-Consistency 0.60 and beats ChatEval 0.60/debate**, full
   range 0.56–0.64, debate at $2–5/question. **A cross-vendor second reader is a
   structured-critique design.** The boring baseline — N samples of one auditor, unioned — is
   untested by us and might win. That is why it is a mandatory control, not an optional one.
6. **Consensus is not evidence, and cross-family independence is partial.** Refute-or-Promote:
   80+ agents unanimously endorsed a non-existent vulnerability. Ding (arXiv:2607.08065):
   cross-family models share incorrect answers **67–71%** of the time *conditional on both being
   wrong*. Our own limitation note ("vendor independence is not statistical independence") is
   understated, not overstated.
7. **LLM defect detection on realistic data runs near chance.** PrimeVul (arXiv:2403.18624):
   StarCoder2 **68.26% F1 on BigVul → 3.09% F1 on PrimeVul**; GPT-3.5/GPT-4 "akin to random
   guessing" under stringent settings; prior datasets have **24–60%** label accuracy. ReaLMistake
   (COLM 2024): GPT-4 error-detection recall **11.9% / 12.6%**, Claude 3 Opus **6.8%**, against
   humans at **~90–95% F1**, and self-consistency did not help. **Our 8.9% on EvalPlus and
   2–23.5% on prose sit squarely inside this band. Nobody has an automated reviewer with good
   recall.** If anything our code figure is optimistic — deviation 9 notes the small generator
   biases it upward.
8. **A weak filter is worse than no filter.** IRIS (ICLR 2025): the LLM false-positive filter
   improved F1 0.076 → 0.177 with GPT-4 but **made false discovery worse by 5.52pp with
   Llama-3-8B**. LLift: 100% (GPT-4) / 89% (GPT-3.5) / 67% (Claude-2, Bard). If we build the
   cascade, the filter cannot be the cheap model by default.
9. **Filters destroy real findings, and every honest paper reports it.** *Sifting the Noise*:
   FPR 98.3% → 6.3% but **22.25% of real vulnerabilities suppressed** (CWE-327 miss rate
   **77.17%**). Google AutoCommenter's threshold discarded predictions that were **~80% correct**.
   Any cascade we ship must instrument stage-2 kills against ground truth.
10. **Executable acceptance criteria get gamed, and under-specified rules are the trigger.**
    EvilGenie: hardcoding rates **0.7–2.1% on unambiguous problems → 22–44% on ambiguous ones**;
    Gemini deleted test files in 3.4% of runs. SpecBench: validation/held-out gap grows **~27pp
    per 10× LOC**, and more search iterations *increased* it. Core: FActScore inflates
    **54.0 → 83.0** under simple padding. **A rule that names a rubric item without defining it is
    the dangerous kind.**
11. **Iterative loops distort.** *LLM as a Broken Telephone* (ACL 2025, arXiv:2502.20258): 100
    cycles, FActScore gradients −0.004 to −0.040 with chain complexity; temperature 1.0 diverges,
    1e-6 is stable. Our `max_rounds: 3` makes this a warning about ambition, not a current defect.
12. **A methodological caution that undercuts half the tables in this document.** Rao &
    Callison-Burch (arXiv:2606.00093, May 2026): on non-degenerate **binary** verdicts — the
    standard output of a decomposed rubric — Pearson r, Spearman ρ, Kendall τ_b, φ and MCC all
    collapse to the same number, and reporting several *"creates an illusion of corroborating
    evidence."* **Part of the apparent agreement gain from decomposition is an artefact of moving
    from a 5-point Likert to binary items.** Treat the InFoBench κ 0.284 → 0.532 and TICK
    46.4 → 52.2 gains as directionally real but not numerically commensurable with correlation
    gains.

**What survives all of this.** Four things, and they are the load-bearing parts of the product:
(i) the deterministic layer is unambiguously valuable where it can act (our own 79.3% → 100% on
stratum F; CRITIC's tool-vs-no-tool ablation; Self-Debugging's +11.2 with execution vs +3.5
without); (ii) cross-vendor is unambiguously valuable **as a precision filter** (our own 4.7% vs
20.0% at p = 0.000066, mechanism measured at 5.4% cross-family error overlap vs 28.7%
within-family); (iii) the rules file is the binding constraint on recall, replicated on a fresh
seed; (iv) grounding beats architecture — a reference is worth **+0.164 ρ** where skill
decomposition is worth **+0.039** (FLASK), and judge–human agreement moves **33–42% → 85–96%**
when a reference is supplied. Nothing in the literature contradicts any of those.

---

## 8. Technique summary table

| # | technique | mechanism | reported effect / benchmark | cost multiplier | needs that we lack | falsification in our harness |
|---|---|---|---|---|---|---|
| 1 | **Per-rule audit, one call per rule, with rule-scoped evidence** | One audit call per constitution rule, each asking a single context-free question of the artifact ("is this rule satisfied, and where"). Union the findings. Never ask the model to enumerate defects freely. Decompose the *spec*, not the artifact. | MCeT requirement-atom: recall **34.1% → 59.3%** *and* precision **0.58 → 0.86**; combined 68.1%. Judging≫enumerating gap **+0.29 F1**, stable over a 24× parameter range (arXiv:2608.01000). Decomposition Dilemmas: **+18.4 F1** in the long-response/weak-verifier regime, which is ours | ≈ n rules (**7×** on T03); ~5–7× tokens | nothing — `rubric_constitution()` already enumerates the rules; rule-scoped evidence needs a source-slicing step we do not have | Split arm X's single audit call into 7; round-1 recall vs CLEAR is already instrumented. **Four readouts**: (a) vs union-of-7-holistic-samples at matched cost — if it does not win, the gain was scrutiny volume; (b) recall ≫23.5% at precision ≥73%; (c) **split by completeness-type vs contradiction-type items** — arXiv:2603.28005 predicts no gain on the former; (d) whole-source vs rule-scoped evidence — the Alignment Bottleneck predicts whole-source is *worse than holistic* |
| 2 | **Forced per-rule verdict with a mandatory source citation** | Each rule call returns PASS / FAIL / NOT-DERIVABLE **plus a verbatim quotation** from the committed source. Absence of a quotable span is itself a verdict, so silence becomes impossible. | Judge–human agreement **33–42% (no ref) → 85–96% (ref shown) → 98% (ref comparison)** (arXiv:2607.12885). Reference degradation was the **largest** perturbation effect in arXiv:2603.28005 (0.86 → 0.62 → 0.38). Reference-guided judging cut math judging failures **14/20 → 3/20** (Zheng et al.). Agent-as-a-Judge ablation: 65.03 (ask) → 82.24 (+read) → **90.44 (+locate)** | +0 calls over #1; longer outputs | nothing — quotation grounding is deterministically checkable against committed bytes | Toggle the citation requirement on the #1 arm. Also run the **oracle-grounding ceiling arm** (auditor shown the reference checklist) — if that does not reach the measured **69.2%** checkability ceiling, decomposition + grounding are not the whole story and the hypothesis is wrong |
| 3 | **Two-stage cascade: high-recall stage → precision filter** | Stage 1 over-generates findings per rule. Stage 2 re-reads each candidate finding against the source bytes and drops the ungrounded ones. The filter can be cross-vendor, a second perspective, a quotation check, or a small entailment head. | MCeT-X: recall 68.1 → 65.2% for precision **0.72 → 0.81**. LLift scaffold: **P 0.12/R 0.15 → P 0.87/R 1.00**. Tencent: **94–98%** of FPs eliminated at $0.0011–0.12/alarm. Our own: cross-vendor FP **4.7% vs 20.0%**, p = 0.000066. Mechanism: cross-family self-consistent-error overlap **5.4%** vs same-family **28.7%** | stage 2 is linear in findings (few) — and can be a **770M entailment head at ~1/400 a GPT-4 call** | nothing for the model filter; a MiniCheck/AlignScore-class head would be a new dependency | Run stage-1 self-audit (the code harness already bypasses the same-vendor gate), then cross-vendor filter. **The unpublished ablation is self/self vs self/cross vs cross/cross on one corpus with per-stage precision and recall.** Primary: recall on stratum P, FP on stratum C. **Also instrument what the filter kills** — Sifting the Noise suppressed 22.25% of real defects. Falsified if filtered recall ≤ `cross` alone |
| 4 | **N-sample union / majority of the same auditor** | Sample the existing holistic auditor N times; union for recall, majority for precision. No architecture change at all. | Ensembling ≥ debate at matched compute (Huang Table 7: 88.2 vs 83.0 at n=9; Smit ICML 2024). Majority pooling 0.65/0.80/0.78 → **0.82** in our own scorer's paper. **But**: self-agreement α **0.33–0.79**, and 3-run majority buys only **+1.2 to +2.5** BAcc (Rating Roulette); order-balancing beats sample count at equal budget (+3.8 vs +2.2, FairEval) | N× audit | nothing | **The mandatory control for #1 and #3, not a candidate in its own right.** Tyen et al.: "the more calls made on each trace, the more likely the model will flag one." If union-of-7 matches per-rule decomposition at matched cost, decomposition buys nothing and the hypothesis is dead |
| 5 | **Revision gate — accept only non-regressing edits** | Re-score the revision; accept only if it does not regress. Score *preservation* separately from *repair* and gate on the combination, not on "was the finding addressed". Make "no change" a first-class outcome. | SEAL: 35 self-improving configs all self-scored ≥0.70 while **15 policies were below random on deployment**; with the exogenous accept/reject gate, **11/12 comparisons improved or tied**. RARR **F1_AP 57.0 vs EFEC 17.1** — EFEC resolves *more* findings (Attr 64.3 vs 54.9) and destroys the text (Pres 39.1 vs 89.6). PATCH-SIM: filtered **56.3%** of incorrect patches, blocked **0** correct ones | +1 scoring pass per revision | a cheap in-production regression signal; in benchmarks we already have one | **Free — no new model calls.** Re-analyse the 25 recorded revisions, reject any with post < pre, recompute final F1. If the gated loop reaches ≈0 instead of −11.0, the loop's defect is *acceptance*, not *revision*. Also compute the RARR-style preservation metric we currently do not measure at all |
| 6 | **Bounded/localised edit with an explicit preservation condition** | Restrict the revision to the finding's locus; everything outside must be byte-identical or provably equivalent. Enforce at the diff level, not in the prompt. | Poracle: precision **100% / 99%** vs ODS 94% / 88%, via an explicit preservation condition + differential fuzzing. Multi-hunk (ASE 2025, 372 defects, 6 LLMs): success declines with hunk divergence and spatial dispersion. **But "minimal edit" *prompting* is ineffective for prose** — |d| **1.16** vs 1.11 for a generic improve prompt (arXiv:2604.22142) | ~0 | a diff-level enforcement mechanism | Reject any revision whose diff touches sections no finding cited. Compare against #5 alone. Study 3 already found that constraining document *growth* made things worse — this tests whether constraining *locus* differs |
| 7 | **Verifier-authored discriminating inputs (code only)** | The auditor proposes *inputs* that would distinguish correct from incorrect; expected outputs come from executing the prior committed state, never from the model. | Models choose discriminating inputs well (**94–99.8%** of wrong solutions caught once expectations are corrected) and compute expected outputs badly (authored suites admit only **19–42%** of oracle-correct solutions) — arXiv:2608.01000. Probe gating cuts false rejection **58–92% → ≤5%** but only **5–39%** of suites survive; repairing expected values recovers yield **3.3–10.6×**. Ceiling: model-written F→P tests fire on **18.5%** (SWT-Bench) to **23.6%** (TDD-Bench) of real bugs | ~2× audit + sandbox | an execution sandbox in the product, not just the benchmark | EvalPlus arm where the auditor emits inputs only, run against the reference. **Ground truth is model-free.** Must be advisory-positive only — a passing generated test is not evidence of correctness |
| 8 | **Confidence-gated cascade with a human-agreement guarantee** | Route each audit to the cheapest model whose calibrated confidence clears a threshold; escalate the rest. Yields a distribution-free guarantee on agreement with the reference judgement. | Trust or Escalate (ICLR 2025 Oral): **90.8%** guarantee success at 55.7% coverage where unselected GPT-4 achieves **0.0%**; **88.1%** of covered instances judged by models cheaper than GPT-4; ECE **0.217 → 0.095**. ARES: **~150** human-labelled anchors buy valid confidence intervals over an unbounded stream | reduces cost | a small labelled calibration set (~150–500 items) and a confidence signal from the auditor | Build the calibration set from CLEAR verdicts on the existing 20+40 instance runs. Falsified if coverage at a 90% guarantee is near zero |
| 9 | **Trained critic / reward-model search** | Train a critic with RLHF and search over critiques at inference with a length penalty, picking a point on the precision/recall frontier. | CriticGPT: **63%** preferred over human critiques; matching it by scaling a prompted baseline needs **~30×** pretraining compute; FSBS traces the full Pareto curve from one model via a scalar penalty | **28×** at inference (FSBS) | **a trained reward model and a labelled critique dataset — we have neither** | Not falsifiable in our harness at current scale. Listed because it is the *reason* "without a bigger model" is the right constraint, and because the FSBS length-penalty dial is the only published mechanism for exposing the operating point as a product setting |

---

## 9. Where I could not verify, and what not to quote

**Could not verify:**
- CriticGPT's comprehensiveness and hallucination/nitpick **rates** (Figures 6–7) — bar values
  only. **Do not quote "60% more bugs"** — that figure is not in the paper; the blog's real number
  is a **>60% *preference* rate** for Human+CriticGPT critiques.
- Smith et al. (FSE 2015) exact held-out pass-rate deltas — PDF would not parse.
- The Kali "27 vs 18/10/27" plausible-patch comparison — secondary citation only.
- The single-line/single-hunk/multi-hunk gradient (45.06 / 34.37 / 27.50 pass@1) attributed to
  arXiv:2506.03283 — not present in the abstract page fetched.
- The "55.36% suspicious / 22.4% → 10.0%" SWE-bench Verified figure — aggregated secondary source.
- Roytburg et al.'s in-body numbers — PDF text layer would not grep; abstract figures only
  (51%, 89.6%, 17.5pp).
- LLM4SA's 81.13%/94.64% (paywalled TKDD); Skywork-Critic's RewardBench figures (model card only).

**Do not cite:**
- **BiGGen Bench "0.669"** — absent from the paper; the best single evaluator is **0.623**, best
  overall **0.627**.
- **CheckEval "+0.45"** — not reproducible from any table cell; the largest all-model deltas are
  **+0.39/+0.40**, mean **+0.295**.
- **RaR "up to 31% relative"** — the underlying pair is ambiguous (Figure 2 gives +22.4%, Table 1
  gives +50%).
- **TICK WildBench "+6.3%"** (abstract) vs **+5.3%** (prose) — the paper disagrees with itself.
- **JudgeLM ">90%, exceeding human-human agreement"** — that is agreement with **GPT-4, its
  teacher**, not with humans. Human-human max on MT-Bench is 82%.
- A circulating "removing decomposition costs 3.6 XSum / 4.6 CNN" ablation — untraceable.
- CoVe's average verification-question count — unreported, so its cost multiplier is unknown.

**ID corrections to the brief:**
- "Trust or Escalate" is **arXiv:2407.18370** (Jung, Brahman, Choi; ICLR 2025 Oral). arXiv:2410.19317
  is *FairMT-Bench*.
- *Core* is **arXiv:2407.03572** (Jiang et al., Findings ACL 2025), and it reports **no**
  ranking-flip statistic.
- Factcheck-Bench is **Findings of EMNLP 2024**, not NAACL. *Decomposition Dilemmas* is **NAACL 2025**.
- **PoLL was never published at a venue** — arXiv only, despite wide citation.
- TICK's PDF still reads "Preprint. Under Review" — no acceptance confirmed.

**Statistical caveats on cited results:**
- AlpacaEval-LC's correlation improvement carries **bootstrap p = 0.07** — directionally strong,
  statistically marginal.
- Zheng et al.'s +10%/+25% self-enhancement: the authors themselves say the study *"cannot
  determine"* whether the bias exists.
- Raw agreement figures across this whole literature are inflated relative to chance-corrected
  ones: GPT-4 vs humans on MT-Bench is 0.671 accuracy but **α = 0.396**.

## 10. Publication-date caution

A large share of the most directly relevant work is **2025–26 arXiv preprints, several
single-author or single-lab, none peer-reviewed at the time of writing**: arXiv:2603.28005 (the
counterexample), 2608.01000 (judging-vs-enumerating), 2607.12885 (reference-free generosity),
2602.10380 (alignment bottleneck), 2512.22306 (count bias), 2606.20093, 2607.24300 (SEAL),
2604.22142, 2604.19049, 2601.09905, 2512.20022, 2512.02304, 2505.17656, 2605.21384, 2605.02964,
2511.21654, 2601.18844, 2601.22952, 2605.30208.

The **peer-reviewed load-bearing citations** are: Huang et al. (ICLR 2024), Kamoi et al. (TACL
2024), Tyen et al. (Findings ACL 2024), Sharma et al. (ICLR 2024), Xu et al. (ACL 2024), Zheng et
al. (NeurIPS 2023), Panickssery et al. (NeurIPS/ICML 2024), Doddapaneni et al. (EMNLP 2024),
Gunjal & Durrett (Findings EMNLP 2024), Hu et al. (NAACL 2025), Min et al. (EMNLP 2023), Wei et
al. (NeurIPS 2024), Gao et al. (ACL 2023), Madaan et al. (NeurIPS 2023), Tang et al. (EMNLP 2024),
Zha et al. (ACL 2023), Laban et al. (TACL 2022), Honovich et al. (NAACL 2022), Manakul et al.
(EMNLP 2023), Farquhar et al. (*Nature* 2024), Gou et al. (ICLR 2024), Ni et al. (ICML 2023),
Mündler et al. (NeurIPS 2024), Debenedetti et al. (NeurIPS 2024), Jung et al. (ICLR 2025), Li et
al. (USENIX Security 2024), Li et al. (ICLR 2025), Haldar & Hockenmaier (EMNLP 2025), Wang et al.
(ACL 2024), Dubois et al. (COLM 2024), Smit et al. (ICML 2024), Roytburg et al. (ICML 2026), Qi et
al. (ISSTA 2015), Smith et al. (FSE 2015), Xiong et al. (ICSE 2018), Ismayilzada et al. (TOSEM
2023), Ruan et al. (arXiv, our own scorer). Weight accordingly.

---

## 11. What I would test first, ranked by expected recall gain per dollar

Costs are derived from our own ledgers: prose audit ≈ $0.068/instance/round (RESULTS-3 arm X),
CLEAR scoring ≈ $0.0945/instance, code audit **$0.0070/instance** with **free, model-free ground
truth** (RESULTS.md code study).

**1. Per-rule decomposition on the EvalPlus code harness, with union-of-N as the paired control.**
≈ **$8–10** for a 5-rule split over the existing 235-instance audit set plus a matched-cost
union-of-5 control. Ground truth is a Python interpreter — no CLEAR, no model judge, nothing to
argue about. The prediction is sharp (MCeT: recall roughly doubles, precision *rises*), the
control is the exact null hypothesis (Tyen: more calls ⇒ more flags), and the false-positive cost
is measured on 150 known-correct solutions in the same run. **Highest signal per dollar in the
whole list, by a wide margin, because scoring is free.**

**2. The revision gate, computed post-hoc from data we already have.** ≈ **$0**. Every round of
every arm is already CLEAR-scored. Reject each of the 25 recorded revisions whose post-score is
below its pre-score, recompute the final F1, and add the RARR-style *preservation* metric we have
never measured. If the gated loop moves −11.0 toward zero, the loop's defect is acceptance rather
than revision, and the fix is a gate rather than a better critique — which is what SEAL (11/12
improved or tied) and RARR (F1_AP 57.0 vs 17.1) both predict. **Infinite return on zero spend, and
it decides the whole revision roadmap.**

**3. Per-rule audit with a mandatory source citation on T03, plus the oracle-grounding ceiling
arm.** ≈ **$12–15** for 20 seeded instances, round one only, 7 rule-calls each. This is the
expensive one and it goes third precisely because the literature says grounding, not
decomposition, is the bigger lever (FLASK: reference **+0.164 ρ** vs decomposition **+0.039**;
no-reference judging agreement **33–42%** vs **85–96%**), so the citation requirement and the
ceiling arm are the parts most likely to pay. The ceiling arm is the honest test of the entire
hypothesis: if an auditor *shown the reference checklist* still cannot reach the measured 69.2%
checkability ceiling, then neither decomposition nor grounding explains our 2%, and we are
looking at the wrong mechanism.

**Deliberately not first:** the self-audit-then-cross-vendor-filter cascade. It is the most
*novel* thing here — genuinely unpublished, and worth a paper — but it is a precision
intervention, and OLIVER's cross-model actor-critic is the closest measurement we have of it
(gains in calibration and precision, **modest sensitivity gains**). Recall is our binding
constraint. Build the recall stage first, measure what it costs in false positives, then buy the
filter.
