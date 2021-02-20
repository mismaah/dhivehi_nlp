"""Get definitions definitions of Dhivehi words and the word list. Definitions
obtained from radheef.mv. 

                                                    ބަސްތަކުގެ ލިސްޓާއި ބަސްތަކުގެ މާނަ ހޯދުން
"""

import sqlite3


def db_connect(db_path="./store/dhivehi_nlp.db"):
    con = sqlite3.connect(db_path)
    return con


def get_definition(word):
    """Returns meaning of word.

                                                             ބަހުގެ މާނަ އަނބުރާ ދޭނެއެވެ
    """
    con = db_connect()
    cursor = con.cursor()
    query = f"SELECT definition FROM radheef WHERE word='{word}'"
    cursor.execute(query)
    definition = cursor.fetchone()
    con.close()
    if definition is None:
        return
    return definition[0]


def get_wordlist():
    """Returns a list of all the Dhivehi words in the radheef (dictionary).

                                                  ހުރިހާ ބަސްތަކެއްގެ ލިސްޓެއް އަނބުރާ ދޭނެއެވެ
    """
    con = db_connect()
    cursor = con.cursor()
    query = "SELECT word FROM radheef"
    cursor.execute(query)
    words = [word[0] for word in cursor.fetchall()]
    return words
