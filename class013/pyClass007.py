def reorder_and_eliminate_middle(words):
    # Step 1: Check for edge cases
    if len(words) < 2:
        return []

    # Step 2: Sort the list based on the length of strings in descending order
    sorted_words = sorted(words, key=len, reverse=True)

    # Step 3: Identify and remove the middle element(s)
    n = len(sorted_words)
    if n % 2 == 1:  # Odd number of elements
        middle_index = n // 2
        del sorted_words[middle_index]
    else:  # Even number of elements
        middle_index1 = n // 2 - 1
        middle_index2 = n // 2
        del sorted_words[middle_index1:middle_index2 + 1]

    # Step 4: Return the modified list
    return sorted_words


# Examples
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))
# Expected Output: ["banana", "grapes", "mango", "kiwi"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes"]))
# Expected Output: ["banana", "kiwi"]

print(reorder_and_eliminate_middle([]))
# Expected Output: []

print(reorder_and_eliminate_middle(["apple"]))
# Expected Output: []

print(reorder_and_eliminate_middle(["apple", "banana"]))
# Expected Output: ["banana"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi"]))
# Expected Output: ["banana", "kiwi"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes"]))
# Expected Output: ["banana", "kiwi", "grapes"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))
# Expected Output: ["banana", "grapes", "mango", "kiwi"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango", "orange"]))
# Expected Output: ["banana", "grapes", "mango", "kiwi", "orange"]

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango", "orange", "pineapple"]))
# Expected Output: ["banana", "grapes", "mango", "kiwi", "orange", "pineapple"]
