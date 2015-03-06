import random
import re

class KeywordDataModel:
  def __init__(self):
    # self.kwprob_true[kw] is the probability that an item which contains the keyword kw is classified as "1"
    self.kwprob_true = {}
    # self.kwprob[kw] is the probability that an item contains the keyword kw
    self.kwprob = {}
  def get_keywords(s):
    kw = s.split(" ")
    kw = list(filter(lambda x: len(x)>3, map((lambda x: re.sub('[^a-zA-Zöäüß]', '', x.lower().strip())), kw)))
    return kw
  def train(self,items):
    num_items = len(items)
    all_kws = set()
    for item in items:
      for kw in KeywordDataModel.get_keywords(item.title):
        all_kws.add(kw)
    for kw in all_kws:
      total = 0
      pos = 0
      for item in items:
        if kw in KeywordDataModel.get_keywords(item.title):
          total += 1
          if item.class_:
            pos +=1
      self.kwprob_true[kw] = float(pos)/total
      self.kwprob[kw] = float(total)/num_items
  def class_prob(self,item):
    total_prob = float(0)
    for kw, prob in self.kwprob_true.items():
      if kw in KeywordDataModel.get_keywords(item.title):
        total_prob += prob * self.kwprob[kw]
    return total_prob
  def class_(self,item):
    return random.random() <= self.class_prob(item)
  def __str__(self):
    return "Keyword Data Model: %s" % self.kwprob_true
