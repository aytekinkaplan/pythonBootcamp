# `ord` takes a single character and returns its ASCII/Unicode value
print(ord('H'))  # Output: 72
# `chr` takes an ASCII/Unicode value and returns the corresponding character
print(chr(72))  # Output: 'H'

# Comparing Strings
print("Hello" == "Hello")  # Output: True
print("Hello" == "hello")  # Output: False
print("Hello" != "Hello")  # Output: False
print("Hello" != "hello")  # Output: True
print("Hello" > "Hello")  # Output: False
print("Hello" > "hello")  # Output: False
print("Hello" < "Hello")  # Output: False
print("Hello" < "hello")  # Output: True
print("Hello" >= "Hello")  # Output: True
print("Hello" >= "hello")  # Output: False
print("Hello" <= "Hello")  # Output: True
print("Hello" <= "hello")  # Output: True
print("Hello" is "Hello")  # Output: True
print("Hello" is "hello")  # Output: False
print("Hello" in "Hello")  # Output: True
print("Hello" in "hello")  # Output: False
print("Hello" not in "Hello")  # Output: False
print("Hello" not in "hello")  # Output: True

# Comparing Numbers
print(1 == 1)  # Output: True
print(1 == 2)  # Output: False
print(1 != 1)  # Output: False
print(1 != 2)  # Output: True
print(1 > 1)  # Output: False
print(1 > 2)  # Output: False
print(1 < 1)  # Output: False
print(1 < 2)  # Output: True
print(1 >= 1)  # Output: True
print(1 >= 2)  # Output: False
print(1 <= 1)  # Output: True
print(1 <= 2)  # Output: True
print(1 is 1)  # Output: True
print(1 is 2)  # Output: False
print(1 in [1])  # Output: True
print(1 in [2])  # Output: False

# Comparing Booleans
print(True == True)  # Output: True
print(True == False)  # Output: False
print(True != True)  # Output: False
print(True != False)  # Output: True
print(True > True)  # Output: False
print(True > False)  # Output: True
print(True < True)  # Output: False
print(True < False)  # Output: False
print(True >= True)  # Output: True
print(True >= False)  # Output: True
print(True <= True)  # Output: True
print(True <= False)  # Output: False
print(True is True)  # Output: True
print(True is False)  # Output: False
print(True in [True])  # Output: True
print(True in [False])  # Output: False
print(True not in [True])  # Output: False
print(True not in [False])  # Output: True

# Comparing None
print(None == None)  # Output: True
print(None == 0)  # Output: False
print(None != None)  # Output: False
print(None != 0)  # Output: True
print(None >= None)  # Output: True
print(None >= 0)  # Raises TypeError
print(None <= None)  # Output: True
print(None <= 0)  # Raises TypeError
print(None is None)  # Output: True
print(None is 0)  # Output: False
print(None in [None])  # Output:

