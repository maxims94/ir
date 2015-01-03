import feedparser
import json
import dateutil.parser
import re
import logging

from src.item import Item

class RSS:

    def get_items_by_url(url):

        items = []

        url = url.strip()

        f = feedparser.parse(url)
        if len(f.entries) == 0:
            return items

        for item in f.entries:

            #logging.debug(item)

            obj = Item()

            if 'title' in item:
                obj.title = item['title']

            if 'summary' in item:
                summary = item['summary']
                summary = re.sub('<[^<]+?>', '', summary)
                obj.summary = summary

            if 'published' in item:
                published = item['published']

                try:
                    published = dateutil.parser.parse(published).timestamp()
                except:
                    logging.warning("Unable to parse due to invalid 'published' value: '{}'".format(item))
                    continue

                obj.published = int(published)

            if 'links' in item:
                if 'href' in item['links'][0]:
                    obj.link = item['links'][0]['href']

            #logging.debug(obj.link)

            obj.source = url

            items.append(obj)

        return items
