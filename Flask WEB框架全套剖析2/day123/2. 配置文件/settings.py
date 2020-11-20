class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "asudflkjdfadjfakdf"


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass