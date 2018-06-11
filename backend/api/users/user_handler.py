from flask import request, jsonify, Blueprint
from api.users.user_service import UserService


users_api = Blueprint('users_api', __name__)


@users_api.route('/api/users')
def get_all_users():

    try:
        users = UserService.get_all_users()
    except Exception as e:
        return jsonify(error=str(e))

    return jsonify(users=users)


user_add_api = Blueprint('user_add_api', __name__)


@user_add_api.route('/api/user', methods=['POST'])
def add_new_user():

    body = request.get_json()
    try:
        new_user = UserService.add_new_user(data=body)
        if new_user:
            return jsonify(message="New user has been created")
        return jsonify(message="Something went wrong")
    except Exception as e:
        return jsonify(error=str(e))
