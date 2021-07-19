from flask import *

from is_it_rick.main import app
from is_it_rick import config

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/register-rick-roll/', methods=['GET'])
def register_rick_roll():
    return render_template('register_rick_roll.html')