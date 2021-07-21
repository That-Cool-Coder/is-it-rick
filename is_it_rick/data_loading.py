import jsonpickle

from is_it_rick import config
from is_it_rick.data_structures import *
from is_it_rick.data_loading import *

def load_rick_roll_database() -> list:
    file = None
    try:
        file = open(config.RICK_ROLL_DATABASE_FILE, 'r', encoding='utf-8')
        data = file.read()
        rick_rolls = jsonpickle.decode(data)
        return rick_rolls
    finally:
        if file is not None:
            file.close()

def save_rick_roll_database(rick_rolls: list):
    file = None
    try:
        file = open(config.RICK_ROLL_DATABASE_FILE, 'w+', encoding='utf-8')
        str_data = jsonpickle.encode(rick_rolls)
        file.write(str_data)
    finally:
        if file is not None:
            file.close()