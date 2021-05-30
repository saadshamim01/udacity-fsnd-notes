from flask import Flask, request
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = 'fsnd1998.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error,
        self.status_code = status_code

def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/')

app = Flask(__name__)


def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)

    auth_header = request.headers['Authorization']
    headers_part = auth_header.split(' ')

    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() = 'bearer':
        abort(401)
    return header_parts[1]


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)

    @app.route('/headers')
    @requires_auth
    def headers(jwt):
        jwt = get_token_auth_header()
        print(jwt)




    print('hello world')
    return 'not implemented'
