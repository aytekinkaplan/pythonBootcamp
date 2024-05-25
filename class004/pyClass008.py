def can_access_library(user_age):
    if user_age >= 18:
        return True
    else:
        return False


print(can_access_library(int(input("Enter your age: "))))


def is_happy(user_age):
    if user_age >= 18:
        return True
    else:
        return False


print(is_happy(int(input("Enter your age: "))))

