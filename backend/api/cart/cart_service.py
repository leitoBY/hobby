from backend.api.cart.cart_repository import CartRepository


class CartService:

    @classmethod
    def get_all_products_on_user_cart(cls, user_id: int) -> dict:
        CartRepository.get_all_products_on_user_cart(user_id=user_id)
