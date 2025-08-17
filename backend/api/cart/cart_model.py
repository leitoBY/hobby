from backend.connection import db

cart_products = db.Table("cart_products",
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Product', secondary=cart_products, lazy='subquery',
                           backref=db.backref('cart', lazy=True))

    def __init__(self, user_id: int, product: int):
        self.user_id = user_id
        self.product = product
