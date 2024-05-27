from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

    def stop_engine(self):
        return "Motorcycle engine stopped"


# Test the implementation
car = Car()
print(car.start_engine())  # Output: Car engine started
print(car.stop_engine())  # Output: Car engine stopped

motorcycle = Motorcycle()
print(motorcycle.start_engine())  # Output: Motorcycle engine started
print(motorcycle.stop_engine())  # Output: Motorcycle engine stopped
