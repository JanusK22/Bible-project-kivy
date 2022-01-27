import os
import sqlite3
import pandas as pd


class Importer:
    def __init__(self, file, version):
        self.file_name = os.path.splitext(file)[0]
        self.file_type = os.path.splitext(file)[1]
        self.connexion = sqlite3.connect("Datas/Database/Bible.db")
        self.version = version
        self.file = file

    def csv_importer(self):
        df = pd.read_csv(self.file, names=["Book", "Chapter", "Verse_number", "Verse"], sep="\t")
        df["Version"] = self.version
        df.to_sql('Bibles', self.connexion, if_exists='append', index=False)

    def import_to_db(self):
        if self.file_type == ".csv":
            self.csv_importer()
