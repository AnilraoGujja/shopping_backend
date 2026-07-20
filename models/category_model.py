from database.db import get_connection

def create_category(category_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO categories (category_name)
    VALUES (%s)
    """
    cursor.execute(query, (category_name,))
    conn.commit()

    cursor.close()
    conn.close()

def get_all_categories():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()

    cursor.close()
    conn.close()
    return categories

def get_category_by_id(category_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM categories WHERE category_id = %s"
    cursor.execute(query, (category_id,))
    category = cursor.fetchone()

    cursor.close()
    conn.close()
    return category     

def update_category(category_id, category_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE categories
    SET category_name = %s
    WHERE category_id = %s
    """
    cursor.execute(query, (category_name, category_id))
    conn.commit()

    cursor.close()
    conn.close()

def delete_category(category_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM categories WHERE category_id = %s"
    cursor.execute(query, (category_id,))
    conn.commit()

    cursor.close()
    conn.close()    

