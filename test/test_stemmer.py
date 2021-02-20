import unittest
from dhivehi_nlp import stemmer


class test_stemmer(unittest.TestCase):
    def test_stemmer_one_word_0(self):
        self.assertEqual(stemmer.stem("ކަމެއްކަން"), "ކަމެއް")

    def test_stemmer_one_word_1(self):
        self.assertEqual(stemmer.stem("ކަމެއްކަމަކީ"), "ކަމެއް")

    def test_stemmer_one_word_2(self):
        self.assertEqual(stemmer.stem("ކަމެއްކަމުން"), "ކަމެއް")

    def test_stemmer_one_word_3(self):
        self.assertEqual(stemmer.stem("ބަހެއް"), "ބަސް")

    def test_stemmer_one_word_4(self):
        self.assertEqual(stemmer.stem("ގަހެއް"), "ގަސް")

    def test_stemmer_one_word_5(self):
        self.assertEqual(stemmer.stem("އެކައްޗެއް"), "އެކަތި")

    def test_stemmer_list_0(self):
        self.assertEqual(
            stemmer.stem(
                [
                    "ކަމެއްކަން",
                    "ކަމެއްކަމަކީ",
                    "ކަމެއްކަމުން",
                    "ބަހެއް",
                    "ގަހެއް",
                    "އެކައްޗެއް",
                ]
            ),
            ["ކަމެއް", "ކަމެއް", "ކަމެއް", "ބަސް", "ގަސް", "އެކަތި"],
        )

    def test_stemmer_list_1(self):
        self.assertEqual(
            stemmer.stem(
                "އައްޑޫ ސިޓީގެ ހިތަދޫ އެމްޑީޕީގެ ހަރުގެ ފުލުހުން ވަދެ ތަޅާލައިފިކަމަށް ކުރީގެ ރައީސް މުހައްމަދު ނަޝީދު ވިދާޅުވި ވިދާޅުވުން ފުލުހުން ދޮގުކޮށްފި އެވެ"
            ),
            [
                "އައްޑޫ",
                "ސިޓީ",
                "ހިތަދޫ",
                "އެމްޑީޕީ",
                "ހަރު",
                "ފުލުހުން",
                "ވަދެ",
                "ތަޅާލައިފި",
                "ކުރީ",
                "ރައީސް",
                "މުހައްމަދު",
                "ނަޝީދު",
                "ވިދާޅުވި",
                "ވިދާޅުވުން",
                "ފުލުހުން",
                "ދޮގުކޮށް",
                "އެވެ",
            ],
        )


if __name__ == "__main__":
    unittest.main()
