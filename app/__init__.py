from flask import Flask
from flask_pymongo import PyMongo
from config import config


mongo = PyMongo(authSource='admin')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongo.init_app(app)

    from .main import main as main_blueprint
    from .api import api as api_blueprint
    from .commands import commands as commands_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(commands_blueprint)

    return app
