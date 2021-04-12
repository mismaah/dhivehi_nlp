"""Tokenize text into separate sentences or words (tokens).

ލިޔުމުގައިވާ ޖުމުލަތަކަށް ނުވަތަ ބަސްތަކަށް އެ ލިޔުން ވަކިކުރުން
"""

import re


def sentence_tokenize(text: str) -> list:
    """
    Returns a list where the text is split into separate sentences with
    preceding and succeeding whitespaces removed.

    ލިޔުމުގައިވާ ޖުމުލަތަކަށް ލިޔުން ވަކިކޮށް އަދި ފެށޭއިރާއި ނިމޭއިރު ހުންނަ ހުސްތަން ނެގުމަށްފަހު ލިސްޓެއް
    އަނބުރާދޭނެއެވެ

    >>> sentence_tokenize("ބުނެފަ އެވެ. އިތުރަށް ހާމައެއް ނުކުރެ އެވެ")
    ["ބުނެފަ އެވެ", "އިތުރަށް ހާމައެއް ނުކުރެ އެވެ"]
    """
    sentences = text.split(".")
    sentences = [i.strip() for i in sentences if i]
    return sentences


def word_tokenize(
    text: str, removePunctuation=False, removeNonDhivehiNumeric=False
) -> list:
    """
    Returns a list where the text is split into separate words (tokens). If the
    text contains multiple sentences, they are run through the
    sentence_tokenize() function first.
    Keyword argument removePunctuation can be passed to remove punctuation
    characters from the resulting tokens.
    Keyword argument removeNonDhivehiNumeric can be passed to remove characters
    other than thaana (unicode range 0780 to 07B1) and numbers (0-9).

    ލިޔުމުގައިވާ ބަސްތަކަށް ލިޔުން ވަކިކޮށް ލިސްޓެއް އަނބުރާދޭނެއެވެ

    >>> word_tokenize("ބުނެފަ އެވެ. އިތުރަށް ހާމައެއް ނުކުރެ އެވެ")
    ["ބުނެފަ", "އެވެ", "އިތުރަށް", "ހާމައެއް", "ނުކުރެ", "އެވެ"],

    >>> word_tokenize("އިތުlރު ހާމައެއް test 112 ނުކުރެ? އެވެ", removeNonDhivehiNumeric=True)
    ["އިތުރު", "ހާމައެއް", "112", "ނުކުރެ", "އެވެ"]

    >>> tokenizer.word_tokenize("މާފަ ބުނެފަ އެވެ. އިތުރު 112 ހާމައެއް، ނުކުރެ؟? އެވެ.", removePunctuation=True)
    ["މާފަ", "ބުނެފަ", "އެވެ", "އިތުރު", "112", "ހާމައެއް", "ނުކުރެ", "އެވެ"]
    """
    sentences = sentence_tokenize(text)
    tokens = []
    for sentence in sentences:
        for token in sentence.split():
            if removeNonDhivehiNumeric:
                token = re.sub(r"[^\u0780-\u07B10-9]+", "", token)
            if not removeNonDhivehiNumeric and removePunctuation:
                token = re.sub(r"[.(),\'\"?؟:;،]+", "", token)
            if token == "":
                continue
            tokens.append(token)
    return tokens
