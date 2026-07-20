from models.user_model import create_user, get_user_by_email
from utils.jwt_helper import generate_token
def register_user(full_name, email, password, phone):
    create_user(full_name, email, password, phone)

def login_user(email, password):
    user = get_user_by_email(email)

    if user and user["password"] == password:
        token = generate_token(user)

        return {
            "message": "login successfull",
            "token": token,
            "user":{
                "user_id": user["user_id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "phone": user["phone"]
            }
        }
    return{
        "message":"invalid email or password bro"
    }