# Get the first tag found in the history from the current HEAD
git describe --tags --always --dirty='-*' > .release.txt
# Use rubber to make a PDF
rubber --pdf notes.tex
