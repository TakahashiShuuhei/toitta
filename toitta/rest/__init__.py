# coding: utf-8
from toitta.usecase.response import ResponseType

STATUS_CODES = {
    ResponseType.SUCCESS: 200,
    ResponseType.RESOURCE_ERROR: 404,
    ResponseType.PARAMETERS_ERROR: 400,
    ResponseType.SYSTEM_ERROR: 500
}