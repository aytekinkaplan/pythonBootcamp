def reverse_chunks(numbers):
    # Loop through the list in steps of 3
    for i in range(0, len(numbers), 3):
        # Reverse the chunk of three elements
        numbers[i:i + 3] = numbers[i:i + 3][::-1]
    return numbers


# Example usage
print(reverse_chunks([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]
