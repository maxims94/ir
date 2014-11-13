import feedparser
import json
import dateutil.parser
import re

class RSS:

    def get_items_by_url(url):

        items = []

        url = url.strip()

        f = feedparser.parse(url)
        if len(f.entries) == 0:
            return items

        for item in f.entries:

            obj = Item()

            if 'title' in item:
                obj.title = item['title']

            if 'summary' in item:
                summary = item['summary']
                summary = re.sub('<[^<]+?>', '', summary)
                obj.summary = summary

            if 'published' in item:
                published = item['published']
                published = dateutil.parser.parse(published).timestamp()
                obj.published = int(published)

            obj.source = url

            items.append(obj)

        return items
