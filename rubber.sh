# Get the first tag found in the history from the current HEAD
git describe --tags --always --dirty='-*' > .release.txt
rubber --pdf notes.tex
