def is_list_sorted(lst):
    # Check for Empty List
    if not lst:
        return True

    # Iterate and Compare
    for i in range(1, len(lst)):
        # Element Comparison
        if lst[i - 1] > lst[i]:
            return False

    # Concluding the Loop
    return True


# Test cases
print(is_list_sorted([10, 20, 30]))  # Output: True
print(is_list_sorted([10, 30, 20]))  # Output: False
print(is_list_sorted([30, 20, 10]))  # Output: False
print(is_list_sorted([]))  # Output: True


def reverse_list(lst):
    # Initialize pointers
    start = 0
    end = len(lst) - 1

    # Loop until start pointer is less than end pointer
    while start < end:
        # Exchange elements at positions start and end
        lst[start], lst[end] = lst[end], lst[start]

        # Move pointers
        start += 1
        end -= 1

    # Return reversed list
    return lst


# Testing the function with examples
print(reverse_list([10, 20, 30]))  # Output: [30, 20, 10]
print(reverse_list([5, 15, 25, 35]))  # Output: [35, 25, 15, 5]
print(reverse_list([1]))  # Output: [1]

