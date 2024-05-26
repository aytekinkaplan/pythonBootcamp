class Car:
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def display(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Max Speed:", self.max_speed)


car1 = Car("BMW", "Black", 200)
car1.display()

car2 = Car("Audi", "White", 220)
car2.display()

car3 = Car("Ferrari", "Red", 250)
car3.display()

print(type(car1))
print(type(car1.name))
