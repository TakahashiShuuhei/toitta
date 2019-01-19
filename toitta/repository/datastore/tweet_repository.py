# coding: utf-8

from google.cloud import datastore


class TweetRepository:
    _instances = {}

    def __init__(self, env):
        project = env.PROJECT
        namespace = env.DATASTORE_NAMESPACE
        self.client = datastore.Client(project=project, namespace=namespace)

    @classmethod
    def get_instance(cls, env):
        if not env.ENV in cls._instances:
            cls._instances[env.ENV] = TweetRepository(env)
        return cls._instances[env.ENV]

    def add_tweet(self, tweet):
        key = self.client.key('Tweet')
        entity = datastore.Entity(key)
        entity.update({
            'user_id': tweet.user_id,
            'parent_id': tweet.parent_id,
            'tweet': tweet.tweet,
            'type': tweet.type,
            'created_at': tweet.created_at
        })

        self.client.put(entity)
        tweet.id = entity.key.id
        return tweet
