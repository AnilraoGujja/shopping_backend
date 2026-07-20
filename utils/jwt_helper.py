import jwt
import datetime

SECRET_KEY = "my_secret_key" 
 # Replace with your own secret key for production

def generate_token(user):
    payload = {
        "user_id": user["user_id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token expiration time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token