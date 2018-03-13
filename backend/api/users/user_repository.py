from backend.repository import Repository
from backend.api.users.user_model import UserModel

class UserRepository(Repository):

    model = UserModel
