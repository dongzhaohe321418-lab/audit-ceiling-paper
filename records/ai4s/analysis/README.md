# Science-study analysis code

Each directory is `benchmarks/ai4s/*.py` copied from the harness at the commit that produced that
study's admitted records (harness branches in `records/PROVENANCE.md`):

| directory | study | harness commit |
|---|---|---|
| `data-6c4bdbb/` | scientific data (C17) | 6c4bdbb |
| `results-e3baa55/` | scientific results (C18) | e3baa55 |
| `code-cb3b8d9/` | scientific code (C19) | cb3b8d9 |

They import the harness package (`crossaudit`) and the ceiling-study statistics helpers, so they run
from a harness checkout, not from this repository. The scripts under `records/ai4s/runs/analysis/`
are earlier snapshots kept with the run archive; where they differ, these copies are the ones the
reports cite. Home-directory prefixes were replaced by `~`.
