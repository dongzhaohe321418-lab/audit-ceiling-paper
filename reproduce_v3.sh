#!/bin/sh
# Reproduce the ICML 2027 manuscript (tex/paper_v3.tex) from the released experiment records. No model calls, no
# network. Usage:
#
#     ./reproduce_v3.sh [path to crossaudit-harness checkout]      (default: ../crossaudit-harness)
#
# 1. With REANALYSE=1 and the harness's Python environment (ANALYSIS_PYTHON=...), first reruns the registered analyses
#    (E6 open units, E6 positive controls, E1, E8, E9, E10, E11) and the exploratory exception-scoring sensitivity from the raw
#    audit and witness records (set CROSSAUDIT_BENCH_EXECUTOR to the E1/E6 executor; E11 uses E7's own), overwriting the results files under benchmarks/code/records/icml/.
# 2. Regenerates tex/numbers.tex (every E6/E1 number the main text quotes) and checks it is identical to the copy the
#    paper compiles.
# 3. Regenerates the E6 and natural-failure figures into figures/ and copies them to tex/.
# Then build with:  cd tex && tectonic paper_v3_submission.tex   (anonymous)  or  tectonic paper_v3.tex
set -eu
cd "$(dirname "$0")"
H="${1:-../crossaudit-harness}"
R="$H/benchmarks/code/records/icml"
PY="${PYTHON:-python3}"            # needs matplotlib and numpy for the figures
APY="${ANALYSIS_PYTHON:-$PY}"      # the harness environment (see its README) for REANALYSE=1
EPY="${E11_PYTHON:-$APY}"          # E7/E11 environment (E11's freeze binds its package list)
[ -d "$R" ] || { echo "no records at $R"; exit 1; }

if [ "${REANALYSE:-0}" = 1 ]; then
  : "${CROSSAUDIT_BENCH_EXECUTOR:?REANALYSE=1 needs CROSSAUDIT_BENCH_EXECUTOR, the E1/E6 executor Python (harness README)}"
  SRC="$(cd "$H/src" && pwd)"
  ( cd "$H/benchmarks/code/icml" && export PYTHONPATH="$SRC"
    "$APY" analyse_e6.py --split test --kind open
    "$APY" analyse_e6.py --split test --kind det
    "$APY" analyse_e1.py --split test
    "$APY" analyse_e1.py --split test --taxonomy
    "$APY" e6_exception_sensitivity.py
    cd ../../e8 && "$APY" e8.py analyse test
    cd ../e9 && "$APY" e9.py analyse test
    cd ../e10 && "$APY" e10.py analyse test
    cd ../e11 && env -u CROSSAUDIT_BENCH_EXECUTOR "$EPY" -W ignore e11.py analyse --split test
    env -u CROSSAUDIT_BENCH_EXECUTOR "$EPY" -W ignore e11_report.py test
    env -u CROSSAUDIT_BENCH_EXECUTOR "$EPY" -W ignore e11_admissibility.py test ) > /dev/null
  echo "registered analyses rerun"
fi

T=figures/.numbers.regenerated
"$PY" figures/make_numbers.py "$R" test test > "$T"
if cmp -s "$T" tex/numbers.tex; then echo "numbers: identical to tex/numbers.tex"
else echo "numbers: DIFFER from tex/numbers.tex"; diff "$T" tex/numbers.tex || true; rm -f "$T"; exit 1; fi
rm -f "$T"

"$PY" figures/make_fig_e6.py "$R/e6_results_v4_test.json" figures/fig_e6_test
"$PY" figures/make_fig_natural.py figures/data/natural_v4.json figures/fig_natural
cp figures/fig_e6_test.pdf tex/fig_e6.pdf
cp figures/fig_natural.pdf tex/fig_natural.pdf
echo "figures: fig_e6.pdf and fig_natural.pdf regenerated into tex/"
