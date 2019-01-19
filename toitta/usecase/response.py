# coding: utf-8
from enum import Enum


class ResponseType(str, Enum):
    SUCCESS = 'Success'
    RESOURCE_ERROR = 'ResourceError'
    PARAMETERS_ERROR = 'ParametersError'
    SYSTEM_ERROR = 'SystemError'


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return '{}: {}'.format(msg.__class__.__name__, '{}'.format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request):
        message = '\n'.join(['{}: {}'.format(err['parameter'], err['message'])
                             for err in invalid_request.errors])
        return cls(ResponseType.PARAMETERS_ERROR, message)

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(ResponseType.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(ResponseType.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(ResponseType.PARAMETERS_ERROR, message)


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseType.SUCCESS
        self.value = value

    def __bool__(self):
        return True
