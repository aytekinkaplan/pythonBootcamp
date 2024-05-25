# Comparing Numbers
print(1 == 1)  # Output: True
print(1 == 2)  # Output: False

print(1 != 1)  # Output: False
print(1 != 2)  # Output: True

print(1 > 1)  # Output: False
print(1 > 2)  # Output: False

print(1 < 1)  # Output: False
print(1 < 2)  # Output: True

print(1 >= 1)  # Output: True
print(1 >= 2)  # Output: False

print(1 <= 1)  # Output: True
print(1 <= 2)  # Output: True

# `is` should not be used for comparing values, but rather object identity
print(1 is 1)  # Output: True (small integers are cached, so it's True)
print(1 is 2)  # Output: False

# `in` is used for iterable objects, not individual numbers
print(1 in [1])  # Output: True
print(1 in [2])  # Output: False
