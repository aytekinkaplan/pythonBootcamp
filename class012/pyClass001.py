# Object-Oriented Programming Basics Revisited

# Classes

# Classes are a way to organize data and functions into a single unit.

# Objects are instances of a class.

# Classes are blueprints for creating objects.

# Objects are created from classes.

# Classes are used to create instances of objects.

# Some classes have attributes and some have methods.

# Some examples of classes:

# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."

#     def __repr__(self):
#         return f"{self.name} is {self.age} years old."

#     def __del__(self):
#         print(f"{self.name} has left the building.")

#     def __eq__(self, other):
#         if self.name == other.name and self.age == other.age:
#             return True
#         else:
#             return False

#     def __lt__(self, other):
#         if self.age < other.age:
#             return True
#         else:
#             return False

#     def __gt__(self, other):
#         if self.age > other.age:
#             return True
#         else:
#             return False

#     def __add__(self, other):
#         return self.age + other.age

#     def __sub__(self, other):
#         return self.age - other.age

#     def __mul__(self, other):
#         return self.age * other.age

#     def __truediv__(self, other):
#         return self.age / other.age

#     def __floordiv__(self, other):
#         return self.age // other.age

#     def __mod__(self, other):
#         return self.age % other.age

#     def __pow__(self, other):
#         return self.age ** other.age

#     def __invert__(self):
#         return ~self.age

#     def __lshift__(self, other):
#         return self.age << other.age
