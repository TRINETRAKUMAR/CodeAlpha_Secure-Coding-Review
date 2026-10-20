
# insecure_login.py
# Intentionally vulnerable example for security review only

USERNAME = "admin"
PASSWORD = "admin123"  # Vulnerability: hardcoded password


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Vulnerability: password compared directly
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    login()
