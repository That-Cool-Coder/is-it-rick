PRODUCTION = True
VERSION = '1.1.0-beta'

if PRODUCTION:
    BASE_URL = '/is-it-rick/'
    RICK_ROLL_DATABASE_FILE = '/var/www/is_it_rick_data/rick_rolls.json'
else:
    BASE_URL = '/'
    RICK_ROLL_DATABASE_FILE = 'testing_data/rick_rolls.json'

DATABASE_READ_INTERVAL = 10
APP_NAME = 'Is It Rick?'
APP_SLOGAN = 'Fast, free Rick Roll detector'
APP_DESCRIPTION = 'Check if a URL leads to a Rick Roll.'

TESTING_PORT = 5000