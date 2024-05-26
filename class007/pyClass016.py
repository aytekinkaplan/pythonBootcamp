# Word Reverser using For Loop

# Define a function to reverse words in a string using for loop
def reverse_words(text):
    words = text.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)


# Example usage
text = "Hello, World!"
reversed_text = reverse_words(text)
print(reversed_text)
