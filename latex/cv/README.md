# CV build instructions

This CV uses `biblatex` with the `biber` backend, so running `bibtex` will **not** work.

## Quick build (recommended)
```bash
./build_cv.sh
```

## Manual build
```bash
pdflatex cv.tex
biber cv
pdflatex cv.tex
pdflatex cv.tex
```

## Requirements
- TeX Live (or equivalent) with `latexmk`, `biblatex`, and `biber` installed.
