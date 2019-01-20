# coding: utf-8
import logging

from toitta.domain.user import UserConstants, User, hash_password
from toitta.usecase.request import ValidRequestObject, InvalidRequestObject
from toitta.usecase.response import ResponseFailure, ResponseSuccess


class UserAddRequest(ValidRequestObject):

    def __init__(self,
                 name,
                 password,
                 email,
                 description):
        self.name = name
        self.password = password
        self.email = email
        self.description = description

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'name' not in adict:
            invalid_req.add_error('name', 'nameは必須です')
            return invalid_req

        if 'password' not in adict:
            invalid_req.add_error('password', 'passwordは必須です')
            return invalid_req

        if 'email' not in adict:
            invalid_req.add_error('email', 'emailは必須です')
            return invalid_req

        if len(adict['name']) < UserConstants.MIN_NAME_LENGTH:
            invalid_req.add_error('name', 'nameは{}文字以上'.format(UserConstants.MIN_NAME_LENGTH))

        if len(adict['password']) < UserConstants.MIN_PASSWORD_LENGTH:
            invalid_req.add_error('password', 'passwordは{}文字以上'.format(UserConstants.MIN_PASSWORD_LENGTH))

        # TODO パスワードの条件
        # TODO 名前の条件

        if invalid_req.has_errors():
            return invalid_req

        return cls(name=adict.get('name'),
                   password=adict.get('password'),
                   email=adict.get('email'),
                   description=adict.get('description'))


class UserAddUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, request):
        if not request:
            return ResponseFailure.build_from_invalid_request_object(request)

        try:
            # TODO ユーザー名の重複チェック
            # TODO emailの重複チェック
            # TODO メールを送信し、そこに記載したリンクからじゃないと登録できないようにする
            user = self._build_user(request)
            user = self.repository.add_user(user)
            response = ResponseSuccess(user)
            return response
        except Exception as e:
            logging.exception(e)
            return ResponseFailure.build_system_error(e)

    def _build_user(self, request):
        return User(id=None,
                    name=request.name,
                    password=hash_password(request.password),
                    email=request.email,
                    description=request.description)
