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
| R1-M1 | One estimator, two names: 33/110 is "union recall", 67/110 becomes "flag coverage" | **Resolved** | `CLAIMS.md` forbidden-claims list corrected; results §3.5 uses one name; the last two main-text uses of "flag coverage" (Figure 2 caption, §3.5 heading) and C11's title renamed to union recall |
| R1-M2 | Residual is 57 at three families, 32 at six; the class that leaves supplies the third leg | **Resolved** | `results.tex`, §3.4; computed 43 of 68 undetermined instances are flagged by some family, and the undetermined share is 44/57 = 77.2% against 25/32 = 78.1% |
| R1-M3 | The model rater is one of the auditor families whose misses define the population | **Resolved, with a smaller number** | P1's L3 (`gpt-5.6-luna`, not one of the residual's families — it was a secondary route, `cheap-cross`, in the explore study; the earlier "no audit role" was false) is shown to have rated exactly the residual (asserted in `rate3/residual_crosstab.py`); §3.4 now reports its 38/57 = 66.7% beside the pair's 77.2% and reads it as support for *most*, not for 77%. The per-instance cross-tab (30 of 44) is pending review in `CLAIMS.md` |
| R1-M4 | Title and abstract assert a decomposition the three legs cannot deliver | **Resolved** | Retitled "What Moves the Ceiling … Measured One at a Time"; abstract and introduction now say each factor is measured alone and the limit is not apportioned; the stale `manuscript/abstract.md` draft, which still asserted withdrawn claims, is superseded by a pointer |
| R1-M5 | Method describes two substrates; one produced nothing; population construction never given | **Resolved** | §2.1 rewritten: one substrate carries every result, the second is named as closed; 542→540 exclusions with reason, generator `claude-haiku-4-5-20251001`, the registered two-pass pooling rule with per-pass P/C/F counts, P 110 on 56 problems, C 150 of 910 by seed. Five stale "both substrates"/"no sweep"/"coverage unvalidated" sentences in the discussion and Limitations fixed; the Limitations still carried R2-M3's withdrawn 2–5-point range |
| R1-M6 | "Cross-vendor" is confounded with "OpenAI model"; no mirror arm | **Declined for now, disclosed** | Running the mirror is a new generation ladder plus two audit ladders; recorded as an unidentified axis |
| R1-M7 | Every primary interval is of unverified coverage and the simulation costs nothing | **Partly resolved** | R2-M3's measurement supersedes it; see below |
| R1-M8 | Bonferroni family membership is never stated per p-value | **Resolved** | `1e3860c`: results §3 states each p value's family — §3.3 in the ceiling study's 16-member family (0.003125); §3.2 is study 18's single primary with no family; P3's are uncorrected beside an interval-registered primary |
| R1-M9 | False-positive rates are quoted as prices without adjudication | **Open** | |
| R2-M1 | The abstract quotes the interval the paper's own rule forbids | **Resolved** | `54a5802`; all four sites now carry the exact unconditional [−3.6, +26.8], which contains zero |
| R2-M2 | "Falls monotonically" is contradicted by its own source table | **Resolved** | `54a5802`; the ladder 1.67–1.68 is printed |
| R2-M3 | The coverage statement reinstates a range the source report withdrew | **Resolved** | `b46542d` measured coverage table replaced the range; `1e3860c` removes a stale results sentence that still said coverage was unvalidated |
| R2-M4 | Multiplicity is applied to p-values and never to intervals | **Resolved** | `1e3860c`: stated in results §3 that intervals are unadjusted and interval-only directions are worded as directions; −5.3 [−10.3, −0.7] no longer "establishes"; `CLAIMS.md` C11 aligned. No adjusted interval computed: the sweep registered no family, and inventing one would be post hoc |
| R2-M5 | The flattening statistic is a singleton count; its interval covers a different variance | **Resolved** | `1e3860c`: §3.1 gives the closed form 17/(8·110), verified against `counts_k`, and says the interval carries task- not reading-sampling variance |
| R2-M6 | "All 70 subsets on each side" is false; astra has one | **Resolved** | `07e255e` in the paper; `38ebc41` in `CLAIMS.md` C11, which had kept the error |
| R2-M7 | "Twenty readings" overstates effective depth; one family gains 1.8 points over eight | **Resolved** | `07e255e`; `def00e0` repaired a split number it left in §3.1 and labels "nearer thirteen" a heuristic |
| R3-M1 | The reviewer of record is a measured auditor family and a ground-truth rater | **Resolved** | `5e2ca54`; disclosed in methods, seventh limitation, astra-ranking claims marked self-assessed |
| R3-M2 | The blinding experiment was not blinded | **Resolved** | `5e2ca54`; inference withdrawn, reduced to an n=1 uncontrolled disagreement count |
| R3-M3 | The repository does not contain what the Reproducibility section claims | **Resolved** | `reproduce.sh` regenerates Figures 1–3 and Table 1 from records in the repo and verifies the table byte-for-byte; run from a fresh clone with HOME unset. Reports, verbatim reviews (both archives) and every study's preregistration mirrored with source commits; README inventory maps claim→report→review→record. The licence statement from `479f36e` was **false** — it applied ExpertLongBench's CC BY-NC-SA to MIT/Apache corpora — and is corrected. Found on the way: Figure 1's false annotation and caption (`d96d878`); the sweep was a second unregistered analysis the paper did not name |
| R3-M4 | "Every study was preregistered" has a documented counterexample | **Resolved** | `b46542d`; the exception is named in the abstract, introduction and methods |
| R3-M5 | "No measurement ever moved" is false | **Resolved** | `5e2ca54`; two counterexamples named |
| R3-M6 | The manuscript carries a framing its own ledger has corrected | **Resolved** | §3.4 and `CLAIMS.md` C12 now agree; Figure 3 panels relabelled by definition and registration status, caption aligned |
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

## Whole-manuscript review, round 1 (`codex-review-paper1`, gpt-6-astra, at `306bd8d`): NOT SUBMITTABLE

Every finding was checked against the records before anything moved; all fifteen held.

| # | finding | action |
|---|---|---|
| 1 | 43/68, 25/32, 78.1% and the coverage cells entered `tex/` without admission | `reports/RESULTS-DERIVED.md` written; listed as pending in `CLAIMS.md`; put to round 2 for a ruling, removed if refused |
| 2 | related work kept study 23's "direction is substrate-dependent" | rewritten as open; forbidden pattern added |
| 3 | P3 called "not conditioned on being missed"; oracle contradictions attributed to the benchmarks; "no model judges any outcome" | all three corrected |
| 4 | "writes down more of what is wrong", "a fact about severity calibration" | replaced by rule-dependence only; abstract likewise |
| 5 | "no measurement moved" false (sweep r1, P1 71→67, P3) | corrected in methods, results, Limitations; an unverified "no measurement moved" about five other studies removed rather than kept |
| 6 | `astra` "beats both" / "dominating on both axes" | replaced by the paired contrasts |
| 7 | abstract and Table 1 dropped mandatory qualifications | C2 operating point, C3 interval and cost, C13 exact p in the abstract; C2 false-positive row and 44/57 interval in Table 1 |
| 8 | one-signed exception unstated; coverage claim too broad in Table 1 caption | exception stated in §2.3; caption narrowed to single-rate intervals. **Found on the way:** P3's bootstrap criterion was close to guaranteed by construction (one-signed discordance, p ≈ 0.003 of a resample below zero); stated in results and C13 |
| 9 | Figure 2 hides unequal depths | caption states K per family |
| 10 | review archive incomplete; methods promised harness assets | early rounds of 3b and testgen-val mirrored; methods now says where the assets live (publishing product source is the owner's decision) |
| 11 | 38/57 read as a smaller estimate of the same quantity | rewritten as a different construct |
| 12 | P3 secondary and naming omission missing | both added |
| 13 | stale review-status statements; "four to eleven rounds" excluded ceiling 1's 21 | corrected in intro, results, methods |
| 14 | "tests nothing" overcorrected | "exploratory, none confirmatory" |
| 15 | reproduce.sh wrote to /tmp, did not refresh tex/ copies; record regeneration overstated | fixed; coverage record verified to regenerate byte-identically |

## Whole-manuscript review, round 2 (at `93615fd`): NOT SUBMITTABLE — `RESULTS-DERIVED.md` quotable

Round 1's findings 3, 5, 9, 10, 11, 13, 14 ruled fixed; 2, 4, 6, 7, 8, 12, 15 partly. Both sections
of `RESULTS-DERIVED.md` ruled **quotable** → admitted as **C14** and **C15**. Eight new findings,
all verified before acting:

| # | finding | action |
|---|---|---|
| 1 | "two-thirds of the headline is how much each union was permitted to grow" allocates cause; related work called the route contrast self-preference; the closing paragraph said recall moves with specification determinacy | allocation removed; self-preference disclaimed; closing paragraph now separates what moves recall from what misses are associated with |
| 2 | coverage stated for all primary intervals; "exact unconditional" unqualified | coverage limited to single rates in results and discussion; the unconditional interval described as grid-approximated and unclustered in results, methods and Table 1 |
| 3 | the ledger kept "severity calibration" and "dominating on both axes"; results said "no false-positive difference" for −0.3 [−3.8, +3.4] | ledger C2 corrected; "unresolved difference" |
| 4 | **our own new sentence overstated**: 0.003 is the probability of a resample being exactly zero, not below it, and the near-guarantee is conditional on five observed success-bearing problems | rewritten conditionally in results and C13; the reviewer's 27 zero resamples in 10,000 reproduced independently before use |
| 5 | the secondary's population misdescribed | now: where study 21's consensus and L3 agree |
| 6 | abstract dropped the cost interval and P3's interval | both added (1867 characters) |
| 7 | the flattening bar's depth dependence was stated backwards | corrected, with the curve's own increments (2.9 at step 4, 1.9 at step 8) |
| 8 | "refreshes the copies" was false | "checks each is byte-identical" |

## Whole-manuscript review, round 3 (at `fb400e3`): NOT SUBMITTABLE — converging

Round 2's findings 3–8 ruled fixed; 1 and 2 partly. C14 ruled faithful; C15 needed narrower
scope. Seven findings, all verified, plus one of ours:

| # | finding | action |
|---|---|---|
| R3-1 (blocking) | "what moved diagnosis was specification text that agreed with the oracle" — a mechanism from a post-hoc split (**our sentence**) | replaced: classified after the outcome, agreeing instances may be easier, does not say which property moved diagnosis; forbidden pattern added |
| R3-2 | Limitations still claimed coverage for "the primary intervals"; C15 overreached rates and implementation; C3 in the ledger said "exact"; methods SE | all scoped: single rates, tested rates 0.10–0.60, 600 resamples, integer-index percentiles vs interpolation, SE 0.01–0.02 |
| R3-3 | intro said the pooled contrast puts the rule outside the false-positive constraint | now the correct-stratum observed rate, 10/56, against 3/56 |
| R3-4 | "partly definitional" overcorrected an empirical association | now empirical, with the disjoint +23.3 [2.0, 43.6], not causal |
| R3-5 | a general law of resampling from per-instance counts; the diminishing shape is by construction | reduced to the arithmetic; stated that the shape is not evidence of a ceiling |
| R3-6 | Bonferroni stated as universal; one p value missing its sign-flip | per-study policy stated; 0.146 / 0.183 |
| R3-7 | Table 1 still said "pending" for C14 | "post hoc (C14)" |
| ours | **"a model with no audit role anywhere" for gpt-5.6-luna was false** — it was `cheap-cross` in the explore study and read these same instances | corrected in results, abstract, tracker, CLAIMS and P4's Amendment 1; forbidden pattern added |

## Whole-manuscript review, round 4 (at `77dbade`): NOT SUBMITTABLE

R3-1, 3, 4, 7 ruled fixed; 2, 5, 6 partly. C14 and C15 keep their admission. Seven findings; the
two about outside papers were checked against the papers themselves before acting.

| # | finding | action |
|---|---|---|
| R4-1 | related work said neither consensus-validation paper measures how many wrong assertions survive the filter — **false**: ConVerTest reports retained-suite precision 84–91% against ground truth; CANDOR reports oracle correctness 0.894–0.930 (both confirmed at source) | rewritten: both measure it; ours differs in unit (retained failing test–candidate applications) and bar (registered 2%) |
| R4-2 | simulation coverage still attributed directly to production intervals and to an estimate rather than a true rate | "simulations of an analogous interval ... at a true rate of 0.03"; discussion scoped; derived report scoped to tested rates |
| R4-3 | sampling asserted as the cause of the flat route in results, the Figure 1 caption, and a discussion heading | all three now say the design does not separate sampling from model |
| R4-4 | "neither beats the free comparator" — not established either way | "neither is shown to improve on it", with the small observed advantage |
| R4-5 | heading still said luna "audited nothing" | "a rater outside the residual's families" |
| R4-6 | two p values without their paired test | both added from the record (1.0e-5; 0.0156 both) |
| R4-7 | SWR-Bench's aggregation (a synthesising model call) equated with a Boolean union (confirmed at source) | distinguished |
