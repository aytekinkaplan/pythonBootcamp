# Exploring Inheritance in Object-Oriented Programming (OOP)

# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((self.make, self.model, self.speed, self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 0

    def switch_off(self):
        self.is_on = False
        self.speed = 0

    def increase_speed(self):
        if self.is_on:
            self.speed += 1

    def decrease_speed(self):
        if self.is_on and self.speed > 0:
            self.speed -= 1


# Child class
class Car(Vehicle):
    pass


# Child class
class Plane(Vehicle):
    pass


# Create a Car object and test the methods
car = Car('Toyota', 'Corolla')
print(car)  # Output: ('Toyota', 'Corolla', 0, False)

car.switch_on()
print(car)  # Output: ('Toyota', 'Corolla', 0, True)

car.increase_speed()
print(car)  # Output: ('Toyota', 'Corolla', 1, True)

car.decrease_speed()
print(car)  # Output: ('Toyota', 'Corolla', 0, True)

car.switch_off()
print(car)  # Output: ('Toyota', 'Corolla', 0, False)
