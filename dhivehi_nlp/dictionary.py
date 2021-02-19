import sqlite3


def db_connect(db_path="./dhivehi_nlp/radheef.db"):
    con = sqlite3.connect(db_path)
    return con


def get_definition(word):
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
    con = db_connect()
    cursor = con.cursor()
    query = "SELECT word FROM radheef"
    cursor.execute(query)
    words = [word[0] for word in cursor.fetchall()]
    return words
