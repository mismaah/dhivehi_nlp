import sqlite3
import pkg_resources


def _db_connect():
    db_path = pkg_resources.resource_filename("dhivehi_nlp", "data/dhivehi_nlp.db")
    con = sqlite3.connect(db_path)
    return con