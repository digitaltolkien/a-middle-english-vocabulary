import re


def OR(*lst):
    return "(" + "|".join(lst) + ")"


ETC = r"&c\."

CAP_WORD = r"[A-ZÞȜ\-][a-zéþȝ()<>\- ]*-?"

HEADWORD = fr"#{CAP_WORD}#(, #{CAP_WORD}#)*"
HEADWORD_REF = fr"({CAP_WORD}(, {CAP_WORD})*|next)"

pos = [
    r"v",
    r"adv",
    r"n",
    r"conj",
    r"pron",
    r"prons",
    r"prep",
    r"adj",
    r"masc",
    r"fem",
    r"pl",
    r"acc",
    r"gen\. sg",
    r"pp",
    r"pron\. pl",
    r"pron. fem",
    r"def\. art",
    r"n\. pl",
    r"pa\. t",
    r"interj",
    r"pa\. t\. sg",
    r"pres\. pl",
    r"adj\. superl",
]
POS = fr"_({'|'.join(pos)})\._(\^\d)?"

PROPER_NAMES = r"(God|April|a Roman)"
OTHER_GLOSSES = r"(boast\(ing\)|alas!|coming \(to\)|\(a\) single)"
GLOSS = fr"([a-z\- ]+|{PROPER_NAMES}|{OTHER_GLOSSES})( \([a-z\- ]+\))?"
GLOSSES = fr"(\? )?{GLOSS}([,;] {GLOSS})*"

TEXT_REF = fr"[IVX]+( _[a-z]_)? \d+(, \d+)*( \(note\)| \(_see_ note\)| \(MS\.\))?"
TEXT_REF_DOT = r"X _introd\._"
TEXT_REFS_DOT = fr"({TEXT_REF_DOT}|{TEXT_REF}(, {TEXT_REF})*(\.|, {ETC}))"

ETYM = r"\[[^\]]+\]"

BIG_SEE = OR(
    fr"_See_ {HEADWORD_REF} {POS}; {HEADWORD_REF}\.",  # missing comma?
    fr"_See_ {HEADWORD_REF}, {ETC}",
    fr"_See_ {HEADWORD_REF}, {POS} and {POS}",  # missing comma?
    fr"_See_ {HEADWORD_REF}, {POS}, and {POS}",
    fr"_See_ {HEADWORD_REF}, {POS}, {POS}",
    fr"_See_ {HEADWORD_REF}, {POS}; {HEADWORD_REF}, {POS}",
    fr"_See_ {HEADWORD_REF}, {POS}; {HEADWORD_REF}; {HEADWORD_REF}\.",
    fr"_See_ {HEADWORD_REF}, {POS}; {HEADWORD_REF}\.",
    fr"_See_ {HEADWORD_REF}, {POS}",
    fr"_See_ {HEADWORD_REF}, and next\.",
    fr"_See_ {HEADWORD_REF}, and prec\.",
    fr"_See_ {HEADWORD_REF}; {HEADWORD_REF}, {ETC}",
    fr"_See_ {HEADWORD_REF}; {HEADWORD_REF}, {POS}",
    fr"_See_ {HEADWORD_REF}; {HEADWORD_REF}; {HEADWORD_REF}, {POS}",
    fr"_See_ {HEADWORD_REF}; {HEADWORD_REF}; {HEADWORD_REF}\.",
    fr"_See_ {HEADWORD_REF}; {HEADWORD_REF}\.",
    fr"_See_ {HEADWORD_REF}; and {HEADWORD_REF}, {POS}",
    fr"_See_ {HEADWORD_REF}\.",
)

HEADWORD_POS = fr"{HEADWORD}(, {POS})?"
HEADWORD_POS_DOT = fr"{HEADWORD}(\.|, {POS})"

HEADWORD_DOT = OR(
    fr"{HEADWORD_POS_DOT}",
    fr"{HEADWORD_POS} {GLOSS}, {TEXT_REF}\.",
    fr"{HEADWORD} \({HEADWORD}\); {HEADWORD}\.",
    fr"{HEADWORD} \(=  ï̄e\)\.",
    fr"{HEADWORD}, {ETC}; {HEADWORD}\.",
    fr"{HEADWORD}, {ETC}",
    fr"{HEADWORD}, {GLOSS}, {TEXT_REF}\.",
    fr"{HEADWORD}, {HEADWORD}, {ETC}",
    fr"{HEADWORD}, {HEADWORD}\.",
    fr"{HEADWORD}; {HEADWORD_POS_DOT}",
    fr"{HEADWORD}; {HEADWORD}, {ETC}",
    fr"{HEADWORD}; {HEADWORD}; {HEADWORD_POS_DOT}",
)

HEADWORD_REF_POS = fr"{HEADWORD_REF}(, {POS})?"
HEADWORD_REF_POS_DOT = fr"{HEADWORD_REF}(\.|, {POS})"

LITTLE_SEE = fr"_see_ {HEADWORD_REF_POS}"
LITTLE_SEE_DOT = (
    fr"_see_ ({HEADWORD_REF_POS_DOT}|{HEADWORD_REF_POS}, and note\.|note\.)"
)

regexes = [
    re.compile(r)
    for r in [
        fr"{HEADWORD_DOT} {BIG_SEE}$",
        fr"{HEADWORD_POS} {GLOSSES} {TEXT_REFS_DOT} {ETYM}$",  # missing comma?
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF} \({LITTLE_SEE}\)\. {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}, {ETYM}$",  # comma instad of perid
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {ETYM} {BIG_SEE}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REFS_DOT}$",
        fr"{HEADWORD_POS} {GLOSSES}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_POS} {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_POS}, {GLOSSES}, {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD} = {CAP_WORD} {GLOSS} \({POS}\), {TEXT_REFS_DOT}$",
        fr"{HEADWORD} = {CAP_WORD} \+ {CAP_WORD}\.$",
        fr"{HEADWORD}, {HEADWORD}, _pp._ of {HEADWORD_REF_POS_DOT}$",
        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE_DOT}$",
        fr"{HEADWORD}, {TEXT_REF}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD}\. _See also_ {HEADWORD_REF_POS_DOT}$",
        fr"{HEADWORD}\. _See_ also {HEADWORD_REF_POS_DOT}$",
        fr"{HEADWORD}, {TEXT_REF}: \? read _[^_]+_, {GLOSSES}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD} \(_intill_\), {POS} {GLOSSES}, {TEXT_REFS_DOT}$",
        fr"#U-#, #V-#; for init\. _u_, _v_ \(in III\) see also F\.$",
    ]
]


def check_entry(entry):
    for regex in regexes:
        if regex.match(entry):
            return True
    return False
