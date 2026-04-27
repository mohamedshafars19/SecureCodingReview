Secure Coding Review Report

Project: Login System using SQLite

1. SQL Injection Vulnerability
Issue: User input directly included in SQL query.
Risk: Attackers can bypass authentication using malicious input.
Fix: Use parameterized queries.

2. Plain Text Password Storage
Issue: Passwords stored without encryption.
Risk: Data breach exposes all user credentials.
Fix: Use hashing algorithms like SHA-256.

3. Insecure Password Input
Issue: Password visible during input.
Risk: Shoulder surfing attack.
Fix: Use getpass module.

4. Lack of Input Validation
Issue: No checks on user input.
Risk: Allows malicious payloads.
Fix: Validate and sanitize inputs.

5. No Logging Mechanism
Issue: No monitoring of login attempts.
Risk: Attacks go undetected.
Fix: Implement logging system.

Conclusion:
The vulnerable system was exposed to multiple high-risk security threats. The secure version mitigates these issues using parameterized queries, password hashing, secure input handling, and logging.