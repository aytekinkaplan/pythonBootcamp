def login(username, password):
    pass


# Example usage
print(login("admin", "password"))  # Output: True
print(login("user", "password"))  # Output: False


def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False


# Example usage
print(login("admin", "password"))  # Output: True
print(login("user", "password"))  # Output: False


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def login(self):
        pass

    def logout(self):
        pass

    def select_product(self, product):
        pass
