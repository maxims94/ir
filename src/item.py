class Item:

    def __init__(self):

        self.title = None
        self.summary = None
        self.published = 0
        self.source = None
        self.class_ = None

    def is_classified(self):
        return self.class_ != None

    def set_class(self, val):
        self.class_ = val

    def get_class(self):
        return self.class_

    def is_positive_class(self):
        return int(self.class_) == 1

    def has_title(self):
        return self.title != None

    def flat(self):
        return {
            'title': self.title,
            'summary': self.summary,
            'published': self.published,
            'source': self.source,
            'class_': self.class_
        }


    def __eq__(self, other):
        return self.title == other.title and self.summary == other.summary and self.published == self.published

    def __ne__(self, other):
        return not __eq__(self, other)
    
    def __str__(self):

        if self.title == None:
            return "None"
        else:
            return self.title

    def from_json(self, d):
        print(d['title'])
        self.title = d['title']
        self.summary = d['summary']
        self.published = d['published']
        self.source = d['source']
        self.class_ = d['class_']
