import sqlite3


class Query_sql:
    def __init__(self):
        self.path = "Datas/Database/"
        self.conn = sqlite3.connect(self.path + "Bible.db")
        self.cursor = self.conn.cursor()

    def random_verse(self) -> object:
        verse = self.cursor.execute("SELECT * FROM Bibles ORDER BY RANDOM() LIMIT 1").fetchall()
        return verse

    def book(self, book):
        fetched_book = self.cursor.execute(f"SELECT * FROM Bibles WHERE Version = '{book}'").fetchall()
        return fetched_book
