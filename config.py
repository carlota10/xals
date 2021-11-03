import os
from datetime import timedelta


class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False

    API_PAGINATION = 100

    PROPAGATE_EXCEPTIONS = True  # needed due to Flask-Restful not passing them up

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # ref: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications/33790196#33790196

    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_NAME = "X-CSRF-TOKEN"

    REMEMBER_COOKIE_DURATION = timedelta(days=15)
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True

    BACKEND_SERVER_PORT = "4999"
    BACKEND_SERVER_HOST = "127.0.0.1"
    BACKEND_SERVER_URL = f"https://{BACKEND_SERVER_HOST}:{BACKEND_SERVER_PORT}"

    SECRET_KEY = os.getenv("SECRET")

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

    SQLALCHEMY_ECHO = False

    CSRF_DISABLE = True

    LOGIN_DISABLED = True

    SSL_CERT = "development/cert.pem"
    SSL_KEY = "development/key.pem"

    CSRF_COOKIE_SAMESITE = "Lax"  # allow development frontend server
    FRONTEND_SERVER_URL = "https://127.0.0.1:3000"

    SQLALCHEMY_DATABASE_URI = "postgres://bxdyxoqsvvhyxt:ef4120efdf1acb51df3c13535e6a4e30fa60e9b19423b7e9a0b8e1842db77631@ec2-176-34-168-83.eu-west-1.compute.amazonaws.com:5432/d5vibot3fktq2o"


class DevelopmentBuiltConfig(DevelopmentConfig):
    CSRF_COOKIE_SAMESITE = "Strict"
    SESSION_PROTECTION = "basic"  # not strict to allow the remember me
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"
    CSRF_DISABLE = False
    LOGIN_DISABLED = False

    DEVELOPMENT = False

    FRONTEND_SERVER_URL = "https://127.0.0.1:4999"

    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "", "people.db"
    )


class ProductionConfig(Config):
    CSRF_COOKIE_SAMESITE = "Lax"
    SESSION_PROTECTION = "strong"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"

    BACKEND_SERVER_PORT = "443"
    BACKEND_SERVER_HOST = os.getenv("BACKEND_SERVER_HOST")
    BACKEND_SERVER_URL = "https://%s:%s" % (BACKEND_SERVER_HOST, BACKEND_SERVER_PORT)
    FRONTEND_SERVER_URL = BACKEND_SERVER_URL

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class HerokuManualLiveConfig(ProductionConfig):

    SECRET_KEY = "super-secret"

    FRONTEND_SERVER_URL = os.getenv("BACKEND_SERVER_HOST")
    BACKEND_SERVER_PORT = "443"
    BACKEND_SERVER_HOST = "centrifuga4.herokuapp.com"

    SQLALCHEMY_DATABASE_URI = os.getenv("MANUAL_DATABASE_URL")


class TestingConfig(DevelopmentConfig):
    TESTING = True


class TestingConfigNoDb(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = None
