# Secure Coding Review 

## 📌 Project Overview
This project demonstrates security vulnerabilities in a login system and how to fix them using secure coding practices.

---

## 🔴 Vulnerable Application
The vulnerable version of the application is prone to **SQL Injection attacks**.

### Example Attack:
Username: ' OR '1'='1' --
Password: anything

---

### Result:
✔ Login Successful (Unauthorized Access)

### Issues:
- SQL Injection vulnerability
- Plain text password storage
- No input validation
- No logging mechanism

---

## 🟢 Secure Application
The secure version fixes these issues using:

- Parameterized queries (prevents SQL Injection)
- Password hashing (SHA-256)
- Secure password input (getpass)
- Logging of login attempts

---

## 🔐 Security Improvements
| Vulnerability | Fix |
|--------------|-----|
| SQL Injection | Parameterized Queries |
| Plain Password | Hashing |
| Visible Input | getpass |
| No Logging | Log File |

---

## 🛠 Tools Used
- Python
- SQLite
- Hashlib
- Scapy (previous task)

---

## ▶ How to Run

### Step 1: Setup Database

python setup_db.py


### Step 2: Run Vulnerable App

python vulnerable_app.py


### Step 3: Run Secure App

python secure_app.py

## ▶ How to Run

### Step 1: Setup Database

---

## 🎯 Learning Outcome
This project helped me understand:
- How SQL Injection attacks work
- Importance of secure coding practices
- Real-world authentication vulnerabilities

---

## 🔗 Internship
Completed as part of CodeAlpha Cyber Security Internship
