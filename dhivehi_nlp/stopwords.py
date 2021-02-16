"""Remove stopwords from text and return the resulting tokens.
  ލިޔުމުގައިވާ ބަސްތަކުގެ ތެރެއިން ލިޔުމުގެ މާނައަށް ބަދަލުނުގެންނަ ބަސްތައް ނެގުމަށްފަހު ބާކީހުރި ބަސްތައް އަނބުރާދިނުން
"""

from dhivehi_nlp import tokenizer


def get_stopwords():
    """
    Returns a list of stopwords.
                                                    ސްޓޮޕްވާޑް ތަކުގެ ލިސްޓެއް އަނބުރާދޭނެއެވެ
    """
    return [
        "އަދި",
        "ދަށުން",
        "އެވެ",
        "ވަނަ",
        "ވަނީ",
        "މިވަނީ",
        "އެ",
        "މި",
        "އާއި",
        "އިން",
        "ވެސް",
        "ކަމަށް",
        "ނަމަ",
        "ވާތީ",
        "ވުރެ",
        "ހުރި",
        "ހުންނެވި",
        "ކޮށް",
        "އިރު",
        "ދެން",
        "ހަމަ",
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
        "އަށް",
        "ވަރަށް",
        "ކަމުން",
        "ކަމުގައި",
    ]


def remove_stopwords(text):
    """
    Returns a list of tokens from the input text after removing the stopwords.
                         ލިޔުމުގައިވާ ސްޓޮޕްވާޑް ނެގުމަށްފަހު ބާކީހުރި ބަސްތައް ލިސްޓެއް ގޮތަށް އަނބުރާދޭނެއެވެ
    """
    tokens = tokenizer.word_tokenize(text, removePunctuation=True)
    stopwords = get_stopwords()
    results = []
    for token in tokens:
        if token not in stopwords:
            results.append(token)
    return results
