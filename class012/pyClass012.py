# Implement the `start_engine` method to return "Engine started".
class Engine:
    def start_engine(self):
        return "Engine started"


# Implement `number_of_wheels` method to return number of wheels - 4.
class Wheels:
    def number_of_wheels(self):
        return 4


# Make class inherit from Engine & Wheels
# Implement the `drive` method to return "Car is driving".
class Car(Engine, Wheels):
    def drive(self):
        return "Car is driving"


# Example Invocations:

vehicle = Car()

# Test engine start
result_start = vehicle.start_engine()
print(result_start)  # Output: "Engine started"

# Test drive
result_drive = vehicle.drive()
print(result_drive)  # Output: "Car is driving"

# Test number of wheels
num_wheels = vehicle.number_of_wheels()
print(num_wheels)  # Output: 4
