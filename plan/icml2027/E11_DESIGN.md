# E11 design: second-domain replication by localised edits (draft, 2026-11-14)

## Why
After E9 and E10, GPT's re-review (reviews/review_gpt_M2.md) scores the paper 6/10 and names the remaining weakness:
all evidence comes from 41 selected units of short HumanEval+/MBPP+ functions; E7 (BigCodeBench) stopped at
construction. A convincing second-domain replication is the one change it expects to move the score to 7.

## Why E7 failed, and the fix
E7's funnel (held out): 93 tasks -> 37 pre-admitted -> 18 admitted -> 7 red team -> 5 both judges. The main rejections
were independent implementations that disagreed with the reference outside the open class, or rule-B implementations
that disagreed with the reference: on library-heavy tasks two models writing whole programs from scratch differ in
many incidental ways. E11 removes that source of failure by construction:
- Program B = the reference with the open class handled by an explicit guarded branch that reproduces the
  reference's behaviour; program A = the same file with that branch implementing rule A. Both programs are byte-equal
  outside the branch, so they agree with the reference outside the class by construction, and they differ only in
  the open behaviour; neither is the untouched benchmark solution, so recognition of the canonical code cannot tell
  them apart.
- A model writes the branch (condition from the frozen class predicate, body for each rule); execution then checks,
  as in E6 v4.3: B agrees with the reference on every registered input; A agrees outside the class; A and B differ on
  at least two valid class inputs; both pass the visible tests; red team; two judges blind to which rule is the
  benchmark's, plus E9-style judges outside the construction with contradiction (resolved) items.

## Population
E7's 121 deterministic BigCodeBench tasks (28 development / 93 held out), reusing E7's frozen corpus, hidden inputs and
proposals where valid. No E7 task was ever audited, so held-out audit outcomes are unseen; E7's construction records
were seen and this is disclosed. If fewer than 20 held-out units survive, extend to further unused BigCodeBench tasks
by the same frozen filter before any audit.

## Arms and analysis
E6's arms restricted to the confirmatory set: none, sentence-a, sentence-b, pointer (E10's), two low-budget
configurations, two readings per cell (32 readings per unit). Registered hypotheses mirror E6-5 and E10-1 and the
convention advantage E6-2 / flag preference, with E6's frozen scoring and the BigCodeBench comparator from E7.
Feasibility gate fixed before any audit: at least 20 held-out units after both judges.

## Steps
1. Branch-writing prompt and executable checks (`benchmarks/e11/`), development pilot on the 28 development tasks.
2. Preregistration; GPT review; freeze; held-out construction; gate.
3. If go: held-out audits (about 32 x units calls), witnesses, analysis; E9-style admissibility check.
4. Paper: replace the E7 paragraph with E11, keeping E7's negative result.

## Risks
Explicit guarded branches may make the open behaviour conspicuous to auditors (a code-level pointer); E10's pointer
arm measures that kind of effect, and the none arm reports it. Library tasks may resist a clean class predicate.

## Development pilot, first attempt (2026-11-14)
27 development tasks with E7 proposals: 108/108 edits parsed; pre-admitted 18 (E7: 12), admitted under v4.3 11
(E7: 2), red team passed 6 (E7: 0), both judges 4 (E7: 0). Localised edits remove E7's main failure. At this yield the
88 held-out proposals would give about 13 units, below the gate of 20, so E11 adds E6's second, outcome-blind
construction attempt for problems without a first-attempt unit (piloting now); a wider deterministic library list
would add only 27 tasks.
