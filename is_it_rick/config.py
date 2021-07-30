try:
    from is_it_rick.local_config import PRODUCTION, \
        BASE_URL, RICK_ROLL_DATABASE_FILE, USER_DATABASE_FILE, \
        TESTING_PORT
except:
    PRODUCTION = True
    BASE_URL = '/'
    RICK_ROLL_DATABASE_FILE = '/var/www/is_it_rick_data/rick_rolls.json'
    USER_DATABASE_FILE = 'var/www/is_it_rick_data/users.json'
    TESTING_PORT = 5000

VERSION = '1.1.0-beta'
APP_NAME = 'Is It Rick?'
APP_SLOGAN = 'Fast, free Rick Roll detector'
APP_DESCRIPTION = 'Check if a URL leads to a Rick Roll.'

DATABASE_READ_INTERVAL = 10