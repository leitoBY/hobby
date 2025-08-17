import uuid

from werkzeug.security import generate_password_hash

from backend.api.users.user_model import User
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
        if not data.get('email'):
            raise Exception('Email is required')
        if not data.get('username'):
            raise Exception('Username is required')
        if not data.get('password'):
            raise Exception('Password is required')

        email = data.get('email')
        user_already_exists = cls.find_user_by_email(email)
        if user_already_exists:
            raise Exception('User with selected email already exists')

        username = data.get('username')
        password = data.get('password')
        hashed_password = generate_password_hash(password)
        new_user = User(
            public_id = str(uuid.uuid4()),
            username=username,
            email=email,
            password=hashed_password)
        try:
            UserRepository.add(new_user)
            UserRepository.commit()
            print(f'Successfully created user: {username} with email: {email}')
            return new_user
        except Exception as e:
            print('Error in database operation: {0}'.format(str(e)))
            print('Exception type:', type(e).__name__)
            import traceback
            print('Traceback:', traceback.format_exc())
            UserRepository.rollback()
            raise Exception(f'Failed to create user: {str(e)}')

    @classmethod
    def find_user_by_email(cls, email):
        return UserRepository.find_user_by_email(email)

    @classmethod
    def find_user_by_public_id(cls, public_id):
        return UserRepository.find_user_by_public_id(public_id)
