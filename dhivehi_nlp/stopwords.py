"""Remove stopwords from text and return the resulting tokens.

ލިޔުމުގައިވާ ބަސްތަކުގެ ތެރެއިން ލިޔުމުގެ މާނައަށް ބަދަލުނުގެންނަ ބަސްތައް ނެގުމަށްފަހު ބާކީހުރި ބަސްތައް އަނބުރާ ދިނުން
"""

from dhivehi_nlp import tokenizer, tagger


def get_stopwords():
    """
    Returns a list of stopwords.

    ސްޓޮޕްވާޑް ތަކުގެ ޑިކްށަނަރީއެއް އަނބުރާދޭނެއެވެ
    """
    return tagger.get_pos_list("އަކުރު") + [
        "ދަށުން",
        "ވަނަ",
        "ވަނީ",
        "މިވަނީ",
        "އެ",
        "މި",
        "އާއި",
        "ވެސް",
        "ކަމަށް",
        "ނަމަ",
        "ވާތީ",
        "ވުރެ",
        "ހުރި",
        "ހުންނެވި",
        "ކޮށް",
        "އިރު",
        "އެކު",
        "މީގެ",
        "ފަހު",
        "ފަހުން",
        "ފަހުގެ",
        "ކުރި",
        "ކުރިން",
        "ކުރީގެ",
        "އެގޮތުން",
        "ބެހޭ",
        "ވަރަށް",
        "ކަމުން",
        "ކަމުގައި",
    ]


def remove_stopwords(text: str):
    """
    Returns a list of tokens from the input text after removing the stopwords.

    ލިޔުމުގައިވާ ސްޓޮޕްވާޑް ނެގުމަށްފަހު ބާކީހުރި ބަސްތައް ލިސްޓެއް ގޮތަށް އަނބުރާދޭނެއެވެ
    
    >>> remove_stopwords("ބުނެފައި އަދި އިތުރު")
    ["ބުނެފައި", "އިތުރު"]
    """
    tokens = tokenizer.word_tokenize(text, removePunctuation=True)
    stopwords = get_stopwords()
    results = []
    for token in tokens:
        if token not in stopwords:
            results.append(token)
    return results
