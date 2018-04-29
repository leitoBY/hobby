from flask import Flask

app = Flask(__name__, static_url_path='/static')

# TODO move such thing to config file
app.config['SECRET_KEY'] = 'My_super_secret_key'


if __name__ == '__main__':

    from backend.api.users.user_handler import users_api
    from backend.api.users.user_handler import user_add_api
    from backend.api.database.database_handler import database_api
    from backend.api.authentication.login_handler import login_api
    from backend.api.authentication.register_handler import register_api
    from backend.app.users.application_user_list import users_app
    from backend.app.products.main_product_page import products_store
    from backend.app.user_carts.user_carts import user_cart

    app.register_blueprint(users_api)
    app.register_blueprint(user_add_api)
    app.register_blueprint(database_api)
    app.register_blueprint(login_api)
    app.register_blueprint(register_api)
    app.register_blueprint(users_app)
    app.register_blueprint(products_store)
    app.register_blueprint(user_cart)

    app.run(debug=True)
