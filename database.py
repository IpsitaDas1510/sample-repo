import sqlite3
from datetime import datetime

DB_FILE = 'students.db'

def get_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_database():
    """Initialize database and create tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL,
            year TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✓ Database initialized")

    # READ
def get_all_students():
    """Get all students"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM students ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert Row objects to dictionaries
    students = []
    for row in rows:
        students.append(dict(row))
    
    return students