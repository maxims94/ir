import random

class RulesCollection:
  def __init__(self, items):
    self.items = items

  def random(self, prob):
    for item in self.items:
      self.random_item(item, prob)
  
  def random_item(self, item, prob):
      rnd = random.uniform(0,1)
      if rnd <= prob:
        item.class_ = 1
      else:
        item.class_ = 0
