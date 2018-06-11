from connection import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.Float, nullable=False)

    def __init__(self, title: str, description: str, price: float):
        self.title = title
        self.description = description
        self.price = price

    def __repr__(self):
        return '<title %r>' % self.title
