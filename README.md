# Secure Coding Review

A beginner-friendly cybersecurity project that reviews a Python login application, identifies common security weaknesses, and demonstrates safer coding practices.

## Features

- Manual source code review
- Hardcoded credential identification
- Password hashing demonstration
- Basic input validation
- Bandit static analysis
- Security findings and remediation report

## Project Structure

- `insecure_login.py` — intentionally vulnerable learning example
- `secure_login.py` — improved educational example
- `security_report.md` — findings, risks, and remediation recommendations
- `README.md` — project overview

## Requirements

- Python 3
- Visual Studio Code
- Bandit

## Installation

Install Bandit:

```bash
python -m pip install bandit
```

## Run the Examples

```bash
python insecure_login.py
python secure_login.py
```

## Run Security Analysis

```bash
python -m bandit -r insecure_login.py
python -m bandit -r secure_login.py
```

## Disclaimer

The vulnerable program is intentionally insecure and is intended only for local educational testing. The secure example is a demonstration, not a production-ready authentication system.

## Author

Add your name here.
