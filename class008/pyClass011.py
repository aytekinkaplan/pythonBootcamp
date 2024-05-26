class RGBColor:
    def __init__(self, red, green, blue):
        # Initializing the red, green, and blue attributes
        self.red = red
        self.green = green
        self.blue = blue

    def invert(self):
        # Inverting the color
        self.red = 255 - self.red
        self.green = 255 - self.green
        self.blue = 255 - self.blue

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue


# Example usage:
color = RGBColor(255, 0, 0)
color.invert()
print(color.get_red())  # Prints: 0
print(color.get_green())  # Prints: 255
print(color.get_blue())  # Prints: 255
