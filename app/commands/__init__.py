from flask import Blueprint


commands = Blueprint('commands', __name__, cli_group=None)


from . import init_db
