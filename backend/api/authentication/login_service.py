import jwt
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
from api.users.user_service import UserService

# TODO this variables also need to move to config files
JWT_SECRET = "EXTRA_SECRET_KEY"
JWT_EXP_DELTA_SECONDS = 3600


class LoginService:

    @classmethod
    def login(cls, data: dict) -> dict:
        email = data.get('email')
        password = data.get('password')

        user = UserService.find_user_by_email(email=email)
        if not user or not check_password_hash(pwhash=user.password, password=password):
            raise Exception("wrong email or password combination")

        return cls._generate_access_jwt_token(user=user)

    @classmethod
    def _generate_access_jwt_token(cls, user):
        payload = {
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

        jwt_token = encoded_jwt.decode('utf-8')
        return jwt_token
