import re

class Model:
    def __init__(self, db):
        self.db = db

    def generate(self):

        self.rules = {}

        for item in self.db.get_items():
            if item.get_class() == 1 and item.has_title():
                kw = Model.get_keywords(item.title)
                for k in kw:
                    if k in rules:
                        rules[k] += 1
                    else:
                        rules[k] = 1

    def apply(self, item):
        pass

    def get_keywords(s):
      kw = s.split(" ")
      kw = list(filter(lambda x: len(x)>3, map((lambda x: re.sub('[^a-zA-Zöäüß]', '', x.lower().strip())), kw)))
      return kw
