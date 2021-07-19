from flask import *

from is_it_rick.main import app
from is_it_rick import config

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html', app_name=config.APP_NAME,
        app_slogan=config.APP_SLOGAN)

@app.route('/register-rick-roll/', methods=['GET'])
def register_rick_roll():
    return render_template('register-rick-roll.html', app_name=config.APP_NAME,
        app_slogan=config.APP_SLOGAN)