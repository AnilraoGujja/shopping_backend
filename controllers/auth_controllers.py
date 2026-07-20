from flask import request, jsonify
from services.auth_service import login_user, register_user 
from utils.auth_middleware import token_required

def register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')
    register_user(full_name, email, password, phone)
    return jsonify({
        "message": "User registered successfully!"
    }), 201


def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    result = login_user(email, password)
    if result["message"] == "login successfull":
        return jsonify(result), 200
    return jsonify(result), 401

@token_required
def profile(data):
    return jsonify({
        "message": "Profile fetched successfully!",
        "user": data
    }), 200