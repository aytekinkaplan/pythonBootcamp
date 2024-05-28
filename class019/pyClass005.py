def count_words(input_string):
    # Initialize an empty dictionary to store word counts
    word_occurrences = {}

    # Split the input string into words using split() method
    words = input_string.split()

    # Iterate over each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_occurrences:
            word_occurrences[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_occurrences[word] = 1

    # Return the dictionary containing word counts
    return word_occurrences


# Test cases
print(count_words("This is an example."))
# Output: {'This': 1, 'is': 1, 'an': 1, 'example.': 1}

print(count_words("Hello world! Hello everyone."))
# Output: {'Hello': 2, 'world!': 1, 'everyone.': 1}

print(count_words("This is an awesome occasion. This has never happened before."))
# Output: {'This': 2, 'is': 1, 'an': 1, 'awesome': 1, 'occasion.': 1, 'has': 1, 'never': 1, 'happened': 1, 'before.': 1}
