## Findings

**The measurements reproduce. The replacement policy is sensible, but its description still overstates the tests.**

1. **§5 attributes archive reconstruction to tests that never perform it.** [RESULTS-TESTGEN-VAL.md:264](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/RESULTS-TESTGEN-VAL.md:264) says `test_testgen_val.py` proves the chain starting with reconstruction of `numbers.json` and `exploratory.json` from archived outcomes. It does not invoke either report generator or compare reconstructed records.

   I intercepted file reads in memory and separately:
   - Replaced study 17’s entire `rows.jsonl` with an empty string.
   - Changed A’s recorded right-retained numerator to `999`.

   **All 43 runnable tests passed under each mutation.** These tests establish downstream table equality and selected string checks. My independent replay establishes reconstruction for this checkout; that is different evidence.

   The sufficient correction is wording: “Independent replay reproduced the records byte for byte; automated tests compare the generated tables and selected prose strings.”

2. **Rendering guarantees remain in supporting code.** [splice_tables.py:25](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/testgen/splice_tables.py:25) still says “what renders is a function of the records plus this fixed placement.” Its heading commentary also promises that an unregistered subheading cannot be inserted. [_scan’s docstring:205](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-testval/benchmarks/code/tests/test_testgen_val.py:205) claims renderer-equivalent state and that no marker renders as code.

   These remain false. §5 withdraws the broad guarantee, but the withdrawal has not reached these comments.

## Mutations: the class remains open

I ran **19 document mutations** against all 43 runnable tests, preserving files on disk. Ten controls were rejected, including corrupted cells, swapped interval headings, duplicate rows, malformed delimiters, comments, raw `<pre>` wrappers and oversized fences.

**Nine mutations survived**, all leaving the five generated blocks byte-identical. I rendered the variants through Pandoc’s GFM reader:

- Fencing the registered exploratory heading removes that rendered heading.
- An indented or setext heading introduces “As preregistered” above exploratory material.
- A three-backtick “closer” carrying trailing text passes the scanner but leaves the document inside code: **zero rendered tables instead of five**.
- New processing-instruction and CDATA wrappers pass the checks and reduce rendered table elements from five to two.
- Contradictory verdict prose and an altered, unchecked numerical sentence also pass.

These are counterexamples to rendering guarantees, **not reasons to continue expanding the Markdown blacklist**.

## Measurement verification

I reproduced **`numbers.json`, `exploratory.json` and `tables.md` byte for byte**, using archived records and intercepting output writes in memory. Independently implemented Wilson and problem-cluster bootstrap calculations agreed across **all 66 rate blocks**, using seed 20260915 and 10,000 resamples.

| Rule | Wrong / kept | Wilson 95% | Problem-cluster interval | Retention |
|---|---:|---:|---:|---:|
| A | 11/90 = 12.2% | 7.0–20.6% | 3.6–22.6% | 5/7 |
| B | 15/101 = 14.9% | 9.2–23.1% | 6.5–25.5% | 6/7 |
| C′ | 11/86 = 12.8% | 7.3–21.5% | 3.9–23.9% | 5/7 |

**All three rules and H17 remain killed.** No existing numerical record value changed from the initial results commit. Table rows match round 4 after normalising the disclosed indentation change; round 9 changes no table lines.

Additional checks:

- Both archive manifests verified: **20 study-17 entries and 11 study-16 entries**. All three copied inputs match study 16 byte for byte.
- Suite shapes, response identities and AST identities reconstructed. All **444 prompt hashes** match draw 1.
- All **870 stored rule decisions and flags** independently reconstructed. The rules consume candidate failure sets; canonical outcomes supply scoring labels. The execution path imports study 16’s unchanged `run_generated`.
- The primary redefinition, comparator baseline, selection order and kill precede calls. Earliest inferred request: **22:46:34.725**, after code commit **22:46:23**.
- The floor is correct: **29/1,188 = 2.441%**. It applies to these candidate-outcome rules and this unique-test retention convention.
- Correlation reproduces: **23/32 versus 13/189** is the matched draw-2 comparison. **37/222** is marginal prevalence, not the matched control. The results correctly distinguish them and qualify the mechanism.
- Identity counts reproduce: **13/222 and 8/222**. Ledger totals, token counts, the single malformed-response retry, 75-second wait and 31.764-second successful call agree.
- Amendment 2’s **73 calls/$0.577** matches a snapshot within 22:51; **77 calls** had completed by its 22:51:45 commit. It still preceded draw 3.
- Sections 1–2’s quantitative claims agree with the records. A retains C′’s applications plus four correct F-stratum applications; the stronger assertion that paid rules “do not beat” C′ is appropriately withdrawn.
- No generated source strings appeared in committed study-17 JSON records. `execute.py`, `architectures.py`, `src/` and kernel paths are unchanged.

**Execution limits:** 43 tests passed; three executor tests failed because this environment cannot create temporary directories. I did not re-execute archived generated tests. Local corpus files were also absent, preventing reconstruction of prompt text from the corpus; archived prompt-hash equality was verified.

## What I would do

**Declare the records authoritative and Markdown a convenience. Stop rendering hardening.** Correct the two remaining descriptions above. If further engineering effort is available, automate the archive-to-record reconstruction check rather than add another Markdown restriction.

**not quotable — the revised §5 still claims the tests establish archive-to-record reconstruction that they do not test.**
