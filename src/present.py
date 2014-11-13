class Present:
    def __init__(db):
        self.db = db

    def show(model=None):
        for item in db.get_items():
            if model:
                print(item)
            else:
                print(model.apply(item), "|", item)

