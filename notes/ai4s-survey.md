# AI4S audit survey: LLM auditors of scientific code, results and data (2023–2026)

Compiled 2026-09-23. I opened every entry at its arXiv abstract page (arXiv IDs below), and some also at the arXiv HTML full text or the GitHub/Hugging Face repo. Numbers come from the abstract unless marked **[HTML]**, which means a figure read from the arXiv HTML full text through a summarising fetch. Check those against the PDF before citing them. I checked licences and gold availability with the GitHub API and the Hugging Face API/files on the same date. I left out anything I could not open, including the ACM page for the LLM leakage-detection paper, which returned 403.

---

## 1. Tables by area

### A. LLM code critics/verifiers with executable or labelled ground truth (the few most relevant)

| Paper | Measures | Ground truth | Numbers read | Gap vs. our setting |
|---|---|---|---|---|
| *LLM Critics Help Catch LLM Bugs*, McAleese, 2024, arXiv [2407.00215](https://arxiv.org/abs/2407.00215) | RLHF-trained critic finds bugs in model-written code | Human-inserted bugs and human preference ratings | Model critiques preferred over human ones in 63% of cases. Critics hallucinate bugs, and human+critic teams hallucinate less | Human-judged, with no hidden-test oracle. Not cross-vendor. Not scientific code |
| *CodeJudge: Evaluating Code Generation with LLMs*, Tong, 2024, EMNLP 2024, arXiv [2410.02184](https://arxiv.org/abs/2410.02184) | LLM judges semantic correctness without tests | Test outcomes on 4 codegen datasets, 5 languages | Beats prior methods "in most settings". Llama-3-8B beats a GPT-3.5 method | Judge-as-metric (correlation), not auditor recall/FPR under a block decision. Generic code |
| *SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation*, Zeng, 2025, FSE 2026, arXiv [2509.01494](https://arxiv.org/abs/2509.01494) | Review comments on 1000 verified GitHub PRs | Structured issue list; LLM coverage check (~90% agreement with humans) | Multi-review aggregation raises F1 by up to 43.67% | Aggregating multiple reviews is our "repeated readings" axis, but ground truth is review issues, not executed tests. Not scientific |
| *Multi-Agent Code Verification via Information Theory*, Rajan, 2025, arXiv [2511.16708](https://arxiv.org/abs/2511.16708) | Ensemble of 4 specialised LLM agents as bug detector | 99 samples with "verified labels" | 76.1% bugs caught. Single to multi agent 32.8% to 72.4%, with diminishing gains +14.9/+13.5/+11.2 pp | Same diminishing-returns shape as our union recall, but tiny N, general code, no hidden-test oracle, no scientific substrate |

### B. Scientific-code / data-driven-science benchmarks with executable or programmatic evaluation

| Paper | What is evaluated | Ground truth | Size / key number | Licence; gold/tests public? |
|---|---|---|---|---|
| *SciCode: A Research Coding Benchmark Curated by Scientists*, Tian, 2024, arXiv [2407.13168](https://arxiv.org/abs/2407.13168) | Function-level scientific code (16 subfields) | Scientist-written gold solutions + test cases (numeric targets in `test_data.h5`) | 80 main / 338 subproblems. Claude3.5-Sonnet 4.6% on main problems | Apache-2.0. HF split check: **dev 15 problems / 50 steps with `ground_truth_code`. Test 65 problems / 291 steps have test cases (288 steps) but no gold code.** Numeric targets downloaded separately (Google Drive) |
| *ScienceAgentBench*, Chen, 2024, ICLR 2025, arXiv [2410.05080](https://arxiv.org/abs/2410.05080) | Self-contained Python program for a data-driven task from 44 papers | Expert-validated gold programs + per-task eval scripts on outputs (incl. figures) | 102 tasks. Best agent 32.4% (34.3% with knowledge). o1-preview 42.2% | Code MIT, tasks mostly CC BY 4.0 (a few keep upstream licences). Gold programs in a password-zipped full release (anti-contamination). Dockerised eval |
| *DiscoveryBench*, Majumder, 2024, arXiv [2407.01725](https://arxiv.org/abs/2407.01725) | Hypothesis discovery from datasets | Gold hypotheses/workflows from papers; facet-based (LLM) matching | 264 real + 903 synthetic tasks. Best system 25% | ODC-By (LICENSE file). Gold hypotheses in repo. Scoring is semantic, not execution |
| *BLADE*, Gu, 2024, EMNLP 2024 (repo: Findings), arXiv [2408.09667](https://arxiv.org/abs/2408.09667) | Analysis decisions for open research questions | Independent expert analyses; computational matching | 12 datasets/questions. "Often limited to basic analyses" | Code Apache-2.0, data ODC-By. Gold analyses public |
| *CORE-Bench*, Siegel, 2024, arXiv [2409.11363](https://arxiv.org/abs/2409.11363) | Reproduce results from a paper's code+data (CS, social sci, medicine) | Answers to questions about reproduced outputs | 270 tasks / 90 papers. Best 21% on hardest level | MIT. Test set GPG-encrypted (password in README). Docker/Azure harness. Capsules are heavy |
| *PaperBench*, Starace, 2025, arXiv [2504.01848](https://arxiv.org/abs/2504.01848) | Replicate 20 ICML 2024 papers from scratch | Author-co-developed rubrics (8,316 gradable items), graded by LLM judge | Best agent 21.0%. **[HTML]** judge o3-mini SimpleJudge P=R=F1=0.83 on JudgeEval, ~$66/paper | MIT (openai/preparedness). Needs GPUs. Ground truth is rubric + LLM judge, not execution |
| *SciReplicate-Bench*, Xiang, 2025, arXiv [2504.00255](https://arxiv.org/abs/2504.00255) | Implement algorithms from 36 NLP papers | Annotated reference code + test cases (execution accuracy) | 100 tasks. Best 39% execution accuracy | Repo xyzCS/SciReplicate-Bench. GitHub reports **no licence** |
| *LMR-Bench*, Yan, 2025, EMNLP 2025 (venue from ACL Anthology search listing, not opened), arXiv [2506.17335](https://arxiv.org/abs/2506.17335) | Fill masked functions in NLP research repos | Annotated unit tests + LLM judge | 28 tasks / 23 papers | Repo has `unit_test/`, `golden_files/`, per-project Docker. GitHub reports no licence |
| *ResearchCodeBench*, Hua, 2025, arXiv [2506.02314](https://arxiv.org/abs/2506.02314) | Implement novel ML contributions (2024–25 papers) | Deterministic execution tests | 212 challenges. Best (Gemini-2.5-Pro-Preview) 37.3% | Repo PatrickHua/ResearchCodeBench, ships unit-test sanity script. GitHub reports no licence |
| *MLAgentBench*, Huang, 2023, arXiv [2310.03302](https://arxiv.org/abs/2310.03302) | ML experimentation (improve a metric) | Task metric improvement | 13 tasks. Claude 3 Opus 37.5% avg success | MIT. Outcome metric, not a correctness oracle |
| *REPRO-Bench*, Hu, 2025, ACL 2025 Findings, arXiv [2507.18901](https://arxiv.org/abs/2507.18901) | Agent *assesses* reproducibility of a social-science paper (score 1–4) | Public human reproduction reports | 112 papers. Best agent 21.4%. REPRO-Agent +71% relative | Repo public ("gold-standard reproducibility annotations"). No licence on GitHub. Mixed languages (Stata/R) |
| *DSDBench*, Yang, 2025, EMNLP 2025, arXiv [2503.22388](https://arxiv.org/abs/2503.22388) | Detect/locate multi-hop multi-bug errors in data-science code | Synthesised bugs with runtime errors | 1,117 samples, 741 cause-effect pairs | Public repo, no licence detected. Bugs are *runtime* (crash), not silent |
| *Your Simulation Runs but Solves the Wrong Physics* (MooseBench), Song, 2026, arXiv [2605.09360](https://arxiv.org/abs/2605.09360) | Whether generated MOOSE simulation code encodes intended PDE | Deterministic reconstruction of PDE from Kernel/BC objects (Intent Fidelity Score) | 220 cases. **39–40% runnable but solving the wrong physics** | Released "with this work". Licence not checked |
| *SA-Bench*, Hu, 2026, Findings EMNLP 2026, arXiv [2608.24252](https://arxiv.org/abs/2608.24252) | Semantic drift of paper-reproduction repos | 1,491 atomic implementation claims (SAUs) | Best config mean SAU 0.301. Overall 0.221 | "Publicly available". Licence not checked |
| *PETSCAgent-Bench*, Zhang, 2026, arXiv [2603.15976](https://arxiv.org/abs/2603.15976) | HPC scientific code quality beyond pass/fail | 14 evaluators: deterministic checks + LLM | Qualitative in abstract | Not checked |

Two further reproduction benchmarks opened: *ReplicatorBench* (Nguyen, 2026, KDD 2026 AI4Sciences, [2602.11354](https://arxiv.org/abs/2602.11354)) includes **non-replicable** claims as negatives. *SocSci-Repro-Bench* in *AI Coding Agents Can Reproduce Social Science Findings* (Alizadeh, 2026, [2606.11447](https://arxiv.org/abs/2606.11447)) has 221 tasks, including demonstrably non-reproducible ones, and reports that giving agents the PDF "introduces bias on tasks where reproduction is impossible".

### C. LLMs as verifiers of scientific results/claims

| Paper | Measures | Ground truth | Numbers read | Gap |
|---|---|---|---|---|
| *When AI Co-Scientists Fail: SPOT*, Son, 2025, arXiv [2505.11855](https://arxiv.org/abs/2505.11855) | Find errata/retraction-grade errors in papers | 91 real errors in 83 papers, author-cross-validated | No model >21.1% recall or >6.1% precision (o3 best). Across 8 runs models "rarely rediscover the same errors" | Closest *shape* to ours (recall, precision, run-to-run instability) but papers not code, no execution oracle |
| *FLAWS*, Xi, 2025, arXiv [2511.21843](https://arxiv.org/abs/2511.21843) | Identify+localise inserted claim-invalidating errors | 713 LLM-inserted paper–error pairs | GPT-5 39.1% identification at k=10 | Synthetic insertions, text only, no FPR on clean papers |
| *To Err Is Human*, Bianchi, 2025, arXiv [2512.05925](https://arxiv.org/abs/2512.05925) | GPT-5 "Paper Correctness Checker" on published AI papers | Human expert confirmation; injected mistakes | Precision 83.2% (263/316). Mistakes/paper 3.8→5.9 (NeurIPS 2021→2025). **[HTML]** recall 60.0% on 90 injected mistakes (15 copies of 5 papers) | Recall only on injected text errors. No code execution |
| *Reviewing Scientific Papers for Critical Problems With Reasoning LLMs*, Zhang, 2025, NeurIPS 2025 AI4Science WS, arXiv [2505.23824](https://arxiv.org/abs/2505.23824) | Critical-error identification in withdrawn arXiv papers | Withdrawal reasons; LLM-as-judge scoring | o3 best (no figure in abstract) | Judge-scored, no execution |
| *Automatic Reviewers Fail to Detect Faulty Reasoning*, Dycke, 2025, TACL 2026, arXiv [2508.21422](https://arxiv.org/abs/2508.21422) | Counterfactual flaw injection into research logic | Controlled counterfactuals | Flaws have "no significant effect" on generated reviews | Reviewer-generators, not blocking auditors |
| *SciCoQA*, Baumgärtner, 2026, ACL 2026, arXiv [2601.12910](https://arxiv.org/abs/2601.12910) | Detect paper–code discrepancies | 92 real (GitHub issues, reproducibility reports) + 543 synthetic | Best models detect 46.7% of real discrepancies (22 models). **[HTML]** also reports precision. CC BY 4.0 | **Code + paper**, but ground truth is annotated discrepancy, not executed behaviour |
| *The More You Automate, the Less You See*, Luo, 2025, NeurIPS 2025 AI4Science (Spotlight), arXiv [2509.08713](https://arxiv.org/abs/2509.08713) | LLM auditor detects 4 pitfalls (leakage, metric misuse, …) in AI-scientist outputs | Controlled constructions, balanced pos/neg | **[HTML]** gemini-2.5-flash auditor: 55% (paper only) vs 82% accuracy (paper+logs+code), 100 balanced samples. FPR ~40% vs 14% | Reports **both recall and FPR** of an LLM auditor on scientific artefacts. Small N, single vendor, constructed cases |
| *SciTab*, Lu, 2023, EMNLP 2023, arXiv [2305.13186](https://arxiv.org/abs/2305.13186); *SciVer*, Wang, 2025, arXiv [2506.15569](https://arxiv.org/abs/2506.15569) | Claim-vs-table / multimodal claim verification | Expert labels (1.2K; 3,000) | SciTab: all but GPT-4 near random | Verifies claims against *reported* tables, not against re-executed code/data |
| *ARA*, Riehl, 2026, arXiv [2605.02651](https://arxiv.org/abs/2605.02651) | Predict reproducibility from paper workflow graph | ReScience C (213), ReproBench, GoldStandardDB | ~61% accuracy. ReproBench 60.71% vs 36.84% | Document-only prediction |

### D. LLMs for data auditing

| Paper | Measures | Ground truth | Numbers read | Gap |
|---|---|---|---|---|
| *Are LLMs Better than Reported? Detecting Label Errors…*, Nahum, 2024, arXiv [2410.18889](https://arxiv.org/abs/2410.18889) | LLM-ensemble flags mislabeled examples (TRUE, SummEval) | Expert re-annotation | "Substantial number of label errors". Correction raises reported performance | NLP labels, not scientific measurements. No executable oracle |
| *Exploring LLM Agents for Cleaning Tabular ML Datasets*, Bendinelli, 2025, ICLR 2025 WS, arXiv [2503.06664](https://arxiv.org/abs/2503.06664) | LLM+Python cleans intentionally corrupted Kaggle data | Injected corruptions; downstream model performance | Row-level errors found. Cross-row (distribution/trend) errors missed | Closest to a data-audit substrate with a known corruption oracle. No FPR framing |
| *scicode-lint*, Samsonau, 2026, arXiv [2603.17893](https://arxiv.org/abs/2603.17893) | Methodology bugs (leakage, bad CV, seeds) in scientific Python | Human-labelled Kaggle notebooks; LLM-judged on 38 papers | Preprocessing leakage 65% precision at 100% recall (Kaggle). 62% precision on papers (LLM-judged), 54% held-out. 97.7% on controlled tests | Straddles D and E: data-leakage audit of *scientific code*. Ground truth partly LLM-judged, not executed |

(LLM-based leakage detection with static slicing, "LeakCheckLLM", is listed at ACM DOI 10.1145/3808199. The page returned 403 so I have not listed it. Only a search snippet was seen.)

### E. LLM auditor recall **and** false-positive rate on *scientific* code/results

I found none that combines (i) scientific code, (ii) a hidden executable oracle as ground truth, and (iii) auditor recall and FPR on clean items. Partial matches: Luo 2025 (recall+FPR, constructed cases, 100 items, one model), scicode-lint (precision/recall, partly LLM-judged), SPOT (recall+precision, papers), SciCoQA (recall+precision, paper–code discrepancy), MooseBench (deterministic physics verifier, not an LLM auditor).

---

## 2. Closest prior work and what is novel for us

1. **Luo et al. 2025, *Hidden Pitfalls of AI Scientist Systems* ([2509.08713](https://arxiv.org/abs/2509.08713)).** An LLM audits code and logs of AI-scientist runs and reports accuracy and per-pitfall FPR. *Not covered there:* hidden-test ground truth, multiple vendors, repeated-reading union curves, the rulebook-sentence effect, and scale beyond 100 constructed items.
2. **SPOT, Son 2025 ([2505.11855](https://arxiv.org/abs/2505.11855)).** Recall ≤21.1%, precision ≤6.1%, low run-to-run rediscovery. This is the closest analogue to our "union recall of repeated readings" finding, but the substrate is manuscripts with errata, not executed code. *Novel for us:* the same reliability questions answered against an interpreter oracle, where the denominator is exact.
3. **SciCoQA, Baumgärtner 2026 ([2601.12910](https://arxiv.org/abs/2601.12910)).** LLMs read paper plus code and flag discrepancies. Best recall on real cases is 46.7%. *Novel for us:* whether a flagged or missed discrepancy changes executed output, and a block/allow decision with FPR on correct code.
4. **scicode-lint, Samsonau 2026 ([2603.17893](https://arxiv.org/abs/2603.17893)).** LLM-generated patterns for methodology bugs, with precision/recall on labelled notebooks. *Novel for us:* a general auditor (not a pattern linter), cross-vendor, and executable ground truth instead of LLM-judged precision.
5. **Rajan 2025 ([2511.16708](https://arxiv.org/abs/2511.16708)) and SWR-Bench ([2509.01494](https://arxiv.org/abs/2509.01494)).** Diminishing returns from adding agents or aggregating reviews on general code. *Novel for us:* the same curve on scientific code with hidden tests, plus the finding that misses concentrate where the specification never determined the behaviour. SciReplicate-Bench's note that "missing or inconsistent algorithm descriptions" block reproduction points the same way from the generator side.

**What is not novel:** that LLMs find some scientific errors, that recall is low and unstable across runs (SPOT), that code access helps auditing (Luo), and that execution alone misses wrong-physics code (MooseBench). **What appears novel, as far as this survey can tell:** measuring an LLM auditor's recall *and* false-positive rate against a **hidden, interpreter-executed oracle** on **scientific** code, across vendors and repeated readings, and separating misses by whether the specification determined the behaviour. That extends to (2) results, where re-execution decides if a reported number follows, and (3) data, where injected label/leakage/corruption faults have known ground truth.

---

## 3. Feasibility of each B benchmark as an audit substrate

- **SciCode**: Best fit. Apache-2.0, offline, pure-Python numeric tests. Test split has tests but **no gold code** (dev: 15 problems / 50 steps with gold). Candidate solutions must come from generators, which matches our HumanEval+/MBPP+ design. Numeric targets `test_data.h5` sit on Google Drive.
- **ScienceAgentBench**: Good. Code MIT, tasks CC BY 4.0 (a few upstream licences), gold programs and eval scripts in a password zip, Docker harness. Datasets are heavier and some checks are figure/LLM-based, so use the programmatic-metric subset.
- **DiscoveryBench**: Weak for code audit. ODC-By, gold hypotheses public, but scoring is semantic hypothesis matching. Usable for "does the claim follow from the data" with an LLM-free re-analysis only if we build it.
- **BLADE**: Moderate for result audits. Apache-2.0/ODC-By, expert analyses public, but many valid analyses exist, so no single executable truth.
- **CORE-Bench**: Good for result auditing (does the reported number follow from code+data). MIT, test set GPG-encrypted with a public password, Docker. Capsules are large and some need GPU.
- **PaperBench**: Poor as an oracle. MIT, but ground truth is rubric + LLM judge (JudgeEval F1 0.83), and it needs GPUs and full replications.
- **SciReplicate-Bench**: Promising (test cases, execution accuracy), but no licence file. Ask the authors before redistribution.
- **LMR-Bench**: Promising (unit tests, golden files, Docker per project) but small (28) and no licence file detected.
- **ResearchCodeBench**: Promising (212 deterministic tests) but no licence file detected.
- **MLAgentBench**: Unsuitable as a correctness oracle (metric improvement only). MIT.
- **REPRO-Bench / ReplicatorBench / SocSci-Repro-Bench**: Suitable for (2) result audits with human reproduction verdicts as ground truth. Mixed Stata/R environments. REPRO-Bench repo has no licence.
- **DSDBench**: Bugs are runtime crashes, which are trivially detectable by execution. Not the silent-failure regime we care about. No licence.
- **MooseBench**: Strong silent-failure oracle (deterministic PDE reconstruction), but domain-specific (MOOSE install). Licence not checked.
- **SA-Bench**: Claim-level annotations, not executable. Licence not checked.
