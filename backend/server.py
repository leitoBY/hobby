from flask import Flask
from backend.app.main.main_page import main, add_post, contacts, donate
from backend.api.blog.blog_post_handler import blog_post_api
from backend.api.comment.comment_handler import comment_api

from backend.api.users.user_handler import users_api
from backend.api.users.user_handler import user_add_api
from backend.api.database.database_handler import database_api
from backend.api.authentication.login_handler import login_api
from backend.api.authentication.register_handler import register_api
from backend.api.authentication.logout_handler import logout_api
from backend.app.users.application_user_list import users_app
from backend.app.products.main_product_page import products_store
from backend.app.user_carts.user_carts import user_cart
from backend.config import get_config
from backend.connection import init_db


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = get_config().SECRET_KEY
init_db(app)

if __name__ == '__main__':
    app.register_blueprint(main)
    app.register_blueprint(add_post)
    app.register_blueprint(contacts)
    app.register_blueprint(donate)
    app.register_blueprint(blog_post_api)
    app.register_blueprint(comment_api)

    app.register_blueprint(users_api)
    app.register_blueprint(user_add_api)
    app.register_blueprint(database_api)
    app.register_blueprint(login_api)
    app.register_blueprint(register_api)
    app.register_blueprint(logout_api)
    app.register_blueprint(users_app)
    app.register_blueprint(products_store)
    app.register_blueprint(user_cart)

    app.run(host='0.0.0.0', port=5000, debug=True)
