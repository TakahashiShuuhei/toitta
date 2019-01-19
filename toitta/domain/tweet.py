# coding: utf-8
from datetime import datetime
from enum import Enum


class Tweet(object):
    def __init__(self,
                 id,
                 tweet,
                 type_,
                 user_id,
                 liked=None,
                 retweeted=None,
                 tags=None,
                 images=None,
                 parent_id=None,
                 created_at=None):
        self.id = id
        self.tweet = tweet
        self.type = type_
        self.user_id = user_id
        self.liked = liked if liked else []
        self.retweeted = retweeted if retweeted else []
        self.tags = tags if tags else self._find_tags(tweet)
        self.images = images if images else []
        self.parent_id = parent_id
        self.created_at = created_at if created_at else datetime.now()

    def _find_tags(self, tweet):
        # TODO
        return []

    def to_dict(self):
        return {
            'id': self.id,
            'tweet': self.tweet,
            'type': self.type,
            'user_id': self.user_id,
            'parent_id': self.parent_id,
            'created_at': self.created_at.isoformat()
        }


class TweetType(Enum):
    NORMAL = 'normal'
    RETWEET = 'retweet'
    LIKE = 'like'


class TweetConstants(object):
    MAX_LENGTH = 140
