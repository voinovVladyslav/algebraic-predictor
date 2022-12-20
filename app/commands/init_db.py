from app import mongo
from . import commands


@commands.cli.command('init')
def init_db():
    """
    command for creating basic collections
    when first started project
    """
    db = mongo.db
    print(f'Start initialize process for db: {db.name}')
    collections_list = db.list_collection_names()

    if 'users' in collections_list:
        print('Collection "users" already exists')
    else:
        db.create_collection('users')
        print('Create "users" collection')

    if 'projects' in collections_list:
        print('Collection "projects" already exists')
    else:
        db.create_collection('projects')
        print('Create "projects" collection')
    print('Finished db initialization')
