import threading
import time
import jsonpickle

from is_it_rick import config
from is_it_rick.common import *
from is_it_rick.data_structures import *

rick_rolls = []
users = []
session_ids = []

def load(file_name: str):
    file = None
    try:
        file = open(file_name, 'r', encoding='utf-8')
        data = file.read()
        rick_rolls = jsonpickle.decode(data)
        return rick_rolls
    finally:
        if file is not None:
            file.close()

def save(file_name: str, data):
    file = None
    try:
        file = open(file_name, 'w+', encoding='utf-8')
        str_data = jsonpickle.encode(data)
        file.write(str_data)
    finally:
        if file is not None:
            file.close()

def start_database_read_loop():
    threading.Thread(target=database_read_loop, daemon=True).start()

def database_read_loop():
    global rick_rolls, users, session_ids
    while True:
        rick_rolls = load(config.RICK_ROLL_DATABASE_FILE)
        users = load(config.USER_DATABASE_FILE)
        session_ids = load(config.SESSION_ID_DATABASE_FILE)

        delete_expired_session_ids(session_ids)
        save(config.SESSION_ID_DATABASE_FILE, session_ids)

        time.sleep(config.DATABASE_READ_INTERVAL)

def delete_expired_session_ids(session_ids):
    # Loop through session ids backwards to avoid messing up indexes
    for idx in range(len(session_ids) -1, -1, -1):
        session_id = session_ids[idx]
        if session_id.has_expired():
            del session_ids[idx]

def check_if_signed_in(session_id_value: str):
    '''Check if session_id_value is valid.

    Returns a boolean stating the validity and the session id
    that the value belongs to (None if the session id is invalid).
    '''
    if session_id_value is None:
        return False, None

    existing_session_id = find_in_iterable(session_ids,
        lambda x: x.value == session_id_value)
    is_signed_in = False
    if existing_session_id is not None and \
        not existing_session_id.has_expired():
        is_signed_in = True
    return is_signed_in, existing_session_id