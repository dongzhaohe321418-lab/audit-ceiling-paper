# Related Work: Ensembles, Cascades, and the Behaviour of LLM Judges

## Panels, juries, and cascades

Aggregating several inexpensive judges improves agreement with humans at the level of aggregate scores, but the published gains are aggregate-level and the aggregation rule carries more weight than the composition of the panel. Verga et al. report that a Panel of LLM Evaluators drawn from Command-R, Claude-3 Haiku, and GPT-3.5 reaches Cohen's κ of 0.763 against human annotators on KILT-NQ where a single GPT-4 judge reaches 0.627, and Kendall-τ of 0.778 against Chatbot Arena rankings where GPT-4 reaches 0.667, at roughly one-seventh the token cost \citep{verga2024poll}. Two details bear on our measurements more than the headline. First, PoLL uses *max* voting — a union — for binary correct/incorrect judgements, reserving average pooling for graded 1–5 scores; majority voting on binary decisions is not evaluated. Second, the panel's benefit is quantified as reduced dispersion of *aggregate* accuracy deltas (standard deviation 2.2 for the panel against 6.1 for GPT-3.5 alone), not as per-instance stability. Our observation that majority-of-3 across architectures removes 1.4 false positives while costing 5.5 recall is therefore not in tension with PoLL: majority is an intersection-flavoured rule applied where PoLL applied a union, and on binary defect decisions with a low base rate the recall cost dominates. The reported union across six models reaching 83.3% on injected errors against 71.6% for the best single model points the same way, though we have not verified those figures against the primary source \citep{unverified2606}.

Cascades formalise the alternative. Jung et al. escalate to a stronger judge only under low confidence and supply a distribution-free guarantee of human agreement: on TL;DR at a 90% target their method attains a 90.8% guarantee-success rate at 55.7% coverage, where GPT-4 without abstention attains 0%; on ChatArena at an 80% target it covers 79.1% of instances with 88.1% of those decided by Mistral-7B or GPT-3.5 \citep{jung2024trust}. The mechanism is abstention, not aggregation. This is the right comparison for our two-stage cross filter: a cascade buys reliability by declining to answer, so its cost appears as reduced coverage; our filter answers and prunes, so its cost appears as recall collapsing to 3.6%.

Multi-agent debate does not clear the bar set by simple sampling. Reproducing Du et al.'s protocol on the full GSM8K test set rather than a 100-example subset, Huang et al. measure debate at 83.0 against self-consistency at 88.2 at nine sampled responses \citep{huang2024selfcorrect}. Smit et al. find every debate configuration on MedQA within a 0.56–0.64 accuracy band and no debate protocol reliably ahead of self-consistency or ensembling \citep{smit2024mad}.

## The reproducibility floor

Judge verdicts are unstable at the instance level even when aggregates are not, and the instability does not shrink with repetition. Haldar and Hockenmaier measure a judge's Krippendorff α *against itself* across three identical runs at 0.33 for Llama-3.1, 0.63 for DeepSeek-R1, and 0.79 for Qwen-3 on SummaC, and report that Qwen-3 returned the same MT-Bench judgement on all three runs in only 61.3% of cases; extending to five runs produced no significant change, which they interpret as a model-and-dataset property rather than a sampling artefact \citep{haldar2025roulette}. Our 6-of-20 verdict flips over identical bytes sit inside this regime, and because the model exposes no temperature control the flips cannot be attributed to a decoding parameter. That our aggregate recall reproduces to the decimal while per-instance findings do not is the expected consequence: majority-vote aggregation over three runs buys only 1.2 to 2.5 balanced-accuracy points in that study, precisely because averaging suppresses variance without touching a model's systematic component.

## When agreement is evidence and when it is reflex

Consistency is not evidence of correctness for the class of errors a model makes stably. Tan et al. define self-consistent errors — the same wrong answer across all stochastic samples and greedy decoding — and show that semantic entropy, the leading self-consistency detector, reaches AUROC 0.4608 on them against 0.8820 on inconsistent errors, that is, at or below chance \citep{tan2025consistent}. Unanimity across runs therefore selects for whatever is stable in the model, which may be signal or may be prior.

Which of the two dominates appears to depend on whether the task admits verifiable ground truth. Ye et al. report that judge bias is markedly more pronounced on alignment datasets than on fact-related ones, and attribute this to the wider genuine quality gaps in factual items, which bias is insufficient to overturn \citep{ye2024calm}. This is, we think, the most plausible published account of our prose/code split: findings the auditor raises on every prose run are correct 45% of the time against 88% for the rest, while in code the intersection improved the recall/false-positive ratio. Prose audit resembles the alignment regime, where a stable stylistic prior can dominate a narrow quality gap; code audit resembles the fact-related regime, where the gap is wide enough that stability tracks evidence. Huang et al. supply the mechanism for the prior itself: a critique instruction functions as an additional prompt that can bias the model away from its optimal response, turning correct answers incorrect in 11.6% of GPT-3.5 CommonSenseQA cases against 5.8% in the other direction \citep{huang2024selfcorrect}. Tyen et al. quantify the same trade-off directly: moving GPT-4 from trace-level to step-level scrutiny on Dyck languages raises recall on faulty traces from 7.37 to 43.91 while accuracy on clean traces falls from 98.41 to 13.79 \citep{tyen2024mistakes}. Scrutiny volume, not scrutiny quality, drives the false positives — which is why unanimity under repeated scrutiny marks a reflex.

## Filters need evidence, not second opinions

Published two-stage pipelines that preserve recall give the second stage new information rather than a second opinion. LLift filters roughly 53,000 warnings that UBITect's symbolic execution left undecided out of 140,000 candidates, reaching 50% precision while retaining 100% recall on known bugs; ablating its evidence-gathering scaffold — post-constraint analysis, progressive prompting, task decomposition, self-validation — collapses the same model on the same data from precision 0.87 / recall 1.00 to 0.12 / 0.15 \citep{li2024llift}. Where the second stage is opinion alone, recall is the first casualty: an agentic SAST filter cut false-positive rate from 98.3% to 6.3% while suppressing 22.25% of real vulnerabilities, and 77.17% of CWE-327 instances \citep{xiong2026sifting}; a weak filter model raised CodeQL's false-discovery rate by 5.52 points rather than lowering it \citep{li2025iris}; and Google's deployed review filter discarded below-threshold predictions that were still roughly 80% correct \citep{vijayvergiya2024autocommenter}. Our 3.6% is an extreme instance of this failure mode, and we read it as evidence that cross-model filtering without independent evidence is a conservatism mechanism rather than a precision mechanism.

## A lenient but precise self-judge

The self-preference literature predicts leniency, and our self-audit arm — 82% precision, gating 3.3% of instances against 80.0% — is what leniency looks like when precision is measured on a small number of claims. Lu et al. find that verifier false-positive rate, in the sense of wrongly accepting a bad solution, falls as solver–verifier dissimilarity rises (r = −0.552, slope −2.727), and that models favour solutions resembling their own \citep{lu2025verification}. Wataoka et al. locate the mechanism in perplexity rather than identity: judges over-reward low-perplexity text regardless of whether they generated it \citep{wataoka2024selfpref}. Panickssery et al. establish that the recognition capacity exists — GPT-4 distinguishes its own summaries at 73.5% accuracy without fine-tuning — and that self-recognition and self-preference are linearly and causally linked \citep{panickssery2024selfpref}. We therefore read 82% precision at a 3.3% gate rate as a placement of the decision criterion, not as superior discrimination; the arm makes few claims and most survive. This reverses the direction of our earlier prose measurement, in which self-audit flagged correct work more often than a cross-vendor judge, and we note that the self-correction literature accommodates both signs through criterion placement rather than discrimination: Sharma et al. show models wrongly conceding error on correct answers in 42% (GPT-4) to 98% (Claude 1.3) of cases under a single challenge, unchanged when restricted to answers held at 95% confidence \citep{sharma2024sycophancy}. What the literature does *not* predict is a self-judge with better discrimination than a cross-vendor one, and we do not claim it.

---

```bibtex
@article{verga2024poll,
  title  = {Replacing Judges with Juries: Evaluating {LLM} Generations with a Panel of Diverse Models},
  author = {Verga, Pat and Hofst{\"a}tter, Sebastian and Althammer, Sophia and Su, Yixuan and Piktus, Aleksandra and Arkhangorodsky, Arkady and Xu, Minjie and White, Naomi and Lewis, Patrick},
  journal = {arXiv preprint arXiv:2404.18796},
  year   = {2024},
  note   = {Tables 1--3, \S3.1, \S4.4--4.5}
}

@inproceedings{jung2024trust,
  title     = {Trust or Escalate: {LLM} Judges with Provable Guarantees for Human Agreement},
  author    = {Jung, Jaehun and Brahman, Faeze and Choi, Yejin},
  booktitle = {International Conference on Learning Representations (ICLR), Oral},
  year      = {2025},
  note      = {arXiv:2407.18370; Tables 1--3, Figures 3--4}
}

@inproceedings{huang2024selfcorrect,
  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},
  author    = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024},
  note      = {arXiv:2310.01798; Tables 3, 7, Figure 1}
}

@inproceedings{smit2024mad,
  title     = {Should We Be Going {MAD}? A Look at Multi-Agent Debate Strategies for {LLM}s},
  author    = {Smit, Andries and Duckworth, Paul and Grinsztajn, Nathan and Barrett, Thomas D. and Pretorius, Arnu},
  booktitle = {International Conference on Machine Learning (ICML), PMLR 235},
  year      = {2024},
  note      = {arXiv:2311.17371; Table 2}
}

@inproceedings{haldar2025roulette,
  title     = {Rating Roulette: Self-Inconsistency in {LLM}-as-a-Judge Frameworks},
  author    = {Haldar, Rajarshi and Hockenmaier, Julia},
  booktitle = {Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2025},
  note      = {arXiv:2510.27106; Tables 1--3}
}

@article{tan2025consistent,
  title   = {Too Consistent to Detect: A Study of Self-Consistent Errors in {LLM}s},
  author  = {Tan, Hexiang and Sun, Fei and Liu, Sha and Su, Du and Cao, Qi and Chen, Xin and Wang, Jingang and Cai, Xunliang and Wang, Yuanzhuo and Shen, Huawei and Cheng, Xueqi},
  journal = {arXiv preprint arXiv:2505.17656},
  year    = {2025},
  note    = {Tables 2--4}
}

@article{ye2024calm,
  title   = {Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
  author  = {Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},
  journal = {arXiv preprint arXiv:2410.02736},
  year    = {2024},
  note    = {Table 4, \S4.1}
}

@inproceedings{tyen2024mistakes,
  title     = {{LLM}s Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location},
  author    = {Tyen, Gladys and Mansoor, Hassan and Carbune, Victor and Chen, Peter and Mak, Tony},
  booktitle = {Findings of the Association for Computational Linguistics (ACL)},
  year      = {2024},
  note      = {arXiv:2311.08516; Tables 4, 9}
}

@inproceedings{li2024llift,
  title     = {The Hitchhiker's Guide to Program Analysis: A Journey with Large Language Models},
  author    = {Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun},
  booktitle = {USENIX Security Symposium},
  year      = {2024},
  note      = {arXiv:2308.00245; \S6.1, Tables 4--5}
}

@article{xiong2026sifting,
  title   = {Sifting the Noise: A Comparative Study of {LLM} Agents in Vulnerability False Positive Filtering},
  author  = {Xiong, Yunpeng and Zhang, Ting},
  journal = {arXiv preprint arXiv:2601.22952},
  year    = {2026},
  note    = {Preprint, not peer reviewed}
}

@inproceedings{li2025iris,
  title     = {{IRIS}: {LLM}-Assisted Static Analysis for Detecting Security Vulnerabilities},
  author    = {Li, Ziyang and Dutta, Saikat and Naik, Mayur},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2025},
  note      = {arXiv:2405.17238; Table 1}
}

@inproceedings{vijayvergiya2024autocommenter,
  title     = {{AI}-Assisted Assessment of Coding Practices in Modern Code Review},
  author    = {Vijayvergiya, Manushree and Salawa, Ma{\l}gorzata and Budiseli{\'c}, Ivan and Zheng, Dan and Lamblin, Pascal and Ivankovi{\'c}, Marko and Carin, Juanjo and Lewko, Mateusz and Andonov, Jovan and Petrovi{\'c}, Goran and Tarlow, Daniel and Maniatis, Petros and Just, Ren{\'e}},
  booktitle = {Proceedings of AIware},
  year      = {2024},
  note      = {arXiv:2405.13565}
}

@article{lu2025verification,
  title   = {When Does Verification Pay Off? A Closer Look at {LLM}s as Solution Verifiers},
  author  = {Lu, Jack and Teehan, Ryan and Jin, Jinran and Ren, Mengye},
  journal = {arXiv preprint arXiv:2512.02304},
  year    = {2025},
  note    = {False positive defined as wrongly accepting an incorrect solution; polarity is inverse to ours}
}

@article{wataoka2024selfpref,
  title   = {Self-Preference Bias in {LLM}-as-a-Judge},
  author  = {Wataoka, Koki and Takahashi, Tsubasa and Ri, Ryokan},
  journal = {arXiv preprint arXiv:2410.21819},
  year    = {2024}
}

@inproceedings{panickssery2024selfpref,
  title     = {{LLM} Evaluators Recognize and Favor Their Own Generations},
  author    = {Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},
  booktitle = {International Conference on Machine Learning (ICML)},
  year      = {2024},
  note      = {arXiv:2404.13076; \S1, \S3.2--3.4}
}

@inproceedings{sharma2024sycophancy,
  title     = {Towards Understanding Sycophancy in Language Models},
  author    = {Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R. and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R. and Kravec, Shauna and Maxwell, Timothy and McCandlish, Sam and Ndousse, Kamal and Rausch, Oliver and Schiefer, Nicholas and Yan, Da and Zhang, Miranda and Perez, Ethan},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024},
  note      = {arXiv:2310.13548}
}

@misc{unverified2606,
  title  = {Coordinator-supplied benchmark, union across six models},
  note   = {arXiv:2606.19749. Figures (83.3\% union vs 71.6\% best single on injected errors) supplied by the coordinator and NOT verified against the primary source by this survey. Verify before submission.},
  year   = {2026}
}
```
