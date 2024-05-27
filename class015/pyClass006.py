def slice_and_double(numbers, a, b):
    # Adjust out-of-bounds indices
    a = max(0, a)
    b = min(len(numbers), b)

    # Create the resulting list by combining three parts
    # 1. The part before the slice
    before_slice = numbers[:a]
    # 2. The doubled slice
    doubled_slice = [x * 2 for x in numbers[a:b]]
    # 3. The part after the slice
    after_slice = numbers[b:]

    # Combine all parts and return the result
    return before_slice + doubled_slice + after_slice


# Example usage
print(slice_and_double([1, 2, 3, 4, 5], 1, 4))  # Output: [1, 4, 6, 8, 5]
print(slice_and_double([10, 11, 12], 0, 2))  # Output: [20, 22, 12]
print(slice_and_double([7, 8, 9, 10], 1, 5))  # Output: [7, 16, 18, 20]
print(slice_and_double([3, 6, 9, 12], -1, 3))  # Output: [6, 12, 18, 12]
print(slice_and_double([15, 20, 25, 30], 2, 10))  # Output: [15, 20, 50, 60]
