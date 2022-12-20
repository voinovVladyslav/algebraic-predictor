from flask import Flask
from flask_pymongo import PyMongo
from config import config


mongo = PyMongo(authSource='admin')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongo.init_app(app)

    from .main import main as main_bp
    from .api import api as api_bp
    from .commands import commands as commands_bp
    from .models import models as models_bp
    from .utils import utils as utils_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(commands_bp)
    app.register_blueprint(models_bp)
    app.register_blueprint(utils_bp)

    return app
