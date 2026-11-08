At HEAD **`633f31a`**:

**(a) Remaining blockers: none.**

- **E6:** Both contracts now follow **10 s → 10 s → 60 s**. The first two timeouts remain retriable infrastructure failures; a final timeout receives terminal no-credit. Successful execution at 60 s continues scoring. The rewritten freeze **verifies**.
- **Cached E6 records:** Checked **21,582 records across eight witness files**, including archived versions. None contains an `outside_domain` result caused by a reference timeout. **No cached-score invalidation is required for this defect.**
- **E8:** Empty complete-case populations no longer crash: primary estimates are `null`, `estimable=False`, and bounds remain available. The P9 selectivity fixture now gives **S endpoints of 0 and 100 points**. Pairing, directional reporting, validation, retry and missing-reading fixtures also pass.

**(c) Verdicts**

- **E6 release: yes.**
- **E8 release: yes — cleared to freeze and run.** `FREEZE8_test.json` remains absent and must be generated before held-out execution; its enforcement checks pass.

All replays were read-only, with mocked calls and in-memory outputs. No model calls or file changes were made.