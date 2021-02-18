from dhivehi_nlp import tokenizer


def ngrams(text, n):
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


def unigrams(text):
    return ngrams(text, 1)


def bigrams(text):
    return ngrams(text, 2)


def model(text, n):
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
