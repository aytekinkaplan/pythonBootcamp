# Create a list of squares of numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of cubes of numbers from 0 to 9
cubes = [x ** 3 for x in range(10)]
print(cubes)  # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Create a list of odd numbers from 0 to 9
odds = [x for x in range(10) if x % 2 != 0]
print(odds)  # Output: [1, 3, 5, 7, 9]

# Convert a string to a list of characters
char_list = list("hello")
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# Convert a string to a list of characters
char_list = list("Hello World!")
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert a tuple to a list
tuple_data = (1, 2, 3, 4)
list_from_tuple = list(tuple_data)
print(list_from_tuple)  # Output: [1, 2, 3, 4]

# Convert a set to a list
set_data = {1, 2, 3, 4}
list_from_set = list(set_data)
print(list_from_set)  # Output: [1, 2, 3, 4]

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of squares of numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of numbers from 5 to 14 with a step of 2
numbers = list(range(5, 15, 2))
print(numbers)  # Output: [5, 7, 9, 11, 13]

# Create a list with 10 zeros
zeros = [0] * 10
print(zeros)  # Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Create a list of strings representing numbers 0 to 9
number_strings = [str(num) for num in range(10)]
print(number_strings)  # Output: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
