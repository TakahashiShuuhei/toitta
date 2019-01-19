# coding: utf-8


class Config:
    """Base configuration"""


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    PROJECT = 'gcp-dev-161714'
    DATASTORE_NAMESPACE = 'toitta'


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    PROJECT = 'local-gcp-dev'
    DATASTORE_NAMESPACE = 'toitta-local'
