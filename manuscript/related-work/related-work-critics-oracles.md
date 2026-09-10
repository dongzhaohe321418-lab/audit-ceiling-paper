# Related Work: Critics, Test Oracles, and What a Benchmark's Hidden Suite Actually Decides

Each paragraph marks how far its claim was checked: **[read]** the paper's own text was
fetched and the figure taken from it, **[abstract]** only the abstract or a search summary was
seen, **[source]** a released artefact was inspected directly. Nothing below is quoted from
memory.

## Critics that read code

The closest published relative of our reading auditor is the trained critic. OpenAI's
CriticGPT is an RLHF-trained model that writes natural-language critiques of model-written
code; on code containing inserted bugs it outperforms both unaided contractors and a baseline
assistant, and human–critic teams hallucinate less than the critic alone \citep{mcaleese2024critics}
**[abstract]**. Two differences set our measurement apart, and both matter for what a ceiling
means. First, CriticGPT is evaluated largely on *inserted* bugs, which are specification-
determined by construction; our stratum P is the residue of an ordinary generation run, where
whether the specification determines the failure is exactly the open question (§Results,
claim 4). Second, the reported quantity is a preference or a per-critique comparison, not the
union recall of repeated independent readings, so it says nothing about where reading
saturates. Our injection study is deliberately built to sit on CriticGPT's side of that line so
the two populations can be compared under one auditor.

Aggregating several review passes is known to help. SWR-Bench evaluates automated code review
on 1,000 manually verified pull requests with full project context and reports that a simple
multi-review aggregation raises F1 by up to 43.67% \citep{zeng2025swrbench} **[read]**. That is
the same mechanical move as our union-of-K, used in the opposite direction: as a method for
improving a reviewer rather than as an instrument for finding its limit. We are not aware of
published saturation curves — union recall as a function of the number of independent
readings, with the marginal gain of the last reading — for code review, and that gap is what
claim 1 fills.

Recall is also known to fall as the number of defects in one artefact rises. A controlled
injection benchmark over 40,000 files reports a *count bias*: models under-report, with recall
below 0.30 in high-density Python settings against near-perfect F1 on single-defect C tasks
\citep{beyond2025multivuln} **[read, abstract-level figures]**. Their manipulated variable is
defect density and ours is the number of readings; the two are complementary, and their
released construction is the natural second substrate for our saturation curve because its
ground truth, like our injected population's, does not depend on a benchmark's oracle.

## What the hidden suite decides, and what the prose decides

Our central negative result — that most of what the auditors missed is failure the prose does
not determine — belongs to a line that has been converging on the same point from several
directions.

EvalPlus rebuilt HumanEval and MBPP with far larger test suites and reported defects in the
original reference solutions themselves \citep{liu2023evalplus} **[abstract]**. More telling
for our purposes is what its code does rather than what its paper says: `_special_oracle.py`
carries bespoke oracles for the tasks where differential testing against the reference was not
applicable — eight MBPP tasks whose output *order* the prose leaves open, and three tasks whose
hand-written oracle docstring states which reading the authors chose, for instance that a
pyramid's "height" is the perpendicular distance to the apex \citep{liu2023evalplus} **[source]**.
Each of those is an engineering record that the specification did not settle the expected value.

Richter and Papadakis name the phenomenon and measure it: models collapse onto a single
incorrect reading of an underspecified task rather than producing the diverse outputs an
ambiguity would predict, affecting over 10% of MBPP tasks, and their §1 footnotes name twelve
MBPP tasks they identified by hand as ambiguous, incomplete or contradictory
\citep{richter2026collapse} **[read]**. Twelve of those tasks fall inside our defect
population; our raters, who labelled them before this paper was fetched, call ten of them
oracle-defined, and both disagreements sit on their *incomplete* class, which is precisely the
boundary our two categories draw. Related work reaches the same conclusion by a third route:
three researchers independently reviewed a classifier's flags on MBPP originals and confirmed
72.7% of them as under-specified, though the task ids were not released
\citep{specvalidator2026} **[read, ids unavailable]**.

The oracle problem is the same fact seen from the test-generation side. On HumanEval, 88.89%
of errors in model-generated test cases are wrong expected values rather than invalid inputs
\citep{chen2023testing} **[abstract]**; a study of 24 Java repositories finds that generated
oracles tend to capture the code's *actual* behaviour rather than its intended behaviour
\citep{konstantinou2024oracles} **[read]**. Our claim is the auditing counterpart: when the
prose does not fix the value, neither a generated test nor a reading auditor has anything to be
right about, and a recall number computed against that suite measures the benchmark as much as
the auditor.

## Consensus as a substitute for ground truth

Several systems propose to validate generated tests without a reference implementation by
agreement — self-consistency and majority voting over sampled test cases, cross-validation of
code against tests, or multi-agent discussion converging on an expected value
\citep{convertest2026, hallucination2025consensus} **[read abstract; full method not verified]**.
Both report gains in test validity and coverage; neither, as far as we can see from what is
published, reports how many *wrong* assertions survive the filter, which is the quantity that
decides whether the filter can be trusted. We measure it directly on a frozen set of
canonical-failing tests and find that corroboration across independent generations does not
reach the threshold we preregistered, because wrong tests recur by problem: the draws agree
because the problem is hard or its prose is loose, not because agreement tracks correctness.
This is the concrete case of a general result — self-consistent errors are exactly the class
that consistency-based detectors cannot see \citep{tan2025consistent} **[cited in the ensembles
note]**.

## Who audits whom

That an evaluator should not be the model under evaluation is by now a standard
recommendation, supported by measurements of self-preference and family bias in LLM judges
\citep{selfpref2025, biasintheloop2026} **[abstract]**. Our contribution is not the
recommendation but its size on model-free ground truth: replacing the cross-vendor auditor with
a same-vendor one costs 12.7 points of union recall at eight readings, and replacing it with a
stronger same-vendor model costs 26.4. Architectural work on agent runtimes argues for
enforcement surfaces no execution path can bypass \citep{sarc2026} **[abstract]**; the audited
runtime measured here satisfies that property and adds the vendor separation, which is the
part these measurements are about.

## Preregistration in this literature

Preregistering an evaluation protocol before the models exist is beginning to appear in machine
learning, both as a proposal for agent experiments and as a defence against tuning a pipeline
until it reports what the author wanted \citep{prereg2026agents, prereghacking2026}
**[abstract]**. Every study reported here was preregistered before its first model call, and
every departure is recorded as a numbered amendment with the reason and the timing; four of our
own hypotheses were killed by their preregistered rules. We record this as method rather than
as a contribution, but it is the reason the negative results in this paper can be read as
results rather than as failures to find an effect.
