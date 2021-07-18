from enum import Enum

from flask import jsonify
import validators

from is_it_rick import errors

class Status(Enum):
    OK = 'OK'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

class StatusCode(Enum):
    OK = 'OK'

    # StatusCodes that go with Status WARNING
    INVALID_URL = 'INVALID_URL'
    INVALID_REQUEST = 'INVALID_REQUEST'

    # StatusCodes that go with Status ERROR
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'

def request_fields_valid(required_fields: list, request_json: dict):
    '''Return a bool that states whether all of required_fields
    are in request_json
    '''
    return all(key in request_json for key in required_fields)

def create_response(status=Status.OK, status_code=StatusCode.OK, **kwargs):
    return jsonify({
        'status' : status.value,
        'status_code' : status_code.value,
        **kwargs
    })

def url_valid(url: str):
    return validators.url(url)