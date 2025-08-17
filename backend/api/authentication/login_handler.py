from flask import jsonify, request, render_template, Blueprint, make_response, redirect
from backend.api.authentication.login_service import LoginService
from backend.decorators.user_decorators import get_current_user

login_api = Blueprint('login_api', __name__)
@login_api.route('/login', methods=['GET', 'POST'])
def login_user():

    if request.method == 'GET':
        current_user = get_current_user()
        # If user is already logged in, redirect to home
        if current_user:
            return redirect('/')
        return render_template('login.html', user=current_user)
    else:
        # Handle both JSON (API) and form data (web form)
        if request.is_json:
            body = request.get_json()
            if not body:
                return jsonify(error="No JSON data provided"), 400
        else:
            # Handle form data
            body = {
                'email': request.form.get('email'),
                'password': request.form.get('password')
            }
            
        try:
            jwt_token = LoginService.login(data=body)
            if jwt_token:
                response = make_response(redirect('/'))
                response.set_cookie('jwt_token', jwt_token)
                return response
            return jsonify(message="Something went wrong"), 500
        except Exception as e:
            if request.is_json:
                return jsonify(error=str(e)), 401
            else:
                # For form submissions, redirect back to login with error
                current_user = get_current_user()
                return render_template('login.html', error=str(e), user=current_user)
