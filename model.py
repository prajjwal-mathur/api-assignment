from config import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    sold = db.Column(db.Boolean, nullable=False)