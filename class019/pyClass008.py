data = {'x': 10, 'y': 20, 'z': 30}
print(data.get('w', 40))

data = {'x': 10, 'y': 20, 'z': 30}
print(data.get('w'))
# Creating a dictionary
occurances = {'a': 5, 'b': 6, 'c': 8}

# Accessing an existing key using get
print(occurances.get('a'))  # Output: 5

# Accessing a non-existent key using get without a default value
print(occurances.get('d'))  # Output: None

# Accessing a non-existent key using get with a default value
print(occurances.get('d', 10))  # Output: 10
print(occurances.get('a'))  # Output: 5

