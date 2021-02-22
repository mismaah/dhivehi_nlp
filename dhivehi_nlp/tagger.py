"""Tag words in text according to specified rules or patterns. For example,
tagging words based on which part of speech it belongs to.

ބަހުގެ ގަވައިދަށް ބެލުމަށްފަހު އެންމެ އކަށީގެންވާ ޓެގެއް ކަނޑައެޅުން
"""

import re
import sqlite3
from dhivehi_nlp import tokenizer


def _db_connect(db_path="./store/dhivehi_nlp.db"):
    con = sqlite3.connect(db_path)
    return con


def _get_tag(word: str) -> str:
    con = _db_connect()
    cursor = con.cursor()
    query = f"SELECT part_of_speech FROM pos WHERE word='{word}'"
    cursor.execute(query)
    tag = cursor.fetchone()
    con.close()
    return tag


def _pos_rules():
    return [
        {"pos": "މަސްދަރު", "rules": ["ުން"]},
        {"pos": "ނަންއިތުރު", "rules": ["ތެރި"]},
        {"pos": "ނަންއިތުރުގެ ނަން", "rules": ["ކަން"]},
        {"pos": "ކަންއިތުރު", "rules": ["ހަށް", "ރަށް", "ކޮށް"]},
        {"pos": "ކަން", "rules": ["އްޖެ", "ނީ", "ާނެ", "ކޮށްފަ"]},
        # {"pos": "އިތުރު", "rules": []},
        # {"pos": "އަކުރު", "rules": []},
    ]


def _match_rules(token: str, rules: list) -> str:
    for i in rules:
        patterns = re.compile("(" + "|".join(i["rules"]) + ")$")
        if patterns.search(token):
            return i["pos"]
    return "ނަން"


def parts_of_speech(text: str):
    """
    Tag words according to which part of speech they belong to. Initially they
    are checked against a database of predefined words and tags. If not found in
    the database, the tags are determined based on the patterns in the word.
    If even this doesn't manage to tag the word, the default 'ނަން' tag is given
    as it is the most common tag (almost equivalent to NN in english).

    ބަހުގެ ބައިތަށް ކަމަށްވާ ނަން، ކަން، ނަންއިތުރު، ކަންއިތުރު، މަސްދަރު، ނަންއިތުރުގެ ނަން، އިތުރު އަދި
    އަކުރުންކުރެ އެންމެ އެކަށީގެންވާ ބައި އެބަހަކާ ޓެގު ކުރުން

    >>> parts_of_speech("ނުބައިކޮށް")
    [("ނުބައިކޮށް", "ކަންއިތުރު")]

    >>> parts_of_speech("ބާރުވެރިކަމުގައި ހުރުމުން މީހުންނަށް އެކަން ބަލައިނުގަނެވުނީ ބާވައެވެ")
    [
        ("ބާރުވެރިކަމުގައި", "ނަން"),
        ("ހުރުމުން", "މަސްދަރު"),
        ("މީހުންނަށް", "ނަން"),
        ("އެކަން", "ނަންއިތުރުގެ ނަން"),
        ("ބަލައިނުގަނެވުނީ", "ކަން"),
        ("ބާވައެވެ", "ނަން"),
    ]
    """
    tokens = tokenizer.word_tokenize(text, removePunctuation=True)
    tagged = []
    for token in tokens:
        tag = _get_tag(token)
        if not tag:
            tagged.append((token, _match_rules(token, _pos_rules())))
        else:
            tagged.append((token, tag[0]))
    return tagged
