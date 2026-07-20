from flask import Blueprint
from controllers.product_controllers import create_product, get_products, get_product, update_product, delete_product
from utils.auth_middleware import token_required

product_bp = Blueprint('product', __name__)

product_bp.route('/products', methods=['POST'])(token_required(create_product))
product_bp.route('/products', methods=['GET'])(token_required(get_products))
product_bp.route('/products/<int:product_id>', methods=['GET'])(token_required(get_product))
product_bp.route('/products/<int:product_id>', methods=['PUT'])(token_required(update_product))
product_bp.route('/products/<int:product_id>', methods=['DELETE'])(token_required(delete_product))


