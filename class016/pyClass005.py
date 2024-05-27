def binary_search(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Example usage
# Example 1: Search in a list of sorted numbers
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
print("Found at index:", result)  # Output: Found at index: 3

# Example 2: Search for a nonexistent element
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
print("Found at index:", result)  # Output: Found at index: None

# Example 3: Search in an empty list
result = binary_search([], 4)
print("Found at index:", result)  # Output: Found at index: None
