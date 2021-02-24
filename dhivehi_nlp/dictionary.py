"""Get definitions definitions of Dhivehi words and the word list. Definitions
obtained from radheef.mv. 

ބަސްތަކުގެ ލިސްޓާއި ބަސްތަކުގެ މާނަ ހޯދުން
"""

import sqlite3
import pkg_resources


def _db_connect():
    db_path = pkg_resources.resource_filename("dhivehi_nlp", "data/dhivehi_nlp.db")
    con = sqlite3.connect(db_path)
    return con


def get_definition(word: str) -> str:
    """Returns meaning of word.

    ބަހުގެ މާނަ އަނބުރާ ދޭނެއެވެ
    
    >>> get_definition('ތަންވަޅު')
    'ނ. 1 ދަނޑިވަޅު. 2 ފުރުޞަތު. 3 ވަގުތު.'
    """
    con = _db_connect()
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
    con = _db_connect()
    cursor = con.cursor()
    query = "SELECT word FROM radheef"
    cursor.execute(query)
    words = [word[0] for word in cursor.fetchall()]
    return words
