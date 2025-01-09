import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    conn = sqlite3.connect(('./database/magazine.db'))
    conn.row_factory = sqlite3.Row
    return conn

# Utility function to execute queries
def execute_query(query, params=()):
    conn = sqlite3.connect(('./database/magazine.db'))
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    return cursor
