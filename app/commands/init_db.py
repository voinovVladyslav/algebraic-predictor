import logging

from app import mongo
from . import commands


@commands.cli.command('init_db')
def init_db():
    """
    command for creating basic collections
    when first started project
    """
    db = mongo.db
    logging.info(
        'Start initialize process for db: %s',
        db.name
    )
    collections_list = db.list_collection_names()

    if 'users' in collections_list:
        logging.warning('Collection "users" already exists')
    else:
        db.create_collection('users')
        logging.info('Create "users" collection')

    if 'projects' in collections_list:
        logging.warning('Collection "projects" already exists')
    else:
        db.create_collection('projects')
        logging.info('Create "projects" collection')

    logging.info(
        'Finished db initialization'
    )
