def is_anagram(string1, string2):
    # If the lengths of the strings are different, they cannot be anagrams
    if len(string1) != len(string2):
        return False

    # Initialize two lists of 26 zeros
    list1 = [0] * 26
    list2 = [0] * 26

    # Count the occurrences of each character in string1
    for char in string1:
        index = ord(char) - ord('a')  # Calculate the index for character 'a' to 'z'
        list1[index] += 1

    # Count the occurrences of each character in string2
    for char in string2:
        index = ord(char) - ord('a')  # Calculate the index for character 'a' to 'z'
        list2[index] += 1

    # Compare the two lists
    return list1 == list2


# Test cases
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "hey"))  # Output: False
print(is_anagram("apple", "ppale"))  # Output: True
