# Introduction To Set in Python with Examples

numbers = [1,2,3,2,1]
print(numbers)  # Output: [1, 2, 3, 2, 1]
numbers_set = set(numbers)
print(numbers_set)  # Output: {1, 2, 3}

numbers_set.add(3)
print(numbers_set)  # Output: {1, 2, 3}

numbers_set.remove(3)
print(numbers_set)  # Output: {1, 2}

numbers_set.clear()
print(numbers_set)  # Output: set()

numbers_set = {1, 2, 3, 4, 5}
print(numbers_set)  # Output: {1, 2, 3, 4, 5}


string_set = {"a", "b", "c", "d", "e", "f", "g"}
print(string_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

string_set.add("h")
print(string_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

string_set.remove("h")
print(string_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

string_set.clear()
print(string_set)  # Output: set()

string_set = {"a", "b", "c", "d", "e", "f", "g"}
print(string_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}


hello_set = {"h", "e", "l", "l", "o"}
print(hello_set)  # Output: {'h', 'e', 'l', 'o'}

hello_list = list(hello_set)
print(hello_list)  # Output: ['h', 'e', 'l', 'l', 'o']

hello_list = list(hello_set)
print(hello_list)  # Output: ['h', 'e', 'l', 'o']


hello_tuple = tuple(hello_set)
print(hello_tuple)  # Output: ('h', 'e', 'l', 'o')


hello_set = set(hello_tuple)
print(hello_set)  # Output: {'h', 'e', 'l', 'o'}

hello_set = set(hello_list)
print(hello_set)  # Output: {'h', 'e', 'l', 'o'}

hello_set = set("hello")
print(hello_set)  # Output: {'h', 'e', 'l', 'o'}

print(min(numbers_set))  # Output: 1
print(max(numbers_set))  # Output: 4
print(sum(numbers_set))  # Output: 10
print(len(numbers_set))  # Output: 4

