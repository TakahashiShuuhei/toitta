# coding: utf-8

from flask import request, jsonify, Blueprint

from toitta.repository.datastore.repository_provider import repository_provider
from toitta.rest import STATUS_CODES
from toitta.usecase.tweetadd.tweet_add_usecase import TweetAddRequest, TweetAddUseCase


blueprint = Blueprint('tweet', __name__)


@blueprint.route('/api/v1/tweet', methods=['POST'])
def add_tweet():
    repository = repository_provider.tweet_repository()
    request_object = TweetAddRequest.from_dict(request.json)
    use_case = TweetAddUseCase(repository)
    response_object = use_case.execute(request_object)
    body = response_object.value
    if response_object:
        body = body.to_dict()
    status_code = STATUS_CODES.get(response_object.type, 200)
    return jsonify(body), status_code
