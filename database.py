import sqlite3
from datetime import datetime

DB_FILE = 'students.db'

def get_connection():
    """Get database connection""""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row 
    return conn
    