from app import mongo
from . import commands


@commands.cli.command('drop')
def drop_db():
    """
    remove all collections from database
    """
    db = mongo.db
    collections_list = db.list_collection_names()
    if not collections_list:
        print('Database has 0 collections')
        return

    for collection_name in collections_list:
        print(f'Dropped {collection_name}')
        db.drop_collection(collection_name)
    print('Successfully deleted all collections')
