from flask import jsonify, Blueprint, render_template
from api.cart.cart_service import CartService


user_cart = Blueprint('user_cart', __name__)


@user_cart.route('/cart')
def get_all_users():

    try:
        # will get user from token
        user = {"id" : 1}
        products = CartService.get_all_products_on_user_cart(user_id=user.get("id", None))
    except Exception as e:
        return jsonify(error=str(e))

    return render_template("product_list.html", products=products)
