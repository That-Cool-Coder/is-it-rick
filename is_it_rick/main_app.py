from flask import *
from flask_error_templating import ErrorPage, create_http_error_handlers

from is_it_rick import config

from is_it_rick import frontend_routes
from is_it_rick import backend_routes

app = Flask(__name__)

app.register_blueprint(frontend_routes.blueprint)
app.register_blueprint(backend_routes.blueprint)

def start_background_tasks():
    backend_routes.start_background_tasks()

create_http_error_handlers(app, [
    ErrorPage(400, 'Bad request'),
    ErrorPage(401, 'Access is denied to this page'),
    ErrorPage(403, 'You are forbidden to view this page'),
    ErrorPage(404, 'The page you are looking for does not exist'),
    ErrorPage(418, 'I\'m a teapot!'),
    ErrorPage(500, 'Internal server error'),
], 'http_error_page.html', base_url = config.BASE_URL)