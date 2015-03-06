import random

class RandomDataModel:
  def __init__(self):
    self.prob = 0
  def train(self,items):
    num = len(items)
    pos = 0
    for item in items:
      if item.class_ == 0:
        pos += 1
    self.prob = float(pos)/num
  def class_prob(self,item):
    return self.prob
  def class_(self,item):
    return random.random() <= self.prob
  def __str__(self):
    return "[Random Data Model (prob: %0.2f)]" % self.prob
