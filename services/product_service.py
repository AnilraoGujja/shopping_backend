from models.product_model import create_product, get_all_products, get_product_by_id, update_product, delete_product
def add_product(product_name, description, price, stock, category_id):
    create_product(product_name, description, price, stock, category_id)
    return {"message": "Product added successfully!"}

def fetch_all_products():
    return get_all_products()

def fetch_product_by_id(product_id):
    product = get_product_by_id(product_id)
    if product:
        return product
    else:
        return {"message": "Product not found!"}    
    
def edit_product(product_id, product_name, description, price, stock):
    if not get_product_by_id(product_id):
        return {"message": "Product not found!"}
    update_product(product_id, product_name, description, price, stock)
    return {"message": "Product updated successfully!"}

def remove_product(product_id):
    if not get_product_by_id(product_id):
        return {"message": "Product not found!"}
    delete_product(product_id)
    return {"message": "Product deleted successfully!"}

