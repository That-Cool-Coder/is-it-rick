from is_it_rick import config
from is_it_rick.data_loading import *
from is_it_rick.data_structures import *

rick_rolls = [
    RickRoll('https://storage.calbabreaker.repl.co/secret.mp4')
]

save_rick_roll_database(rick_rolls)