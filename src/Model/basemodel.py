from peewee import SqliteDatabase, Model

db = SqliteDatabase('items.db')

"""This is the Base class for all Models
   It's main purpose is to define a single database
"""
class BaseModel(Model):
    class Meta:
        database = db
        db.connect()