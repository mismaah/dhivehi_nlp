import unittest
from dhivehi_nlp import stopwords

class test_tokenizer(unittest.TestCase):
    def test_stopwords(self):
        self.assertEqual(stopwords.remove_stopwords("ބުނެފައި އަދި އިތުރު"), ["ބުނެފައި","އިތުރު"])

if __name__ == "__main__":
    unittest.main()