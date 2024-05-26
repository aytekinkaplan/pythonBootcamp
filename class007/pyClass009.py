def is_vowel(char):
    vowel_string = 'aeiouAEIOU'
    return char in vowel_string

# Example usage:
print(is_vowel('a'))  # Output: True
print(is_vowel('b'))  # Output: False
print(is_vowel('A'))  # Output: True
print(is_vowel('E'))  # Output: True
print(is_vowel('z'))  # Output: False
