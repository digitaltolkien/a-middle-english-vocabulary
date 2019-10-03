import re

languages = [  # without final period
    "AFr",  # Anglo-French
    "Anglo-L",  # Anglo-Latin (?)
    "Du",  # Dutch
    "E",  # English
    "Mn.E",  # Modern English
    "Fr",  # French
    "Fris",  # (Modern) Frisian (dialects)
    "G",  # German
    "Goth",  # Gothic
    "Icel",  # (Modern) Icelandic
    "Kt",  # OKt. Kentish; Kentish dialect of Old English.
    "L",  # Latin
    "Med.L",  # Mediaeval Latin
    "LG",  # ???
    "MDu",  # Middle Dutch
    "ME",  # Middle English
    "MHG",  # Middle High German
    "MLG",  # Middle Low German
    "Norw",  # Norwegian (not in list)
    "Nth",  # Northumbrian;
    "ONth",  # Northumbrian dialect of Old English.
    "NWM",  # North West Midland.
    "OE",  # Old English
    "OFr",  # Old French
    "OFris",  # Old Frisian
    "OHG",  # Old High German
    "OIcel",  # Old Icelandic (?)
    "OIr",  # Old Irish
    "ON",  # Old NOrse
    "ONFr",  # Northern dialects of Old French
    "OS",  # Old Saxon (Old Low German)
    "OSwed",  # Old Swedish (?)
    "Swed",  # Swedish
    # WS.; OWS. West Saxon (dialect of Old English).
]

IT = r"_[^_]+_"
IT_END = fr"(_[^_]+!_|{IT}\.)"
LANG = fr"(({'|'.join(languages)})\.|Latin|Welsh)"
CAP_WORD = r"[A-ZÞ]([a-zþȝ]|p\(p\))+(\([en]\))?-?"
GRM = r"(prep|n|v|adj|adv|pl|fem|neut|masc|str|wk|dat|acc|gen|sg|nom|pa|t|3 sg|conj|intr|compar|collect|refl|pret|pres|subj|p)\."
SUP = r"\^\d+"
QV = r"_q\.v\._"
SV = r"s\.v\."
SVV = r"s\.vv\."
CF = r"(cf\.|_cf\._|Cf\.|_Cf\._)"  # italics inconsistency?
NED = r"_N\.E\.D\._"  # The Oxford (New) English Dictionary
EDD = r"_E\.D\.D\._"
GLOSS = r"([a-z\- ']+|Briton|w\(h\)op)"
ETC = r"&c\."
INFL_BY = r"infl\. by"
REF = "VII 167"
SEE_APP = r"_see_ (App\.,|Appendix,|Appendix) p\. \d+\."  # inconsistency

ECHOIC = r"[Ee]choic"
ECHOIC_END = r"[Ee]choic\."

GRMS = fr"{GRM}( {GRM})*"

HEADREF_1 = fr"{CAP_WORD}, _{GRM}_{SUP}"
HEADREF_2 = fr"{CAP_WORD}, _{GRM}_"
HEADREF_3 = fr"{CAP_WORD} _{GRM}_"  # inconsistent comma
CAP_WORDS = fr"{CAP_WORD}(, {CAP_WORD})*"

NEXT_PREC = r"(next\.?|prec\.|Next\.?|Prec\.)"

HEADREF = fr"({HEADREF_1}|{HEADREF_2}|{HEADREF_3}|{CAP_WORDS}|{NEXT_PREC}|{CAP_WORD}, {QV})"
HEADREF_END = fr"({HEADREF_1}|{HEADREF_2}|{HEADREF_3}|{CAP_WORDS}\.|{NEXT_PREC}|{CAP_WORD}, {QV})"

SEE_HEADREF = fr"_see_ {HEADREF}"
SEE_HEADREF_END = fr"_see_ {HEADREF_END}"
CAP_SEE_HEADREF = fr"_See_ {HEADREF}"
CAP_SEE_HEADREF_END = fr"_See_ {HEADREF_END}"

CF_HEADREF = fr"{CF} {HEADREF}"
CF_HEADREF_END = fr"{CF} {HEADREF_END}"

GLOSSES = fr"{GLOSS}(, {GLOSS})*(, {ETC})?"
GLOSSES_END = fr"{GLOSS}(, {GLOSS})*(, {ETC}|\.)"

Q = r"(\? )?"

ETYM_01 = fr"{LANG} {IT}, {GRM}"
ETYM_01_END = fr"{LANG} {IT}, {GRM}"
ETYM_02 = fr"{LANG} {IT}"
ETYM_02_END = fr"{Q}{LANG} {IT_END}"
ETYM_03_END = fr"{LANG} {IT}, {IT_END}"
ETYM_04_END = fr"{LANG} {IT}, {LANG} {IT_END}"
ETYM_05_END = fr"{LANG} {IT}, {GLOSSES_END}"
ETYM_06_END = fr"{LANG}, {LANG} {IT_END}"
ETYM_07 = fr"{LANG} {IT}, {GLOSSES}"
ETYM_07_END = fr"{LANG} {IT}, {GLOSSES_END}"
ETYM_08 = fr"{LANG} {IT}, {GLOSSES}"
ETYM_08_END = fr"{LANG} {IT}, {GLOSSES_END}"
ETYM_09 = fr"{LANG} {IT}, {GRM}, {GLOSSES}"
ETYM_09_END = fr"{LANG} {IT}, {GRM}, {GLOSSES_END}"
ETYM_10_END = fr"{LANG} {IT}, {LANG} {IT}, {GLOSSES_END}"
ETYM_11 = fr"{LANG}, {LANG} {IT}, {GRM}"
ETYM_12_END = fr"{LANG} {IT} {GLOSSES_END}"
ETYM_13 = fr"{LANG} {IT}, {IT}"
ETYM_14_END = fr"{LANG} {IT}, {IT}, {GLOSSES_END}"
ETYM_15 = fr"{CF} {LANG} gloss {IT}, {GLOSS}"
ETYM_16 = fr"see {NED}"
ETYM_17_END = fr"{IT} \({GRMS} {IT}\), {GRM}"
ETYM_18 = fr"{IT}, {GRM}"
ETYM_19_END = fr"{IT}, {GLOSSES_END}"
ETYM_20_END = fr"{IT}, {LANG} {IT_END}"
ETYM_21_END = fr"{IT}, {IT_END}"
ETYM_22 = fr"{IT}, {GLOSS}"
ETYM_22_END = fr"{IT}, {GLOSSES_END}"
ETYM_23_END = fr"see {NED}, {SV} _{CAP_WORD}_\."

ETYM_000 = fr"{CF} {ETYM_02_END}"
ETYM_001 = fr"{CF} {ETYM_06_END}"
ETYM_005 = fr"{CF} {ETYM_02}"
ETYM_002 = fr"{CF} {ETYM_01}"
ETYM_003 = fr"{CF} {ETYM_03_END}"
ETYM_004 = fr"{CF} {ETYM_04_END}"
ETYM_006 = fr"{Q}{CF} {ETYM_05_END}"
ETYM_007 = fr"{CF} {ETYM_07}"
ETYM_008 = fr"{CF} {IT_END}"
ETYM_009 = fr"{CF} {IT}, {ETC}"
ETYM_010 = fr"{CF} {ETYM_19_END}"
ETYM_011 = fr"{CF} {ETYM_20_END}"

regexes = [
    re.compile(r)
    for r in [
        fr"{CAP_SEE_HEADREF_END}$",
        fr"{CAP_WORDS} {INFL_BY} {CAP_WORD}\.$",
        fr"{CAP_WORDS} \+ {HEADREF_END}$",
        fr"{CF} {ETYM_08}, and _{CAP_WORD}_{SUP} in {EDD}$",
        fr"{CF} {ETYM_09_END}$",
        fr"{CF} {ETYM_10_END}$",
        fr"{CF} {ETYM_11}$",
        fr"{CF} {LANG} {IT}, {LANG}, {LANG} {IT_END}$",
        fr"{CF} {LANG}, {LANG}, {IT_END}$",
        fr"{ETYM_000}$",
        fr"{ETYM_001}$",
        fr"{ETYM_002}$",
        fr"{ETYM_003}$",
        fr"{ETYM_004}$",
        fr"{ETYM_005}; {ETYM_02_END}$",
        fr"{ETYM_005}; {ETYM_16}$",
        fr"{ETYM_006}$",
        fr"{ETYM_007}; {ECHOIC_END}$",  # @@@
        fr"{ETYM_01}; {ETYM_000}$",
        fr"{ETYM_01}; {ETYM_008}$",
        fr"{ETYM_01}; {ETYM_17_END}$",
        fr"{ETYM_01}; {ETYM_18}; {ETYM_18}$",
        fr"{ETYM_01}; {IT_END}$",
        fr"{ETYM_01_END}$",
        fr"{ETYM_02_END}$",
        fr"{ETYM_02} \({CF} {LANG} {IT}, {LANG} {IT}\)\.$",
        fr"{ETYM_02} \+ {ETYM_02_END}$",
        fr"{ETYM_02} \+ {ETYM_02} \({CF} {LANG}, {LANG} {IT}\).$",
        fr"{ETYM_02} \+ {ETYM_02}; {ETYM_000}$",
        fr"{ETYM_02} \+ {ETYM_04_END}$",
        fr"{ETYM_02} \+ {ETYM_22} \({SEE_HEADREF}\)\.",
        fr"{ETYM_02} \+ {GRM} {IT_END}$",
        fr"{ETYM_02} \+ {HEADREF_END}$",
        fr"{ETYM_02} \+ {IT_END}$",
        fr"{ETYM_02} \+ {IT} \({SEE_HEADREF}\)\.$",
        fr"{ETYM_02} \+ {IT} \(intensive\)\.$",
        fr"{ETYM_02} \+ {IT} \(properly {GRM} with {NEXT_PREC} noun\).$",
        fr"{ETYM_02} \+ {IT} indef\.$",
        fr"{ETYM_02} \+ {IT}, {GRMS}$",
        fr"{ETYM_02} \+ {IT}, pp\. of {IT_END}$",
        fr"{ETYM_02} \+ {IT}, pp\.$",
        fr"{ETYM_02} \+ {IT}; {CF} {LANG} \(late\) {IT_END}$",
        fr"{ETYM_02} \+ {IT}; {CF} {NEXT_PREC}$",
        fr"{ETYM_02} \+ {IT}; {ETYM_000}$",
        fr"{ETYM_02} \+ {IT}; {ETYM_008}$",
        fr"{ETYM_02} \+ {IT}; {ETYM_009}$",
        fr"{ETYM_02} \+ {IT}; {ETYM_010}$",
        fr"{ETYM_02} \+ \? {IT} \? {IT_END}$",
        fr"{ETYM_02} blended with {IT} \({IT}\)\.$",
        fr"{ETYM_02} from {ETYM_02_END}$",
        fr"{ETYM_02} rel\. to {IT_END}$",
        fr"{ETYM_02} through {LANG}$",
        fr"{ETYM_02} under influence of {IT_END}$",
        fr"{ETYM_02} with substitution of {GRMS} {IT}.$",
        fr"{ETYM_02}, {ETYM_02}, {ETC}, pp\.$",
        fr"{ETYM_02}, \? {INFL_BY} {IT_END}$",
        fr"{ETYM_02}, \? {INFL_BY} {IT}, {ETC}",
        fr"{ETYM_02}, corruptly from {ETYM_02_END}$",
        fr"{ETYM_02}, formed on {ETYM_02}, pp\.$",
        fr"{ETYM_02}, from {ETYM_02_END}$",
        fr"{ETYM_02}, from {ETYM_22_END}$",
        fr"{ETYM_02}, from {HEADREF_END}$",
        fr"{ETYM_02}, from {LANG}$",
        fr"{ETYM_02}, infl\. in sense by cognate {ETYM_02_END}$",
        fr"{ETYM_02}, influ\. in {LANG} by assoc\. with {IT_END}$",  # abbrev inconsistency
        fr"{ETYM_02}, influenced by {IT_END}$",
        fr"{ETYM_02}; _see_ {NEXT_PREC}$",
        fr"{ETYM_02}; {CF_HEADREF_END}$",
        fr"{ETYM_02}; {CF} {ETYM_12_END}$",
        fr"{ETYM_02}; {CF} {ETYM_13}, in this sense\.$",
        fr"{ETYM_02}; {CF} {IT}, and {LANG} {IT_END}$",
        fr"{ETYM_02}; {CF} {IT}, and {NEXT_PREC}\.$",
        fr"{ETYM_02}; {ETYM_000}$",
        fr"{ETYM_02}; {ETYM_004}$",
        fr"{ETYM_02}; {ETYM_008}$",
        fr"{ETYM_02}; {ETYM_01_END}$",
        fr"{ETYM_02}; {ETYM_011}$",
        fr"{ETYM_02}; {ETYM_02_END}$",
        fr"{ETYM_02}; {ETYM_03_END}$",
        fr"{ETYM_02}; {ETYM_06_END}$",
        fr"{ETYM_02}; {ETYM_08_END}$",
        fr"{ETYM_02}; {ETYM_08}\. {CF_HEADREF}$",
        fr"{ETYM_02}; {ETYM_18}$",
        fr"{ETYM_02}; {ETYM_21_END}$",
        fr"{ETYM_02}; {ETYM_23_END}$",
        fr"{ETYM_02}; {GRM} {IT}, {IT_END}$",
        fr"{ETYM_02}; {GRMS} {IT_END}$",
        fr"{ETYM_02}; {GRMS} {IT} \({ETYM_02}\)\.$",
        fr"{ETYM_02}; {GRMS} {IT}, {IT_END}$",
        fr"{ETYM_02}; {IT_END}$",
        fr"{ETYM_02}; {IT} {GRMS}; {IT}, {ETC}$",
        fr"{ETYM_02}; {IT} \({GRMS}\) \+ {IT_END}$",
        fr"{ETYM_02}; {IT} = {IT} \(see the rimes\)\.$",
        fr"{ETYM_02}; {IT} is freq\. Northern form\.$",
        fr"{ETYM_02}; {IT}, _{GRM}_$",
        fr"{ETYM_02}; {IT}, {IT} {GRM}$",
        fr"{ETYM_02}; {IT}, {IT}; {IT}, {ETC}$",
        fr"{ETYM_02}; {IT}, pp\.$",
        fr"{ETYM_02}; {LANG} vowel and usage show infl\. of {CAP_WORD}\.$",
        fr"{ETYM_02}; {SEE_HEADREF}\.$",
        fr"{ETYM_02}; \? {INFL_BY} {IT_END}$",
        fr"{ETYM_02}; \? {LANG} {IT} \(in sense '{GLOSS}'\)\.$",
        fr"{ETYM_02}; \? from {LANG} {IT}, {GLOSS}, _{GRM}_$",
        fr"{ETYM_02}; accented stem {IT}, {IT}, {ETC}$",
        fr"{ETYM_02}; and direct from {ETYM_02_END}$",
        fr"{ETYM_02}; but see {NED}$",
        fr"{ETYM_02}; early {ETYM_02_END}$",
        fr"{ETYM_02}; obscure\.$",
        fr"{ETYM_02}; on {IT}-form see {NED} {SV} _{CAP_WORD}_\.$",
        fr"{ETYM_02}; on stem-vowel see {NED} {SV} _{CAP_WORD}_\.$",
        fr"{ETYM_02}; on the vowel {SEE_HEADREF}\.$",
        fr"{ETYM_02}; orig\. same word as {HEADREF}$",
        fr"{ETYM_02}; see {NED}, {SV} {ETYM_18}$",
        fr"{ETYM_02}; see {NED}$",
        fr"{ETYM_02}; see {NEXT_PREC}$",
        fr"{ETYM_02}; see note\.$",
        fr"{ETYM_02}; the {IT} forms are difficult to explain.$",
        fr"{ETYM_02}; the confusion with {IT} began in {LANG}$",
        fr"{ETYM_02}; with {IT} {CF} {CAP_WORDS}\.$",
        fr"{ETYM_02}; with the reduced forms {CF_HEADREF_END}$",
        fr"{ETYM_02}\. \({ETYM_005}\)\.$",
        fr"{ETYM_02}\. On {IT} for {IT}, {SEE_APP}$",
        fr"{ETYM_03_END}$",
        fr"{ETYM_04_END}$",
        fr"{ETYM_05_END}$",
        fr"{ETYM_06_END}$",
        fr"{ETYM_08} \(late {LANG} {GRM} {IT}\)\.$",
        fr"{ETYM_08} \(or stem of {NEXT_PREC}\) \+ {IT_END}$",
        fr"{ETYM_08} \+ {ETYM_02_END}$",
        fr"{ETYM_08}, from {ETYM_02_END}$",
        fr"{ETYM_08}; {CF_HEADREF_END}$",
        fr"{ETYM_08}; {ETYM_000}$",
        fr"{ETYM_08}; {ETYM_07_END}$",
        fr"{ETYM_08}; {ETYM_19_END}$",
        fr"{ETYM_08}; {GRMS} {IT_END}$",
        fr"{ETYM_08}; see {NED}$",
        fr"{ETYM_09}; {ETYM_08_END}$",
        fr"{ETYM_10_END}$",
        fr"{ETYM_12_END}$",
        fr"{ETYM_13}; {ETYM_000}$",
        fr"{ETYM_13}; {ETYM_02_END}$",
        fr"{ETYM_13}; {ETYM_21_END}$",
        fr"{ETYM_13}; {GRM} {IT}; {LANG} {GRM} {IT_END}$",
        fr"{ETYM_13}; {GRMS} {IT}, {IT_END}$",
        fr"{ETYM_13}; {IT_END}$",
        fr"{ETYM_13}; {IT}, {IT}, {GRM}$",
        fr"{ETYM_13}; {IT}; {IT_END}$",
        fr"{ETYM_13}; later {IT_END}$",
        fr"{ETYM_13}; pp\. {IT_END}$",
        fr"{ETYM_14_END}$",
        fr"{ETYM_15}; {ETYM_02_END}$",
        fr"{HEADREF} \+ _pp\._ of {CAP_WORD}\.$",
        fr"{HEADREF} \+ {ETYM_02_END}$",
        fr"{HEADREF} \+ {ETYM_02} from {CAP_WORD}\.$",
        fr"{HEADREF} \+ {ETYM_02}; {ETYM_02_END}$",
        fr"{HEADREF} \+ {ETYM_03_END}$",
        fr"{HEADREF} \+ {GRM} {IT_END}$",
        fr"{HEADREF} \+ {HEADREF_END}$",
        fr"{HEADREF} \+ {IT_END}$",
        fr"{HEADREF} and {ETYM_08}\.$",
        fr"{IT} \+ {CAP_WORD}; {CF} {IT}, {SV} {HEADREF}$",
        fr"{IT} \+ {ETYM_02_END}$",
        fr"{IT} \+ {ETYM_02}; {CF} {ETYM_22_END}$",
        fr"{IT} \+ {ETYM_03_END}$",
        fr"{IT} \+ {ETYM_08}\.$",
        fr"{LANG} {IT} {GRM}, {GLOSSES_END}$",
        fr"{LANG} {IT} {GRMS}$",
        fr"{LANG} {IT} {INFL_BY} {ETYM_18}$",
        fr"{LANG} {IT} {INFL_BY} senses of related {ETYM_02_END}$",
        fr"{LANG} {IT} \({ETYM_02}\) {INFL_BY} {IT_END}$",
        fr"{LANG} {IT} \({ETYM_02}\), or {ETYM_02_END}$",
        fr"{LANG} {IT} \({ETYM_02}\); {SEE_APP}$",
        fr"{LANG} {IT} \({ETYM_18}\); {IT_END}$",
        fr"{LANG} {IT} \({GLOSS}\) {IT} \({IT}\)\.$",
        fr"{LANG} {IT} \({GRM} {IT}, {IT}\); {ETYM_02_END}$",
        fr"{LANG} {IT} \({GRM}\), {GLOSSES}; {CF_HEADREF}$",
        fr"{LANG} {IT} \({GRM}\); {SEE_APP}$",
        fr"{LANG} {IT} \({IT}, {GRMS}\); {CF_HEADREF}\.$",
        fr"{LANG} {IT} \({IT}\) \+ {ETYM_02_END}$",
        fr"{LANG} {IT} \({IT}\) \+ {IT} \({ETYM_02}\)\.$",
        fr"{LANG} {IT} \({IT}\), {IT}, {ETC}; {LANG} {GRM} {IT}, {ETC}$",
        fr"{LANG} {IT} \({IT}\), {IT}, {IT}.",
        fr"{LANG} {IT} \({IT}\), or {IT_END}$",
        fr"{LANG} {IT} \({IT}\); {ETYM_21_END}$",
        fr"{LANG} {IT} \({IT}\)\.$",
        fr"{LANG} {IT} \({LANG} {IT}, {LANG} {IT}\)\.$",
        fr"{LANG} {IT} \(\? late {ETYM_02}\); but see {HEADREF}$",
        fr"{LANG} {IT} \(a land-measure\); {ETYM_02_END}$",
        fr"{LANG} {IT} \(from {IT}\) \+ {IT_END}$",
        fr"{LANG} {IT} \(in Sweet\)\.$",
        fr"{LANG} {IT} \(late {IT}\), {ETC}$",
        fr"{LANG} {IT} \(once\), {IT_END}$",
        fr"{LANG} {IT} \(or {IT}\) {IT_END}$",
        fr"{LANG} {IT} and {ETYM_02_END}$",
        fr"{LANG} {IT} and {IT_END}$",
        fr"{LANG} {IT} or {IT}, {INFL_BY} {NEXT_PREC}$",
        fr"{LANG} {IT}, {CAP_WORD}\.$",
        fr"{LANG} {IT}, {CF} {IT_END}$",
        fr"{LANG} {IT}, {ETC}, {GLOSS}\.$",
        fr"{LANG} {IT}, {ETC}, pet-name assoc. with 'John'\.$",
        fr"{LANG} {IT}, {GLOSS} {INFL_BY} unrelated {ETYM_08}\.$",
        fr"{LANG} {IT}, {GLOSS} \({GLOSS}\)\.$",
        fr"{LANG} {IT}, {GLOSS} \(sound\)\.$",
        fr"{LANG} {IT}, {GLOSS}, \(in verse\) {GLOSS}\.$",
        fr"{LANG} {IT}, {GLOSSES} \(of arrow, spear, {ETC}\)\.$",
        fr"{LANG} {IT}, {GRM} {IT}, {IT_END}$",
        fr"{LANG} {IT}, {GRM} \+ {IT_END}$",
        fr"{LANG} {IT}, {GRM} and {GRM}; {ETYM_18}$",
        fr"{LANG} {IT}, {GRM} and {GRM}$",
        fr"{LANG} {IT}, {GRM} of {IT_END}$",
        fr"{LANG} {IT}, {GRM}, {GRM}; {ETYM_18}$",
        fr"{LANG} {IT}, {GRM}, {IT}, {GRM}$",
        fr"{LANG} {IT}, {GRM}, and {IT}, {GRM}$",
        fr"{LANG} {IT}, {GRMS} {IT_END}$",
        fr"{LANG} {IT}, {GRMS}, {GLOSS}\.$",
        fr"{LANG} {IT}, {GRMS}, for \(by\) itself; separately\.$",
        fr"{LANG} {IT}, {GRMS}$",  # inconsistent comma?
        fr"{LANG} {IT}, {INFL_BY} {HEADREF_END}$",
        fr"{LANG} {IT}, {INFL_BY} {IT_END}$",
        fr"{LANG} {IT}, {INFL_BY} related verb; {SEE_HEADREF_END}$",
        fr"{LANG} {IT}, {INFL_BY} suffix {IT_END}$",
        fr"{LANG} {IT}, {IT} \({ETYM_02}\) \+ {GRM} {IT_END}$",
        fr"{LANG} {IT}, {IT} \({GRM}\), {IT_END}$",
        fr"{LANG} {IT}, {IT} \(fem\.\)\.$",
        fr"{LANG} {IT}, {IT} \(still {LANG}\); {CF} {IT}, {IT_END}$",
        fr"{LANG} {IT}, {IT} \+ {GRM} {IT_END}$",
        fr"{LANG} {IT}, {IT} \+ {IT_END}$",
        fr"{LANG} {IT}, {IT}, {ETC}, {GRM}$",
        fr"{LANG} {IT}, {IT}, {ETC}$",
        fr"{LANG} {IT}, {IT}, {GRM}{SUP}$",
        fr"{LANG} {IT}, {IT}, {IT_END}$",
        fr"{LANG} {IT}, {IT}, {IT}, {ETC}$",
        fr"{LANG} {IT}, {IT}, {IT}, {IT_END}$",
        fr"{LANG} {IT}, {IT}, {IT}, {IT}, {ETC}$",
        fr"{LANG} {IT}, {IT}, {IT}; see {NED}$",
        fr"{LANG} {IT}, {IT}, {LANG} {IT_END}$",
        fr"{LANG} {IT}, {IT}, and prob\. unacc\. {IT}, {IT_END}$",
        fr"{LANG} {IT}, {IT}, distinct from {IT_END}$",
        fr"{LANG} {IT}, {IT}, occas\. {IT_END}$",
        fr"{LANG} {IT}, {IT}, str\. and wk\.$",
        fr"{LANG} {IT}, {IT}, str\., later wk\.$",
        fr"{LANG} {IT}, {LANG} {IT}, {GRM}$",
        fr"{LANG} {IT}, {LANG} {IT}; see {NED}$",
        fr"{LANG} {IT}, \? {IT_END}$",
        fr"{LANG} {IT}, \({GRMS}\) {GLOSS}\.$",
        fr"{LANG} {IT}, \(late\) {IT_END}$",
        fr"{LANG} {IT}, \(once in gloss\.\) {IT_END}$",
        fr"{LANG} {IT}, \(once\) {IT_END}$",
        fr"{LANG} {IT}, and {IT} prefix\.$",
        fr"{LANG} {IT}, and \(from 14th c\.\) {IT}, {ETC}$",
        fr"{LANG} {IT}, and occas\. in same sense {IT_END}$",
        fr"{LANG} {IT}, and with weak stress {IT}\(\?\)\.$",
        fr"{LANG} {IT}, earlier {IT_END}$",
        fr"{LANG} {IT}, early confused with {IT_END}$",
        fr"{LANG} {IT}, in {ETYM_22_END}$",
        fr"{LANG} {IT}, in {IT}; see {NED}, s.v. _{CAP_WORD}_\.$",
        fr"{LANG} {IT}, late {GRMS} {IT_END}$",
        fr"{LANG} {IT}, late {IT_END}$",
        fr"{LANG} {IT}, later {IT_END}$",
        fr"{LANG} {IT}, oblique forms of {IT_END}$",
        fr"{LANG} {IT}, older {IT_END}$",
        fr"{LANG} {IT}, older, {IT_END}$",
        fr"{LANG} {IT}, or {ETYM_02_END}$",
        fr"{LANG} {IT}, or {ETYM_03_END}$",
        fr"{LANG} {IT}, or {IT_END}$",
        fr"{LANG} {IT}, or {IT}; {ETYM_02_END}$",
        fr"{LANG} {IT}, orig\. 'mated' in chess\.$",
        fr"{LANG} {IT}, pers\. and impers\.$",
        fr"{LANG} {IT}, pp\. {IT_END}$",
        fr"{LANG} {IT}, pp\. {IT}; {CF} {LANG} pp\. {IT_END}$",
        fr"{LANG} {IT}, pp\. {IT}$",  # @@@ missing final .
        fr"{LANG} {IT}, pp\., {GLOSS}\.$",
        fr"{LANG} {IT}, prob\. {INFL_BY} senses of {ETYM_02_END}$",
        fr"{LANG} {IT}, reduced under wk\. stress\.$",
        fr"{LANG} {IT}, rel\. to {ETYM_22_END}$",
        fr"{LANG} {IT}, rel\. to {HEADREF}$",
        fr"{LANG} {IT}, rel\. to {IT}, {CAP_WORD}\.$",
        fr"{LANG} {IT}, stem of {IT_END}$",
        fr"{LANG} {IT}, str\.; {IT}, wk\.; both intr\.$",
        fr"{LANG} {IT}, to file; or {ETYM_02_END}$",
        fr"{LANG} {IT}, with {IT} > {IT_END}$",
        fr"{LANG} {IT}, with {LANG} {IT} > {IT_END}$",
        fr"{LANG} {IT}{SUP} \+ {IT_END}$",
        fr"{LANG} {IT}\.{SUP}$",
        fr"{LANG} \? {IT}, rel\. to {IT_END}$",
        fr"{LANG} \? {IT}; {ETYM_02_END}$",
        fr"{LANG} \(allit\.\) {ETYM_22_END}$",
        fr"{LANG} \(from {LANG}\) {IT_END}$",
        fr"{LANG} \(i\) {IT}, \(ii\) {IT_END}$",
        fr"{LANG} \(late\) {IT}, prob\. modelled on {ETYM_02_END}$",
        fr"{LANG} \(once\) {IT}; {CF} {ETYM_18}$",
        fr"{LANG} \(only {LANG}\) {IT}, of unknown origin\.$",
        fr"{LANG} \(rare\) {IT_END}$",
        fr"{LANG} also {IT}; \? obscurely rel\. to {HEADREF_END}$",
        fr"{LANG} forms point to {ETYM_02_END}$",
        fr"{LANG} in {ETYM_21_END}$",
        fr"{LANG} in {IT_END}$",
        fr"{LANG} in {IT}; see {NED} {SV} {IT_END}$",
        fr"{LANG} unacc\. form {IT}, or {ETYM_02}; {SEE_HEADREF}\.$",
        fr"{LANG}, {LANG} {IT}, {LANG} {IT_END}$",
        fr"{LANG}; also appears in {LANG} in {LANG} form {IT_END}$",
        fr"{LANG}$",
        fr"\? {ETYM_02} \({CF} {IT}\)\.$",
        fr"\? {ETYM_02} \+ {IT}; {CF} {IT}, Layamon 969\.$",
        fr"\? {ETYM_02}; {ETYM_000}$",
        fr"\? {ETYM_02}; earliest {LANG} sense appar\. '{GLOSS}'.",
        fr"\? {ETYM_02}; see {NED}$",
        fr"\? {ETYM_08}; {CF_HEADREF}\.$",
        fr"\? {ETYM_08}; {CF} senses of {IT}.$",
        fr"\? {ETYM_14_END}$",
        fr"\? {LANG} {IT} < {IT} \({ETYM_005}\)\.$",
        fr"\? {LANG} {IT}, {GRMS}, or {GRM}, of {IT_END}$",
        fr"\? {LANG} {IT}, {IT}, {GLOSSES}; {CF_HEADREF_END}$",
        fr"\? Altered form of {ETYM_02_END}$",
        fr"\? From {NEXT_PREC}$",
        fr"\? Obscure alteration of {ETYM_02_END}$",
        fr"\? Rel\. to {NEXT_PREC}$",
        fr"\? Related \(as {IT} to {IT}\) to {ETYM_02_END}$",
        fr"\? Related to {HEADREF}$",
        fr"\? Same as {NEXT_PREC}$",
        fr"A Northern form\. ON\. {IT_END}$",
        fr"A variant, usually Northern, of {HEADREF_END}$",
        fr"Altered by assoc\. with {NEXT_PREC} from {ETYM_02_END}$",
        fr"As {CAP_WORD}, with alteration of final spirant; {CF_HEADREF}\.$",
        fr"As {NEXT_PREC} with subst\. of interchangeable {IT_END}$",
        fr"As {NEXT_PREC}; for older {GRMS} {SEE_HEADREF}\.$",
        fr"As {NEXT_PREC}$",
        fr"Back-formation from {CAP_WORD}\.$",
        fr"Blend of {ETYM_02}, and {ETYM_02_END}$",
        fr"Blend of {ETYM_08}, and {ETYM_08}\.$",
        fr"Children's language\.$",
        fr"{ECHOIC}, on model of {HEADREF_END}$",
        fr"{ECHOIC}; {CF_HEADREF_END}$",
        fr"{ECHOIC}; {ETYM_005}; {ETYM_01_END}$",
        fr"{ECHOIC_END}$",
        fr"Extended from {CAP_WORD} with abstract {IT_END}$",
        fr"Extended from {CAP_WORD}, _conj\._, with {GRM} {IT_END}$",
        fr"Extended from {ETYM_02_END}$",
        fr"Extended from {ETYM_02}; {CF_HEADREF}\.$",
        fr"Extended from {NEXT_PREC}$",
        fr"First two words of Latin prayer\.$",
        fr"Formed on {HEADREF_END}$",
        fr"Formed on {LANG} {IT} pp\. of {IT_END}$",
        fr"From _{NEXT_PREC}_$",  # @@@ why italic?
        fr"From {CAP_WORD}, {GLOSS}\. {CAP_SEE_HEADREF}; {HEADREF_END}$",
        fr"From {ETYM_01_END}$",
        fr"From {ETYM_02_END}$",
        fr"From {ETYM_02} \+ {IT_END}$",
        fr"From {ETYM_02}, extended from {HEADREF}$",
        fr"From {ETYM_02}, formed on {HEADREF_END}$",
        fr"From {ETYM_02}; {ETYM_000}$",
        fr"From {ETYM_03_END}$",
        fr"From {ETYM_06_END}$",
        fr"From {ETYM_08_END}$",
        fr"From {ETYM_08}; _see_ Piers Pl\. C X 215\.$",
        fr"From {ETYM_08}; obscure\.$",
        fr"From {ETYM_10_END}$",
        fr"From {ETYM_11}$",
        fr"From {ETYM_22}; {ETYM_000}$",
        fr"From {HEADREF_END}$",
        fr"From {HEADREF}; {ETYM_000}$",
        fr"From {HEADREF}$",
        fr"From {IT_END}$",
        fr"From {IT}, old infin\. stem of {HEADREF}$",
        fr"From {LANG} {IT}, {ETC}, extended from {NEXT_PREC}$",
        fr"From {LANG} {IT}, {ETYM_02_END}$",
        fr"From {LANG} {IT}, {IT} \({ETYM_02}\), {GLOSS}\.$",
        fr"From {LANG} {IT}, {IT}, {GRM}; {ETYM_02_END}$",
        fr"From {LANG} {IT}, {IT}, {GRM}; {SEE_HEADREF}\.$",
        fr"From {LANG} {IT}, {IT}, {GRM}$",
        fr"From {LANG} {IT}, {IT}, on anal\. of {ETYM_21_END}$",
        fr"From {LANG} {IT}, {IT}, pp\.$",
        fr"From {LANG} {IT}, {LANG} {IT} \(related to {NEXT_PREC}\)\.$",
        fr"From {NEXT_PREC} \({CF} {REF}\); {ETYM_000}$",
        fr"From {NEXT_PREC} \(i\)\.$",
        fr"From {NEXT_PREC} in {LANG} sense '{GLOSS}'\.$",
        fr"From {NEXT_PREC} in frequent sense '{GLOSS}'\.$",
        fr"From {NEXT_PREC}; {CF} Cath\. Angl\., '_coker_, autumnarius'\.$",  # @@@
        fr"From {NEXT_PREC}; {ETYM_000}$",
        fr"From {NEXT_PREC}; {ETYM_002}$",
        fr"From {NEXT_PREC}; {ETYM_003}$",
        fr"From {NEXT_PREC}; {ETYM_02_END}$",
        fr"From {NEXT_PREC}; cf, {ETYM_02_END}$",  # @@@
        fr"From {NEXT_PREC}$",
        fr"From \(obscure\) {ETYM_08}; see {NED}$",
        fr"From pp\. of {HEADREF_END}$",
        fr"From pres\. p\. of {CAP_WORD}\.$",
        fr"From stem of {CAP_WORD}; {ETYM_000}$",
        fr"Further reduced from {HEADREF_END}$",
        fr"Late {ETYM_02}, from {ETYM_02_END}$",
        fr"Late {ETYM_02}, from {ETYM_04_END}$",
        fr"Late OE\. {IT} from {ETYM_02_END}$",
        fr"Late OE\. {IT}, {IT}\.",
        fr"Modelled on {ETYM_02_END}$",
        fr"Nonce-use of {ETYM_08}\.$",
        fr"Northern form of {HEADREF_END}$",
        fr"Not known; only allit\.$",
        fr"Not known\.$",
        fr"Obscure; {ETYM_001}$",
        fr"Obscure; {ETYM_006}$",
        fr"Obscure; {ETYM_23_END}$",
        fr"Obscure; {Q}{CF_HEADREF}, and {ETYM_02_END}$",
        fr"Obscure; appar\. peculiar to {CAP_WORD}\.$",
        fr"Obscure; usually Northern\.$",
        fr"Obscure\.$",
        fr"Obscurely rel\. to {ETYM_08}; see {NED}$",
        fr"OE\. {IT} \({IT}, but not WS\.\)\.$",
        fr"OE\. {IT} \(Kt\. {IT}\); {ETYM_21_END}$",
        fr"OE\. {IT} \(Kt\. {IT}\)\.$",  # Kt inconsistency
        fr"OE\. {IT} \(late WS\. {IT}\)\.$",
        fr"OE\. {IT} \(rare\)\.$",
        fr"OE\. {IT}, \(Kt\. {IT}\)\.$",  # Kt inconsistency
        fr"OE\. {IT}, \(Kt\.\) {IT_END}$",  # Kt inconsistency
        fr"OE\. {IT}, Kt\. {IT_END}$",  # Kt inconsistency
        fr"OE\. {IT}, late {ETYM_02_END}$",
        fr"OE\. {IT}; {GRM} {IT} \(Kt\. {IT}\)\.$",
        fr"OE\. \({LANG}\) {IT_END}$",
        fr"OE\. \({LANG}\) {IT} from {ETYM_02_END}$",
        fr"OE\. \(late 11th c\.\) {IT_END}$",
        fr"OE\. \(late\) {IT_END}$",
        fr"OE\. \(late\) {IT} from {ETYM_02_END}$",
        fr"OE\. \(late\) {IT}, {GLOSS}\.$",
        fr"OE\. \(late\) {IT}, from {ETYM_02_END}$",
        fr"OE\. \(rare {LANG}\) {IT}; {ETYM_02_END}$",
        fr"OE\. \(WS\.\) {IT_END}$",
        fr"Origin of name doubtful; see {NED}$",
        fr"Perh\. distinct verbs; {ETYM_23_END}$",
        fr"Pp\. of {CAP_WORD}.$",
        fr"Prob\. {ETYM_02}, rel\. to {NEXT_PREC}$",
        fr"Prob\. from {NEXT_PREC}$",
        fr"Prob\. rel\. to {ETYM_02_END}$",
        fr"Prob\. related to {CAP_WORD}\.$",
        fr"Prob\. same as {ETYM_07}$",
        fr"Prob\. same as {NEXT_PREC}$",
        fr"Reduced form of {HEADREF_END}$",
        fr"Reduced form of {HEADREF}$",
        fr"Reduced unaccented form of {IT}; {SEE_HEADREF}\.$",
        fr"Reduction of {CAP_WORD}{SUP}, {QV}$",
        fr"Rel\. to {HEADREF}; {ETYM_001}$",
        fr"Related to {CAP_WORD} as {NEXT_PREC}$",
        fr"See {NED} {SV} {IT_END}$",
        fr"See {NED} {SVV} {ETYM_21_END}$",
        fr"See {NED} {SVV} {IT}, {GRM}{SUP}, {IT}.$",
        fr"See {NED}, {SV} {IT_END}$",  # inconsistent comma
        fr"See {NED}, {SV} {IT} \d+\.$",  # not quite sure what the last part means
        fr"See {NED}, {SV} {IT}, and {IT_END}$",
        fr"See {NED}$",
        fr"Shortened from {ETYM_02_END}$",
        fr"Shortened from {ETYM_02}; {SEE_HEADREF_END}$",
        fr"Shortened from {ETYM_20_END}$",
        fr"Shortened from {HEADREF_END}$",
        fr"Stem of {ETYM_01_END}$",
        fr"Stem of {ETYM_02_END}$",
        fr"Stem of {ETYM_02}, or {ETYM_02}; {SEE_HEADREF_END}$",
        fr"Stem of {HEADREF} \+ {ETYM_02_END}$",
        fr"Stem of {HEADREF} \+ {ETYM_02}; {ETYM_000}$",
        fr"Stem of {HEADREF} with {LANG} monophthongization\.$",
        fr"Stem of {LANG} {IT} \+ {IT}\.",
        fr"Stem of {LANG} {IT}, {GRM}, {LANG} {IT_END}$",
        fr"Stem of {NEXT_PREC}$",
        fr"Unaccented form of {ETYM_02}\. {CAP_SEE_HEADREF}\.$",
        fr"Unaccented reduction of {CAP_WORD}\.$",
        fr"Unknown; {ETYM_000}$",
        fr"Unknown\.$",


        fr"{ETYM_13}; {Q}with {IT}, {CF} rare {LANG} {IT_END}$",
        fr"{LANG} {IT}, {ETC}; {CF} {LANG} \(from {LANG}\) {IT_END}$",
        fr"{LANG} {IT}, {IT}, {ETC} accented stem of {IT_END}$",
        fr"Orig\. {IT}, {LANG} {IT}, {GRM}, \(as\) companions\.$",
        fr"Originally {IT} {GRM} and {IT} {GRMS}; {CF_HEADREF_END}$",
        fr"{CAP_SEE_HEADREF}; {CF} {LANG} and dial\. {IT}, {GLOSSES_END}$",

    ]
]


def check_etymology(etymology):
    for regex in regexes:
        if regex.match(etymology):
            return True
    return False
