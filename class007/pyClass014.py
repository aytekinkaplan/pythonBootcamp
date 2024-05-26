def is_anagram(string1, string2):
    # Sort both strings and compare them
    return sorted(string1) == sorted(string2)


# Example usage:
print(is_anagram('listen', 'silent'))  # Output: True
print(is_anagram('hello', 'world'))  # Output: False
print(is_anagram('rat', 'tar'))  # Output: True
print(is_anagram('evil', 'vile'))  # Output: True
print(is_anagram('fluster', 'restful'))  # Output: True
print(is_anagram('binary', 'brainy'))  # Output: True
print(is_anagram('adobe', 'abode'))  # Output: True
print(is_anagram('adobe', 'abodee'))  # Output: False
print(is_anagram('adobe', 'boade'))  # Output: False
print(is_anagram('apple', 'pale'))  # Output: False
