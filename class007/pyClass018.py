def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False


# Example usage
print(login("admin", "password"))  # Output: True
print(login("user", "password"))  # Output: False
