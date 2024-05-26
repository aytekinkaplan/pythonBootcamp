def find_multiples(number, limit):
    # Initialize a list to store the multiples
    multiples = []

    # Loop to find multiples of the number that are less than the limit
    for i in range(number, limit, number):
        multiples.append(i)

    # Return the list of multiples
    return multiples


# Testing the function
print(find_multiples(3, 10))  # Expected Output: [3, 6, 9]
print(find_multiples(5, 22))  # Expected Output: [5, 10, 15, 20]
print(find_multiples(7, 50))  # Expected Output: [7, 14, 21, 28, 35, 42, 49]
print(find_multiples(4, 4))  # Expected Output: []
print(find_multiples(10, 5))  # Expected Output: []
