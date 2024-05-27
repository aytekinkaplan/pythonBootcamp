from abc import ABC, abstractmethod


class AbstractVehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def increase_speed(self):
        pass

    @abstractmethod
    def decrease_speed(self):
        pass


class Vehicle(AbstractVehicle):
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def increase_speed(self):
        pass

    def decrease_speed(self):
        pass

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
        if self.is_on:
            self.speed -= 1

    def drive(self):
        if self.is_on:
            return f"{self.make} {self.model} is driving"
        else:
            return f"{self.make} {self.model} is not on"

    def stop(self):
        if self.is_on:
            return f"{self.make} {self.model} is stopped"
        else:
            return f"{self.make} {self.model} is not on"

    def accelerate(self):
        if self.is_on:
            return f"{self.make} {self.model} is accelerating"
        else:
            return f"{self.make} {self.model} is not on"

    def brake(self):
        if self.is_on:
            return f"{self.make} {self.model} is braking"
        else:
            return f"{self.make} {self.model} is not on"


# Create a Car object and test the methods
car = Vehicle('Toyota', 'Corolla')
print(car)  # Output: ('Toyota', 'Corolla', 0, False)

car.switch_on()
print(car)  # Output: ('Toyota', 'Corolla', 0, True)

car.increase_speed()
print(car)  # Output: ('Toyota', 'Corolla', 1, True)

car.decrease_speed()
print(car)  # Output: ('Toyota', 'Corolla', 0, True)

car.switch_off()
print(car)  # Output: ('Toyota', 'Corolla', 0, False)
