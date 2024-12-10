from Repository import repository
from Product import product
from flask import Flask, jsonify, request

app = Flask(__name__)
repo = repository()

@app.route('/products', methods=['GET'])
def get_all_products():
    products = repo.fetch_all()
    return jsonify([product(*p).to_dict() for p in products])

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = repo.fetch_one(id)
    if product:
        return jsonify(product(*product).to_dict())
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = repo.create(data['name'], data['price'])
    return jsonify({'id': product_id}), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    if repo.fetch_one(id):
        repo.update(id, data['name'], data['price'])
        return jsonify({'message': 'Product updated'}), 200
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    if repo.fetch_one(id):
        repo.delete(id)
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'message': 'Product not found'}), 404