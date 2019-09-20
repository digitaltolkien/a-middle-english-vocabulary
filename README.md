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


## Code for Etymology Patterns

Currently running `./check_etymologies.py` and building regular expressions in `etym_patterns.py`.
