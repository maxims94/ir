import json
import os.path
import sys
import random
import irlib

def write_db(db):
    with open('database', 'w') as f:
        json.dump(db, f)

def calc_item_value(item, rules):
    kw = irlib.get_keywords(item['title'])
    val = 0
    for k in kw:
        if k in rules:
            val += rules[k]
    return val

class UserInterface(object): 
    def __init__(self):
        with open('database', 'r') as f:
            self.db = json.load(f)

        self.rules = None

        if os.path.isfile("rules"):
            with open('rules', 'r') as f:
                self.rules = json.load(f)

        self.sdb = []
        if self.rules == None:
            self.sdb = sorted(self.db, reverse=True, key=lambda item: item['published'])
        else:
            for e in self.db:
                e['value'] = calc_item_value(e, self.rules)
                self.sdb.append(e)
            self.sdb = sorted(self.sdb, reverse=True, key=lambda item: item['value'])
    def show(self):
        for item in self.sdb:
            if self.rules == None:
                print(item['title'])
            else:
                print(item['value'], "|", item['title'])
    def process(self):
        for item in self.sdb:
            if 'class' in item:
                continue

            print(">>>",item['title'])
            print(item['summary'][:300])
            choice = input("Does this item contain useful information (Y/N)?: ").lower()
            if choice == "y":
                print("Mark as useful.")
                item['class'] = 1
                write_db(self.sdb)

            elif choice == "n":
                print("Mark as useless.")
                item['class'] = 0
                write_db(self.sdb)

            elif choice == "c":
                print("Cancel.")
            else:
                print("Skip item")