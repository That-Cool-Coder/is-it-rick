from flask import *

from is_it_rick import config

blueprint = Blueprint('frontend', __name__, url_prefix=config.BASE_URL)

@blueprint.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html', base_url=config.BASE_URL)

@blueprint.route('/register-rick-roll/', methods=['GET'])
def register_rick_roll():
    return render_template('register_rick_roll.html', base_url=config.BASE_URL)