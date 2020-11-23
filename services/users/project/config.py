# services/users/project/config.py


import os


class BaseConfig:
    """Configuracion Base"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_key"
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Configuracion de Testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    """Configuracion de Production"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
