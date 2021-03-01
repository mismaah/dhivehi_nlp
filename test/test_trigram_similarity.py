import unittest
from dhivehi_nlp import trigram_similarity


class test_trigram_similarity(unittest.TestCase):
    def test_generate_trigram(self):
        result = {
            "  ބ",
            " ބަ",
            "ބަޔ",
            "ަޔަ",
            "ޔަކ",
            "ަކު",
            "ކު ",
        }
        self.assertEqual(trigram_similarity.generate_trigrams("ބަޔަކު"), result)

    def test_similarity(self):
        text = "ރަށްތައް އުފެދިފައިވާ ގޮތުން ވަކިވަކި ކުދިކުދި ރަށްރަށް ހުރި ކަމުގައި ވިޔަސް އެއްބަޔަކު އަނެއް ބަޔަކަށް ބަރޯސާވާ ކަމާއި ވަކި ދަތުރުފަތުރުކޮށް އެއްބައެއްގެ"
        result = [
            {"word": "ބަޔަކަށް", "similarity": 0.5555555555555556},
            {"word": "އެއްބަޔަކު", "similarity": 0.45454545454545453},
            {"word": "ބަރޯސާވާ", "similarity": 0.2222222222222222},
        ]
        self.assertEqual(
            trigram_similarity.get_similarity("ބަޔަކު", text, max_output=3), result
        )

    def test_similarity_dict_0(self):
        result = [
            {"word": "ބަޔަކު", "similarity": 1.0},
            {"word": "ބަ", "similarity": 0.6666666666666666},
            {"word": "ބ", "similarity": 0.5},
            {"word": "ބަޔޭބަޔޭ", "similarity": 0.42857142857142855},
            {"word": "ބަޔާން", "similarity": 0.42857142857142855},
        ]
        self.assertEqual(
            trigram_similarity.get_similarity("ބަޔަކު", max_output=5), result
        )

    def test_similarity_dict_1(self):
        result = [
            {"word": "ހަރު", "similarity": 1.0},
            {"word": "ހަހަރު", "similarity": 0.7142857142857143},
            {"word": "ހަ", "similarity": 0.6666666666666666},
        ]
        self.assertEqual(
            trigram_similarity.get_similarity("ހަރު", max_output=3), result
        )


if __name__ == "__main__":
    unittest.main()
