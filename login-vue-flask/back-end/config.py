import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "secret-key"
    JWT_SECRET_KEY = "jwt-secret-key"
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    MONGODB_SETTINGS = {
        'db': 'vue_flask',
        'host': 'mongodb://cuong:1@localhost:27017/vue_flask?authSource=admin'
    }
