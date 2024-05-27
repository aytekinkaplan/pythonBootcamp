names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
result = [name for name in names if 'e' in name]
print(result)  # Guess the output

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num for num in numbers if num % 2 == 0]
print(result)  # Guess the output

sentence = "The quick brown fox jumps over the lazy dog"
result = [char for char in sentence if char.lower() in 'aeiou']
print(result)  # Guess the output

original_list = [1, 2, 3, 4, 5]
result = [num ** 2 for num in original_list]
print(result)  # Guess the output

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num ** 2 for num in numbers if num % 2 != 0]
print(result)  # Guess the output

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(result)  # Guess the output

sentence = "Hello World! How are you doing?"
result = [len(word) for word in sentence.split()]
print(result)
