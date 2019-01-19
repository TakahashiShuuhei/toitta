# coding: utf-8
import logging

from toitta.domain.tweet import TweetType, TweetConstants, Tweet
from toitta.usecase.request import ValidRequestObject, InvalidRequestObject
from toitta.usecase.response import ResponseFailure, ResponseSuccess


class TweetAddRequest(ValidRequestObject):

    def __init__(self,
                 tweet,
                 type_,
                 user_id,
                 parent_id=None):
        self.tweet = tweet
        self.type = type_
        self.user_id = user_id
        self.parent_id = parent_id

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'type' not in adict:
            invalid_req.add_error('type', 'typeは必須です')
            return invalid_req

        if 'tweet' not in adict and adict['type'] == TweetType.NORMAL.value:
            invalid_req.add_error('tweet', 'つぶやきを指定してください')

        if len(adict.get('tweet', '')) > TweetConstants.MAX_LENGTH:
            invalid_req.add_error('tweet', 'つぶやきは{}文字以内'.format(TweetConstants.MAX_LENGTH))

        if 'user_id' not in adict:
            invalid_req.add_error('user_id', 'user_idは必須です')

        if invalid_req.has_errors():
            return invalid_req

        return cls(tweet=adict.get('tweet'),
                   type_=adict.get('type'),
                   user_id=adict.get('user_id'),
                   parent_id=adict.get('parent_id'))


class TweetAddUseCase(object):

    def __init__(self, repository):
        self.repository = repository

    def execute(self, request):
        if not request:
            return ResponseFailure.build_from_invalid_request_object(request)

        try:
            # TODO ユーザーの存在チェック
            # TODO parentの存在チェック
            tweet = self._build_tweet(request)
            tweet = self.repository.add_tweet(tweet)
            response = ResponseSuccess(tweet.to_dict())
            return response
        except Exception as e:
            logging.exception(e)
            return ResponseFailure.build_system_error(e)

    def _build_tweet(self, request):
        return Tweet(id=None,
                     tweet=request.tweet,
                     type_=request.type,
                     user_id=request.user_id,
                     parent_id=request.parent_id)

