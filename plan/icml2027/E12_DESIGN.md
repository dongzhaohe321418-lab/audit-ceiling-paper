# E12 design: unused library tasks, unmarked edits, contradiction controls (draft, 2026-11-15)

## Why
GPT's re-review after E11 (reviews/review_gpt_M3.md) scores the paper 7/10 and names the remaining limit: E11's 18
units reuse E7's familiar tasks and proposals, and every edited program carries an explicit branch that cues the open
behaviour in every arm. Its suggested change with the greatest upside: one preregistered study on 30-50 previously
unused library tasks, with less conspicuous edits and contradiction (positive) controls.

Meaningful-research check: E12 answers whether the sentence effect survives (a) tasks no earlier study constructed,
and (b) programs whose open behaviour is not marked by a dedicated branch. Either a positive or a null result changes
what the paper may claim about library code; the pilot decides feasibility before any held-out call.

## Population (no new download)
BigCodeBench tasks on disk (`benchmarks/e7/data/bigcodebench.jsonl`, 1,140) that E7/E11 did not use: mock-free tests
with at least three test methods and no file, network, plotting, clock or subprocess code. A first count gives 259
tasks (2026-11-15), 173 of which use randomness (147 seeded in the solution or test). Determinism is established by
execution, not by the filter: each reference is run twice per recorded input in fresh processes and must give equal
outputs under the comparator. The standard-library half of BigCodeBench was audited in an earlier, unreported
substrate study (no contract randomisation); overlapping tasks are disclosed or excluded (decide before the pilot).

## Construction (E11 with two changes)
1. Unmarked edits: the implementing vendor edits the reference so that the program follows the rule, with the
   instruction not to add a dedicated branch, flag, comment or name that singles out the inputs concerned; the change
   must be expressed in the existing logic where possible. Execution checks as in E6/E11. Report edit sizes and the
   share of programs with an added conditional (static check), per rule.
2. Positive controls: E6's `det` kind (behaviours the task's words decide) on the same tasks, so that E9's Disc and
   the selectivity of flagging are estimable.
Everything else: E6 v4.3 admission, red team, the two judges, E6's second attempt, E9's outside judges.

## Arms and hypotheses
E11's arms (none, pointer, sentence-a/b), two low-budget configurations, two readings per cell. E12-1: sentence minus
none; E12-2: sentence minus pointer (ordered, as E11). Positive controls: flag preference on decided behaviours.
Report the false-flag rate (E11: 26.4%) and whether unmarked edits lower pointer minus none.

## Gate and power
Gate 20 held-out units after both judges (fixed now). Effects of 50-60 points (E11) are detectable at 20 with large
margin; the gate protects against a population dominated by a few problems.

## Steps
1. Corpus module and determinism check; count usable tasks (dev/held-out split by seeded hash).
2. Unmarked-edit prompt and static branch check; development pilot (construction only).
3. Preregistration, GPT review, protocol freeze; held-out construction; gate; population freeze.
4. Audits, analysis, E9-style admissibility with controls; paper (transfer paragraph and appendix).
Deadline: ICML 2027 full paper 2027-01-22; E12 must be frozen by mid-December to leave time for writing.

## Feasibility result (2026-11-15, no model calls): E12 not run on this corpus
`benchmarks/e12/corpus12.py` + `prepare12.py` (E7's feasibility check and input recorder, unchanged): 176 eligible
tasks (40 dev / 136 held out); 113 references pass their suites in the executor (nltk, statsmodels and other packages
absent); 37 have at least three deterministic recorded inputs (10 dev / 27 held out). Of the rest, 37 give no
deterministic input (31 use randomness seeded by the test rather than an argument), 22 give one or two, 17 call the
entry point only with keywords. At E11's yield (18 units from 93 held-out tasks), 27 held-out tasks project about 5
units, far below the gate of 20; seeding every call would change E6's frozen execution harness and still project
about 12. Decision: E12 is not run on on-disk BigCodeBench. A second unused library benchmark (e.g. DS-1000) would
need a new download, which requires the user's approval; otherwise the remaining time goes to the paper.
