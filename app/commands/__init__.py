from flask import Blueprint


commands = Blueprint('commands', __name__, cli_group='db')


from . import (
    init_db,
    drop_db,
    list_collections,
    create_admin,
)
