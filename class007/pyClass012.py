def find_right_most_digit(text):
    # Iterate through the characters of the text in reverse order
    for char in reversed(text):
        # Check if the character is a digit
        if char.isdigit():
            # Return the digit as an integer
            return int(char)
    # If no digit is found, return -1
    return -1

# Example usage:
print(find_right_most_digit('The value is 42'))  # Output: 2
print(find_right_most_digit('No digits here'))  # Output: -1
print(find_right_most_digit('abc123'))  # Output: 3
print(find_right_most_digit('123abc'))  # Output: 3
print(find_right_most_digit('abc'))  # Output: -1

