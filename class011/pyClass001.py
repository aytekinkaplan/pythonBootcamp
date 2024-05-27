def rotate_strings(strings, n):
    """
    Rotates a list of strings 'n' times to the right.

    Args:
        strings: A list of strings.
        n: A positive integer representing the number of rotations.

    Returns:
        A new list containing the rotated strings.
    """
    # Handle edge cases
    if not strings or n == 0:
        return strings

    # Rotate the list n times
    for _ in range(n):
        last_element = strings[-1]
        for i in range(len(strings) - 1, 0, -1):
            strings[i] = strings[i - 1]
        strings[0] = last_element

    return strings


# Example usage
strings = ["hello", "world", "python"]
n = 3
rotated_strings = rotate_strings(strings, n)
print(rotated_strings)