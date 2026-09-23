#!/bin/sh
# Regenerate every figure and Table 1 from the records committed in this repository, then check
# that the regenerated table is byte-identical to the one the paper compiles. No model calls,
# no network, no paths outside this checkout. Needs python3 with matplotlib and scienceplots.
set -eu
cd "$(dirname "$0")"
python3 figures/src/make_figures.py
python3 figures/make_fig2_sweep.py
python3 figures/make_fig3_residual.py
python3 figures/make_table1.py > /tmp/table1.$$ 2>/dev/null
if cmp -s /tmp/table1.$$ tex/table1.tex; then echo "table 1: identical to tex/table1.tex"
else echo "table 1: DIFFERS from tex/table1.tex"; diff /tmp/table1.$$ tex/table1.tex; rm -f /tmp/table1.$$; exit 1; fi
rm -f /tmp/table1.$$
# The coverage table (records/coverage_simulation.json) is not rerun here because it takes
# minutes. Its record was produced with, and regenerates exactly under:
#   python3 analysis/coverage_simulation.py --reps 400 --boots 600 --seed 20260923
python3 analysis/check_manuscript.py
