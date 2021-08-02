import threading
import time
import jsonpickle

from is_it_rick import config
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
        time.sleep(config.DATABASE_READ_INTERVAL)
