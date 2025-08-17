import jwt

from functools import wraps
from flask import request, jsonify
from backend.api.users.user_service import UserService
from backend.config import get_config

JWT_SECRET = get_config().JWT_SECRET_KEY


def get_current_user():
    """Get current user from JWT token without requiring authentication"""
    token = None
    if 'jwt_token' in request.cookies:
        token = request.cookies['jwt_token']
    
    if not token:
        return None
        
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        current_user = UserService.find_user_by_public_id(public_id=data.get('public_id'))
        return current_user
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            current_user = UserService.find_user_by_public_id(public_id=data.get('public_id'))
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
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
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            current_user = UserService.find_user_by_public_id(
                public_id=data.get('public_id'))
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401

        return func(current_user, *args, **kwargs)

    return decorated
