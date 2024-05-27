# Introduction to Queue as a List

# Example usage
queue = []
queue.append(1)  # Output: Enqueued 1 to the queue.
queue.append(2)  # Output: Enqueued 2 to the queue.
queue.append(3)  # Output: Enqueued 3 to the queue.
queue.append(4)  # Output: Enqueued 4 to the queue.
print(queue)  # Output: Queue([1, 2, 3, 4])

queue.pop(0)  # Output: Dequeued 1 from the queue.
print(queue)  # Output: Queue([2, 3, 4])

queue.pop(0)  # Output: Dequeued 2 from the queue.
queue.pop(0)  # Output: Dequeued 3 from the queue.
queue.pop(0)  # Output: Dequeued 4 from the queue.
print(queue)  # Output: Queue([])

# Uncommenting the next line will raise an exception because the queue is empty
# queue.pop(0)

# Example output
# Queue([2, 3, 4])
# Queue([3, 4])
# Queue([4])
# Queue([])
# Queue([])

# Note: Queue is a linear data structure that follows the FIFO (first in, first out) principle.
# This means that the first element added to the queue will be the first element removed from the queue.
# Enqueue() and isEmpty() and size() are O(1) in the worst case.
# Dequeue() is O(n) in the worst case.
# Peek() is O(1) in the worst case.
# Examples: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
