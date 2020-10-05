# services/users/project/config.py


import os  # new


class BaseConfig:
    """Configuración Base"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # nuevo


class DevelopmentConfig(BaseConfig):
    """Configuración de Development"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # nuevo


class TestingConfig(BaseConfig):
    """Configuración de Testing"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")  # nuevo


class ProductionConfig(BaseConfig):
    """Configuración de Production"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # nuevo
