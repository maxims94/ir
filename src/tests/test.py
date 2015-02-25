#!/bin/python3

import sys
import os
sys.path.insert(1, os.path.dirname(sys.path[0]))
import model
import random
from Services import rssservice

def create():
  print("Create test database.")
  model.reset_tables()
  urls = ["http://www.faz.net/rss/aktuell/politik", "http://newsfeed.zeit.de/gesellschaft/index"]
  for url in urls:
    print("Load: %s" % (url))
    rssservice.load_feed(url)
  print("Added %d entries" % (model.Item.select().count()))

def rules():
  print("Apply rules to database")
  items = model.Item.select(); 
  class_rules = [{}]
  for rule in class_rules:
    apply_rule(rule, items)
  for item in items:
    print("%s | %s" % (str(item.class_), item.title))
    item.save()

def apply_rule(rule, items):
  for item in items:
    item.class_ = random.randint(0,1)

def show():
  print("Show database")
  items = model.Item.select(); 
  for item in items:
    print("%s | %s" % (str(item.class_), item.title))

if __name__ == '__main__':
  arg = sys.argv[1]
  func = {
    "create" : create,
    "rules" : rules,
    "show" : show
  }
  func[arg]()