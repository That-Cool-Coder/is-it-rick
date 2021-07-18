from flask import *
from flask_error_templating import ErrorPage, create_http_error_handlers

app = Flask(__name__)

from is_it_rick.frontend_routes import *
from is_it_rick.backend_routes import *

create_http_error_handlers(app, [
    ErrorPage(400, 'Bad request'),
    ErrorPage(401, 'Access is denied to this page'),
    ErrorPage(403, 'You are forbidden to view this page'),
    ErrorPage(404, 'The page you are looking for does not exist'),
    ErrorPage(418, 'I\'m a teapot!'),
    ErrorPage(500, 'Internal server error'),
], 'http_error_page.html')