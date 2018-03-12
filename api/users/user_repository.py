from repository import Repository
from api.users.user_model import UserModel

class UserRepository(Repository):

    model = UserModel
