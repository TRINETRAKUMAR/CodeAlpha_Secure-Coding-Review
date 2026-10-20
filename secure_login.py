
# secure_login.py
# Educational demonstration of secure password handling

import hashlib
import hmac
import secrets
import getpass

# Demo account only. Production applications should use a database.
USERNAME = "student"

# Generate a random salt and hash a demo password.
# In production, use a vetted password-hashing library such as Argon2id.
SALT = secrets.token_bytes(16)
DEMO_PASSWORD_HASH = hashlib.pbkdf2_hmac(
    "sha256",
    b"DemoPass123!",
    SALT,
    600_000
)


def verify_password(password):
    candidate_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        SALT,
        600_000
    )
    return hmac.compare_digest(candidate_hash, DEMO_PASSWORD_HASH)


def login():
    username = input("Enter username: ").strip()

    if not username or len(username) > 50:
        print("Invalid input.")
        return

    password = getpass.getpass("Enter password: ")

    if len(password) > 128:
        print("Invalid username or password.")
        return

    if username == USERNAME and verify_password(password):
        print("Login successful!")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    login()
