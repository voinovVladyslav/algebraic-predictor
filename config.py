import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/{db_name}".format(
        db_name=os.environ.get('MONGO_INITDB_NAME')
    )
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
