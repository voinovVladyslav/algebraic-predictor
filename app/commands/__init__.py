from flask import Blueprint

from . import init_db


commands = Blueprint('commands', __name__, cli_group=None)
