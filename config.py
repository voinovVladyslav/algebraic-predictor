import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    MONGO_URI = os.environ.get('MONGODB_CONNSTRING')
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
