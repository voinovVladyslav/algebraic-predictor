import getpass

from . import commands
from app.models import User


@commands.cli.command('createadmin')
def create_admin():
    username = getpass.getuser()
    username = input(f'Username (leave blank for "{username}"):') or username
    user = User().get_user()
    if user:
        print('User already exists')
        return
    password = getpass.getpass()
    User().create_admin(username, password)
