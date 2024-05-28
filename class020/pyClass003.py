def swap_elements(input_tuple):
    if len(input_tuple) < 2:
        raise ValueError("The input tuple must have at least two elements.")

    # Create a new tuple with the first and last elements swapped
    swapped_tuple = (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)
    return swapped_tuple


# Testing the function with the given examples
print(swap_elements((1, 2, 3, 4)))  # Output: (4, 2, 3, 1)
print(swap_elements((7, 14, 21, 28)))  # Output: (28, 14, 21, 7)
print(swap_elements(('apple', 'banana', 'cherry')))  # Output: ('cherry', 'banana', 'apple')
print(swap_elements((5, 10)))  # Output: (10, 5)

