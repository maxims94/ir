import feedparser
import json
import dateutil.parser
import re

from item import Item

class RSS:

    @staticmethod
    def get_items_by_url(url):
        items = []
        print("Load data")
        url = url.strip()

        f = feedparser.parse(url)
        if len(f.entries) == 0:
            print("len null")
            return items

        print("Load data")
        print (f.entries)

        for item in f.entries:

            obj = Item()

            if 'title' in item:
                obj.title = item['title']

            if 'summary' in item:
                summary = item['summary']
                summary = re.sub('<[^<]+?>', '', summary)
                obj.summary = summary


            obj.source = url

            items.append(obj)

        return items
