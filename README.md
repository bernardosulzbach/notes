# Notes
![Travis CI](https://travis-ci.org/mafagafogigante/notes.svg?branch=master)

This document is a collection of notes, formulas, and solved problems about
various subjects. It exists mainly for reference purposes.

## Obtaining a release
As modifications are made and reviewed, new releases are made. [Here you can get the
latest release](https://github.com/mafagafogigante/notes/releases/latest). There
are two files: `notes.pdf` and `notes-compressed.pdf`. Both have exactly the
same content, but the latter is a compressed version of the former.

## Building
Issuing the following command should build the PDF.
```bash
$ bash build.sh
```

See the `.travis.yml` file of a snapshot to understand how a given version is
built.

Since Release 16 there is a script called `install-required-packages.sh` that
should install all needed packages in a Debian-based distribution.

## License
![Commons Attribution-ShareAlike 4.0 International License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)

Therefore you're free to **share** (copy and redistribute the material in any
medium or format) and **adapt** (remix, transform, and build upon the material)
for any purpose, **even commercially**.
