# dhivehi_nlp

Natural language processing tools for the Dhivehi language.

### Installation

```
pip install dhivehi_nlp
```

### Modules

Tokenizer - Tokenize text into separate sentences or words (tokens).

Stopwords - Remove stopwords from text and return the resulting tokens.

Stemmer - Remove suffixes from words to return their root form.

Language Models - Create language models to predict future additions. Language
models will give probability based on selected ngram. An ngram is a contiguous
sequence of n tokens from the given input text. Use previously built models to
predict future words.

Dictionary - Get definitions of Dhivehi words and the word list. Definitions
obtained from radheef.mv. 

Corpus - Collections of various Dhivehi texts.

Trigram Similarity - Divides words or phrases into sequences of three
consecutive letters, placed in a set where the order doesn't matter and
duplicates are removed. Used to find string matches even if certain characters
are different or out of order, based on similarity value.

Tagger - Tag words in text according to specified rules or patterns. For
example, tagging words based on which part of speech it belongs to.
