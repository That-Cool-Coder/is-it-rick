import os.path

try:
    from is_it_rick.local_config import PRODUCTION, \
        BASE_URL, DATABASE_DIRECTORY, TESTING_PORT
except:
    PRODUCTION = True
    BASE_URL = '/'
    DATABASE_DIRECTORY = '/var/www/is_it_rick_data/'
    TESTING_PORT = 5000

RICK_ROLL_DATABASE_FILE = os.path.join(DATABASE_DIRECTORY, 'rick_rolls.json')
USER_DATABASE_FILE = os.path.join(DATABASE_DIRECTORY, 'users.json')
SESSION_ID_DATABASE_FILE = os.path.join(DATABASE_DIRECTORY, 'session_ids.json')

VERSION = '1.1.0-beta'
APP_NAME = 'Is It Rick?'
APP_SLOGAN = 'Fast, free Rick Roll detector'
APP_DESCRIPTION = 'Check if a URL leads to a Rick Roll.'

DATABASE_READ_INTERVAL = 10
SESSION_ID_DURATION = 60 * 60 # 1 hour (in seconds)