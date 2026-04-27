import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert sample user
username = "admin"
password = "admin123"

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

conn.commit()
conn.close()

print("Database and table created successfully!")