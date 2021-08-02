from is_it_rick import config, database
from is_it_rick.data_structures import *

want_to_continue = input('Are you sure you want to do initiate (clear) the data files?\n' + 
    'All user and rick roll data will be PERMANENTLY DELETED!\n' + 
    'Type \'yes\' to proceed, type anything else to quit: ')
if want_to_continue != 'yes':
    print('Quitting...')
    quit()

rick_rolls = [
    RickRoll(url_str='https://storage.calbabreaker.repl.co/secret.mp4'),
    RickRoll(url_str='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
]
users = []
session_ids = []

database.save(config.RICK_ROLL_DATABASE_FILE, rick_rolls)
database.save(config.USER_DATABASE_FILE, users)
database.save(config.SESSION_ID_DATABASE_FILE, session_ids)

print('Successfully initiated all databases')