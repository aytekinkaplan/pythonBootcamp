# Understanding Polymorphism in Python with Examples

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

    def start_engine(self):
        pass

    def stop_engine(self):
        pass


# Child classes
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

    def increase_speed(self):
        if self.is_on:
            self.speed += 2


class Plane(Vehicle):
    def start_engine(self):
        return "Plane engine started"

    def stop_engine(self):
        return "Plane engine stopped"

    def increase_speed(self):
        if self.is_on:
            self.speed += 10


# Test the implementation
car = Car("Mazda", "MX-5")
print(car)  # Output: ('Mazda', 'MX-5', 0, False)

car.switch_on()
print(car)  # Output: ('Mazda', 'MX-5', 0, True)

car.increase_speed()
print(car)  # Output: ('Mazda', 'MX-5', 2, True)

car.decrease_speed()
print(car)  # Output: ('Mazda', 'MX-5', 1, True)

car.switch_off()
print(car)  # Output: ('Mazda', 'MX-5', 0, False)

plane = Plane("Boeing", "747")
print(plane)  # Output: ('Boeing', '747', 0, False)

plane.switch_on()
print(plane)  # Output: ('Boeing', '747', 0, True)

plane.increase_speed()
print(plane)  # Output: ('Boeing', '747', 10, True)

plane.decrease_speed()
print(plane)  # Output: ('Boeing', '747', 9, True)

plane.switch_off()
print(plane)  # Output: ('Boeing', '747', 0, False)
