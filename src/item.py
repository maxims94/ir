class Item:

    def __init__(self):

        self.title = None
        self.summary = None
        self.published = 0
        self.source = None
        self.class_ = None

    def is_classified(self):
        self.class_ != None

    def set_class(self, val):
        self.class_ = val

    def get_class(self, val):
        return self.class_

    def has_title(self):
        return self.title != None

    def __eq__(self, other):
        return self.title == other.title and self.summary == other.summary and self.published == self.published

    def __ne__(self, other):
        return not __eq__(self, other)
    
    def __str__(self):

        if self.title == None:
            return "None"
        else:
            return self.title
