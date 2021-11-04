""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict


_punctuation = ',.'
phoneme = ["ieeu", "ieeus", "ieeuf", "ieeur", "ieeux", "ieeuj", "oai", "oais", "oaif", "oair", "oaix", "oaij", "oay", "oays", "oayf", "oayr", "oayx", "oayj", "uaay", "uaays", "uaayf", "uaayr", "uaayx", "uaayj", "uooi", "uoois", "uooif", "uooir", "uooix", "uooij", "wowi", "wowis", "wowif", "wowir", "wowix", "wowij", "wowu", "wowus", "wowuf", "wowur", "wowux", "wowuj", "uya", "uyas", "uyaf", "uyar", "uyax", "uyaj", "uyee", "uyees", "uyeef", "uyeer", "uyeex", "uyeej", "ai", "ais", "aif", "aix", "aij", "ay", "ays", "ayf", "ayr", "ayx", "ayj", "aay", "aays", "aayf", "aayr", "aayx", "aayj", "ao", "aos", "aof", "aor", "aox", "aoj", "au", "aus", "auf", "aur", "aux", "auj", "aau", "aaus", "aauf", "aaur", "aaux", "aauj", "eo", "eos", "eof", "eor", "eox", "eoj", "eeu", "eeus", "eeuf", "eeur", "eeux", "eeuj", "ia", "ias", "iaf", "iar", "iax", "iaj", "iu", "ius", "iuf", "iur", "iux", "iuj", "iee", "iees", "ieef", "ieer", "ieex", "ieej", "oa", "oas", "oas", "oaf", "oaf", "oar", "oar", "oax", "oax", "oaj", "oaj", "oaw", "oaws", "oawf", "oawr", "oawx", "oawj", "oe", "oes", "oef", "oer", "oex", "oej", "oi", "ois", "oif", "oir", "oix", "oij", "ooi", "oois", "ooif", "ooir", "ooix", "ooij", "owi", "owis", "owif", "owir", "owix", "owij", "ua", "uas", "uaf", "uar", "uax", "uaj", "uaa", "uaas", "uaaf", "uaar", "uaax", "uaaj", "uee", "uees", "ueef", "ueer", "ueex", "ueej", "ui", "uis", "uif", "uir", "uix","uij", "uy", "uys", "uyf", "uyr", "uyx", "uyj", "uoo", "uoos", "uoof", "uoor", "uoox", "uooj", "wa", "was", "waf", "war", "wax", "waj", "wi", "wis", "wif", "wir", "wix", "wij", "wow", "wows", "wowf", "wowr", "wowx", "wowj", "wu", "wus", "wuf", "wur", "wux", "wuj", "a", "as", "af", "ar", "ax", "aj", "aa", "aas", "aaaf", "aar", "aax", "aaj", "aw", "aws", "awf", "awr", "awx", "awj", "e", "es", "ef", "er", "ex", "ej", "ee", "ees", "eef", "eer", "eex", "eej", "i", "is", "if", "ir", "ix", "ij", "o", "os", "of", "or", "ox", "oj", "oo", "oos", "oof", "oor", "oox", "ooj", "ow", "ows", "owf", "owr", "owx", "owj", "u", "us", "uf", "ur", "ux", "uj", "w", "ws", "wf", "wr", "wx", "wj", "ng", "ph", "th", "nh", "kh", "tr", "ch", "qw", "z","d", "g", "b", "c", "h", "l", "m", "n", "p", "s", "t", "v"]

symbols = list(_punctuation) + phoneme  
