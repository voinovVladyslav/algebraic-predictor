
from app import mongo
from . import commands


@commands.cli.command('collections')
def list_collections():
    """
    list all existing collections
    """
    db = mongo.db
    collections = db.list_collection_names()
    if collections:
        print(f'Collections: {", ".join(collections)}')
    else:
        print('Database has 0 collections')
