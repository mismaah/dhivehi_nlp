import unittest
from dhivehi_nlp import tagger


class test_tagger(unittest.TestCase):
    def test_pos_0(self):
        self.assertEqual(
            tagger.parts_of_speech("ނުބައިކޮށް"),
            [("ނުބައިކޮށް", "ކަންއިތުރު")],
        )

    def test_pos_1(self):
        self.assertEqual(
            tagger.parts_of_speech("މަންނާނެ"),
            [("މަންނާނެ", "ކަން")],
        )

    def test_pos_2(self):
        self.assertEqual(
            tagger.parts_of_speech(
                "ބާރުވެރިކަމުގައި ހުރުމުން މީހުންނަށް އެކަން ބަލައިނުގަނެވުނީ ބާވައެވެ"
            ),
            [
                ("ބާރުވެރިކަމުގައި", "ނަން"),
                ("ހުރުމުން", "މަސްދަރު"),
                ("މީހުންނަށް", "ނަން"),
                ("އެކަން", "ނަންއިތުރުގެ ނަން"),
                ("ބަލައިނުގަނެވުނީ", "ކަން"),
                ("ބާވައެވެ", "ނަން"),
            ],
        )

    def test_pos_list(self):
        self.assertEqual(len(tagger.get_pos_list("އަކުރު")), 27)


if __name__ == "__main__":
    unittest.main()
