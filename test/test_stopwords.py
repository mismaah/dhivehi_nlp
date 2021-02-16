import unittest
from dhivehi_nlp import stopwords

class test_tokenizer(unittest.TestCase):
    def test_stopwords(self):
        self.assertEqual(stopwords.remove_stopwords("ބުނެފައި އަދި އިތުރު"), ["ބުނެފައި","އިތުރު"])
    def test_stopwords_2(self):
        self.assertEqual(stopwords.remove_stopwords("އިންޓެގްރިޓީ ކޮމިޝަންގެ މެމްބަރު ކަމަށް ބޭފުޅަކު ހޯދަނީ އެ ކޮމިޝަންގެ ރައީސް ކަމުގައި ހުންނެވި ޔޫސުފް މާނިއު މެމްބަރު ކަމުން، ރައީސް ވަކިކުރުމާ"), ["އިންޓެގްރިޓީ","ކޮމިޝަންގެ","މެމްބަރު","ބޭފުޅަކު","ހޯދަނީ","ކޮމިޝަންގެ","ރައީސް","ޔޫސުފް","މާނިއު","މެމްބަރު","ރައީސް","ވަކިކުރުމާ"])

if __name__ == "__main__":
    unittest.main()