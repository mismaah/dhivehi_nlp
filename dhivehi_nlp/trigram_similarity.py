"""Trigram similarity divides words or phrases into sequences of three
consecutive letters, place in a set where the order doesn't matter and
duplicates are removed. Used to find string matches even if certain characters
are different, based on similarity value.

                                         ލިޔުނު އަކުރުތަކާ ނުވަތަ ބަސްތަކާއި އެއްގޮތް ބަސްތައް ހޯދުން
"""

import re
from dhivehi_nlp import dictionary


def generate_trigrams(text: str):
    """
    Return a set of trigrams in a given text.
    Preprocessing is done where each space is changed to two spaces. Also, two
    spaces to the beginning and one space to the end of the string are added.

                         ލިޔެފައިވާ ބަހުގެ ނުވަތަ ބަސްތަކުގެ ޓްރައިގްރާމްތައް ސެޓެއްގެ ގޮތުގައި އަނބުރާ ދޭނެއެވެ
    
    >>> generate_trigrams("ބަޔަކު")
    {
        "  ބ",
        " ބަ",
        "ބަޔ",
        "ަޔަ",
        "ޔަކ",
        "ަކު",
        "ކު ",
    }
    """
    text = text.strip()
    text = re.sub(" ", "  ", text)
    text = f"  {text} "
    return set([text[i : i + 3] for i in range(len(text) - 2)])


def _compare_trigrams(trig1: set, trig2: set):
    """
    Checks how many trigrams from the first set are present in the second and
    returns that value divided by the length of the second set.
    """
    count = 0
    for i in trig1:
        if i in trig2:
            count += 1
    return count / len(trig2)


def get_similarity(query: str, text=None, max_output=10):
    """
    Finds the trigram similarity of words compared to the query string and
    returns a list of similar words from the text list ordered according to 
    similarity in descending order.
    The text keyword argument should be a list of strings.
    If a list of words are not provided in the text keyword argument, the
    wordlist from the dictionary is used instead.
    The max_output keyword argument determines the size of the return list and
    is set to 10 by default if argument is not given.

                      ލިޔުނު ބަހާއި އެއްގޮތް ބަސްތައް އެއްގޮތްވާ ނިސްބަތުން ލިސްޓެއް ގޮތުގައި އަނބުރާ ދޭނެއެވެ
    
    >>> get_similarity("ބަޔަކު", max_output=5)
    [
        {"word": "ބަޔަކު", "similarity": 1.0},
        {"word": "ބަ", "similarity": 0.6666666666666666},
        {"word": "ބ", "similarity": 0.5},
        {"word": "ބަޔޭބަޔޭ", "similarity": 0.42857142857142855},
        {"word": "ބަޔާން", "similarity": 0.42857142857142855},
    ]

    >>> text = "ރަށްތައް އުފެދިފައިވާ ގޮތުން ވަކިވަކި ކުދިކުދި ރަށްރަށް ހުރި ކަމުގައި ވިޔަސް އެއްބަޔަކު އަނެއް ބަޔަކަށް ބަރޯސާވާ ކަމާއި ވަކި ދަތުރުފަތުރުކޮށް އެއްބައެއްގެ".split()
    >>> get_similarity("ބަޔަކު", text, max_output=3)
    [
        {"word": "ބަޔަކަށް", "similarity": 0.5555555555555556},
        {"word": "އެއްބަޔަކު", "similarity": 0.45454545454545453},
        {"word": "ބަރޯސާވާ", "similarity": 0.2222222222222222},
    ]
    """
    query_trig = generate_trigrams(query)
    if text == None:
        text = dictionary.get_wordlist()
    results = []
    for word in text:
        word_trig = generate_trigrams(word)
        results.append(
            {"word": word, "similarity": _compare_trigrams(query_trig, word_trig)}
        )
    results = sorted(results, key=lambda k: k["similarity"])[::-1]
    if len(results) > max_output:
        results = results[:max_output]
    return results
