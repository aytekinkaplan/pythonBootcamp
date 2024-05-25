print("Hello World!")
print(type(42))
print(type("Hello World!"))

message = "Hello World!"
print(message)

message = "Goodbye World!"
print(message)

message = "Hello World!"
message = "Goodbye World!"
print(message)

message = "Hello World!"
print(message)

print(message.upper())
print(message)
message = message.upper()
print(message)
message = message.lower()
print(message)
message = message.title()
print(message)
print(message.lower())
message = message.lower()
print(message)
message = message.capitalize()
print(message)
message = message.title()
print(message)
print(message.islower())
print(message.isupper())
message = message.lower()
print(message.islower())
print(message.isupper())
message = message.upper()
print(message.isupper())
print(message.islower())

print('123'.isdigit())  # Output: True
print('A23'.isdigit())  # Output: False
print('2 3'.isdigit())  # Output: False
print('23'.isdigit())  # Output: True

print('23'.isalpha())  # Output: False
print('2A'.isalpha())  # Output: False
print('ABC'.isalpha())  # Output: True
print('ABC123'.isalnum())  # Output: True
print('ABC 123'.isalnum())  # Output: False

print('Hello World'.endswith('World'))  # Output: True
print('Hello World'.endswith('ld'))  # Output: True
print('Hello World'.endswith('old'))  # Output: False
print('Hello World'.endswith('Wo'))  # Output: False
print('Hello World'.startswith('Wo'))  # Output: False
print('Hello World'.startswith('He'))  # Output: True
print('Hello World'.startswith('Hell0'))  # Output: False
print('Hello World'.startswith('Hello'))  # Output: True

print('Hello World'.find('Hello'))  # Output: 0
print('Hello World'.find('ello'))  # Output: 1
print('Hello World'.find('Ello'))  # Output: -1
print('Hello World'.find('bello'))  # Output: -1
print('Hello World'.find('Ello'))  # Output: -1

print('Hello' in 'Hello World')  # Output: True
print('ello' in 'Hello World')  # Output: True
print('Ello' in 'Hello World')  # Output: False
print('bello' in 'Hello World')  # Output: False
