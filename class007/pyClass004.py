# Comparing Strings
print("Hello" == "Hello")  # Output: True
print("Hello" == "hello")  # Output: False

print("Hello" != "Hello")  # Output: False
print("Hello" != "hello")  # Output: True

print("Hello" > "Hello")  # Output: False
print("Hello" > "hello")  # Output: False

print("Hello" < "Hello")  # Output: False
print("Hello" < "hello")  # Output: True

print("Hello" >= "Hello")  # Output: True
print("Hello" >= "hello")  # Output: False

print("Hello" <= "Hello")  # Output: True
print("Hello" <= "hello")  # Output: True

# `is` checks for identity, which means it checks if both variables point to the same object
print("Hello" is "Hello")  # Output: True (strings are interned, so it's True in most cases)
print("Hello" is "hello")  # Output: False

# `in` checks for substring
print("Hello" in "Hello")  # Output: True
print("Hello" in "hello")  # Output: False

# `not in` checks if a string is not a substring
print("Hello" not in "Hello")  # Output: False
print("Hello" not in "hello")  # Output: True
