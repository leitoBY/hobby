from flask import jsonify, request, render_template, Blueprint, make_response, redirect
from api.authentication.login_service import LoginService

login_api = Blueprint('login_api', __name__)
@login_api.route('/login', methods=['GET', 'POST'])
def login_user():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        body = request.get_json()
        try:
            jwt_token = LoginService.login(data=body)
            if jwt_token:
                response = make_response(redirect('/'))
                response.set_cookie('jwt_token', jwt_token)
                return response
                # return jsonify({"jwt_token": jwt_token})
            return jsonify(message="Something went wrong")
        except Exception as e:
            return jsonify(error=str(e))
