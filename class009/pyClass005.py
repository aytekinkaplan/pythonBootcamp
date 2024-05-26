def find_factors(number):
    # Initialize list to store factors
    factors = []

    # Loop through numbers from 1 to number
    for i in range(1, number + 1):
        # Check if i divides number evenly
        if number % i == 0:
            factors.append(i)

    # Return list of factors
    return factors


# Test cases
print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(find_factors(15))  # Output: [1, 3, 5, 15]
print(find_factors(7))  # Output: [1, 7]
