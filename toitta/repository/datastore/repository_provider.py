# coding: utf-8
import os

from toitta.flask_settings import DevConfig, ProdConfig
from toitta.repository.datastore.tweet_repository import TweetRepository
from toitta.repository.datastore.user_repository import UserRepository


class DatastoreRepositoryProvider:
    CONFIG_MAP = {
        'development': DevConfig,
        'production': ProdConfig
    }

    def __init__(self):
        env = os.getenv('FLASK_ENV', 'development')
        self.config = self.CONFIG_MAP.get(env)

    def tweet_repository(self):
        return TweetRepository.get_instance(self.config)

    def user_repository(self):
        return UserRepository.get_instance(self.config)


repository_provider = DatastoreRepositoryProvider()
