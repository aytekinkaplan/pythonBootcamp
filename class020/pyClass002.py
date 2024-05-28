my_tuple = (4, 5, 6, 7, 8)
print(len(my_tuple))

my_tuple = (100, 200, 300)
a, b, c = my_tuple
print(b)

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
result = tuple_1 + tuple_2
print(result)
print("".join(str(n) for n in result))


def my_function(x, y):
    return x + y, x - y


result = my_function(10, 5)
print(result)

nested_tuple = ((1, 2), (3, 4), (5, 6))  # Nested Tuples
print(nested_tuple[1][0])

my_tuple = (10, 20, 30, 40, 50)  # Tuple Slicing
print(my_tuple[-1])
print(my_tuple[1:4])
print(my_tuple[1:-1])

my_tuple = (10, 20, 30, 40, 10)
print(my_tuple.count(10))
print(my_tuple.index(30))

a, b, c = 10, 20, 30  # Tuple Packing and Unpacking
my_tuple = a, b, c
x, y, z = my_tuple
print(x + y + z)
