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
    user = None
    if session_id_value is not None:
        is_signed_in, session_id = database.check_if_signed_in(session_id_value)
        if session_id is not None:
            user = find_in_iterable(database.users,
                lambda x: x.name == session_id.user_name)

    return render_template('manage.html', base_url=BASE_URL,
        signed_in=is_signed_in, rick_rolls=database.rick_rolls, user=user)

@blueprint.route('/view-rick-roll/<rick_roll_id>/', methods=['GET'])
def view_rick_roll(rick_roll_id):
    rick_roll = find_in_iterable(database.rick_rolls, lambda x: str(x.id) == rick_roll_id)
    if rick_roll is None:
        abort(404)
        
    session_id_value = request.cookies.get(config.SESSION_ID_COOKIE_NAME, None)
    user = None
    if session_id_value is not None:
        is_signed_in, session_id = database.check_if_signed_in(session_id_value)
        if session_id is not None:
            user = find_in_iterable(database.users,
                lambda x: x.name == session_id.user_name)

    return render_template('view_rick_roll.html', base_url=config.BASE_URL,
        rick_roll=rick_roll, signed_in=is_signed_in, user=user)