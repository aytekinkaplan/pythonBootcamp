def search_element(list_2D, target):
    # Traverse each row
    for i, row in enumerate(list_2D):
        # Traverse each column in the current row
        for j, value in enumerate(row):
            # Check if the current value is the target
            if value == target:
                return i, j
    # Return (-1, -1) if the target is not found
    return -1, -1


# Test the function with example inputs
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  # Output: (1, 1)
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10))  # Output: (-1, -1)
