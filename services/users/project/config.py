# services/users/project/config.py


class BaseConfig:
    """Configuración Base"""

    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuración de Development"""

    pass


class TestingConfig(BaseConfig):
    """Configuración de Testing"""

    TESTING = True


class ProductionConfig(BaseConfig):
    """Configuración de Production"""

    pass
