from flask import Blueprint
from controllers.category_controllers import create_category, get_categories, get_category, update_category, delete_category
from utils.auth_middleware import token_required

category_bp = Blueprint('category', __name__)

category_bp.route('/categories', methods=['POST'])(token_required(create_category))
category_bp.route('/categories', methods=['GET'])(token_required(get_categories))
category_bp.route('/categories/<int:category_id>', methods=['GET'])(token_required(get_category))
category_bp.route('/categories/<int:category_id>', methods=['PUT'])(token_required(update_category))
category_bp.route('/categories/<int:category_id>', methods=['DELETE'])(token_required(delete_category))