from repository import Repository
from api.cart.cart_model import Cart


class CartRepository(Repository):

    model = Cart

    @classmethod
    def get_all_products_on_user_cart(cls, user_id: int) -> list:
        return cls.session.query(cls.model).filter(cls.model.user_id == user_id).all()
