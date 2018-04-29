from backend.connection import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title %r>' % self.title
