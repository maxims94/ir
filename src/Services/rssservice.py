import feedparser
import re
import os
import dateutil.parser

from Model.item import create_tables, Item

"""Import Feeds and put them into the database """
def importFeeds():
  urls = ["http://www.faz.net/rss/aktuell/politik", "http://newsfeed.zeit.de/gesellschaft/index"]
  for url in urls:
    load_feed(url)

def load_feed(url):
  f = feedparser.parse(url)
  if len(f.entries) == 0:
    return
  for item in f.entries:
    new_item = Item(class_ = 0)
    if 'title' in item:
      new_item.title = item['title']

    if 'summary' in item:
      summary = item['summary']
      new_item.summary = re.sub('<[^<]+?>', '', summary)

    if 'published' in item:
      published = item['published']

      try:
          published = dateutil.parser.parse(published).timestamp()
      except:
          logging.warning("Unable to parse due to invalid 'published' value: '{}'".format(item))
          continue

      new_item.published = int(published)

    if 'links' in item:
      if 'href' in item['links'][0]:
          new_item.link = item['links'][0]['href']

    new_item.source = url
    new_item.save()
