def find_longest_word(text):
    # Split the text into words
    words = text.split()

    # Initialize the longest word as an empty string
    longest_word = ''

    # Iterate through the words
    for word in words:
        # Check if the current word is longer than the longest word found so far
        if len(word) > len(longest_word):
            longest_word = word

    # Return the longest word found
    return longest_word


# Example usage:
print(find_longest_word('The quick brown fox jumps over the lazy dog'))  # Output: 'quick'
print(find_longest_word(''))  # Output: ''
print(find_longest_word('A journey of a thousand miles begins with a single step'))  # Output: 'thousand'
print(find_longest_word('To be or not to be, that is the question'))  # Output: 'question'
print(find_longest_word('Short and sweet'))  # Output: 'Short'
