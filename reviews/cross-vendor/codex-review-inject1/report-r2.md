**The withdrawal is justified, but it is not complete at `d3f8334`.** The repair also introduces factual errors. The underlying blocking counts survive as descriptive observations; neither headline survives as prospective evidence for C4.

I modified no files.

**1. The withdrawal has not reached every place the claim lives.**

The banner explicitly says the old results are retained, which preserves history. But the executable report and standalone records still produce the withdrawn interpretation without that banner.

These passages remain in [RESULTS-INJECT.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/RESULTS-INJECT.md:28):

| Location | Surviving claim |
|---|---|
| Lines 31–48 | Specification-determinedness is “fixed by construction”; the primary table labels I “defects the specification determines”; H22a is declared positive on that denominator. |
| Lines 78–82 | “What survives” is 84.2%, which the study “should lead with.” |
| Lines 114–116 | “The auditor is responding to the defect, not to the problem.” The contrast identifies response to the **edit**, including its cues. |
| Line 132 | The fitted asymptote is explicitly “quotable.” |
| Lines 136–149 | The result excludes auditor ability as the explanation of the ceiling and licenses a claim about detecting specification-determined defects. |
| Lines 236–238 | The same-vendor gate is still called conservative, invoking the withdrawn argument. |

Other surviving locations matter independently:

- [report_inject.py](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/report_inject.py:302) still generates the entailment-labelled table and “quotable” asymptote. Its output retains `H22a_primary`, `kill.fires: false`, and a prospective-replication interpretation, without withdrawal metadata.
- The standalone [tables.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/records/inject/tables.md:1) consequently carries those claims without the results banner.
- [PREREGISTRATION.md](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject/PREREGISTRATION.md:18) retains the construction guarantee, the conservativeness argument, Amendment 1’s “can only lower recall,” Amendment 3’s conservative-gate claim, and Amendment 5’s “injected defect and nothing else.” These should remain historical evidence, but need explicit local supersession notices.
- [splice_tables.py](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject/splice_tables.py:32) still requires the cross-tab introduction “it points the other way.” That is a surviving endorsement in executable reporting machinery.
- `benchmarks/CORRECTIONS.md` has no study-22 withdrawal entry, despite the binding experiment-record requirement.

The historical commits should **not** be rewritten. Preserve their claims and timestamps, while making current outputs unambiguously identify which interpretations were withdrawn.

**2. The F6 diagnosis is substantially right, but inaccurate and incomplete. Other filters also under-deliver.**

The complete acceptance predicate for F6 is indeed:

```python
bool(obj.get("witness_input"))
```

There is no later recovery, execution, or connection to the actual hidden failure. Study 21’s `witness_for` path exists but is never called here.

However, “non-empty string check” is false. Among the **281 filter-accepted injections, 179 witnesses are strings and 102 are lists**. F6 checks truthiness, without validating type, argument structure, or meaning. [Implementation](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-inject/benchmarks/code/inject.py:200)

I also exercised these discrepancies using the real filter and suite-result logic, with subprocess execution through `-c` to avoid filesystem writes:

| Filter | Registered claim | Implemented limitation |
|---|---|---|
| F1 | Whitespace-normalized substring, at least six words | Implements that textual check; establishes no semantic connection. |
| F2 | Every visible test passes | Binary suites can report success after `SystemExit(0)` before any assertion completes. |
| F3 | Hidden failure is an assertion or exception, not timeout | Accepts any non-timeout non-pass. An `os._exit(2)` candidate passed all six filters without an assertion or exception. |
| F4 | Adds no import | Compares **sets of module names**. Adding `from math import cos` beside existing `import math` passes. |
| F5 | Compiles and completes at least one visible test | Checks only no visible timeout and no `"SyntaxError"` substring. It remained true after an immediate `ZeroDivisionError`. The early-exit example passed F2 and F5 without completing a test. |
| F6 | Records witness and recovers first failing hidden input | Checks truthiness only. |

These counterexamples establish implementation gaps, not their prevalence in the archived population.

The repair also overstates what registered F6 would have established. Recovering the hidden input and executing a witness still does **not** prove that the specification entails the hidden expected value.

I sampled from sorted IDs using `Random(20260920)`, separately for fifteen members of I and ten filter-rejected instances. The corpus was absent from this worktree; I used the integration checkout’s copy after confirming all three hashes match this branch’s pinned manifest.

All fifteen accepted edits passed the visible suite and failed the hidden suite with the configured executor. My independent semantic decisions are:

| Accepted instance | Admit as a specification violation? |
|---|---|
| `b2:Mbpp/554` | Yes: drops negative odd integers. Supplied witness has incorrect argument nesting. |
| `b2:Mbpp/631` | Yes: collapses consecutive replacements. |
| `b2:Mbpp/82` | Yes: uses radius squared below 10 for sphere volume. |
| `b1:Mbpp/744` | Yes: requires exactly one `None` instead of any. |
| `b1:Mbpp/256` | Yes: counts a prime below 2. |
| `b2:Mbpp/171` | Yes: uses four sides for some pentagons. |
| `b2:HumanEval/9` | Yes: initializes rolling maximum to zero. Witness nesting is wrong; the named class is too broad. |
| `b2:HumanEval/117` | Yes: removes repeated qualifying words. |
| `b1:Mbpp/62` | Yes: excludes the final element from the minimum. |
| `b2:Mbpp/165` | Yes: excludes the 26th position. Supplied `['z']` returns zero in both versions. |
| `b1:HumanEval/123` | Yes: removes required sorting. The duplicate-odd-number portion of its class description is unnecessary. |
| `b1:Mbpp/79` | Yes: substitutes length modulo four for oddness. |
| `b2:Mbpp/390` | Yes: formats only four elements. |
| `b2:Mbpp/257` | Yes: changes the sign while swapping. |
| `b2:HumanEval/4` | Yes: rounds the mean. Witness nesting is wrong; even after repairing nesting, that witness returns 1.5 in both versions. |

These are admissions on independently inspected semantics, **not certifications that their registered witness evidence was complete**. They show why “membership was not established” must not become “the population contains no specification-determined defects.”

For rejected instances, only the first retained candidate is reviewable:

| Rejected instance | Decision on stored candidate |
|---|---|
| `b2:Mbpp/778` | Reject: omitting a final singleton breaks visible tests. |
| `b1:Mbpp/770` | Reject: excludes the nth term; breaks visible tests; quote also too short. |
| `b1:Mbpp/130` | Reject: returns maximum value instead of mode; visible failure. |
| `b2:Mbpp/222` | Reject: accepts mixed types; visible failure. |
| `b2:HumanEval/77` | Reject: truncating cube-root calculation breaks visible tests. |
| `b2:HumanEval/140` | Reject: `> 2` → `>= 3` is equivalent here. |
| `b1:Mbpp/626` | Reject: halves the area; visible failure. |
| `b2:Mbpp/131` | Reject: unchanged code. |
| `b2:HumanEval/141` | Reject: only adds a comment about an existing condition. |
| `b1:HumanEval/120` | Reject: equivalent handling of permitted nonnegative `k`. |

None should have been retained under the registered construction rules. But that conclusion cannot cover their later attempts: `last_code` and `last_quote` use `setdefault`, retaining the **first**, not last, rejected candidate. Later attempts have hashes and filter results, without their candidate text.

The new “seven comments” claim is not reproducibly specified. Scanning Python comment tokens in stored `code` and `last_code` finds **21 distinct instance IDs** containing “bug,” “buggy,” or “defect”: 18 filter-rejected candidates and three filter-accepted candidates. Only `b2:Mbpp/643` reached I. Both gates accepted it, it was flagged **8/8**, and exclusion gives:

\[
89/91=97.8022\%.
\]

That recomputation is correct. It excludes that explicit comment as an explanation of the aggregate result; it does not exclude broader salience. Also, “nothing … was looking for conspicuousness” overstates the failure: the injector prompt explicitly discouraged markers, comments, and deliberate-looking edits. Enforcement was absent.

**3. Descriptive observations survive. C4 does not.**

The blanket position “nothing remains quotable” is too strong—and Amendment 7 itself explicitly preserves descriptive reporting.

I reran the reporter’s computation and rendering in memory:

- `numbers.json`: byte-identical.
- `tables.md`: byte-identical.
- All six generated blocks: exact matches to their splices.

The rejected-arm and stratified results are **absent from the reporter and JSON**. Their table is manually present in the results, contradicting “no figure here is typed by hand.” Nevertheless, independent reconstruction produces:

| Quantity | Independently recovered |
|---|---:|
| Gate-accepted blocking | 90/92 |
| Unmodified twins blocked | 11/92 |
| Discordant pairs | 79 injected-only; 0 twin-only |
| Paired difference | 85.8696 points |
| Paired problem-bootstrap interval | [77.2727, 93.2584] |
| Exact McNemar p | \(3.30872\times10^{-24}\) |
| Gate-rejected sample | 31/40 |
| Frozen natural comparator | 33/110 |
| Stratified estimate | 84.1548% |
| Stratified bootstrap interval | [73.7523%, 93.1016%] |

The independently reconstructed subset-averaged curve is **94.4, 96.5, 97.0, 97.4, 97.6, 97.7, 97.8, 97.8%**. Its K=1 value averages all eight single readings; the actual first draw flagged 86/92.

The stratified estimator is appropriate for the **281 filter-accepted instances**:

\[
\widehat p=\frac{92}{281}\frac{90}{92}
+\frac{189}{281}\frac{31}{40}.
\]

It does not estimate recall on independently established specification-determined defects.

The bootstrap genuinely incorporates variation in the sampled rejected stratum; it does not pretend all 189 were audited. But its advertised coverage is unvalidated. It resamples the fully observed accepted stratum, omits finite-population sampling treatment for the 40-of-189 sample, and independently resamples strata sharing one problem. Those choices require an explicit target—fixed population versus a wider population—and coverage validation. Under the programme’s own §10, the combined conditional interval should be labelled **uncalibrated**.

The duplication finding is partly correct:

- I has **59 distinct program hashes**, with **33 duplicate groups covering 66 instances**.
- **No duplicate group crosses problems.** Problem resampling keeps those duplicates together.
- This does not prove coverage or that problem clustering is universally “at least as conservative.”
- The rejected sample has **35**, not 40, distinct programs. Its five duplicated problems are `HumanEval/43`, `Mbpp/140`, `Mbpp/266`, `Mbpp/569`, and `Mbpp/95`.

The Wilson warning is visible in the results but does not travel with standalone tables. The recommended Tango interval also assumes independent pairs; recommending it without that qualification does not solve duplication.

The probe arithmetic reproduces: **147/152 correct**, with **32 unparsed**; bounds over all 184 are **79.9–97.3%**. But two limitations were missed:

1. **The prober was a gate.** `claude-opus-4-8` appears in all 281 second-gate verdicts and all 184 probe usage entries. “Not a gate” is false.
2. The probe’s injected and natural populations share **zero problem IDs**. It measures separation of these populations using specification and code, not isolated edit conspicuousness.

Consequently, the repair’s assertion that the probe measured the *consequence of the retry mechanism* is itself unsupported causal language.

The cross-tab is correctly reconstructed as **63/65 edited, 4/4 natural-looking, 23/23 unparsed**, with two-sided Fisher **p=1.0** for the classified cells. Its stated 11% probability and 0.12 expectation use **69 classified instances**, not 92; over 92 they are 8.55% and 0.087. More fundamentally, that calculation assumes exchangeable misses, not an auditor “riding exactly” the probe signal. The table supplies no useful discrimination between the proposed explanations; it does not prove equivalence. The old splice-registry sentence still leans on it.

What survives is a narrow description of blocking, gate-associated selection, and population separability. No naming adjudication has run. The remaining “responding to the defect” and “caught” language should not imply verified defect identification.

One defensible reader sentence is:

> On this constructed sample, the auditor blocked 90 of 92 gate-accepted edited programs and 11 of their 92 unmodified twins; the comparison does not establish whether the response was to specification violations or other cues introduced by the edits.

A concrete alternative explanation remains: the visible examples cover only positive values, length-four lists, or multiples of five; the injector preserves those cases by adding conspicuous exceptions such as “use four sides unless divisible by five.” Such edits can produce high blocking across **both gate strata**, while natural hidden-suite failures remain difficult. Removing the edit removes the exception and its cues. Neither comparison distinguishes that explanation from C4.

**4. Independent establishment is necessary, but the proposed successor is underspecified.**

A different person or model can reproduce the same selection bias. Executing F6 and matching the named class to a hidden input also leaves the central oracle question unanswered.

A prospective successor should:

- Sample a fresh, prespecified natural-defect population before auditor outcomes are available.
- Independently establish that the **specification** requires an outcome and excludes the candidate’s—not merely that a reference implementation disagrees.
- Freeze labels before auditing; blind raters to audit outcomes and retain ambiguous/disputed cases under predetermined rules.
- Compare determined and oracle-dependent cases within the same sampling frame, with suitable problem matching or adjustment.
- Prespecify K, blocking versus naming endpoints, estimands, thresholds, and clustered uncertainty.
- For injections, control edit salience independently. Moving this same probe earlier is insufficient; “chance not excluded” would also require an equivalence design, not a non-significant test.

That could prospectively test the earlier **association**. Establishing that the ceiling is *mostly caused* by oracle-definedness additionally requires an operational definition of “mostly” and a design addressing the competing explanations.

The amendment chronology is substantially recoverable. Amendments 1–3 adapted construction after pilots; they were outcome-informed about yield, though not auditor recall. Amendments 4–5 preceded auditing. Amendment 6 followed known results, but preceded its own new arm: **01:12:45 registration, 01:13:19 implementation, 01:13:26.617 first recorded completion**, September 12, UTC+8. The weighted 84.2% headline was not specified there and remains post hoc.

One historical note is wrong: the population-freeze commit followed five paid audit completions, although the population artifact itself predates them. Those five calls cost approximately **$0.0499**, contrary to the subsequent commit’s “nothing spent” account. The history should preserve and annotate that distinction.

Validation limits: the read-only test subset returned **17 passed, 4 failed, 5 deselected**. Failures cover the hand-added table, obsolete cross-tab anchor/assertion, and obsolete ladder expectation. I did not run the full suite, which requires temporary writes. The study diff leaves `src/`, kernel code, and frozen comparator implementation untouched. Committed study records contain no full solutions or finding prose; the absolute “no specification text” claim is too broad, since short quotations—including the `Mbpp/294` prompt in a test—are committed.

**Not quotable as prospective C4 evidence — the construction never independently established the denominator required by that claim.**
