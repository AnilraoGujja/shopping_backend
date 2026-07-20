from models.category_model import create_category, get_all_categories, get_category_by_id, update_category, delete_category
def add_category(category_name):
    create_category(category_name)
    return {"message": "Category added successfully!"}

def fetch_all_categories():
    return get_all_categories()

def fetch_category_by_id(category_id):
    category = get_category_by_id(category_id)
    if category:
        return category
    else:
        return {"message": "Category not found!"}

def edit_category(category_id, category_name):
    if not get_category_by_id(category_id):
        return {"message": "Category not found!"}
    update_category(category_id, category_name)
    return {"message": "Category updated successfully!"}

def remove_category(category_id):
    if not get_category_by_id(category_id):
        return {"message": "Category not found!"}
    delete_category(category_id)
    return {"message": "Category deleted successfully!"}

