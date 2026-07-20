from database.db import get_connection
def create_user(full_name, email, password, phone):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO users (full_name, email, password, phone)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (full_name, email, password, phone))
    conn.commit()

    cursor.close()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE email =%s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user