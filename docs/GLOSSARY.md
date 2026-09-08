# GLOSSARY — append-only

Every term, **defined once**, with the part that introduced it.

This ledger is what makes "define jargon on first use, including jargon from earlier days, with a
link back" mechanical rather than heroic. Before defining a term in a new part, check here: if it
has a row, **link to the part that owns it** rather than redefining it.

| Term | Definition (one sentence) | Introduced in | Day |
| --- | --- | --- | --- |
| interpreter | The `python` program that reads and executes your file; a machine usually has several | day 0 part 1.1 | — |
| package | Code someone else wrote, installed into one specific interpreter rather than into the machine | day 0 part 1.1 | — |
| virtual environment | A directory holding one interpreter and its own packages, isolated from every other | day 0 part 1.1 | — |
| lockfile | The record of exactly which package versions were installed, down to the hash | day 0 part 1.1 | — |
| repository | A directory git is tracking, whose history is append-only | day 0 part 2.1 | — |
| tracked | A file git has been told to record every version of, forever | day 0 part 2.1 | — |
| check | A command that passes or fails with an exit code a script can read | day 0 part 3.1 | — |
| — | — | — | *no terms yet* |
| demo | A system shown on inputs chosen by the person showing it | day 1 part 1.1 | 1 |
| production | A system running on inputs nobody chose, at a volume nobody supervises | day 1 part 1.1 | 1 |
| adoption | Production, plus the intended people using it instead of what they used before | day 1 part 2.1 | 1 |
| baseline | What a number was before the work started, measured rather than recalled | day 1 part 2.2 | 1 |
| exit condition | How long a target must hold, and what must be true of your involvement when it does | day 1 part 2.2 | 1 |
