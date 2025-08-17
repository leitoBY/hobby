from flask import Blueprint, make_response, redirect

logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout', methods=['GET', 'POST'])
def logout_user():
    """Logout user by clearing the JWT token cookie"""
    response = make_response(redirect('/'))
    
    # Clear the JWT token cookie
    response.set_cookie('jwt_token', '', expires=0, path='/')
    
    return response
