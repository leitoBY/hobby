from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/new_work'
db = SQLAlchemy(app)

import models.user_model

@app.route('/create_all')
def create_all_tables():
    db.create_all()
    return "datatables were successfully created!"    

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template("add_user.html")
    else:
        username = request.args.get('username')
        email = request.args.get('email')
        new_user = UserModel(username=username, email=email)
        db.session.add(new_user)
        db.session.comit()
        return redirect('/all')


@app.route('/')
def hello_world():
    username = 'alex2'
    email = 'alex_test2@mail.ru'
    user = models.user_model.UserModel(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return 'hello, {0}!'.format(user)

@app.route('/all')
def get_all_users():
    users = UserModel.query.all()
    response = {}
    for user in users:
        response['username'] = user.username
        response['email'] = user.email
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
