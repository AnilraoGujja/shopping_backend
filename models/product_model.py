from database.db import get_connection

def create_product(product_name, description, price, stock, category_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO products (product_name, description, price, stock, category_id)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (product_name, description, price, stock, category_id))
    conn.commit()

    cursor.close()
    conn.close()

def  get_all_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    cursor.close()
    conn.close()
    return product

def update_product(product_id, product_name, description, price, stock):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE products
    SET product_name = %s, description = %s, price = %s, stock = %s
    WHERE product_id = %s
    """
    cursor.execute(query, (product_name, description, price, stock, product_id))
    conn.commit()

    cursor.close()
    conn.close()

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()

    cursor.close()
    conn.close()