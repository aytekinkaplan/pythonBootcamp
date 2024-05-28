def count_occurrences(input_tuple, target):
    return input_tuple.count(target)


# Test the function with the given example
print(count_occurrences((1, 2, 2, 3, 2), 2))  # Expected Output: 3

# Test the function with an empty tuple
print(count_occurrences((), 2))  # Expected Output: 0
