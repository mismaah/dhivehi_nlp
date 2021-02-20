import unittest
from dhivehi_nlp import language_models


class test_language_models(unittest.TestCase):
    def test_ngrams_one_sentence(self):
        text = ".ބުނެފައި އަދި އިތުރު"
        self.assertCountEqual(
            language_models.ngrams(text, 2),
            [
                {"gram": ("ބުނެފައި", "އަދި"), "count": 1},
                {"gram": ("އަދި", "އިތުރު"), "count": 1},
            ],
        )

    def test_ngrams_multiple_sentences_0(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.ngrams(text, 2),
            [
                {"gram": ("ބުނެފައި", "އަދި"), "count": 2},
                {"gram": ("އަދި", "އިތުރު"), "count": 1},
                {"gram": ("އަދި", "އިތުރުކަމެއް"), "count": 1},
            ],
        )

    def test_ngrams_multiple_sentences_1(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.ngrams(text, 3),
            [
                {"gram": ("ބުނެފައި", "އަދި", "އިތުރު"), "count": 1},
                {"gram": ("ބުނެފައި", "އަދި", "އިތުރުކަމެއް"), "count": 1},
            ],
        )

    def test_ngrams_multiple_sentences_2(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.ngrams(text, 1),
            [
                {"gram": "ބުނެފައި", "count": 2},
                {"gram": "އަދި", "count": 2},
                {"gram": "އިތުރު", "count": 1},
                {"gram": "އިތުރުކަމެއް", "count": 1},
            ],
        )

    def test_model_unigram_prob(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.model(text, 1),
            [
                {"gram": "ބުނެފައި", "probability": 0.3333333333333333},
                {"gram": "އަދި", "probability": 0.3333333333333333},
                {"gram": "އިތުރު", "probability": 0.16666666666666666},
                {"gram": "އިތުރުކަމެއް", "probability": 0.16666666666666666},
            ],
        )

    def test_model_bigram_prob(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.model(text, 2),
            [
                {"gram": ("ބުނެފައި", "އަދި"), "probability": 1},
                {"gram": ("އަދި", "އިތުރު"), "probability": 0.5},
                {"gram": ("އަދި", "އިތުރުކަމެއް"), "probability": 0.5},
            ],
        )

    def test_model_trigram_prob(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertCountEqual(
            language_models.model(text, 3),
            [
                {"gram": ("ބުނެފައި", "އަދި", "އިތުރު"), "probability": 0.5},
                {"gram": ("ބުނެފައި", "އަދި", "އިތުރުކަމެއް"), "probability": 0.5},
            ],
        )


if __name__ == "__main__":
    unittest.main()
