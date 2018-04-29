from backend.repository import Repository
from backend.api.users.user_model import User

class UserRepository(Repository):

    model = User

    @classmethod
    def find_user_by_email(cls, email):
        return cls.session.query(cls.model).filter(cls.model.email == email).first()
