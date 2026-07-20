from functools import wraps
from flask import request, jsonify
import jwt
from utils.jwt_helper import SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            token = token.split(" ")[1]  # Assuming the token is in the format "Bearer <token>"
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": "Token is invalid!", "error": str(e)}), 401
    return decorated