# Exploring Multiple Inheritance in Python

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


# Child class
class Ship(Vehicle):
    pass


# Child class
class Bike(Vehicle):
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

# Create a Plane object and test the methods
plane = Plane('Boeing', '737')
print(plane)  # Output: ('Boeing', '737', 0, False)

plane.switch_on()
print(plane)  # Output: ('Boeing', '737', 0, True)

plane.increase_speed()
print(plane)  # Output: ('Boeing', '737', 1, True)

plane.decrease_speed()
print(plane)  # Output: ('Boeing', '737', 0, True)

plane.switch_off()
print(plane)  # Output: ('Boeing', '737', 0, False)

# Create a Ship object and test the methods
ship = Ship('Titanic', '777')
print(ship)  # Output: ('Titanic', '777', 0, False)

ship.switch_on()
print(ship)  # Output: ('Titanic', '777', 0, True)

ship.increase_speed()
print(ship)  # Output: ('Titanic', '777', 1, True)

ship.decrease_speed()
print(ship)  # Output: ('Titanic', '777', 0, True)

ship.switch_off()
print(ship)  # Output: ('Titanic', '777', 0, False)

# Create a Bike object and test the methods
bike = Bike('Harley-Davidson', 'Roadster')
print(bike)  # Output: ('Harley-Davidson', 'Roadster', 0, False)

bike.switch_on()
print(bike)  # Output: ('Harley-Davidson', 'Roadster', 0, True)

bike.increase_speed()
print(bike)  # Output: ('Harley-Davidson', 'Roadster', 1, True)

bike.decrease_speed()
print(bike)  # Output: ('Harley-Davidson', 'Roadster', 0, True)

bike.switch_off()
print(bike)  # Output: ('Harley-Davidson', 'Roadster', 0, False)


class Truck(Vehicle):
    pass


# Create a Truck object and test the methods
truck = Truck('Ford', 'F150')
print(truck)  # Output: ('Ford', 'F150', 0, False)

truck.switch_on()
print(truck)  # Output: ('Ford', 'F150', 0, True)

truck.increase_speed()
print(truck)  # Output: ('Ford', 'F150', 1, True)

truck.decrease_speed()
print(truck)  # Output: ('Ford', 'F150', 0, True)

truck.switch_off()
print(truck)  # Output: ('Ford', 'F150', 0, False)
