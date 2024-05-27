class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.radius = 0

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle()
circle.radius = 5
print(circle.area())
print(circle.perimeter())


class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle()
rectangle.length = 10
rectangle.breadth = 5
print(rectangle.area())
print(rectangle.perimeter())


class Square(Shape):
    def __init__(self):
        self.length = 0

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


square = Square()
square.length = 5
print(square.area())
print(square.perimeter())


class Triangle(Shape):
    def __init__(self):
        self.base = 0
        self.height = 0

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 3 * self.base


triangle = Triangle()
triangle.base = 10
triangle.height = 5
print(triangle.area())
print(triangle.perimeter())
