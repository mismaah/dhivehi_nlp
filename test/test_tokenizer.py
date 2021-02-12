import unittest
from dhivehi_nlp import tokenizer

class test_tokenizer(unittest.TestCase):
    def test_sentence_tokenizer(self):
        self.assertEqual(tokenizer.sentence_tokenize("މާފަ ބުނެފަ އެވެ. އިތުރު ހާމައެއް ނުކުރެ އެވެ."), ["މާފަ ބުނެފަ އެވެ", "އިތުރު ހާމައެއް ނުކުރެ އެވެ"])

    def test_word_tokenizer_one_sentence(self):
        self.assertEqual(tokenizer.word_tokenize("އިތުރު ހާމައެއް ނުކުރެ އެވެ"), ["އިތުރު", "ހާމައެއް", "ނުކުރެ", "އެވެ"])

    def test_word_tokenizer_multiple_sentence(self):
        self.assertEqual(tokenizer.word_tokenize("މާފަ ބުނެފަ އެވެ. އިތުރު ހާމައެއް ނުކުރެ އެވެ."), ["މާފަ", "ބުނެފަ", "އެވެ", "އިތުރު", "ހާމައެއް", "ނުކުރެ" ,"އެވެ"])

    def test_removeNonDhivehiNumeric(self):
        self.assertEqual(tokenizer.word_tokenize("އިތުlރު ހާމައެއް test 112 ނުކުރެ? އެވެ", removeNonDhivehiNumeric=True), ["އިތުރު", "ހާމައެއް","112", "ނުކުރެ", "އެވެ"])
    
    def test_removePunctuation(self):
        self.assertEqual(tokenizer.word_tokenize("މާފަ ބުނެފަ އެވެ. އިތުރު 112 ހާމައެއް، ނުކުރެ؟? އެވެ.", removePunctuation=True), ["މާފަ", "ބުނެފަ", "އެވެ", "އިތުރު","112", "ހާމައެއް", "ނުކުރެ" ,"އެވެ"])

if __name__ == "__main__":
    unittest.main()
