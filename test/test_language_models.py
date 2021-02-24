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

    def test_news_model_0(self):
        text = "ވަނަ"
        result = [
            {"prediction": "އަހަރު", "probability": 0.18434617471513837},
            {"prediction": "ދުވަހު", "probability": 0.175122083559414},
            {"prediction": "އަހަރުގެ", "probability": 0.09603906673901248},
        ]
        self.assertEqual(language_models.news_model_predict(text, 3), result)

    def test_news_model_1(self):
        self.assertEqual(language_models.news_model_predict("އއައައައ"), None)

    def test_news_model_0(self):
        text = "ވަނީ"
        result = [
            {"prediction": "އެ", "probability": 0.05037284246753924},
            {"prediction": "ބުނެފަ", "probability": 0.03118318819419096},
            {"prediction": "މިދިޔަ", "probability": 0.018616050477134067},
            {"prediction": "ބުނެފައެވެ", "probability": 0.012097825520154351},
            {"prediction": "މި", "probability": 0.012045679720498513},
            {"prediction": "ވިދާޅުވެފަ", "probability": 0.01100276372738176},
            {"prediction": "ވަރަށް", "probability": 0.009803410335297491},
            {"prediction": "އޭނާގެ", "probability": 0.009281952338739114},
            {"prediction": "އޭނާ", "probability": 0.008812640141836576},
            {"prediction": "މިއަދު", "probability": 0.0087083485425249},
        ]
        self.assertEqual(language_models.news_model_predict(text), result)


if __name__ == "__main__":
    unittest.main()
