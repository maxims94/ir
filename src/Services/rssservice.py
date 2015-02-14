import feedparser
import re
import os

from Model.item import create_tables, Item

"""Import Feeds and put them into the database """
def importFeeds():

    # Construct File path to config relative to this file
    # This allows us to start the script from any directory
    pathToConfigFile = os.path.join(os.path.dirname(__file__), '../../config/src.txt')

    for url in open(pathToConfigFile, "r"):
        print("Process:", url)
        url = url.strip()

        f = feedparser.parse(url)
        if len(f.entries) == 0:
            continue
        for item in f.entries:
            new_item = Item(read = False)
            if 'title' in item:
                new_item.title = item['title']

            if 'summary' in item:
                summary = item['summary']
                new_item.summary = re.sub('<[^<]+?>', '', summary)

            if 'published' in item:
                new_item.published = item['published']
            new_item.save()