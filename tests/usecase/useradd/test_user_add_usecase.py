# coding: utf-8
from unittest import mock

from toitta.domain.user import User, hash_password
from toitta.usecase.request import InvalidRequestObject
from toitta.usecase.response import ResponseSuccess, ResponseFailure, ResponseType
from toitta.usecase.useradd.user_add_usecase import UserAddRequest, UserAddUseCase


class TestUserAddRequest:

    def test_valid_request(self):
        adict = {
            'name': 'user_name',
            'password': '1234abcd',
            'email': 'hoge@example.com'
        }

        actual = UserAddRequest.from_dict(adict)

        assert isinstance(actual, UserAddRequest)
        assert bool(actual) is True
        assert actual.name == 'user_name'
        assert actual.password == '1234abcd'
        assert actual.email == 'hoge@example.com'
        assert actual.description is None

    def test_name_is_missing(self):
        adict = {
            'password': '1234abcd',
            'email': 'hoge@example.com'
        }

        actual = UserAddRequest.from_dict(adict)

        assert isinstance(actual, InvalidRequestObject)
        assert bool(actual) is False
        assert actual.has_errors() is True
        assert actual.errors[0] == {'parameter': 'name', 'message': 'nameは必須です'}

    def test_password_is_missing(self):
        adict = {
            'name': 'user_name',
            'email': 'hoge@example.com'
        }

        actual = UserAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'password', 'message': 'passwordは必須です'}

    def test_email_is_missing(self):
        adict = {
            'name': 'user_name',
            'password': '1234abcd'
        }

        actual = UserAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'email', 'message': 'emailは必須です'}

    def test_name_is_too_short(self):
        adict = {
            'name': 'us',
            'password': '1234abcd',
            'email': 'hoge@example.com'
        }

        actual = UserAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'name', 'message': 'nameは3文字以上'}

    def test_password_is_too_short(self):
        adict = {
            'name': 'user_name',
            'password': '1234abc',
            'email': 'hoge@example.com'
        }

        actual = UserAddRequest.from_dict(adict)

        assert actual.errors[0] == {'parameter': 'password', 'message': 'passwordは8文字以上'}


class TestUserAddUseCase:

    def test_user_add_ok(self):
        repo = mock.Mock()
        user = User(id=111,
                    name='user_name',
                    password=hash_password('1234abcd'),
                    email='hoge@example.com',
                    description='')
        repo.add_user.return_value = user

        sut = UserAddUseCase(repo)

        request = UserAddRequest.from_dict({
            'name': 'user_name',
            'password': '1234abcd',
            'email': 'hoge@example.com'
        })

        response = sut.execute(request)

        assert isinstance(response, ResponseSuccess)
        actual = response.value
        assert actual.id == 111
        assert actual.name == 'user_name'
        assert actual.password == hash_password('1234abcd')
        assert actual.email == 'hoge@example.com'
        assert actual.description == ''

    def test_user_add_exception(self):
        repo = mock.Mock()
        repo.add_user.side_effect = RuntimeError('Some Error')

        sut = UserAddUseCase(repo)

        request = UserAddRequest.from_dict({
            'name': 'user_name',
            'password': '1234abcd',
            'email': 'hoge@example.com'
        })

        response = sut.execute(request)

        assert isinstance(response, ResponseFailure)
        assert response.type == ResponseType.SYSTEM_ERROR
        assert response.message == 'RuntimeError: Some Error'

    def test_user_add_invalid_request(self):
        repo = mock.Mock()
        sut = UserAddUseCase(repo)

        invalid_request = InvalidRequestObject()
        invalid_request.add_error('name', 'invalid name')

        response = sut.execute(invalid_request)

        assert isinstance(response, ResponseFailure)
        assert response.type == ResponseType.PARAMETERS_ERROR
        assert response.message == 'name: invalid name'

