from flask import jsonify, request, Blueprint
from backend.api.authentication.login_service import LoginService


login_api = Blueprint('login_api', __name__)
@login_api.route('/login', methods=['POST'])
def login_user():

    body = request.get_json()
    try:
        jwt_token = LoginService.login(data=body)
        if jwt_token:
            return jsonify(jwt_token)
        return jsonify(message="Something went wrong")
    except Exception as e:
        return jsonify(error=str(e))
