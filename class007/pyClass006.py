# Comparing Booleans
print(True == True)  # Output: True
print(True == False)  # Output: False

print(True != True)  # Output: False
print(True != False)  # Output: True

print(True > True)  # Output: False
print(True > False)  # Output: True

print(True < True)  # Output: False
print(True < False)  # Output: False

print(True >= True)  # Output: True
print(True >= False)  # Output: True

print(True <= True)  # Output: True
print(True <= False)  # Output: False

print(True is True)  # Output: True
print(True is False)  # Output: False

# `in` does not apply to booleans
print(True in [True])  # Output: True
print(True in [False])  # Output: False

# `not in` checks if an element is not in an iterable
print(True not in [True])  # Output: False
print(True not in [False])  # Output: True
