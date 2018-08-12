import jwt
from functools import wraps
from flask import request, jsonify
from api.users.user_service import UserService

JWT_SECRET = "EXTRA_SECRET_KEY"


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, JWT_SECRET)
            current_user = UserService.find_user_by_public_id(public_id=data.get('public_id'))
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return func(current_user, *args, **kwargs)

    return decorated

def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'jwt_token' in request.cookies:
            token = request.cookies['jwt_token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, JWT_SECRET)
            current_user = UserService.find_user_by_public_id(
                public_id=data.get('public_id'))
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return func(current_user, *args, **kwargs)

    return decorated
