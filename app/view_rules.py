import sqlite3

def get_db_connection():
    conn = sqlite3.connect('rules.db')
    conn.row_factory = sqlite3.Row
    return conn

def view_rules():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM rules')
    rules = cursor.fetchall()

    for rule in rules:
        print(f"ID: {rule['id']}, Rule: {rule['rule_string']}")

    cursor.close()
    connection.close()

if __name__ == '__main__':
    view_rules()
