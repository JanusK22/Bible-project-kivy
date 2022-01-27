import sqlite3
from sqlite3 import Error

import yaml


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
