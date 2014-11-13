import os
import json

from item import Item

class Database:

    def __init__(self):
        self.__items = []

    def get_items(self):
        return self.__items

    def add(self, item):
        if not item in self.__items:
            self.__items.append(item)
        else:
            print("Duplicate discovered.")

    def read():
        db = Database()

        if os.path.isfile('database'):
            with open('database', 'r') as f:
                d = json.load(f)
                for item in d:
                    db.add(Item.from_json(item))

        return db

    def write(db):
        with open('database', 'w') as f:
            flatten = list(map((lambda x: x.flat()), db.get_items()))
            json.dump(flatten, f)
