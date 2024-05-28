def squares_map(n):
    # Using dictionary comprehension to create the dictionary of squares
    return {i: i * i for i in range(1, n + 1)}


# Test cases
print(squares_map(10))  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(squares_map(5))  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares_map(1))  # Output: {1: 1}

