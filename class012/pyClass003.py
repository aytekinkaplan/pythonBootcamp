class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages!r})"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

    def __add__(self, other):
        return self.pages + other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __truediv__(self, other):
        return self.pages / other.pages

    def __floordiv__(self, other):
        return self.pages // other.pages

    def __mod__(self, other):
        return self.pages % other.pages

    def __pow__(self, other):
        return self.pages ** other.pages

    def __invert__(self):
        return ~self.pages

    def __lshift__(self, other):
        return self.pages << other.pages

    def __rshift__(self, other):
        return self.pages >> other.pages

    def __and__(self, other):
        return self.pages & other.pages

    def __xor__(self, other):
        return self.pages ^ other.pages

    def __or__(self, other):
        return self.pages | other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __ne__(self, other):
        return self.pages != other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __neg__(self):
        return -self.pages


class ReviewBook(Book):
    def __init__(self, title, author, pages, rating):
        super().__init__(title, author, pages)
        self.rating = rating

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, rating: {self.rating}"

    def __repr__(self):
        return f"ReviewBook({self.title!r}, {self.author!r}, {self.pages!r}, {self.rating!r})"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A review book object has been deleted")

    def __add__(self, other):
        return self.rating + other.rating

    def __mul__(self, other):
        return self.rating * other.rating

    def __truediv__(self, other):
        return self.rating / other.rating


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
review1 = ReviewBook("The Great Gatsby", "F. Scott Fitzgerald", 180, 4.5)

print(book1)  # Output: The Great Gatsby by F. Scott Fitzgerald, 180 pages
print(review1)  # Output: The Great Gatsby by F. Scott Fitzgerald, 180 pages, rating: 4.5
