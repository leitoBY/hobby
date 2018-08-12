from connection import db
from api.cart.cart_model import Cart


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    cart = db.relationship('Cart', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
