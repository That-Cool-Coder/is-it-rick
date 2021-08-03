from flask import *

from is_it_rick import database
from is_it_rick.common import find_in_iterable
from is_it_rick.local_config import BASE_URL
from is_it_rick import config

blueprint = Blueprint('frontend', __name__)

@blueprint.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html', base_url=config.BASE_URL)

@blueprint.route('/register-rick-roll/', methods=['GET'])
def register_rick_roll():
    return render_template('register_rick_roll.html', base_url=config.BASE_URL)

@blueprint.route('/sign-in/', methods=['GET'])
def sign_in():
    return render_template('sign_in.html', base_url=config.BASE_URL)

@blueprint.route('/sign-up/', methods=['GET'])
def sign_up():
    return render_template('sign_up.html', base_url=config.BASE_URL)

@blueprint.route('/manage/', methods=['GET'])
def manage():
    session_id_value = request.cookies.get(config.SESSION_ID_COOKIE_NAME, None)

    is_signed_in = False
    if session_id_value is not None:
        existing_session_id = find_in_iterable(database.session_ids,
            lambda x: x.value == session_id_value)
        if existing_session_id is not None and \
            not existing_session_id.has_expired():
            is_signed_in = True

    return render_template('manage.html', base_url=BASE_URL,
        signed_in=is_signed_in, rick_rolls=database.rick_rolls)

@blueprint.route('/view-rick-roll/<rick_roll_id>/', methods=['GET'])
def view_rick_roll(rick_roll_id):
    rick_roll = find_in_iterable(database.rick_rolls, lambda x: str(x.id) == rick_roll_id)
    if rick_roll is None:
        abort(404)
    
    return render_template('view_rick_roll.html', base_url=config.BASE_URL,
        rick_roll = rick_roll)