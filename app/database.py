import sqlite3

def get_db_connection():

    conn = sqlite3.connect('rules.db')
    conn.row_factory = sqlite3.Row  # Enables access by column name
    return conn

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create a table for storing rules if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
