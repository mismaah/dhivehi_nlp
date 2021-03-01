"""Collections of various Dhivehi texts.

    އެކި ބާވަތުގެ ދިވެހި ލިޔުންތައް
"""

import sqlite3
import pkg_resources


def _db_connect():
    db_path = pkg_resources.resource_filename("dhivehi_nlp", "data/dhivehi_nlp.db")
    con = sqlite3.connect(db_path)
    return con


def _db_read(name: str) -> str:
    con = _db_connect()
    cursor = con.cursor()
    query = f"SELECT content FROM corpus WHERE name='{name}'"
    cursor.execute(query)
    content = cursor.fetchone()
    con.close()
    return content[0]


def news():
    """News article from sun.mv https://sun.mv/145845

    ސަން އެމްވީގެ ނޫސް ހަބަރެއް
    """
    return _db_read("news")


def story():
    """Rehendhi short story by Aishath Afra https://vaahaka.com/story/9604/

    އައިޝަތު އަފްރާގެ ކުރުވާހަކަ ރެހެނދި
    """
    return _db_read("story")


def tweet():
    """Tweet by @FSaaira https://twitter.com/FSaaira/status/1334579523006812160

    ފާތުމަތު ސާއިރާގެ ޓްވީޓެއް
    """
    return _db_read("tweet")


def lyrics():
    """Lyrics of Hingaa Hoadhama Hey by Hussain Ali

    ހުސެން އަލީގެ ހިނގާ ހޯދަމާހޭ ލަވައިގެ ޅެން
    """
    return _db_read("lyrics")


def textbook():
    """Excerpt from Dhivehi 3 (Sh) teachers book
    https://www.moe.gov.mv/en/category/view/31

    ދިވެހި 3 (ށ) މުދައްރިސުންގެ ފޮތުން ތަންކޮޅެއް
    """
    return _db_read("textbook")
