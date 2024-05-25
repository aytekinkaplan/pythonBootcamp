# Coding Exercise: Find Last Digit of a Number
# Write a program that reads a number and prints its last digit.

number = int(input("Enter a number: "))

last_digit = number % 10

print("The last digit of", number, "is", last_digit)

print(True and True)   # Output: True
print(False and True)  # Output: False
print(False and False) # Output: False

is_admin = True
has_permission = False
can_delete = is_admin and has_permission
print(can_delete)  # Output: False

print(True or False)   # Output: True
print(False or True)   # Output: True
print(True or True)    # Output: True
print(False or False)  # Output: False

can_read = True
can_write = False
can_access = can_read or can_write
print(can_access)  # Output: True

print(not True)   # Output: False
print(not False)  # Output: True

is_logged_in = False
is_guest = not is_logged_in
print(is_guest)  # Output: True

print(True ^ True)   # Output: False
print(True ^ False)  # Output: True
print(False ^ True)  # Output: True
print(False ^ False) # Output: False

feature_a = True
feature_b = False
one_feature_enabled = feature_a ^ feature_b
print(one_feature_enabled)  # Output: True

a = True
b = False
c = True

# Combining `and`, `or`, and `not` operators
result = (a and not b) or c
print(result)  # Output: True

# Combining `and` and `^` operators
result = (a and b) ^ c
print(result)  # Output: True
