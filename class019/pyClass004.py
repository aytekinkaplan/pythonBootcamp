def count_characters(input_string):
    # Initialize an empty dictionary to store character counts
    char_occurrences = {}

    # Iterate over each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_occurrences:
            char_occurrences[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_occurrences[char] = 1

    # Return the dictionary containing character counts
    return char_occurrences


# Test cases
print(count_characters("apple"))  # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
print(count_characters("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}
print(count_characters("This is an awesome occasion."))
# Output: {'T': 1, 'h': 1, 'i': 3, 's': 4, ' ': 4, 'a': 3, 'n': 2, 'w': 1, 'e': 2, 'o': 3, 'm': 1, 'c': 2, '.': 1}

