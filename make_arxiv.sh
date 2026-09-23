#!/bin/sh
# Build the arXiv source package from exactly what tex/paper.tex compiles, then prove it builds
# alone: copy to an empty directory and run pdflatex twice with the shipped .bbl (arXiv's order),
# with no bibtex, no network and no file from this checkout. Output: arxiv/audit-ceiling-arxiv.tar.gz
set -eu
cd "$(dirname "$0")/tex"
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex >/dev/null
OUT=../arxiv; STAGE=$OUT/src
rm -rf "$OUT"; mkdir -p "$STAGE/sections" "$STAGE/appendix"
cp paper.tex paper.bbl table1.tex icml2026.sty icml2026.bst algorithm.sty algorithmic.sty fancyhdr.sty \
   fig1_saturation.pdf fig2_sweep.pdf fig3_residual.pdf fig4_ai4s.pdf "$STAGE/"
cp sections/*.tex "$STAGE/sections/"; cp appendix/*.tex "$STAGE/appendix/"
( cd "$STAGE" && tar czf ../audit-ceiling-arxiv.tar.gz . )
T=$(mktemp -d); tar xzf "$OUT/audit-ceiling-arxiv.tar.gz" -C "$T"
( cd "$T" && pdflatex -interaction=nonstopmode -halt-on-error paper.tex >/dev/null && \
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex >/dev/null )
if grep -qi "undefined\|Citation .* undefined" "$T/paper.log"; then echo "clean build has undefined references"; exit 1; fi
cp "$T/paper.pdf" "$OUT/paper-from-package.pdf"
echo "package: $(du -h "$OUT/audit-ceiling-arxiv.tar.gz" | cut -f1); clean build: $(pdfinfo "$T/paper.pdf" | awk '/Pages/{print $2}') pages, no undefined references"
rm -rf "$T"
