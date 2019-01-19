# coding: utf-8
from toitta.domain.tweet import TweetType
from toitta.usecase.request import InvalidRequestObject
from toitta.usecase.tweetadd.tweet_add_usecase import TweetAddRequest


class TestTweedAddRequest:

    def test_valid_request(self):
        adict = {
            'type': TweetType.NORMAL.value,
            'user_id': 123,
            'tweet': 'some tweet'
        }

        actual = TweetAddRequest.from_dict(adict)

        assert isinstance(actual, TweetAddRequest)
        assert bool(actual) is True
        assert actual.type == TweetType.NORMAL.value
        assert actual.user_id == 123
        assert actual.tweet == 'some tweet'
        assert actual.parent_id is None

    def test_type_is_missing(self):
        adict = {
            'user_id': 123,
            'tweet': 'some tweet'
        }

        actual = TweetAddRequest.from_dict(adict)

        assert isinstance(actual, InvalidRequestObject)
        assert bool(actual) is False
        assert actual.has_errors() is True
        assert actual.errors[0] == {'parameter': 'type', 'message': 'typeは必須です'}

    def test_type_is_normal_and_tweet_is_missing(self):
        adict = {
            'type': TweetType.NORMAL.value,
            'user_id': 123
        }

        actual = TweetAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'tweet', 'message': 'つぶやきを指定してください'}

    def test_too_long_tweet(self):
        tweet = '0123456789012345678901234567890123456789' \
              + '0123456789012345678901234567890123456789' \
              + '0123456789012345678901234567890123456789' \
              + '0123456789012345678901234567890123456789'
        adict = {
            'type': TweetType.NORMAL.value,
            'user_id': 123,
            'tweet': tweet
        }

        actual = TweetAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'tweet', 'message': 'つぶやきは140文字以内'}

    def test_user_id_is_missing(self):
        adict = {
            'type': TweetType.NORMAL.value,
            'tweet': 'some tweet'
        }

        actual = TweetAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'user_id', 'message': 'user_idは必須です'}
