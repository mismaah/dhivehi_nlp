import unittest
from dhivehi_nlp import dictionary


class test_tokenizer(unittest.TestCase):
    def test_get_definion(self):
        self.assertEqual(dictionary.get_definition("ހަހަރުވެތުން"), "މ. ލޯބިކުރުން.")

    def test_get_definion_not_exist(self):
        self.assertIsNone(dictionary.get_definition("baa"))

    def test_get_wordlist(self):
        self.assertGreater(len(dictionary.get_wordlist()), 25000)


if __name__ == "__main__":
    unittest.main()
