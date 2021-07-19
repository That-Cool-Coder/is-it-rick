import urllib.parse

from flask import *

from is_it_rick.main import app
from is_it_rick import config, errors
from is_it_rick.common import *
from is_it_rick.data_structures import *

# temporary list for testing
rick_rolls = [
    RickRoll('http://rickroll.com', False),
    RickRoll('http://storage.calbabreaker.repl.co/secret.mp4', True),
    RickRoll('https://storage.calbabreaker.repl.co/secret.mp4', True),
]

@app.route(urllib.parse.urljoin(config.API_BASE_URL, 'is_it_rick/'), methods=['POST'])
def is_it_rick():
    '''Check if the given URL is a Rick Roll'''

    if not request_fields_valid(['url'], request.json):
        return create_response(Status.WARNING, StatusCode.INVALID_REQUEST)

    try:
        sent_url = request.json['url']
        if not url_valid(sent_url):
            return create_response(Status.WARNING, StatusCode.INVALID_URL)

        found_rick_roll = None
        for rick_roll in rick_rolls:
            if rick_roll.url == sent_url:
                found_rick_roll = rick_roll
                break
        
        if found_rick_roll is None:
            return create_response(is_rick_roll=False)
        elif found_rick_roll.verified:
            return create_response(is_rick_roll=True, verified=True)
        else:
            return create_response(is_rick_roll=True, verified=False)
    except:
        return create_response(Status.ERROR, StatusCode.UNKNOWN_ERROR)

def register_rick_roll():
    '''Register a URL that leads to a Rick Roll'''
    if not request_fields_valid(['url'], request.json):
        return create_response(Status.WARNING, StatusCode.INVALID_REQUEST)

    try:
        sent_url = request.json['url']
        if not url_valid(sent_url):
            return create_response(Status.WARNING, StatusCode.INVALID_URL)

        found_rick_roll = None
        for rick_roll in rick_rolls:
            if rick_roll.url == sent_url:
                found_rick_roll = rick_roll
                break
        
        if found_rick_roll is not None:
            return create_response(is_rick_roll=False)
        elif found_rick_roll.verified:
            return create_response(is_rick_roll=True, verified=True)
        else:
            return create_response(is_rick_roll=True, verified=False)
    except:
        return create_response(Status.ERROR, StatusCode.UNKNOWN_ERROR)