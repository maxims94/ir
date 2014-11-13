from database import Database
from model import Model

class Present:
    def __init__(self,db):
        self.db = db

    def show(self, model=None):
        if model:

            eval_items = list(map((lambda x: (x, model.apply(x))), self.db.get_items()))
            eval_items = sorted(eval_items, reverse=True, key=(lambda x: x[1]))

            for x in eval_items:
                print(x[1], "|", x[0])

        else:
            for item in self.db.get_items():
                print(item)
