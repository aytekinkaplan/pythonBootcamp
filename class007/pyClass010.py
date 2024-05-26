def count_uppercase_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count


# Example usage:
text = "Hello, World!"
result = count_uppercase_letters(text)
print(result)
