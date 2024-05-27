class Fan:
    # Constructor to initialize the fan
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0  # Initial speed is 0
        self.is_on = False  # Fan is initially off

    # Method to represent the Fan object as a string
    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

    # Method to switch the fan on
    def switch_on(self):
        self.is_on = True
        self.speed = 3  # Set initial speed to 3

    # Method to switch the fan off
    def switch_off(self):
        self.is_on = False
        self.speed = 0  # Reset speed to 0

    # Method to increase the fan speed
    def increase_speed(self):
        if self.is_on and self.speed < 5:  # Max speed is 5
            self.speed += 1

    # Method to decrease the fan speed
    def decrease_speed(self):
        if self.is_on and self.speed > 0:  # Min speed is 0
            self.speed -= 1


# Create a Fan object and test the methods
fan = Fan('Manufacturer 1', 5, 'Green')
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)

fan.switch_on()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 3, True)

fan.increase_speed()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 4, True)

fan.decrease_speed()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 3, True)

fan.switch_off()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)
