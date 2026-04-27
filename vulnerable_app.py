import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

# ❌ SQL Injection vulnerability
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()