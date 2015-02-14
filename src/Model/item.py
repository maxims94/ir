from peewee import CharField, BooleanField, DateField

from Model.basemodel import BaseModel
from Model.basemodel import db

""" Model for items (single feed) """
class Item(BaseModel):
    title = CharField(null = True)
    summary = CharField(null = True)
    published = DateField(null = True)
    source = CharField(null = True)
    link = CharField(null = True)
    read = BooleanField(null = True)

def create_tables():
    db.connect()
    # Drop old Table for Testing purpose
    if Item.table_exists():
        db.drop_tables([Item])
    # Create new one
    db.create_tables([Item])
