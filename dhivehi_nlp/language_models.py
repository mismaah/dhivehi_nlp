from dhivehi_nlp import tokenizer


def ngrams(text, n):
    sentences = tokenizer.sentence_tokenize(text)
    grams = []
    for sentence in sentences:
        tokens = tokenizer.word_tokenize(sentence)
        grams_sentence = [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
        grams = grams + grams_sentence
    return sorted(list(set(grams)))


def unigrams(text):
    return ngrams(text, 1)


def bigrams(text):
    return ngrams(text, 2)
