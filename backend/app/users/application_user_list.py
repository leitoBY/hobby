from flask import jsonify, Blueprint, render_template
from backend.api.users.user_service import UserService


users_app = Blueprint('users_app', __name__)


@users_app.route('/users')
def get_all_users():

    try:
        users = UserService.get_all_users()
    except Exception as e:
        return jsonify(error=str(e))

    return render_template("users_list.html", users=users)
