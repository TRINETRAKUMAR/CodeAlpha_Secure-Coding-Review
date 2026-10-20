# Task 3: Secure Coding Review

## 1. Project Overview

**Project Name:** Secure Coding Review of a Python Login System  
**Programming Language:** Python  
**Application:** Basic Login System  
**Security Tool:** Bandit Static Analyzer  
**Review Method:** Manual Code Inspection and Static Analysis

### Objective

The objective of this project is to identify security vulnerabilities in a basic Python login application, understand their risks, implement safer coding practices, and document the remediation process.

## 2. Scope of Review

The review focuses on:
- Credential management
- Password storage and verification
- User input validation
- Authentication error handling
- Static security analysis

## 3. Security Findings

### Finding 1: Hardcoded Credentials

**Severity:** High  
**File:** `insecure_login.py`

**Description:**  
The username and password are directly written in the source code.

**Risk:**  
Anyone who gains access to the source code may discover the credentials and use them to access the application.

**Remediation:**  
Never hardcode production credentials. Use an appropriate secret-management system and store password verifiers securely.

### Finding 2: Insecure Password Storage

**Severity:** High  
**File:** `insecure_login.py`

**Description:**  
The application compares the supplied password directly with a plaintext password.

**Risk:**  
Plaintext credentials can be exposed if the code or configuration is disclosed.

**Remediation:**  
Use a vetted password-hashing algorithm such as Argon2id, with a unique salt for each password. Never store plaintext passwords.

### Finding 3: Insufficient Input Validation

**Severity:** Medium  
**File:** `insecure_login.py`

**Description:**  
The original application does not impose basic length limits on user input.

**Risk:**  
Unexpected or excessively large inputs may affect application reliability and could contribute to security problems.

**Remediation:**  
Validate input length and format, handle invalid input safely, and enforce limits on the server side.

### Finding 4: No Login Rate Limiting

**Severity:** Medium  
**File:** `insecure_login.py`

**Description:**  
The original application does not limit repeated login attempts.

**Risk:**  
Automated password-guessing attempts may be made repeatedly.

**Remediation:**  
Implement server-side rate limiting, monitoring, and appropriate temporary delays or account protections.

## 4. Remediation Implemented

The revised `secure_login.py` demonstrates:
- Password hashing using PBKDF2-HMAC-SHA256.
- Random salt generation.
- Constant-time hash comparison.
- Basic username and password length validation.
- Masked password input.
- Generic authentication failure messages.

**Limitation:** The revised program is an educational demonstration. Persistent credential storage, production-grade password hashing configuration, rate limiting, secure sessions, and account recovery controls must be added before deployment.

## 5. Testing Plan

| Test Case | Expected Result |
|---|---|
| Correct demo username and password | Login successful |
| Incorrect password | Login rejected |
| Incorrect username | Login rejected |
| Empty username | Input rejected |
| Username exceeding the allowed length | Input rejected |
| Password exceeding the allowed length | Login rejected |

Tests should be executed on both versions, and actual results should be recorded after execution.

## 6. Static Analysis

Bandit was selected to scan the Python source code for common security issues.

Commands used:

`python -m bandit -r insecure_login.py`

`python -m bandit -r secure_login.py`

The actual scanner output should be reviewed and saved with the project. Static analysis supports manual code review but does not guarantee that all vulnerabilities have been found.

## 7. Secure Coding Recommendations

1. Never hardcode passwords, API keys, or other secrets.
2. Use a vetted password-hashing library and unique salts.
3. Validate and limit untrusted input.
4. Apply server-side login rate limiting.
5. Avoid revealing whether a username or password was incorrect.
6. Keep dependencies updated and scan code regularly.
7. Use HTTPS and secure session management in web applications.
8. Review security findings and retest after every fix.

## 8. Conclusion

This project demonstrates how manual inspection and static analysis can help identify common security weaknesses in a Python login application. The revised example introduces safer password handling and basic input validation. Additional controls and testing are required before using a login system in a real application.

## 9. Tools and Technologies

- Python
- Visual Studio Code
- Bandit
- Git
- GitHub
