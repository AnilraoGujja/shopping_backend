from flask import request, jsonify
from services.product_service import add_product, fetch_all_products, fetch_product_by_id, edit_product, remove_product

def create_product():
    data = request.get_json()
    product_name = data.get('product_name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    category_id = data.get('category_id')
    result = add_product(product_name, description, price, stock, category_id)
    return jsonify(result), 201

def get_products():
    products = fetch_all_products()
    return jsonify(products), 200   

def get_product(product_id):
    result = fetch_product_by_id(product_id)
    if "message" in result :
        return jsonify(result), 404
    return jsonify(result), 200

def update_product(product_id):
    data = request.get_json()
    product_name = data.get('product_name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    result = edit_product(product_id, product_name, description, price, stock)
    if result["message"] == "Product not found!":
        return jsonify(result), 404
    return jsonify(result), 200

def delete_product(product_id):
    result = remove_product(product_id)
    if result["message"] == "Product not found!":
        return jsonify(result), 404
    return jsonify(result), 200