You are a senior, adversarial reviewer and area chair for ICML 2027 (main track). The repository in
audit/audit-ceiling-paper is a paper, "What Moves the Ceiling on Automated Audit: from General Code to Scientific
Code, Results and Data" (tex/paper.tex with tex/sections/*.tex and tex/appendix/*.tex; compiled tex/paper.pdf;
claims ledger manuscript/CLAIMS.md; per-study reports in reports/; preregistrations in plan/; records in records/;
earlier cross-vendor reviews in reviews/). The code that produced the records is in audit/crossaudit-harness.
The author wants to turn this into a paper that is solid enough for a main-track venue (ICML 2027, deadline about
late January 2027; NeurIPS 2027 in May is the fallback). Work read-only. Do not trust earlier reviews; form your own
view from the paper and records.

Answer, concretely:
1. As an ICML reviewer today: summary, strengths, weaknesses, scores (soundness, presentation, significance,
   originality, overall 1-10) and the likely decision. Be specific about what a typical ICML reviewer would
   object to (scope, sample sizes, generality beyond one product, model/sampling confounds, post hoc analyses,
   writing, length, the number of separate studies).
2. What is the strongest single paper hidden in this material? Propose one central claim and title, and a
   section-level outline for an 8-page ICML paper (plus appendix), saying which of the existing studies carry
   the argument, which go to the appendix and which should be cut.
3. Which new experiments would most raise the acceptance probability, ranked, given these constraints: one
   researcher, about 10 weeks, an Apple laptop (no GPUs), model access through the OpenAI Codex CLI (GPT models)
   and the Claude Code CLI (Claude models), modest API budget (estimate calls and cost for each), no human
   annotators except the author. For each: the claim it would support, the design (substrates, models, N, ground
   truth, primary endpoint, preregistration), and what result would make the paper stronger or weaker. Consider
   in particular: more generators and auditors (matched sampling), larger and newer substrates (beyond
   HumanEval+/MBPP+; contamination), operating-characteristic curves rather than single operating points, a causal
   test of the specification-determination explanation, and the deterministic-versus-model complementarity in
   science at larger scale.
4. Related work the paper must engage with (LLM critics and code review, CriticGPT-style work, LLM-as-judge for
   code, test generation, verification of scientific results, data validation), naming papers you are confident
   exist; mark anything uncertain.
5. Presentation: what in the current prose would hurt it with reviewers, with examples.

Final message in Markdown, concise but complete.
