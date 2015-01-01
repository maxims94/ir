class Item:

    def __init__(self):

        self.title = None
        self.summary = None
        self.published = 0
        self.source = None
        self.link = None
        self.class_ = 0

    def set_class(self, val):
        assert val == 0 or val == 1;
        self.class_ = val

    def get_class(self):
        return self.class_

    def get_link(self):
        return self.link

    def is_positive_class(self):
        if self.class_ :
            return int(self.class_) == 1
        else :
            return False

    def has_title(self):
        return self.title != None

    def flat(self):
        return {
            'title': self.title,
            'summary': self.summary,
            'published': self.published,
            'source': self.source,
            'link': self.link,
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

    def __repr__(self):
        return self.__str__()

    def from_json(d):
        obj = Item()

        obj.title = d['title']
        obj.summary = d['summary']
        obj.published = d['published']
        obj.source = d['source']
        obj.link = d['link']
        obj.class_ = d['class_']

        return obj
