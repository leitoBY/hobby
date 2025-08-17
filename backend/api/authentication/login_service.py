import jwt

from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from backend.api.users.user_service import UserService
from backend.config import get_config


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
        jwt_secret = get_config().JWT_SECRET_KEY
        jwt_exp_delta_seconds = get_config().JWT_EXP_DELTA_SECONDS

        payload = {
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(seconds=jwt_exp_delta_seconds)
        }
        encoded_jwt = jwt.encode(payload, jwt_secret, algorithm='HS256')

        return encoded_jwt
