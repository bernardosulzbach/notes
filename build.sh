#!/usr/bin/env bash
# Get the first tag found in the history from the current HEAD
git describe --tags --always --dirty='-*' > release.txt
# Use arara to make a PDF
arara notes.tex
# Also make a compressed PDF
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=notes-compressed.pdf notes.pdf
