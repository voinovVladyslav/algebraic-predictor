from flask import Blueprint


commands = Blueprint('commands', __name__, cli_group='db')


from . import init_db
from . import drop_db
from . import list_collections
