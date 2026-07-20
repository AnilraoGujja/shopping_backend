from flask import Flask
from database.db import get_connection
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.category_routes import category_bp  


app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(category_bp)

@app.route('/')
def home():
    try:
        conn = get_connection()
        conn.close()
        return {"message": "Database connection successfully!"}
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == '__main__':
    app.run(debug=True)