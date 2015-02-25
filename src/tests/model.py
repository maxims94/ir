from peewee import CharField, BooleanField, DateField
from peewee import SqliteDatabase, Model

db = SqliteDatabase('items.db')

class BaseModel(Model):
    class Meta:
        database = db
        db.connect()

class Item(BaseModel):
    title = CharField(null = True)
    summary = CharField(null = True)
    published = DateField(null = True)
    source = CharField(null = True)
    link = CharField(null = True)
    class_ = BooleanField(null = True)

db.connect()

def reset_tables():
  if Item.table_exists():
      db.drop_tables([Item])
  db.create_tables([Item])
