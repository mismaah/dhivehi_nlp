"""Create language models to predict future additions. Language models will give
probability based on selected ngram. An ngram is contiguous sequence of n tokens
from the given input text.

ދީފައިވާ ލިޔުމުގައިވާ ބަސްތަކަށް ބެލުމަށްފަހު ފަހުން މިލިޔުމަށް އައިސްދާނެ ބަސްތައް ލަފާކުރާނެ މޮޑެލްއެއް އުފެއްދުން 
"""

from dhivehi_nlp import tokenizer


def ngrams(text: str, n: int):
    """
    Returns a dictionary of the ngrams in the text along with their count.
    The ngram is based on the n value provided. If n = 1, the resulting dict
    will have unigrams. If n = 2, bigrams and so on.
    
    އެންގްރާމް ތަކުގެ ޑިކްށަނަރީއެއް އަނބުރާދޭނެއެވެ. މީގައި އެންގްރާމް ލިޔުމުން ފެނުނު އަދަދު ވެސް ހުންނާނެއެވެ
    
    >>> text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
    >>> ngrams(text, 2)
    [
        {"gram": ("ބުނެފައި", "އަދި"), "count": 2},
        {"gram": ("އަދި", "އިތުރު"), "count": 1},
        {"gram": ("އަދި", "އިތުރުކަމެއް"), "count": 1},
    ]
    """
    if n == 1:
        grams = tokenizer.word_tokenize(text, removePunctuation=True)
    else:
        sentences = tokenizer.sentence_tokenize(text)
        grams = []
        for sentence in sentences:
            tokens = tokenizer.word_tokenize(sentence, removePunctuation=True)
            grams_sentence = [
                tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)
            ]
            grams = grams + grams_sentence
    grams_counted = []
    for gram in set(grams):
        counted = {"gram": gram, "count": grams.count(gram)}
        grams_counted.append(counted)
    return grams_counted


def model(text: str, n: int):
    """
    Returns a dictionary of a word or phrase in the text and the probability
    of the of the word or phrase appearing in the text.
    The ngram is based on the n value provided. If n = 1, the resulting dict
    will have unigrams. If n = 2, bigrams and so on.

    ބަހެެއް ނުވަތަ ބަސްތަކެއް ލިޔުމުން ފެންނާނެ ކަމުގެ ޕްރޮބަބިލިޓީ ތަކުގެ ޑިކްށަނަރީއެއް އަނބުރާދޭނެއެވެ
    
    >>> text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
    >>> model(text, 3)
    [
        {"gram": ("ބުނެފައި", "އަދި", "އިތުރު"), "probability": 0.5},
        {"gram": ("ބުނެފައި", "އަދި", "އިތުރުކަމެއް"), "probability": 0.5},
    ]
    """
    probabilities = []
    if n == 1:
        grams = ngrams(text, 1)
        tokens = tokenizer.word_tokenize(text)
        for i in grams:
            probability = {"gram": i["gram"], "probability": i["count"] / len(tokens)}
            probabilities.append(probability)
    else:
        grams = ngrams(text, n)
        grams_minus = ngrams(text, n - 1)
        for gram in grams:
            if n == 2:
                gram_search = gram["gram"][0]
            else:
                gram_search = gram["gram"][: n - 1]
            for g in grams_minus:
                if g["gram"] == gram_search:
                    probability = {
                        "gram": gram["gram"],
                        "probability": gram["count"] / g["count"],
                    }
                    probabilities.append(probability)
    return probabilities
