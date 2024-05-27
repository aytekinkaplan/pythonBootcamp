class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        """Remove and return the top item from the stack. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        """Return the top item from the stack without removing it. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        item = self.stack[-1]
        print(f"Peeked at the top item: {item}")
        return item

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def __repr__(self):
        return f"Stack({self.stack})"


# Example usage
stack = Stack()
stack.push(10)  # Output: Pushed 10 to the stack.
stack.push(20)  # Output: Pushed 20 to the stack.
stack.push(30)  # Output: Pushed 30 to the stack.
print(stack)  # Output: Stack([10, 20, 30])

stack.peek()  # Output: Peeked at the top item: 30
stack.pop()   # Output: Popped 30 from the stack.
print(stack)  # Output: Stack([10, 20])

stack.pop()   # Output: Popped 20 from the stack.
stack.pop()   # Output: Popped 10 from the stack.
print(stack)  # Output: Stack([])

# Uncommenting the next line will raise an exception because the stack is empty
# stack.pop()
