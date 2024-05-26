def is_hex_string(string):
    # Check if the input string is empty
    if not string:
        return False

    # Valid hexadecimal characters
    hex_digits = '0123456789abcdefABCDEF'

    # Iterate through each character in the string
    for char in string:
        # Check if the character is not in the set of hex digits
        if char not in hex_digits:
            return False

    # If all characters are valid hex digits, return True
    return True


# Example usage:
print(is_hex_string('1a2f4C'))  # Output: True
print(is_hex_string('1g2f4C'))  # Output: False
print(is_hex_string(''))  # Output: False
