# A Middle English Vocabulary

A project to mark up _A Middle English Vocabulary_ by J. R. R. Tolkien and extract lexical information in a more machine-actionable form.


## Source Material

* `43737-0.txt` — text file from Project Gutenberg
* `43737-h.htm` — HTML file from Project Gutenberg
* `5KJeiE-middleenglishvoc00tolkuoft.pdf` — PDF scan from archive.org


## Corrections

* `corrected.txt` — corrected file (mostly transcription errors)

but also, the following errors in printed version:

* **Wlaffyng** is missing `[`
* **Ȝa, Ȝaa** has `OE` for `OE.` in etymology
* **Ver(r)ay** has `OF.` for `OFr.` in etymology
* **Noþeles** has `OE` for `OE.` in etymology
* **Werkman, Workeman** has `OE` for `OE.` in etymology
* **Goddesse** has `OE` for `OE.` in etymology
* **Dedir** has `MnE.` for `Mn.E.` in etymology
* **Breue** has `Med. L.` for `Med.L.` in etymology
* **Danes** has `Med. L.` for `Med.L.` in etymology


## Code for Patterns


Currently running `./check_etymologies.py` and building regular expressions in `etym_patterns.py` for etymological information; and running `./check_entries.py` and building regular expressions in `entry_patterns.py` for overall pattern structure.

There are currently no dependencies for running the script above.

Source code is run through `black`, `isort` and `flake8` which are all dev dependencies in `Pipfile`.


## Planning the TEI Markup

See [Notes on Structure](https://github.com/digitaltolkien/a-middle-english-vocabulary/wiki/Notes-on-Structure). If you have ideas about the TEI markup, create an issue for a particular entry, giving the markup in `corrected.txt`, the proposed TEI markup and we can discuss open questions there.


## License

The underlying dictionary was published prior to 1923 and is considered to be in the public domain. The source material from Project Gutenberg is subject to the Project Gutenberg License.

Code is made available under an MIT License (see `LICENSE`)

Data is made available under a Creative Commons Attribution-ShareAlike 4.0 International Public License.
