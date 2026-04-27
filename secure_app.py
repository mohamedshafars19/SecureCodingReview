import sqlite3
import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ").strip()
password = getpass.getpass("Enter password: ").strip()

hashed_password = hash_password(password)

# ✅ Prevent SQL Injection using parameterized query
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, hashed_password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

# ✅ Logging attempts
with open("security_log.txt", "a") as log:
    log.write(f"Login attempt for user: {username}\n")

conn.close()