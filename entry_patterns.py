import re


def OR(*lst):
    return "(" + "|".join(lst) + ")"


ETC = r"&c\."

CAP_WORD = r"[A-ZÞȜ\-][a-zéþȝ()<>\- ]*-?"

HEADWORD = fr"#{CAP_WORD}#(, #{CAP_WORD}#)*"
HEADWORD_REF = fr"({CAP_WORD}(, {CAP_WORD})*)"

pos = [
    r"2 sg\. pres",
    r"3 pl\. pres",
    r"3 sg\. pres",
    r"acc",
    r"adj",
    r"adj\. superl",
    r"adv",
    r"conj",
    r"def\. art",
    r"fem",
    r"gen\. sg",
    r"interj",
    r"masc",
    r"n",
    r"n\. pl",
    r"n\. sg",
    r"pa\. t",
    r"pa\. t\. sg",
    r"pl",
    r"pp",
    r"prep",
    r"pres\. p",
    r"pres\. pl",
    r"pron. fem",
    r"pron",
    r"pron\. pl",
    r"prons",
    r"v. auxil",
    r"v",
]
POS = fr"_({'|'.join(pos)})\._(\^\d)?"

# playing it safe by whitelisting proper names rather than risk matching a non-gloss
PROPER_NAMES = OR(
    "a Roman",
    "April",
    "Christmas",
    "God",
    "Justice",
    "March",
    "Miller",
    "Monday",
    "Moors",
    "North",
    "Phœnix",
)
# playing it safe by whitelisting glosses involving non-alpha characters rather
# than risk matching a non-gloss
OTHER_GLOSSES = OR(
    "alas!",
    "ho!",
    r"\(a\) single",
    r"\(aroused\)",
    r"\(as name\)",
    r"\(jackdaw\)",
    r"\(level\) place",
    r"\(liability\)",
    r"\(small\) shield",
    r"boast\(ing\)",
    r"coming \(to\)",
    r"Greek \(language\)",
    r"helm\(et\)",
    r"turn\(ing\)",
    r"will \(_fut\._\)",
)
GLOSS = fr"([a-z\- ]+|{PROPER_NAMES}|{OTHER_GLOSSES})( \([a-z\- ]+\))?"
GLOSSES = fr"(\? )?{GLOSS}([,;] {GLOSS})*"

TEXT_REF_EXTRA = fr"( \(note\)| \(_see_ note\)| \(MS\.\)| \(footnote\))"
TEXT_REF = fr"[IVX]+( _[a-z]_)? \d+(, \d+)*{TEXT_REF_EXTRA}?"
TEXT_REF_DOT = r"[IVX]+ _introd\._"
TEXT_REFS_DOT = fr"({TEXT_REF_DOT}|{TEXT_REF}(, {TEXT_REF})*(\.|, {ETC}))"

ETYM = r"\[[^\]]+\]"

REF_PART = OR(
    fr"{HEADWORD_REF}, {ETC}",
    fr"{HEADWORD_REF},? {POS}",  # inconsistency
    fr"{HEADWORD_REF}",
)

REF_PART_DOT = OR(
    fr"(next|prec)\.",
    fr"{HEADWORD_REF}, {ETC}",
    fr"{HEADWORD_REF}, {POS}",
    fr"{HEADWORD_REF}, {POS}(,| and|, and) {POS}",  # inconsistency
    fr"{HEADWORD_REF}, and (next|prec)\.",
    fr"{HEADWORD_REF}\.",
)

BIG_SEE = OR(
    fr"_See_ {REF_PART_DOT}",
    fr"_See_ {REF_PART}; {REF_PART_DOT}",
    fr"_See_ {REF_PART}; {REF_PART}; {REF_PART_DOT}",
    fr"_See_ {REF_PART}; and {REF_PART_DOT}",
)

LITTLE_SEE = fr"_see_ {REF_PART}"
LITTLE_SEE_DOT = OR(
    fr"_see_ {REF_PART_DOT}", fr"_see_ note\.", fr"_see_ {REF_PART}, and note\."
)

BIG_CF = fr"_Cf\._ {REF_PART_DOT}"

BIG_SEE_ALSO = fr"(_See also_|_See_ also) {REF_PART_DOT}"

HEADWORD_POS = fr"{HEADWORD}(,|, {POS})"
HEADWORD_POS_DOT = fr"{HEADWORD}(\.|, {POS})"

HEADWORD_DOT = OR(
    fr"{HEADWORD_POS_DOT}",
    fr"{HEADWORD} \({HEADWORD}\); {HEADWORD}\.",
    fr"{HEADWORD} \(=  ï̄e\)\.",
    fr"{HEADWORD}, {ETC}; {HEADWORD}\.",
    fr"{HEADWORD}, {ETC}",
    fr"{HEADWORD}, {HEADWORD}, {ETC}",
    fr"{HEADWORD}, {HEADWORD}\.",
    fr"{HEADWORD}; {HEADWORD_POS_DOT}",
    fr"{HEADWORD}; {HEADWORD}, {ETC}",
    fr"{HEADWORD}; {HEADWORD}; {HEADWORD_POS_DOT}",
)

regexes = [
    re.compile(r)
    for r in [
        fr"{HEADWORD_DOT} {BIG_SEE_ALSO}$",
        fr"{HEADWORD_DOT} {BIG_SEE}$",
        fr"{HEADWORD_POS} {GLOSSES} {TEXT_REFS_DOT} {ETYM}$",  # missing comma?
        fr"{HEADWORD_POS} {GLOSSES} \({LITTLE_SEE}\), {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF} \({LITTLE_SEE}\)\. {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; {GLOSSES}, {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {BIG_CF}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {BIG_SEE}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {ETYM} {BIG_SEE}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT}$",
        fr"{HEADWORD_POS} {GLOSSES}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_POS} {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD} \(_intill_\), {POS} {GLOSSES}, {TEXT_REFS_DOT}$",
        fr"{HEADWORD} = {CAP_WORD} {GLOSS} \({POS}\), {TEXT_REFS_DOT}$",
        fr"{HEADWORD} = {CAP_WORD} \+ {CAP_WORD}\.$",
        fr"{HEADWORD}, {HEADWORD}, _pp\._ of {REF_PART_DOT}$",
        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE_DOT}$",
        fr"{HEADWORD}, {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD}, {TEXT_REF}: \? read _[^_]+_, {GLOSSES}; {LITTLE_SEE_DOT}$",
        fr"#U-#, #V-#; for init\. _u_, _v_ \(in III\) see also F\.$",
    ]
]


def check_entry(entry):
    for regex in regexes:
        if regex.match(entry):
            return True
    return False
