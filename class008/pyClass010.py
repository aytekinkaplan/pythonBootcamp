class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


# Example usage
rectangle = Rectangle(5, 10)
rectangle.display()


