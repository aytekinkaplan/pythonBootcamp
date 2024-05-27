# Define a Book class with attributes and custom methods
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.year})'

    def __str__(self):
        return f'{self.title} by {self.author}, published in {self.year}'


# Create an instance of Book and print it
book = Book('1984', 'George Orwell', 1949)
print(book)  # Output: 1984 by George Orwell, published in 1949
print(repr(book))  # Output: Book(1984, George Orwell, 1949)
