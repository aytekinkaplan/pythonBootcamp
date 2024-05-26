class MotorBike:
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 10

    def decrease_speed(self):
        self.max_speed -= 10

    def display(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Max Speed:", self.max_speed)


bike1 = MotorBike("Activa 3g", "blue", 180)
bike1.increase_speed()
bike1.display()

bike2 = MotorBike("Yamaha R15", "red", 200)
bike2.decrease_speed()
bike2.display()
