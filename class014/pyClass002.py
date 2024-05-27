# Implementing Stack in Python

# Example usage
stack = []
stack.append(10)  # Output: [10]
stack.append(20)  # Output: [10, 20]
stack.append(30)  # Output: [10, 20, 30]
print(stack)  # Output: [10, 20, 30]

stack.pop()  # Output: 30
stack.pop()  # Output: 20
stack.pop()  # Output: 10
print(stack)  # Output: []

# Uncommenting the next line will raise an exception because the stack is empty
# stack.pop()

# Example output
# [10, 20, 30]
# 30
# 20
# 10
# []

