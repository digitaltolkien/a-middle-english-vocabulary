import re


def OR(*lst):
    return "(" + "|".join(lst) + ")"


QV = r"_q\.v\._"
ETC = r"&c\."

CAP_WORD = r"\*?[A-ZÞȜ\-][a-zéþȝ()<>\- ]*-?"
MULTI_CAP_WORD = OR(
    "Aue Maria",
    "Mappa Mundi",
)
HEADWORD = fr"#({CAP_WORD}|{MULTI_CAP_WORD})#(, #{CAP_WORD}#)*"
HEADWORD_REF = fr"({CAP_WORD}(, {CAP_WORD})*)"

pos = [
    r"1 sg\. pres\. ind",
    r"2 sg\. pres",
    r"3 pl\. pres",
    r"3 sg\. pres",
    r"acc",
    r"adj",
    r"adj\. superl",
    r"adv",
    r"adv\. compar",
    r"conj",
    r"def\. art",
    r"fem",
    r"gen\. sg",
    r"imper. pl",
    r"interj",
    r"masc",
    r"neg\. adv",
    r"n",
    r"n\. dat\. sg",
    r"n\. gen\. sg",
    r"n\. pl",
    r"n\. sg",
    r"pa\. t",
    r"pa\. t\. intr",
    r"pa\. t\. pl",
    r"pa\. t\. sg",
    r"pa\. t\. subj",
    r"pl",
    r"pp",
    r"pp\._ as _prep",
    r"prep",
    r"pres\. p",
    r"pres\. pl",
    r"pron. fem",
    r"pron",
    r"pron\. pl",
    r"prons",
    r"v",
    r"v\. auxil",
    r"v\. imper",
    r"v\. impers",
    r"v\. inf",
    r"v\. intr",
    r"v\. refl",
    r"v\. trans",
]
OTHER_POS = OR(
    r"_pres\. pl\._ \(_refl\._\)",
    r"_n\._ \(as _adj\._\)",
    r"_n\._ \(_collective_\),",  # final comma?
    r"_pa\. t\. \(refl\.\)_",  # really should be _pa. t._ (_refl._)
    r"\(_pp\._\) _adj\._",
    r"_adj\._; _quasi-sb\._",
    r"_n\._ \(_pl\._ as _sg\._\)",
    r"_n\._\^2 _pl\._",
)
POS = fr"(_({'|'.join(pos)})\._(\^\d)?|{OTHER_POS})"

LANG = r"L\."

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
    "Fridays",
    "Southern",
    "Purgatory",
    "Gad-about",
    "Vagabond",
    "Virgin",
    "Rascal",
    "River Jordan",
    "Jill",
    "Christian lands",
    "Christmas",
    "Danes",
    "Danish",
    "Doomsday",
    "English",
    r"English \(language\)",
    "Englishmen",
    "Flemings",
    "French",
    r"Glutton \(personified\)",
    "Greeks",
    "Heaven",
    r"Hebrew \(language\)",
    r"Holy Church \(personified\)",
    "Jew",
    r"Lammas \(August 1st\)",
    "Mass",
    "May",
    "men of the Midlands",
    "Mercians",
    "Normans",
    r"Ocean \(as name of Indian Ocean\)",
    "Paradise",
    "Pastor",
    "people from Flanders",
    "Picts",
    "Pope",
    "Saxon",
    "Scots",
    "Shepherd",
    "Thursday",
    "Vespers of the Dead",
    "Welshmen",
    r"Whitsunday \(with pun on _Wit_\)",
    "Wisdom",
    "Yule",
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
    r"\(to expand\)",
    r"\(edge, cutting weapon\)",
    r"\(act of\) daring",
    r"\(straight\) up",
    r"to praise \(for\)",
    r"\(main\) beam",
    r"guard \(against\)",
    r"beware \(of\)",
    r"reproached \(with\)",
    r"abundance \(of\)",
    r"\(vegetable\) soup",
    r"\(draw\)bridge",
    r"\(secular\) priest",
    r"\(place of\) refuge",
    r"\(frontiers\)",
    r"\(folk\)",
    r"\(in French phrase\) more",
    r"\(a move in chess\)",
    r"\(adorned\)",
    r"\(all\) together",
    r"\(armed\) host",
    r"\(art of\) medicine",
    r"\(art, practice, of\) medicine",
    r"\(as a name\) Nameless, Nobody",
    r"\(away\) from",
    r"\(bequest\)",
    r"\(blinds\)",
    r"\(by God\)",
    r"\(by\) so much",
    r"\(considered\) opinion",
    r"\(dirge\)",
    r"\(even\) though",
    r"\(for\) evermore",
    r"\(French\) romance",
    r"\(green\) plants",
    r"\(hammered\)",
    r"\(it\) is necessary",
    r"\(lawfully\) married",
    r"\(leafy\) spray",
    r"\(legal\) complaint",
    r"\(loud\) shouting",
    r"\(male\) throstle",
    r"\(means of\) living",
    r"\(mental\) pain",
    r"\(method of\) teaching",
    r"\(mina\)",
    r"\(musical\) note",
    r"\(noble\) lineage",
    r"\(of grief, consternation, surprise, &c\.\) alas",
    r"\(performance of\) duty to his liege lord",
    r"\(plates\)",
    r"\(plea, lawsuit\)",
    r"\(professional\) story-tellers",
    r"\(sense of\) loss",
    r"\(shore\)",
    r"\(since long ago\)",
    r"\(something gained in\) hunting",
    r"\(soon\) afterwards",
    r"\(strange\) varieties",
    r"\(the\) Trinity",
    r"\(to acquire\)",
    r"\(to decline\)",
    r"\(to direct\)",
    r"\(to prepare oneself\)",
    r"\(turned\) in the opposite direction",
    r"\(unploughed\) ridges in a field",
    r"\(what is\) soft",
    r"\(wind-pipe\)",
    r"\(worth nought\)",
    r"\(you should\) hate",
    r"\(young\) leek or onion",
    r"are not \(with neg\.\)",
    "I am",
    "I have",
    "I know",
    "I will",
    r"is not \(usually with another neg\.\)",
    r"pieces of \(silver\) money",
    r"that \(over there\)",
    r"will not \(usually with another neg\.\)",
    r"robed \(himself\)",
)
GLOSS = fr"([a-z'\- ]+|{PROPER_NAMES}|{OTHER_GLOSSES})( \([a-z'\- ]+\))?"
GLOSSES = fr"(\? )?{GLOSS}([,;] {GLOSS})*"

TEXT_REF_EXTRA = OR(
    r" \(note\)",
    r" \(_see_ note\)",
    r" \(MS\.\)",
    r" \(footnote\)",
    r" \(cf\. _mul_, Pearl 905\)",
    r" \(first\)",
)
WORK_REF = "[IVX]+"
SUBTEXT_REF = fr"(( _[a-z]_)? (_title_|heading|\d+))"
TEXT_REF = fr"{WORK_REF}({SUBTEXT_REF}| _passim_)(,{SUBTEXT_REF})*{TEXT_REF_EXTRA}?"
TEXT_REF_DOT = r"{WORK_REF} _introd\._"
TEXT_REFS = fr"({TEXT_REF}(, {TEXT_REF})*(, {ETC})?)"
TEXT_REFS_DOT = fr"({TEXT_REF_DOT}|{TEXT_REF}(, {TEXT_REF})*(\.|, {ETC}))"

HEADWORDS = fr"{HEADWORD}(, {HEADWORD})*(, {ETC})?"
HEADWORDS_DOT = fr"{HEADWORD}(, {HEADWORD})*(\.|, {ETC})?"

HEADWORD_WITH_TEXT_REFS = fr"{HEADWORD}, {TEXT_REFS}"

WORK_REF1 = fr"\({WORK_REF}\)"
WORK_REF2 = fr"{WORK_REF}(, {WORK_REF})*"

HEADWORDS_WITH_WORK_REFS = fr"{HEADWORDS},? ({WORK_REF1}|{WORK_REF2})"


QUOTE = r"_[^_]+_"

ETYM = r"\[[^\]]+\]"

REF_PART = OR(
    fr"{HEADWORD_REF}, {ETC}",
    fr"{HEADWORD_REF},? {POS}",
    fr"{HEADWORD_REF},? {POS}(,| and|, and) {POS}",  # inconsistency
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
    fr"_See_ ({REF_PART}; )*{REF_PART_DOT}",
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

HEADWORD_PAREN_HEADWORD = fr"{HEADWORD} \({HEADWORDS}\)"

HEADWORD_LIST_DOT = OR(
    fr"({HEADWORDS}; )+{HEADWORD_PAREN_HEADWORD}\.",
    fr"({HEADWORDS}; )*{HEADWORD_POS_DOT}",
    fr"({HEADWORDS}; )*{HEADWORDS_DOT}",
    fr"{HEADWORDS} \({HEADWORDS}\); {HEADWORDS_DOT}",
    fr"{HEADWORD} \(=  ï̄e\)\.",
    fr"{HEADWORD}; {HEADWORD_PAREN_HEADWORD}; {HEADWORDS_DOT}",
    fr"{HEADWORD}; {HEADWORD_PAREN_HEADWORD}\.",
)

regexes = [
    re.compile(r)
    for r in [
        fr"{HEADWORD_LIST_DOT} {BIG_SEE_ALSO}$",
        fr"{HEADWORD_LIST_DOT} {BIG_SEE}$",
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
        fr"{HEADWORD} \(_[^_]+_\), {POS} {GLOSSES}, {TEXT_REFS_DOT} {ETYM}$",
        fr"{HEADWORD} \(_[^_]+_\), {POS} {GLOSSES}, {TEXT_REFS_DOT}$",
        fr"{HEADWORD} = {CAP_WORD} {GLOSS} \({POS}\), {TEXT_REFS_DOT}$",
        fr"{HEADWORD} = {CAP_WORD} \+ {CAP_WORD}\.$",
        fr"{HEADWORDS}, _pp\._ of {REF_PART_DOT}$",
        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_WITH_TEXT_REFS}; {LITTLE_SEE_DOT}$",
        fr"{HEADWORD_WITH_TEXT_REFS}: \? read _[^_]+_, {GLOSSES}; {LITTLE_SEE_DOT}$",

        fr"#U-#, #V-#; for init\. _u_, _v_ \(in III\) see also F\.$",
        fr"#Y-#; _see also_ Ȝ, I\. For past participles in _y-_ not entered below _see_ the verbs concerned\.$",

        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; _fig\._ {TEXT_REF}\. {ETYM}$",
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; {HEADWORD}, {TEXT_REF}\. {ETYM}$",

        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; {LITTLE_SEE_DOT} {ETYM}$",

        fr"{HEADWORD_POS} {GLOSSES}; {QUOTE}, {GLOSS}, {TEXT_REFS_DOT} {ETYM}$",

        fr"{HEADWORDS}; {LITTLE_SEE_DOT} {HEADWORD}; {LITTLE_SEE_DOT}$",

        fr"{HEADWORD}: familiar form of Robert \(used contemptuously\), {TEXT_REF}; {QUOTE}, {TEXT_REFS_DOT}$",

        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE}$",
        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {HEADWORD}, {LITTLE_SEE_DOT}$",
        fr"{HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE}; {HEADWORD}, {LITTLE_SEE_DOT}$",

        fr"{HEADWORD}: "
        fr"{HEADWORD_POS} {GLOSS}, {TEXT_REF}; "
        fr"{HEADWORD}, {TEXT_REF}; "
        fr"{HEADWORD}, {TEXT_REF}; "
        fr"{HEADWORD}, {GLOSSES}, {TEXT_REF}; "
        fr"{HEADWORD_POS} {GLOSSES}, {TEXT_REF}; "
        fr"{HEADWORD_POS} {TEXT_REF}, {HEADWORD}, {TEXT_REF}, {HEADWORD}, {TEXT_REF}; "
        fr"{HEADWORD}, {TEXT_REF}; "
        fr"{HEADWORD} \(_[^_]+_\), {GLOSS}, {TEXT_REF}; "
        fr"{HEADWORD}, {GLOSS}, {TEXT_REF}\. "
        fr"{ETYM} {BIG_SEE}$",


#        fr"{HEADWORD_POS}",
        fr"{HEADWORD_POS} {GLOSSES}",
        fr"{HEADWORD_POS}; {QUOTE}, {GLOSSES}",
        fr"{HEADWORD_POS} {QUOTE}, {GLOSSES}",

        fr"{HEADWORD} \([^)]+\), {POS} {GLOSSES}",
        fr"{HEADWORD_PAREN_HEADWORD}, {HEADWORD_POS} {GLOSSES}",
        fr"{HEADWORD_PAREN_HEADWORD}, {HEADWORD}, \({HEADWORDS}\), {POS} {GLOSSES}",
        fr"{HEADWORD} \({LANG} {POS}\) {GLOSSES}",
        fr"{HEADWORD} \({POS} of {HEADWORD_REF}, {QV}\), {GLOSSES}",
        fr"{HEADWORD} \(orig\. _pp\._ of {HEADWORD_REF}, {QV}\), {GLOSSES}",
        fr"{HEADWORD}; _[^_]+_ = _[^_]+_, {GLOSSES}",
        fr"{HEADWORD}(; {HEADWORD_WITH_TEXT_REFS})+; {POS} {GLOSSES}",
        fr"{HEADWORD}(; {HEADWORD_WITH_TEXT_REFS})+; {POS} \(i\)",
        fr"{HEADWORD}(; {HEADWORDS_WITH_WORK_REFS})+, {POS} {GLOSSES}",
        fr"{HEADWORD}(; {HEADWORDS_WITH_WORK_REFS})+; {POS} {GLOSSES}",
        fr"{HEADWORD}; {HEADWORDS}; {HEADWORDS_WITH_WORK_REFS}; {POS} {GLOSSES}",
        fr"{HEADWORD}; {HEADWORDS}; {POS} {GLOSSES}",
        fr"{HEADWORD}; {QUOTE}, {GLOSSES}",
        fr"{HEADWORDS_WITH_WORK_REFS}, {HEADWORDS_WITH_WORK_REFS}, {HEADWORD_POS} {GLOSSES}",
        fr"{HEADWORDS_WITH_WORK_REFS}(, {HEADWORDS_WITH_WORK_REFS})+, {POS} {GLOSSES}",
        fr"{HEADWORDS_WITH_WORK_REFS}, {HEADWORD_POS} {GLOSSES}",
        fr"{HEADWORD_POS}; {HEADWORD_POS} {GLOSSES}",
    ]
]


def check_entry(entry):
    for regex in regexes:
        if regex.match(entry):
            return True
    return False


if __name__ == "__main__":
    pass
    # print(re.match(HEADWORD_LIST_DOT, "#Scho#; #S(c)hold-#, #Scholle#; #Schome#; #Schon#; #Schop# (#Shope#)."))
    # for s in "Feld(e); Fele, _adj._; Fende; Fere _n._^1, _n._^2; Fest".split("; "):
    #     print(s, bool(re.match(REF_PART + "$", s)))
