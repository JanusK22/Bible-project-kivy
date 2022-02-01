import sqlite3
from sqlite3 import Error

import yaml
from kivymd.uix.list import ThreeLineListItem, TwoLineListItem, OneLineListItem

from Tools.Query import Query_sql


class Creator:
    def __init__(self):
        self.path = "Datas/Database/"

    def create_database(self):
        try:
            sqlite3.connect(self.path + "Bible.db")
        except Error as e:
            print(e)


class Yaml_tools:
    def __init__(self, file):
        self.filepath = file
        self.file = yaml.safe_load(open('config.yml', 'r'))

    def replace(self, variable, new_value):
        base, pos = variable.split("/")[0], variable.split("/")[1]
        self.file[base][pos] = new_value
        yaml.dump(self.file, open(self.filepath, 'w'))

    def finder(self, path):
        base, pos = path.split("/")[0], path.split("/")[1]
        return self.file[base][pos]


class Read_book:
    def __init__(self, book):
        self.book_name = book
        self.book = Query_sql().book(self.book_name)

    def read_book(self):
        verse_list = []
        for row in self.book[:70]:
            if row[1] == 1 and row[2] == 1:
                print(row[1], row[2])
                verse_list.append(ThreeLineListItem(text=row[0].upper() + "\n", secondary_text="Chapter " + str(row[1]),
                                                    tertiary_text=str(row[2]) + " " + row[3]))
            elif row[1] != 1 and row[2] == 1:
                verse_list.append(TwoLineListItem(text="Chapter " + str(row[1]),
                                                  secondary_text=str(row[2]) + " " + row[3]))
            else:
                verse_list.append(OneLineListItem(text=str(row[2]) + " " + row[3]))

        return verse_list
