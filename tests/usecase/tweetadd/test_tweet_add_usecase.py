# coding: utf-8
from unittest import mock

from toitta.domain.tweet import TweetType, Tweet
from toitta.usecase.request import InvalidRequestObject
from toitta.usecase.response import ResponseSuccess, ResponseFailure, ResponseType
from toitta.usecase.tweetadd.tweet_add_usecase import TweetAddRequest, TweetAddUseCase


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


class TestTweetAddUseCase:

    def test_tweet_add_ok(self):
        repo = mock.Mock()
        tweet = Tweet(id=333,
                      user_id=123,
                      tweet='hoge',
                      type_=TweetType.NORMAL.value)
        repo.add_tweet.return_value = tweet

        sut = TweetAddUseCase(repo)

        request = TweetAddRequest.from_dict({'tweet': 'hoge',
                                             'type': TweetType.NORMAL.value,
                                             'user_id': 123})
        response = sut.execute(request)

        # assert repo.add_tweet.assert_called_with()  # TODO
        assert isinstance(response, ResponseSuccess)
        actual = response.value
        assert actual.id == 333
        assert actual.user_id == 123
        assert actual.tweet == 'hoge'
        assert actual.type == TweetType.NORMAL.value

    def test_tweet_add_exception(self):
        repo = mock.Mock()
        repo.add_tweet.side_effect = RuntimeError('Some Error')

        sut = TweetAddUseCase(repo)

        request = TweetAddRequest.from_dict({'tweet': 'hoge',
                                             'type': TweetType.NORMAL.value,
                                             'user_id': 123})
        response = sut.execute(request)

        assert isinstance(response, ResponseFailure)
        assert response.type == ResponseType.SYSTEM_ERROR
        assert response.message == 'RuntimeError: Some Error'

    def test_tweet_add_invalid_request(self):
        repo = mock.Mock()
        sut = TweetAddUseCase(repo)

        invalid_request = InvalidRequestObject()
        invalid_request.add_error('name', 'invalid name')

        response = sut.execute(invalid_request)

        assert isinstance(response, ResponseFailure)
        assert response.type == ResponseType.PARAMETERS_ERROR
        assert response.message == 'name: invalid name'


