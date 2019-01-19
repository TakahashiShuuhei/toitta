# coding: utf-8
from toitta.usecase.request import InvalidRequestObject
from toitta.usecase.response import ResponseFailure, ResponseType, ResponseSuccess


class TestResponseFailure:

    def test_value(self):
        response = ResponseFailure(ResponseType.SYSTEM_ERROR, 'a message')

        actual = response.value

        assert actual['type'] == ResponseType.SYSTEM_ERROR
        assert actual['message'] == 'a message'

    def test_build_from_invalid_request_object(self):
        invalid_request = InvalidRequestObject()
        invalid_request.add_error('name', 'invalid name')
        invalid_request.add_error('age', 'invalid age')

        actual = ResponseFailure.build_from_invalid_request_object(invalid_request)

        assert bool(actual) is False
        assert actual.type == ResponseType.PARAMETERS_ERROR
        assert actual.message == 'name: invalid name\nage: invalid age'

    def test_build_resource_error(self):
        actual = ResponseFailure.build_resource_error('a message')

        assert bool(actual) is False
        assert actual.type == ResponseType.RESOURCE_ERROR
        assert actual.message == 'a message'

    def test_build_system_error(self):
        actual = ResponseFailure.build_system_error('system error')

        assert bool(actual) is False
        assert actual.type == ResponseType.SYSTEM_ERROR
        assert actual.message == 'system error'

    def test_build_system_error_from_exception(self):
        ex = ValueError('exception message')
        actual = ResponseFailure.build_system_error(ex)

        assert bool(actual) is False
        assert actual.type == ResponseType.SYSTEM_ERROR
        assert actual.message == 'ValueError: exception message'

    def test_build_parameters_error(self):
        actual = ResponseFailure.build_parameters_error('a message')

        assert bool(actual) is False
        assert actual.type == ResponseType.PARAMETERS_ERROR
        assert actual.message == 'a message'


class TestResponseSuccess:

    def test_init(self):
        actual = ResponseSuccess(value=123)

        assert bool(actual) is True
        assert actual.type == ResponseType.SUCCESS
        assert actual.value == 123
