**1. Decision: proceed to full review.**

> The paper introduces a concrete, execution-checked evaluation design for separating agreement with benchmark conventions from contract-grounded defect diagnosis, supported by experiments with two auditor vendors. This warrants full review, where the design’s originality and the generalisability of its findings beyond constructed cases should receive particular scrutiny.

This applies the supplied screening premise, rather than treating presentation weaknesses as grounds for rejecting an otherwise identifiable contribution.

**2. What the ten-minute reader takes away**

“LLM code auditors mistake shared benchmark conventions for defects, and explicitly stating the missing requirement improves diagnosis.”

That broadly matches the findings, but underplays the intended methodological contribution: **the randomised-contract evaluation instrument**. The current title instead suggests a general theory of audit ceilings spanning code, results and data.

**3. Five changes, with exact replacement text**

**① Replace the title** in [paper_v3.tex](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/tex/paper_v3.tex:38>):

> Separating Convention Agreement from Defect Detection in LLM Code Audits

This identifies the ML contribution and removes the broader promise. **Space:** shorter than the existing title.

**② Replace the entire abstract:**

> Code-audit benchmarks can count agreement with an unstated convention as defect detection. We introduce a randomised-contract evaluation using execution-checked program pairs from HumanEval+ and MBPP+. Each pair implements alternative behaviours judged admissible under the task wording; either program can be correct under the assigned contract. With the contract hidden, recall equals the false-flag rate by construction. Across 41 held-out units and two auditor vendors, programs departing from the benchmark convention are flagged 23.8 percentage points more often (exploratory). Stating the missing requirement increases verified diagnosis by 76.8 percentage points; the increase is 58.3 points on 18 reference-edited BigCodeBench tasks. Verified diagnosis requires an executed witness of a contract violation. These experiments isolate convention preference and the effect of revealing requirements; they do not establish a universal ceiling on natural-code auditing. Confirmatory analyses were preregistered, with deviations disclosed.

**Space:** replaces approximately 262 source words with 150, removing the competing natural-failure and earlier-study narratives.

**③ Replace introduction paragraphs 2–3**, from “Models increasingly…” through “…both are admissible”, in [introduction_v2.tex](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/tex/sections/introduction_v2.tex:11>):

> Audit scores can conflate reasoning failures with missing requirements. Classical hypothesis testing bounds recall minus false-flag rate by the total variation distance between the evidence distributions under defective and correct programs. We turn this distinction into an experimental control: for each underspecified task, we construct two execution-checked programs and evaluate them under alternative contracts. With the contract hidden, the same audit responses are scored under both contracts, making recall equal to the false-flag rate by construction. The empirical questions are which convention auditors favour and how revealing the requirement changes diagnosis. Execution checks behaviour; two models that also implement the rules judge admissibility under the task wording.

**Space:** replaces approximately 258 source words with 110. This makes the classical foundation, experimental contribution and semantic-validation limitation immediately distinguishable.

**④ Replace the introduction’s final two paragraphs**, from “Among natural hidden-test failures…” through “Code, records and preregistrations are released”:

> **Contributions and scope.** We contribute an execution-checked randomised-contract evaluation instrument and preregistered evidence of convention preference and improved diagnosis when requirements are revealed. We also describe 150 natural hidden-test failures: both model classifiers judge 34 to have expected values determined by the task wording. This agreement count does not estimate the prevalence of information-limited failures. Earlier studies of scientific code, results and data provide supporting context. Code, records and preregistrations are released.

**Space:** replaces approximately 151 source words with 77. It prevents the supporting studies from appearing to be three additional central contributions.

**⑤ Make Figure 1 explain the experiment and its payoff.**

The actual Figure 1 is [fig_design.tex](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/tex/fig_design.tex:2>), visually inspected on page 3 of [the compiled paper](</Users/ericdong/Library/Application Support/Claude/scratch-workspaces/74ef214a-bb0b-45f3-a0dd-dab068ffcbe9/c2cff56f-cccf-49f5-bf0f-c2a959dccdde/scratch-2026-11-02-a4ee54/audit/audit-ceiling-paper/tex/paper_v3.pdf>); `fig_e6.pdf` supplies Figure 2.

Move the existing schematic into the introduction. Replace its top box with:

> **Task (illustrative):** convert snake case to camel case; leading underscores unspecified. **Auditor input in every arm:** task + one program.

Replace the left brace annotation with:

> H hidden: equality by design  
> recall = false-flag rate

Replace the caption with:

> Randomised-contract evaluation. Either program can be correct, depending on the assigned contract. Hidden-contract equality is guaranteed by design; convention preference and the 76.8-percentage-point diagnosis gain from stating the requirement are empirical findings (41 held-out units). Verified diagnosis requires an executed witness of a contract violation under the benchmark comparator.

**Space:** retain the diagram’s footprint; the small label/caption increase is more than offset by the abstract cut. Exact pagination would still need checking after implementation.

**4. Sentences most vulnerable to misreading**

| Existing wording | Likely misreading |
|---|---|
| Title: “What Moves the Ceiling…” | A new, broadly applicable theoretical ceiling, rather than an evaluation design using classical theory. |
| Abstract: “Audit evaluations cannot observe this classical testing bound because a benchmark fixes a single contract.” | An unsupported universal claim that existing evaluations cannot assess information limits. |
| Introduction: “no auditor, whatever its capacity, can tell them apart” | Auditors cannot distinguish the programs’ behaviours. They can; the hidden intended contract is what they cannot identify under this construction. |
| Abstract: “The benchmark thus rewards agreement with a convention the models share.” | A conclusion about benchmarks generally, rather than these selected cases. |
| Introduction: “No correct program is flagged in that arm (2.1% when …)” | Either a contradiction or a zero-error guarantee. These are different conditions, and zero is an observed sample count. |
| Introduction: “fewer than a quarter are ones that both classifiers agree…” | More than three quarters are proven underspecified or impossible to audit. Lack of joint classifier agreement establishes neither. |

No files were modified.