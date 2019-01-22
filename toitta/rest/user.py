# coding: utf-8

from flask import request, jsonify, Blueprint

from toitta.repository.datastore.repository_provider import repository_provider
from toitta.rest import STATUS_CODES
from toitta.usecase.useradd.user_add_usecase import UserAddRequest, UserAddUseCase

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/v1/user', methods=['POST'])
def add_user():
    repository = repository_provider.user_repository()
    request_object = UserAddRequest.from_dict(request.json)
    user_case = UserAddUseCase(repository)
    response_object = user_case.execute(request_object)
    body = response_object.value
    if response_object:
        body = body.to_dict()
    status_code = STATUS_CODES.get(response_object.type, 200)
    return jsonify(body), status_code
