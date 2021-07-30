from is_it_rick import config
from is_it_rick.data_loading import load_database, save_database
from is_it_rick.data_structures import *

rick_rolls = [
    RickRoll(url_str='https://storage.calbabreaker.repl.co/secret.mp4'),
    RickRoll(url_str='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
    RickRoll(url_str='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
]

users = [
    User('Test User', 'fake hash', admin=True)
]

save_database(config.RICK_ROLL_DATABASE_FILE, rick_rolls)
save_database(config.USER_DATABASE_FILE, users)