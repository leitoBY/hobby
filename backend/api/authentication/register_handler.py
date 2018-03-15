from flask import jsonify, request, Blueprint
from backend.api.users.user_service import UserService

register_api = Blueprint('register_api', __name__)
@register_api.route('/register', methods=['POST'])
def register_new_user():

    body = request.get_json()
    try:
        new_user = UserService.add_new_user(data=body)
        if new_user:
            return jsonify(message="New user has been created")
        return jsonify(message="Something went wrong")
    except Exception as e:
        return jsonify(error=str(e))
