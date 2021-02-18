import unittest
from dhivehi_nlp import language_models


class test_tokenizer(unittest.TestCase):
    def test_ngrams_one_sentence(self):
        text = ".ބުނެފައި އަދި އިތުރު"
        self.assertEqual(
            language_models.ngrams(text, 2), [("ބުނެފައި", "އަދި"), ("އަދި", "އިތުރު")]
        )

    def test_ngrams_multiple_sentences_0(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertEqual(
            language_models.ngrams(text, 2),
            [("ބުނެފައި", "އަދި"), ("އަދި", "އިތުރު"), ("އަދި", "އިތުރުކަމެއް")],
        )

    def test_ngrams_multiple_sentences_1(self):
        text = "ބުނެފައި އަދި އިތުރު. ބުނެފައި އަދި އިތުރުކަމެއް"
        self.assertEqual(
            language_models.ngrams(text, 3),
            [("ބުނެފައި", "އަދި", "އިތުރު"), ("ބުނެފައި", "އަދި", "އިތުރުކަމެއް")],
        )


if __name__ == "__main__":
    unittest.main()
