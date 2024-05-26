def has_consecutive_identical_characters(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False


# Example usage:
text = "Hello, World!"
result = has_consecutive_identical_characters(text)
print(result)
