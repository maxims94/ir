import feedparser
import json
import dateutil.parser
import re


def loadData():
    db = []
    for url in open("src", "r"):
        print("Process:", url)
        url = url.strip()

        f = feedparser.parse(url)
        if len(f.entries) == 0:
            continue

        # print("Available columns:", f.entries[0].keys())
            
        for item in f.entries:
            title = "None"
            if 'title' in item:
                title = item['title']

            summary = "None"
            if 'summary' in item:
                summary = item['summary']
                summary = re.sub('<[^<]+?>', '', summary)

            published = "0"
            if 'published' in item:
                published = item['published']
                published = dateutil.parser.parse(published).timestamp()

            published = int(published)

            print("Item:", title)

            db.append({
                'title': title, 
                'summary': summary, 
                'published': published}
            )
            
    print("Save to 'database'")

    with open('database', 'w') as f:
        json.dump(db, f)