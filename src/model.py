import re
import json

from database import Database

class Model:
    def __init__(self, db):
        self.db = db
        self.rules = {}

    def generate(self):
        for item in self.db.get_items():
            if item.is_positive_class() and item.has_title():
                kw = Model.get_keywords(item.title)
                for k in kw:
                    if k in self.rules:
                        self.rules[k] += 1
                    else:
                        self.rules[k] = 1

    def apply(self, item):
        kw = Model.get_keywords(item.title)
        val = 0
        for k in kw:
            if k in self.rules:
                val += self.rules[k]
        return val

    def __repr__(self):
        return repr(self.rules)

    def get_keywords(s):
      kw = s.split(" ")
      kw = list(filter(lambda x: len(x)>3, map((lambda x: re.sub('[^a-zA-Zöäüß]', '', x.lower().strip())), kw)))
      return kw

    def write(model):
        with open('model', 'w') as f:
            json.dump(model.rules, f)

    def read(db):
        model = Model(db)
        with open('model', 'r') as f:
            model.rules = json.load(f)
        return model
