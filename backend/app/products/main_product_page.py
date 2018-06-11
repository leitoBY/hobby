from flask import jsonify, Blueprint, render_template
from api.products.product_service import ProductService


products_store = Blueprint('products_store', __name__)


@products_store.route('/products')
def get_all_users():

    try:
        products = ProductService.get_all_products()
    except Exception as e:
        return jsonify(error=str(e))

    return render_template("products/product_list.html", products=products)
