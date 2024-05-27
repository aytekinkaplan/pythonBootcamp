class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', genre='{self.genre}')"


# Create Book instances
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
book2 = Book("Pride and Prejudice", "Jane Austen", "Romance")

# Print the Book instances
print(book1)  # Output: Book(title='The Lord of the Rings', author='J.R.R. Tolkien', genre='Fantasy')
print(book2)  # Output: Book(title='Pride and Prejudice', author='Jane Austen', genre='Romance')

