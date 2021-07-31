import threading
import time

from flask import *
from flask.json import load
import argon2
import uuid

from is_it_rick import config, errors
from is_it_rick.common import *
from is_it_rick.data_structures import *
from is_it_rick.data_loading import load_database, save_database

blueprint = Blueprint('backend', __name__)
hasher = argon2.PasswordHasher()

rick_rolls = []
users = []
session_ids = []

def start_background_tasks():
    threading.Thread(target=database_read_loop, daemon=True).start()

def database_read_loop():
    global rick_rolls, users, session_ids
    while True:
        rick_rolls = load_database(config.RICK_ROLL_DATABASE_FILE)
        users = load_database(config.USER_DATABASE_FILE)
        session_ids = load_database(config.SESSION_ID_DATABASE_FILE)
        time.sleep(config.DATABASE_READ_INTERVAL)

@blueprint.route('/api/is_it_rick/', methods=['POST'])
def api_is_it_rick():
    '''Check if the given URL is a Rick Roll'''

    if not request_fields_valid(['url'], request.json):
        return create_response(Status.WARNING, StatusCode.INVALID_REQUEST)

    try:
        found_rick_roll = None
        for rick_roll in rick_rolls:
            if rick_roll.contains(url_str=request.json['url']):
                found_rick_roll = rick_roll
                break
        
        if found_rick_roll is None:
            return create_response(is_rick_roll=False)
        elif found_rick_roll.verified:
            return create_response(is_rick_roll=True, verified=True)
        else:
            return create_response(is_rick_roll=True, verified=False)
    # This will get thrown by URL object creation if invalid
    except errors.InvalidUrl:
        return create_response(Status.WARNING, StatusCode.INVALID_URL)
    except BaseException as e:
        raise_if_debug(e)
        return create_response(Status.ERROR, StatusCode.UNKNOWN_ERROR)

@blueprint.route('/api/register_rick_roll/', methods=['POST'])
def api_register_rick_roll():
    '''Register a URL that leads to a Rick Roll'''
    global rick_rolls

    if not request_fields_valid(['url'], request.json):
        return create_response(Status.WARNING, StatusCode.INVALID_REQUEST)

    try:
        # Load the rick rolls straight from file to clear cache
        rick_rolls = load_database(config.RICK_ROLL_DATABASE_FILE)

        # First check that the URL is not already listed
        found_rick_roll = None
        for rick_roll in rick_rolls:
            if rick_roll.contains(url_str=request.json['url']):
                found_rick_roll = rick_roll
                break
            
        if found_rick_roll is not None:
            return create_response(Status.WARNING, StatusCode.URL_ALREADY_REGISTERED)

        new_rick_roll = RickRoll(url_str=request.json['url'], verified=False,
            description=request.json.get('description', ''))
        rick_rolls.append(new_rick_roll)
        save_database(config.RICK_ROLL_DATABASE_FILE, rick_rolls)
        return create_response() # Create empty nominal response

    # This will get thrown by URL object creation if invalid
    except errors.InvalidUrl:
        return create_response(Status.WARNING, StatusCode.INVALID_URL)
    except BaseException as e:
        raise_if_debug(e)
        return create_response(Status.ERROR, StatusCode.UNKNOWN_ERROR)

@blueprint.route('/api/sign_in/', methods=['POST'])
def sign_in():
    '''Obtain a session ID for later use'''
    global session_ids

    if not request_fields_valid(['username', 'password'], request.json):
        return create_response(Status.WARNING, StatusCode.INVALID_REQUEST)
    
    try:
        user = find_in_iterable(users, lambda x: x.name == request.json['username'])
        if user is None:
            return create_response(Status.WARNING, StatusCode.INVALID_CREDENTITALS)
        
        # Check that the password is correct.
        # If it's wrong than an exception is raised,
        # thus needing no if statement for checking correctness
        hasher.verify(user.password_hash, request.json['password'])

        # Create a session id, save it, then return it
        new_session_id = SessionId(str(uuid.uuid4()), user.name,
            time.time() + config.SESSION_ID_DURATION)
        session_ids.append(new_session_id)
        save_database(config.SESSION_ID_DATABASE_FILE, session_ids)

        return create_response(session_id=new_session_id.value)

    except argon2.exceptions.VerifyMismatchError:
        return create_response(Status.WARNING, StatusCode.INVALID_CREDENTITALS)
    except BaseException as e:
        raise_if_debug(e)
        return create_response(Status.ERROR, StatusCode.UNKNOWN_ERROR)
