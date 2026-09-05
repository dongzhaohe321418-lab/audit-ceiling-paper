## Related Work: Decomposition as a Route to Audit Recall

The dominant response to the unreliability of holistic LLM judgement has been to decompose it. The decompose-then-verify pattern established by FActScore \cite{min2023factscore} splits a generation into atomic facts — 26.3 to 40.8 per biography — and verifies each against a knowledge source; SAFE \cite{wei2024longfact} extends this with per-fact search. Both are routinely cited as evidence that decomposition improves error detection, but neither measures that. FActScore's headline "less than 2% error rate" is the absolute difference between the estimated and human-annotated aggregate score (1.4% for InstructGPT, 0.4% for ChatGPT, but 8.7% for retrieval-augmented PerplexityAI), and its Pearson of 0.99 is across 13 system-level means, not per-error agreement; the paper contains no holistic baseline. SAFE's numbers are agreement with crowdworkers on 16,011 individual facts (72.0%) and a 100-case disagreement audit in which SAFE was correct 76% of the time against the annotators' 19%. That establishes decomposition beats cheap human labour, not that it beats a holistic judge, and it reports no false-positive budget. The field's foundational citations are therefore weaker support for the recall claim than their usage suggests.

Where recall is measured directly against expert-found defects, decomposition can win substantially. MCeT \cite{mahmoud2025mcet} evaluates sequence diagrams against requirements text and reports that the direct holistic approach finds fewer than 35% of the issues experienced engineers find at a precision of 0.58, while a combined approach that splits both the diagram into atomic interactions and the requirements into self-contained items reaches 65% recall at 0.81 precision — 90% more human-reported issues, plus roughly six additional issues per diagram not reported by the engineers. This is the closest published analogue to our setting, and notably decomposition improved precision rather than trading it away. We flag two limits: we could not retrieve the per-variant table separating requirement-atom from diagram-atom contributions, nor any token-overhead figure, so the cost multiplier for MCeT is unverified; and internal circulation of this result as "59.3% recall / 0.86 precision at ~6x tokens" is incorrect on all three figures. Chain-of-Verification \cite{dhuliawala2023cove} shows a similar gain on generation rather than audit — Llama-65B list-question precision 0.17 to 0.36, longform FActScore 55.9 to 71.4 — but its own ablation attributes the effect to verification *independence* rather than granularity: the factored (0.32) and two-step (0.36) variants beat the joint variant (0.29), which differs only in whether the verifier attends to the original draft. FineSurE \cite{song2024finesure} localises the benefit further: keyfact decomposition is marginally *worse* than holistic G-Eval on faithfulness (0.833 vs 0.841 summary-level Pearson) and far better on completeness (0.688 vs 0.314).

The controlled head-to-heads, however, mostly favour holistic judging, and they do so precisely on omission. Zhang \cite{zhang2026rethinking} matches prompt richness across arms — the confound that makes most atomic-vs-holistic comparisons uninterpretable — and finds holistic wins on two of three benchmarks across all four model families tested, with ASQA accuracy 0.720 vs 0.565 for GPT-4.1 (cluster-bootstrap CI [+0.120, +0.190]; sign test 66 sources favouring holistic against 5, p = 2.1e-14) while using fewer tokens. The advantage sits almost entirely in the `partially_supported` class, +14.5 to +33.0 points for proprietary families: decomposition fragments the completeness reasoning that omission detection requires. The rubric-side analogue is stronger still. On 2,400 perturbed answers, Doddapaneni et al. \cite{doddapaneni2024blindspots} find that adding rubrics to single-answer scoring *raises* GPT-4-Turbo's undetected-error rate from 0.57 to 0.85 on long-form, 0.54 to 0.73 on factual, and 0.57 to 0.80 on instruction-following — while the same decomposition helps in pairwise format. Composing NLI labels from atomic sub-judgements underperforms holistic judgement for every model tested \cite{srikanth2025microscope}, by 15.4 points for GPT-4o on defeasible NLI. These are consistent with our own finding that across fifteen architectures under a 6.7% false-positive constraint, none beat holistic cross-vendor auditing at 20.0% recall.

The reconciling variable appears to be the gap between verifier strength and input complexity. Hu et al. \cite{hu2025dilemmas} vary decomposer and verifier factorially and recover a clean sign flip: with a strong verifier on short claims, decomposition costs 3.2 to 8.9 balanced-accuracy points (WICE/MiniCheck, 80.01 to 71.11 for FActScore-style splitting); with a weak verifier on long responses it gains large F1 (45.88 to 64.32), largely in regimes where the holistic verifier fails outright. Akhter et al. \cite{akhter2026bottleneck} identify the second condition: sub-claims paired with sub-claim-aligned evidence gain 0.0625 F1, whereas sub-claims re-using one claim-level evidence pool *lose* 0.0672 F1 and collapse to roughly 0.44 F1 under noisy labels. Decomposition buys recall when it changes what evidence is retrieved, not when it merely changes how the judgement is phrased. Our measurement that decomposition bought +9.1 recall for +8.0 false positives (p = 0.0042) in code with model-free ground truth sits inside this account: with proportional false-positive cost, the gain is a movement along the operating curve rather than an improvement of it, which is also what we observe when unioning K identical draws.

Two further hazards are documented. Decomposition is gameable in the direction of leniency: padding a generation with obvious or repetitive subclaims inflates FActScore from 54.0% to 83.0%, and a tautological biography scores 100% against 81.5% for a real one \cite{jiang2025core}. And atomisation destroys the context that error detection needs — fully atomic facts recover only 22.4% of not-supported cases because context-free atoms default to supported, rising to 38.8% with minimal added context \cite{gunjal2024molecular}; individually-factual atoms compose into false paragraphs, overstating Llama-13b-chat by 16.4 points \cite{chiang2024dfactscore}. The failure direction is asymmetric in our setting too: an auditor asked to write executable checks blocked correct code more often than defective code (kill fired 13/56), which is the same leniency-and-misfire pathology arriving through a stricter interface.

Finally, the literature's largest decomposition effects are on *agreement*, not accuracy, and should not be read as recall. Decomposed yes/no questions raise human inter-annotator kappa from 0.284 to 0.532 on identical instructions \cite{qin2024infobench}; checklists raise cross-model Krippendorff alpha from 0.09 to 0.48 \cite{lee2025checkeval}. Judge-versus-human gains are an order of magnitude smaller — 5.8 points of exact agreement for TICK \cite{cook2024tick}, +0.039 Spearman for FLASK \cite{ye2024flask}, whose own ablation shows the reference answer contributes +0.164, four times more than skill decomposition. Rao and Callison-Burch \cite{rao2026agreement} further show that on binary verdicts, the standard output of a decomposed rubric, Pearson, Spearman, Kendall, phi and MCC coincide, so ordinal-scale and binary-item agreement figures are not commensurable across these papers. Cost compounds the ambiguity: measured pipelines run roughly 60 model and search calls per response for VeriScore and 49,622 tokens for SAFE \cite{rajendhran2025verifast, wan2025fastfact}, against one call for a holistic judge. No prior work we found reports decomposition recall under a fixed false-positive budget, which is the comparison an audit ceiling requires and the one we make.

---

```bibtex
@inproceedings{min2023factscore,
  title     = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},
  author    = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},
  booktitle = {Proceedings of EMNLP},
  year      = {2023},
  eprint    = {2305.14251},
  archivePrefix = {arXiv}
}

@inproceedings{wei2024longfact,
  title     = {Long-form Factuality in Large Language Models},
  author    = {Wei, Jerry and Yang, Chengrun and Song, Xinying and Lu, Yifeng and Hu, Nathan and Huang, Jie and Tran, Dustin and Peng, Daiyi and Liu, Ruibo and Huang, Da and Du, Cosmo and Le, Quoc V.},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2024},
  eprint    = {2403.18802},
  archivePrefix = {arXiv}
}

@article{mahmoud2025mcet,
  title   = {{MCeT}: Behavioral Model Correctness Evaluation using Large Language Models},
  author  = {Mahmoud, Khaled Ahmed and others},
  journal = {arXiv preprint arXiv:2508.00630},
  year    = {2025},
  note    = {Huawei Research Canada. Author list and per-variant results table unverified; arxiv.org was unreachable at time of writing}
}

@inproceedings{dhuliawala2023cove,
  title     = {Chain-of-Verification Reduces Hallucination in Large Language Models},
  author    = {Dhuliawala, Shehzaad and Komeili, Mojtaba and Xu, Jing and Raileanu, Roberta and Li, Xian and Celikyilmaz, Asli and Weston, Jason},
  booktitle = {Findings of the Association for Computational Linguistics: ACL},
  year      = {2024},
  eprint    = {2309.11495},
  archivePrefix = {arXiv}
}

@inproceedings{song2024finesure,
  title     = {{FineSurE}: Fine-grained Summarization Evaluation using {LLM}s},
  author    = {Song, Hwanjun and Su, Hang and Shalyminov, Igor and Cai, Jason and Mansour, Saab},
  booktitle = {Proceedings of ACL},
  year      = {2024},
  eprint    = {2407.00908},
  archivePrefix = {arXiv}
}

@article{zhang2026rethinking,
  title   = {Rethinking Atomic Decomposition for {LLM} Judges: A Prompt-Controlled Study of Reference-Grounded {QA} Evaluation},
  author  = {Zhang, Xinran},
  journal = {arXiv preprint arXiv:2603.28005},
  year    = {2026},
  note    = {Single-author preprint; 200 examples per dataset; single human annotator}
}

@inproceedings{doddapaneni2024blindspots,
  title     = {Finding Blind Spots in Evaluator {LLM}s with Interpretable Checklists},
  author    = {Doddapaneni, Sumanth and Khan, Mohammed Safi Ur Rahman and Verma, Sshubam and Khapra, Mitesh M.},
  booktitle = {Proceedings of EMNLP},
  year      = {2024},
  eprint    = {2406.13439},
  archivePrefix = {arXiv}
}

@article{srikanth2025microscope,
  title   = {{NLI} under the Microscope: What Atomic Hypothesis Decomposition Reveals},
  author  = {Srikanth, Neha and Rudinger, Rachel},
  journal = {arXiv preprint arXiv:2502.08080},
  year    = {2025}
}

@inproceedings{hu2025dilemmas,
  title     = {Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?},
  author    = {Hu, Qisheng and Long, Quanyu and Wang, Wenya},
  booktitle = {Proceedings of NAACL},
  year      = {2025},
  eprint    = {2411.02400},
  archivePrefix = {arXiv}
}

@article{akhter2026bottleneck,
  title   = {The Alignment Bottleneck in Decomposition-Based Claim Verification},
  author  = {Akhter, Mahmud Elahi and Ruggeri, Federico and Bilal, Iman Munire and Procter, Rob and Liakata, Maria},
  journal = {arXiv preprint arXiv:2602.10380},
  year    = {2026}
}

@inproceedings{jiang2025core,
  title     = {Core: Robust Factual Precision with Informative Sub-Claim Identification},
  author    = {Jiang, Zhengping and Zhang, Jingyu and Weir, Nathaniel and Ebner, Seth and Wanner, Miriam and Sanders, Kate and Khashabi, Daniel and Liu, Anqi and Van Durme, Benjamin},
  booktitle = {Findings of the Association for Computational Linguistics: ACL},
  pages     = {19833--19856},
  year      = {2025},
  eprint    = {2407.03572},
  archivePrefix = {arXiv}
}

@inproceedings{gunjal2024molecular,
  title     = {Molecular Facts: Desiderata for Decontextualization in {LLM} Fact Verification},
  author    = {Gunjal, Anisha and Durrett, Greg},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP},
  pages     = {3751--3768},
  year      = {2024},
  eprint    = {2406.20079},
  archivePrefix = {arXiv}
}

@inproceedings{chiang2024dfactscore,
  title     = {Merging Facts, Crafting Fallacies: Evaluating the Contradictory Nature of Aggregated Factual Claims in Long-Form Generations},
  author    = {Chiang, Cheng-Han and Lee, Hung-yi},
  booktitle = {Findings of the Association for Computational Linguistics: ACL},
  year      = {2024},
  eprint    = {2402.05629},
  archivePrefix = {arXiv}
}

@inproceedings{qin2024infobench,
  title     = {{InFoBench}: Evaluating Instruction Following Ability in Large Language Models},
  author    = {Qin, Yiwei and Song, Kaiqiang and Hu, Yebowen and Yao, Wenlin and Cho, Sangwoo and Wang, Xiaoyang and Wu, Xuansheng and Liu, Fei and Liu, Pengfei and Yu, Dong},
  booktitle = {Findings of the Association for Computational Linguistics: ACL},
  year      = {2024},
  eprint    = {2401.03601},
  archivePrefix = {arXiv}
}

@inproceedings{lee2025checkeval,
  title     = {{CheckEval}: A Reliable {LLM}-as-a-Judge Framework for Evaluating Text Generation using Checklists},
  author    = {Lee, Yukyung and Kim, Joonghoon and Kim, Jaehee and Cho, Hyowon and Kang, Jaewook and Kang, Pilsung and Kim, Najoung},
  booktitle = {Proceedings of EMNLP},
  year      = {2025},
  eprint    = {2403.18771},
  archivePrefix = {arXiv}
}

@article{cook2024tick,
  title   = {{TICK}ing All the Boxes: Generated Checklists Improve {LLM} Evaluation and Generation},
  author  = {Cook, Jonathan and Rockt{\"a}schel, Tim and Foerster, Jakob and Aumiller, Dennis and Wang, Alex},
  journal = {arXiv preprint arXiv:2410.03608},
  year    = {2024},
  note    = {Preprint; no confirmed venue}
}

@inproceedings{ye2024flask,
  title     = {{FLASK}: Fine-grained Language Model Evaluation based on Alignment Skill Sets},
  author    = {Ye, Seonghyeon and Kim, Doyoung and Kim, Sungdong and Hwang, Hyeonbin and Kim, Seungone and Jo, Yongrae and Thorne, James and Kim, Juho and Seo, Minjoon},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024},
  eprint    = {2307.10928},
  archivePrefix = {arXiv}
}

@article{rao2026agreement,
  title   = {Agreement Metrics for {LLM}-as-Judge Evaluation: What to Report and Why},
  author  = {Rao, Delip and Callison-Burch, Chris},
  journal = {arXiv preprint arXiv:2606.00093},
  year    = {2026}
}

@inproceedings{rajendhran2025verifast,
  title     = {{VeriFastScore}: Speeding up Long-form Factuality Evaluation},
  author    = {Rajendhran, Rishanth and Zadeh, Amir and Sarte, Matthew and Li, Chuan and Iyyer, Mohit},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP},
  year      = {2025},
  eprint    = {2505.16973},
  archivePrefix = {arXiv}
}

@article{wan2025fastfact,
  title   = {{FaStfact}: Faster, Stronger Long-Form Factuality Evaluations in {LLM}s},
  author  = {Wan, Yingjia and Tan, Haochen and Zhu, Xiao and Zhou, Xinyu and Li, Zhiwei and Lv, Qingsong and Sun, Changxuan and Zeng, Jiaqi and Xu, Yi and Lu, Jianqiao and Liu, Yinhong and Guo, Zhijiang},
  journal = {arXiv preprint arXiv:2510.12839},
  year    = {2025}
}
```
