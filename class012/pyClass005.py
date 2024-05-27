class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0  # Initial speed is 0
        self.is_on = False  # Fan is initially off

    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3  # Set initial speed to 3

    def switch_off(self):
        self.is_on = False
        self.speed = 0  # Reset speed to 0

    def increase_speed(self):
        if self.is_on and self.speed < 5:  # Max speed is 5
            self.speed += 1

    def decrease_speed(self):
        if self.is_on and self.speed > 0:  # Min speed is 0
            self.speed -= 1


class Light:
    def __init__(self, make, wattage, color):
        self.make = make
        self.wattage = wattage
        self.color = color
        self.is_on = False  # Light is initially off

    def __repr__(self):
        return repr((self.make, self.wattage, self.color, self.is_on))

    def switch_on(self):
        self.is_on = True

    def switch_off(self):
        self.is_on = False


class Room:
    def __init__(self, name, fan, light):
        self.name = name
        self.fan = fan
        self.light = light

    def __repr__(self):
        return repr((self.name, self.fan, self.light))

    def switch_on_fan(self):
        self.fan.switch_on()

    def switch_off_fan(self):
        self.fan.switch_off()

    def increase_fan_speed(self):
        self.fan.increase_speed()

    def decrease_fan_speed(self):
        self.fan.decrease_speed()

    def switch_on_light(self):
        self.light.switch_on()

    def switch_off_light(self):
        self.light.switch_off()

    def increase_light_wattage(self):
        self.light.increase_wattage()

    def decrease_light_wattage(self):
        self.light.decrease_wattage()


# Create instances of Fan and Light
fan = Fan('Manufacturer A', 5, 'White')
light = Light('Manufacturer B', 60, 'Warm White')

# Create a Room instance with the Fan and Light
room = Room('Living Room', fan, light)

# Test the Room methods
print(
    room)  # Output: ('Living Room', ('Manufacturer A', 5, 'White', 0, False), ('Manufacturer B', 60, 'Warm White', False))

room.switch_on_fan()
room.increase_fan_speed()
print(
    room)  # Output: ('Living Room', ('Manufacturer A', 5, 'White', 4, True), ('Manufacturer B', 60, 'Warm White', False))

room.switch_on_light()
print(
    room)  # Output: ('Living Room', ('Manufacturer A', 5, 'White', 4, True), ('Manufacturer B', 60, 'Warm White', True))

room.switch_off_fan()
room.switch_off_light()
print(
    room)  # Output: ('Living Room', ('Manufacturer A', 5, 'White', 0, False), ('Manufacturer B', 60, 'Warm White', False))
