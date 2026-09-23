**I would block quotation of 338b62b.** The numerical results reproduce, but the corrected extraction still changes the tests shown to the models, and the report retains conclusions that its own re-run contradicts. No files were modified.

1. **Blocking: the correction introduces a second test-extraction defect.**  
   [corpus2.py:138](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-sub2/benchmarks/code/substrate2/corpus2.py:138) slices the “class header” through the first member’s `def` line, thereby retaining that member’s decorators. It then emits the retained members with their decorators again.

   Across the frozen frame, **26 tasks have altered method ASTs**. On **17**, decorators from an excluded hidden method are attached to a visible method. This affects **24 audited instances: 12 P and 12 C**.

   I executed an in-memory reproduction using BigCodeBench/12 and a stub raising the expected `FileNotFoundError`. The intact selected test passes; the displayed version fails:

   ```text
   TypeError: TestCases.test_script_does_not_exist() takes 2 positional arguments but 5 were given
   ```

   All 300 displayed modules parse, and no excluded test-method definitions appear. Those checks are insufficient: hidden decorators leak, and the displayed suite differs semantically from the scored suite. The registered digest faithfully freezes this defect.

2. **Blocking: the report simultaneously withdraws and reasserts the old conclusions.**  
   [RESULTS-SUBSTRATE2.md:270](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-sub2/benchmarks/code/RESULTS-SUBSTRATE2.md:270) still says both H23d intervals exclude zero. [Section 7](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-sub2/benchmarks/code/RESULTS-SUBSTRATE2.md:362) still says the self gain ratio is undefined, the cross curve saturates, and the FP intervals do not meet. It also retains **41.0/39.3-point** differences beside the new intervals; the current differences are **46.8/29.3**.

   The opening banner claims the old numbers remain unedited and the re-run is incomplete, while the body contains the completed re-run. Amendment 2’s promised preservation and side-by-side reporting of old/new H23a and H23c is therefore not fulfilled.

3. **The generation guard is only partly effective; another stale artifact is already contaminating the report.**  
   Wrong or missing `audit_set.json` generation digests were correctly refused. However, [the cache guard](/Users/ericdong/Documents/Crossaudit/review-worktrees/wt-sub2/benchmarks/code/substrate2/audit2_sub.py:139) receives rows from `explore.load_detector()`, which **discards `solution_sha256`**. I planted a wrong digest in memory: `--plan` still exited successfully and reported every arm complete.

   Additional gaps:

   - `self_coverage.json` is still the **September 11 void-run snapshot**. Its reuse produces **250 / 249** coverage and old denial counts.
   - `self_coverage_first_read.json` is likewise presented without adequately separating its generation.
   - `cost.json` remains reused by existence alone; passing another archive does not invalidate it.
   - The report builder bypasses the generation/cache guards.
   - Neither generation nor audit entry point calls `verify_frame.py`, contrary to its documentation. The archived supervisor does call it.
   - The audit driver does not hash the actual loaded solution bytes against the committed instance digest.

   For the present archive, I nevertheless verified **all 600 generator prompt hashes**, actual solution hashes, and cached candidate hashes against the corrected inputs. These checks passed; they do not repair the extraction defect.

4. **The arithmetic reproduces.**  
   I ran the report entry point with `--run <archive>` and the splice entry point, intercepting writes in memory. `numbers.json` matched after excluding `written_utc`; `tables.md` and the resulting results document matched byte-for-byte.

   Independent cache calculations gave:

   | Quantity | Recomputed result |
   |---|---:|
   | Cross recall, K=8 | 76/99 = 76.8% [65.7, 87.0] |
   | Cross false positives, K=8 | 68/150 = 45.3% [36.4, 54.4] |
   | H23a versus substrate 1 | +46.8 points [31.6, 61.3] |
   | H23c versus substrate 1 | +29.3 points [18.3, 40.2] |
   | H23d, P | +4.04 points [−10.10, 18.18] |
   | H23d discordance / McNemar | 16 versus 12 / p=0.57159 |
   | Cross/self split instances | 96/249 and 12/249 |

   I independently enumerated draw subsets for both families’ P and C curves; all points matched the stored precision. Cross last-step gains are **1.5152 points P** and **1.4167 C**. Self gains are **0 P** and **0.1667 C**. Notably, the self P last-step gain remains zero despite prose saying that artifact was removed.

5. **The six reversals are coherent observations, not six independent demonstrations of an input effect.**  
   Several share the same underlying flag counts and curves. Candidate regeneration, scope replacement, sampling variability, and time separation can all contribute. Only **147 IDs** are common to both audited scopes; only **48 of those** retain identical candidate hashes. On that common set I reproduced **0→8 self splits** and **40 changed union verdicts**.

   I found no interval or p value attached directly to a void-versus-re-run difference, and the explicit nonvalidation disclaimer is appropriate. But phrases such as “itself a consequence of the correction” overattribute causation. The remaining extraction defect further prevents interpreting this as a clean corrected-input replication.

   The archive also contradicts Amendment 3’s claim of 4,000 complete initial readings: the first stale-scope invocation had **3,557 readings**, with cross d7 at 57 and d8 empty. Self proceeded before cross completed. That chronology needs explicit reporting.

6. **Spend reconciles; the denial wording overclaims.**  
   Archive ledgers total **$37.156596**, including **$22.253239** for the initial stale-scope invocation, portions of which were reused. The current cost snapshot agrees.

   The **73,285** cross failure rows comprise **72,594 circuit-breaker refusals and 691 HTTP-429 rows**—not 73,285 provider denials. The code records usage after a completion, and these failures are excluded from reading caches. That supports “no reading and no recorded completion cost”; the archive alone is not an independent billing statement. Nor does it establish that the long time separation had no statistical consequences.

7. **The green tests do not establish the claimed correction.**  
   All **31 study tests pass**, including with the defects above present. The new parsing and method-membership tests are meaningful but miss decorator preservation. Several report rewrites merely require the corrected sentence somewhere, allowing the contradictory old sentence elsewhere.

   Remaining result-encoding assertions include `sign_matches_substrate1 is False`, `sp_cross > sp_self`, gain ratios being lower at every K, and the primary interval excluding zero. The superseded extraction test is also still collected as an empty passing test. These are not adequate substitutes for independent calculations and contradiction checks.

   The full application suite could not collect in this read-only environment because it requires temporary directories; this was unrelated to the three known Monte-Carlo timeouts. The branch diff leaves `src/` and kernel code untouched. Inspection of committed study records found no corpus, solution, or finding text; current execution-error fields contain unittest outcome summaries.

**not quotable — the re-run still shows models a different, sometimes runtime-broken visible suite from the one used for scoring.**
