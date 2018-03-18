from werkzeug.security import generate_password_hash

from backend.api.users.user_model import UserModel
from backend.api.users.user_repository import UserRepository


class UserService:

    @classmethod
    def get_all_users(cls):

        users = UserRepository.get_all()
        user_list = []
        for user in users:
            user_info = {}
            user_info['username'] = user.username
            user_info['email'] = user.email
            user_list.append(user_info)

        return user_list

    @classmethod
    def add_new_user(cls, data: dict):

        email = data.get('email')
        user_already_exists = cls.find_user_by_email(email)
        if user_already_exists:
            raise Exception('User with selected email is already exists')

        username = data.get('username')
        password = data.get('password')
        hashed_password = generate_password_hash(password=password, method="sha256")
        new_user = UserModel(username=username, email=email, password=hashed_password)
        try:
            UserRepository.add(new_user)
            UserRepository.commit()
            return new_user
        except Exception as e:
            print('Error in database operation: {0}'.format(str(e)))
            UserRepository.rollback()

    @classmethod
    def find_user_by_email(cls, email):
        return UserRepository.find_user_by_email(email)
