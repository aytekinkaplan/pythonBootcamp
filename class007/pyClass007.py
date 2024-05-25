# Comparing None
print(None == None)  # Output: True
print(None == 0)  # Output: False

print(None != None)  # Output: False
print(None != 0)  # Output: True

# NoneType cannot be ordered, so comparisons will raise an error
# print(None > None)  # Raises TypeError
# print(None > 0)  # Raises TypeError

# print(None < None)  # Raises TypeError
# print(None < 0)  # Raises TypeError

print(None >= None)  # Output: True (Python 3.9+)
print(None >= 0)  # Raises TypeError

print(None <= None)  # Output: True (Python 3.9+)
print(None <= 0)  # Raises TypeError

print(None is None)  # Output: True
print(None is 0)  # Output: False

# `in` does not apply to None
print(None in [None])  # Output: True
print(None in [0])  # Output: False

# `not in` checks if an element is not in an iterable
print(None not in [None])  # Output: False
print(None not in [0])  # Output: True

# `is not` checks for inequality
print(None is not None)  # Output: False
print(None is not 0)  # Output: True