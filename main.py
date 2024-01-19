from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from config import app, db
from model import Product

def initialize_database():
    # Fetch JSON data from the third-party API
    response = requests.get('https://s3.amazonaws.com/roxiler.com/product_transaction.json')
    data = response.json()

    for item in data:
        product_transaction = Product(**item)
        db.session.add(product_transaction)
    db.session.commit()


initialize_database()

@app.route('/transactions', methods=['GET'])
def get_transactions():
    month = request.args.get('month')
    search_query = request.args.get('search')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    query = Product.query

    if month:
        query = query.filter(Product.dateOfSale.strptime('%m').contains(month))

    if search_query:
        query = query.filter((Product.title.contains(search_query)) |
                             (Product.description.contains(search_query)) |
                             (Product.price.contains(search_query)))

    transactions = query.paginate(page, per_page, False)
    return jsonify([product.to_dict() for product in transactions.items])


if __name__ == '__main__':
    app.run(debug=True)