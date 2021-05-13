"""Get definitions definitions of Dhivehi words and the word list. Definitions
obtained from radheef.mv. 

ބަސްތަކުގެ ލިސްޓާއި ބަސްތަކުގެ މާނަ ހޯދުން
"""

from dhivehi_nlp._helpers import _db_connect


def get_definition(word: str) -> list:
    """Returns definitions of word as a list. Returns empty list if not found.

    ބަހުގެ މާނަ އަނބުރާ ދޭނެއެވެ

    >>> get_definition('ތަންވަޅު')
    ['1. ދަނޑިވަޅު.', '2. ފުރުޞަތު.', '3. ވަގުތު.']

    As seen in the above example where the, there are some problems when
    displaying dhivehi text in a list. It starts out correctly then switches to
    right to left orientation midway. This is only a display bug as when printed
    separately, the output is correct.

    >>> for i in dictionary.get_definition('ތަންވަޅު'):
    ...     print(i)
    1. ދަނޑިވަޅު.
    2. ފުރުޞަތު.
    3. ވަގުތު.
    """
    con = _db_connect()
    cursor = con.cursor()
    query = f"SELECT definition FROM radheef WHERE word='{word}'"
    cursor.execute(query)
    result = cursor.fetchone()
    con.close()
    if result is None:
        return []
    definitions = result[0].split("\n")
    return definitions


def get_wordlist() -> list:
    """Returns a list of all the Dhivehi words in the radheef (dictionary).

    ހުރިހާ ބަސްތަކެއްގެ ލިސްޓެއް އަނބުރާ ދޭނެއެވެ
    """
    con = _db_connect()
    cursor = con.cursor()
    query = "SELECT word FROM radheef"
    cursor.execute(query)
    words = [word[0] for word in cursor.fetchall()]
    return words
