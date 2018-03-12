from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':

    from api.users.user_handler import users_api
    from api.users.user_handler import user_add_api
    from api.database.database_handler import database_api
    app.register_blueprint(users_api)
    app.register_blueprint(user_add_api)
    app.register_blueprint(database_api)

    app.run(debug=True)
