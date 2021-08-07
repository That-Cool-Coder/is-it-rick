from enum import Enum

from flask import jsonify

from is_it_rick import errors, config

class Status(Enum):
    OK = 'OK'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

class StatusCode(Enum):
    OK = 'OK'

    # StatusCodes that go with Status WARNING
    INVALID_URL = 'INVALID_URL'
    INVALID_REQUEST = 'INVALID_REQUEST'
    URL_ALREADY_REGISTERED = 'URL_ALREADY_REGISTERED'
    INVALID_CREDENTITALS = 'INVALID_CREDENTIALS'
    NOT_SIGNED_IN = 'NOT_SIGNED_IN'
    RICK_ROLL_NOT_FOUND = 'RICK_ROLL_NOT_FOUND'
    USER_NOT_ADMIN = 'USER_NOT_ADMIN'

    # StatusCodes that go with Status ERROR
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'

def request_fields_valid(required_fields: list, request_json: dict) -> bool:
    '''Return a bool that states whether all of required_fields
    are in request_json
    '''
    return all(key in request_json for key in required_fields)

def create_response(status=Status.OK, status_code=StatusCode.OK, **kwargs) -> str:
    return jsonify({
        'status' : status.value,
        'status_code' : status_code.value,
        **kwargs
    })

def raise_if_debug(exception: BaseException):
    print('Raising this error because program is in debug mode:')
    if not config.PRODUCTION:
        raise exception

def find_in_iterable(iterable: iter, checker_function):
    '''Find a value in iterable that returns true when passed to checker_function.
    If checker_function throws an error for a value then the result is treated as false.

    Returns None if no item matches.'''
    def safe_checker_function(value):
        try:
            return checker_function(value)
        except:
            return False
    return next((value for value in iterable if safe_checker_function(value)), None)