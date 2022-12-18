from app import mongo
from . import commands

@commands.cli.command('init_db')
def init_db():
    print(mongo.db.name)
    print(mongo.db.list_collection_names())
