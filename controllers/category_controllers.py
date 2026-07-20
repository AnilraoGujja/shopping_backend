from flask import request, jsonify
from services.category_service import add_category, fetch_all_categories, fetch_category_by_id, edit_category, remove_category  

def create_category():
    data = request.get_json()
    category_name = data.get('category_name')
    result = add_category(category_name)
    return jsonify(result), 201

def get_categories():
    categories = fetch_all_categories()
    return jsonify(categories), 200

def get_category(category_id):
    result = fetch_category_by_id(category_id)
    if "message" in result:
        return jsonify(result), 404
    return jsonify(result), 200

def update_category(category_id):
    data = request.get_json()
    category_name = data.get('category_name')
    result = edit_category(category_id, category_name)
    if result["message"] == "Category not found!":
        return jsonify(result), 404
    return jsonify(result), 200

def delete_category(category_id):
    result = remove_category(category_id)
    if result["message"] == "Category not found!":
        return jsonify(result), 404
    return jsonify(result), 200 