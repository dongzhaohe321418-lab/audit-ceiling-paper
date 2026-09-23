# Pre-submission review, master tracker

**Not reviewer-facing.** Three mock referees, run in isolated contexts, each given the same
manuscript packet and its own emphasis brief, none shown another's report. Decision treated as
**major revision** on all three postures.

Status vocabulary. **Resolved** — the change is in the repository and the commit is named.
**Partly resolved** — some of the concern is answered and the remainder is stated as an open
limitation rather than fixed. **Declined** — the concern is understood and not acted on, with a
reason. **Open** — requires work not yet done.

| ID | Concern, in one line | Status | Where |
|---|---|---|---|
| R1-M1 | One estimator, two names: 33/110 is "union recall", 67/110 becomes "flag coverage" | **Partly resolved** | `CLAIMS.md` forbidden-claims list corrected; the main-text naming is **open** |
| R1-M2 | Residual is 57 at three families, 32 at six; the class that leaves supplies the third leg | **Resolved** | `results.tex`, §3.4; computed 43 of 68 undetermined instances are flagged by some family, and the undetermined share is 44/57 = 77.2% against 25/32 = 78.1% |
| R1-M3 | The model rater is one of the auditor families whose misses define the population | **Partly resolved** | Disclosed in `methods.tex` and Limitations; a re-rating by a non-participating model is **open** |
| R1-M4 | Title and abstract assert a decomposition the three legs cannot deliver | **Open** | Retitling deferred until R1-M1's naming is settled |
| R1-M5 | Method describes two substrates; one produced nothing; population construction never given | **Open** | |
| R1-M6 | "Cross-vendor" is confounded with "OpenAI model"; no mirror arm | **Declined for now, disclosed** | Running the mirror is a new generation ladder plus two audit ladders; recorded as an unidentified axis |
| R1-M7 | Every primary interval is of unverified coverage and the simulation costs nothing | **Partly resolved** | R2-M3's measurement supersedes it; see below |
| R1-M8 | Bonferroni family membership is never stated per p-value | **Open** | |
| R1-M9 | False-positive rates are quoted as prices without adjudication | **Open** | |
| R2-M1 | The abstract quotes the interval the paper's own rule forbids | **Resolved** | `54a5802`; all four sites now carry the exact unconditional [−3.6, +26.8], which contains zero |
| R2-M2 | "Falls monotonically" is contradicted by its own source table | **Resolved** | `54a5802`; the ladder 1.67–1.68 is printed |
| R2-M3 | The coverage statement reinstates a range the source report withdrew | **Open** | The referee's own simulation is more informative than ours and must be reproduced before quoting |
| R2-M4 | Multiplicity is applied to p-values and never to intervals | **Open** | |
| R2-M5 | The flattening statistic is a singleton count; its interval covers a different variance | **Open** | |
| R2-M6 | "All 70 subsets on each side" is false; astra has one | **Open** | |
| R2-M7 | "Twenty readings" overstates effective depth; one family gains 1.8 points over eight | **Open** | |
| R3-M1 | The reviewer of record is a measured auditor family and a ground-truth rater | **Resolved** | `5e2ca54`; disclosed in methods, seventh limitation, astra-ranking claims marked self-assessed |
| R3-M2 | The blinding experiment was not blinded | **Resolved** | `5e2ca54`; inference withdrawn, reduced to an n=1 uncontrolled disagreement count |
| R3-M3 | The repository does not contain what the Reproducibility section claims | **Partly resolved** | `479f36e` states the corpus-licence constraint; the inventory and the runnable code path are **open** |
| R3-M4 | "Every study was preregistered" has a documented counterexample | **Open** | |
| R3-M5 | "No measurement ever moved" is false | **Resolved** | `5e2ca54`; two counterexamples named |
| R3-M6 | The manuscript carries a framing its own ledger has corrected | **Resolved** | §3.4 and `CLAIMS.md` C12 now agree; Figure 3 panel labels **open** |
| R3-M7 | Five review-status statements stale or contradictory; 44 against 47 rounds | **Resolved** | `5e2ca54`; count corrected to 47 with its convention |

## Where the referees agree

Two or more raised, independently:

* **The prose overstates what the records support, and the errors run toward the hypothesis.**
  R1 found it in the naming of an estimator, R2 in an interval and a monotonicity claim, R3 in
  the preregistration and no-measurement-moved claims. Three of R2's four were in our favour.
* **The instrument that validates the work shares the failure mode under study.** R1 raised it
  about the rater, R3 about the reviewer. Both are the same model, `gpt-6-astra`.
* **Coverage is stated rather than bounded.** R1-M7 and R2-M3, from opposite directions.

## What no referee challenged

No referee found an arithmetic error. R2 reproduced six headline quantities from the raw records
with an independent implementation and every one matched. R1 verified five studies directly. R3
recomputed the Bonferroni threshold, the survival probabilities, the exchange rate and every
percentage-point difference in the results. **The measurements are not in dispute; the sentences
built on them were.**
