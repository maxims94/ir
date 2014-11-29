import os
import json

from item import Item

class Database:

    def __init__(self):
        self.__items = []
        self.read()

    def get_items(self):
        return self.__items

    def add(self, item):
        if not item in self.__items:
            self.__items.append(item)
        else:
            print("Duplicate discovered.")

    def read(self):
        if os.path.isfile('database'):
            with open('database', 'r') as f:
                # d = json.load(f)
                # for item in d:
                #     print(d)
                #     self.add(Item().from_json(d))
                print("article")
                articles = json.load(f)
                print(articles)
                for article in articles:
                    item = Item()
                    item.from_json(article)
                    self.add(item)

    def write(self):
        with open('database', 'w') as f:
            flatten = list(map((lambda x: x.flat()), db.get_items()))
            json.dump(flatten, f)
