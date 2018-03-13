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
        username = data.get('username')
        email = data.get('email')
        new_user = UserModel(username=username, email=email)
        try:
            UserRepository.add(new_user)
            UserRepository.commit()
            return new_user
        except Exception as e:
            print('Error in database operation: {0}'.format(str(e)))
            UserRepository.rollback()
