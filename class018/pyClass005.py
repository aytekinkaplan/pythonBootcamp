def find_intersection(num1, num2, limit):
    # If either number is zero, return an empty set
    if num1 == 0 or num2 == 0:
        return set()

    # Generate multiples of num1 up to the limit
    multiples_num1 = {i for i in range(num1, limit + 1, num1)}

    # Generate multiples of num2 up to the limit
    multiples_num2 = {i for i in range(num2, limit + 1, num2)}

    # Compute the intersection of the two sets
    intersection = multiples_num1 & multiples_num2

    # Return the intersection set
    return intersection


# Example usage
print(find_intersection(4, 6, 30))  # Output: {12, 24}
print(find_intersection(3, 5, 20))  # Output: {15}
