# Is it a Right Angled Triangle?

# Input
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# Process and Output
if side1 ** 2 + side2 ** 2 == side3 ** 2:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")
