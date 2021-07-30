import jsonpickle

from is_it_rick import config
from is_it_rick.data_structures import *

def load_database(file_name: str):
    file = None
    try:
        file = open(file_name, 'r', encoding='utf-8')
        data = file.read()
        rick_rolls = jsonpickle.decode(data)
        return rick_rolls
    finally:
        if file is not None:
            file.close()

def save_database(file_name: str, data):
    file = None
    try:
        file = open(file_name, 'w+', encoding='utf-8')
        str_data = jsonpickle.encode(data)
        file.write(str_data)
    finally:
        if file is not None:
            file.close()