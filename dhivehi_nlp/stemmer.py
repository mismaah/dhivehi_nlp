"""Remove suffixes from words to return their root form.

ބަހުގެ ފަހަތުގައި ވާ އަކުރުތައް ނެގުމަށްފަހު ބަހުގެ އަސްލުގޮތް އަނބުރާ ދިނުން
"""

import re
from dhivehi_nlp import tokenizer


def get_rules() -> "dict[str, str]":
    """
    Returns a dictionary of stemming rules.

    ބަހުގެ ފަހަތުގައި ވާ އަކުރުތައް ނެގުމަށްފަހު ބަހުގެ އަސްލުގޮތް ކަނޑައަޅާ ގަވައިދުތަކުގެ ޑިކްށަނަރީއެއް އަނބުރާދޭނެއެވެ
    """
    return {
        "ކަން": "",
        "ކަމަކީ": "",
        "ކަމުން": "",
        "ކަމެއް": "",
        "ކަމަށް": "",
        "ފި": "",
        "ގެ": "",
        "ތައް": "",
        "ތަކަށް": "",
        "ކޮށް": "",
        "ނާ": "",
        "ވައި": "",
        "ހަކަށް": "",
        "ތަކުގެ": "",
        "އެވެ": "",
        "އަށް": "",
        "އްޗެއް": "ތި",
        "ގަކީ": "ގު",
        "ހެއް": "ސް",
        "ދުމާ": "ދުން",
        "ހުމެއް": "ހުން",
        "ކަމެއް": "ކަން",
        "ސުން": "ސް",
        "ނުމުން": "ން",
        "ތުން": "ތް",
    }


def stem(text) -> list:
    """
    Returns a stemmed form of the given word(s).
    If the input is a string with a single word or a list with one element, the
    return value is a string. Otherwise a list is returned.

    ބަހުގެ ފަހަތުގައި ވާ އަކުރުތައް ނެގުމަށްފަހު ބަހުގެ އަސްލުގޮތް އަނބުރާ ދިނުން

    >>> stem("އެކައްޗެއް")
    "އެކަތި"
    >>> stem(["ކަމެއްކަން", "ކަމެއްކަމަކީ", "ކަމެއްކަމުން", "ބަހެއް", "ގަހެއް", "އެކައްޗެއް"])
    ["ކަމެއް", "ކަމެއް", "ކަމެއް", "ބަސް", "ގަސް", "އެކަތި"]
    """
    if isinstance(text, str):
        tokens = tokenizer.word_tokenize(text, removePunctuation=True)
    else:
        tokens = text
    patterns = re.compile("(" + "|".join(get_rules().keys()) + ")$")
    stems = []
    for i in tokens:
        stem = patterns.sub(lambda x: get_rules().get(x.group(), x.group()), i)
        if stem == "":
            continue
        stems.append(stem)
    if len(stems) == 1:
        stems = stems[0]
    return stems
