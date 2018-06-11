from flask import jsonify, request, render_template, Blueprint
from api.users.user_service import UserService

register_api = Blueprint('register_api', __name__)
@register_api.route('/register', methods=['GET', 'POST'])
def register_new_user():

    if request.method == 'GET':
        return render_template('register.html')

    else:
        body = request.get_json()
        try:
            new_user = UserService.add_new_user(data=body)
            if new_user:
                return jsonify(message="New user has been created")
            return jsonify(message="Something went wrong")
        except Exception as e:
            return jsonify(error=str(e))
