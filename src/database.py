import os

class Database:

    def __init__(self):
        self.__items = []

    def get_items(self):
        return self.items

    def add(self, item):
        if not item in self.__items:
            self.__items.append(item)

    def read():
        if os.path.isfile('database'):
            with open('database', 'r') as f:
                return json.load(f)
        else:
            return Database()

    def write(db):
        with open('database', 'w') as f:
            json.dump(db, f)
