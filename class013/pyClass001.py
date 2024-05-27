# Introduction To List Slicing

# Create a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the list
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list
sliced_list = numbers[2:6]
print(sliced_list)  # Output: [3, 4, 5, 6]

# Reverse the list
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Concatenate the list
concatenated_list = numbers + sliced_list
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6]

# Repeat the list
repeated_list = numbers * 3
print(repeated_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

# Sort the list
sorted_list = sorted(numbers)
print(sorted_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Reverse the list
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Find the length of the list
length = len(numbers)
print(length)  # Output: 10

# Check if the list is empty
is_empty = not numbers
print(is_empty)  # Output: False

# Check if the list is not empty
is_not_empty = numbers
print(is_not_empty)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Clear the list
numbers.clear()
print(numbers)  # Output: []