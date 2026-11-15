# ICML 2027 submission package (prepared 2026-11-15; re-check after ICML's late-November process announcement)

Deadlines (AoE): abstract registration **2027-01-14**, full paper **2027-01-22**. OpenReview account and profile
needed by 2027-01-08 (an institutional e-mail activates immediately). Submission is done by the author; nothing here
is submitted automatically.

## Files
| Item | File | Notes |
|---|---|---|
| Paper (anonymous) | `tex/paper_v3_submission.pdf` | 8-page main text, references, Impact Statement, AI Disclosure Statement, appendices in one PDF (about 0.4 MB; limit 50 MB). Rebuild: `cd tex && tectonic paper_v3_submission.tex`. |
| Supplementary (anonymous) | `../supplementary/supplementary_anon.zip` | Code, preregistrations and records (about 37 MB). Check the author instructions for the supplementary size limit and whether a zip is accepted. |
| Camera-ready / arXiv (named) | `tex/paper_v3.pdf` | Not for review. |

## OpenReview form
**Title** (subtitle chosen by the co-author in the human review, 2026-11-15; the old subtitle was "from General Code
to Scientific Code, Results and Data"):
> What Moves the Ceiling on Automated Code Audit: Separating Convention Agreement from Defect Detection

**Abstract** (plain text, macros expanded from `tex/numbers.tex`; regenerate if the paper changes):
> Audit benchmarks grade automated code auditors against a hidden reference. When a task leaves a behaviour open, 
> the evidence an auditor sees can fit the program and the reference equally well. Recall minus false-flag rate is 
> then bounded by how well that evidence separates them. A benchmark with one fixed contract cannot show how much 
> of its score this explains. We introduce a randomised-contract evaluation using execution-checked program pairs 
> built from HumanEval+ and MBPP+ tasks. The programs differ only on a behaviour that two model judges deem the 
> task leaves open (a blind human reader agrees on 35 of 41), and are graded against a randomly drawn contract 
> revealed in different ways. With the contract withheld on 41 held-out units, auditors from two vendors flag the 
> program that departs from the benchmark's behaviour 23.8 points more often than the one that follows it 
> (exploratory; registered convention advantage 11.6). The difference is 28.9 points among 38 of 41 units in a 
> preregistered control with all code shared outside one branch body; a stricter symmetric-body control was 
> inconclusive under its registered missing-unit test. Two generator models' task-only solutions follow the 
> benchmark's behaviour 89% of the time; on these units, the benchmark therefore rewards agreement with a 
> convention the models share. One sentence stating the missing requirement adds 76.8 points to verified 
> diagnosis, 60.4 more than a pointer to the inputs concerned, and 58.3 on 18 reference-edited BigCodeBench 
> data-science tasks. In only 34 of 150 natural hidden-test failures do two model classifiers agree that the 
> task's words single out the expected value. Confirmatory analyses were preregistered; we disclose deviations.

**TL;DR** (if the form asks): On code tasks that leave a behaviour open, hidden-test "detections" by LLM auditors
largely reward agreement with the benchmark's convention; stating the missing requirement in one sentence turns them
into verified diagnoses.

**Keywords**: LLM evaluation; code review; automated auditing; benchmark validity; underspecification;
preregistration.

**Contribution type** (required, new in 2027): **Datasets, Evaluations and Benchmarks** (chosen by the co-author in the
human review; alternative **General**).

**Primary area**: evaluation / benchmarks (choose the closest listed area; social and safety aspects of LLMs is a
possible secondary).

**Reciprocal reviewer**: designate one of the two authors as the submission's reciprocal reviewer (each author may be
designated for at most six submissions); if neither is eligible, this uses each author's one allowed submission
without an eligible reviewer. Check eligibility in the Submission Quotas and Reciprocal Reviewing guide.

**LLM policy / AI disclosure**: the paper includes the required AI Disclosure Statement (Claude as research agent,
GPT as reviewer and editor, separate Claude instances as cold reviewers). If the form asks again, use that text.

**Conflicts**: enter institutional and recent co-author conflicts in the OpenReview profile.

## Checks before uploading
- [ ] Re-read ICML's late-November announcement (after 2026-11-25) and the author instructions for any process change.
- [ ] `tex/paper_v3_submission.pdf`: main text ends on page 8; no author names, affiliations or repository links
      (checked automatically in every build here); fonts embedded, no Type-3.
- [ ] Supplementary zip: no names or home paths (checked); size within the limit.
- [x] Human admissibility check (H1): done by a co-author 2026-11-15; in Section 4, the Limitations and the appendix.
- [x] Subtitle: keep "Separating Convention Agreement from Defect Detection" (co-author's choice).
- [ ] AI Disclosure Statement: the co-author answered "can't judge"; the first author signs it off.
- [x] Author list: Zhaohe Dong (Independent researcher; corresponding) and Yuhao Chen (University of Wisconsin–Madison,
      inferred from his wisc.edu address: confirm). Both need OpenReview profiles.
