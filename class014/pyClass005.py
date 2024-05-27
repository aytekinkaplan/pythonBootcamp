class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        """Remove and return the front item from the queue. Raise an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.queue.pop(0)
        print(f"Dequeued {item} from the queue.")
        return item

    def front(self):
        """Return the front item from the queue without removing it. Raise an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        item = self.queue[0]
        print(f"Front item: {item}")
        return item

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def __repr__(self):
        return f"Queue({self.queue})"

# Example usage
queue = Queue()
queue.enqueue(1)  # Output: Enqueued 1 to the queue.
queue.enqueue(2)  # Output: Enqueued 2 to the queue.
queue.enqueue(3)  # Output: Enqueued 3 to the queue.
queue.enqueue(4)  # Output: Enqueued 4 to the queue.
print(queue)      # Output: Queue([1, 2, 3, 4])

queue.front()     # Output: Front item: 1
queue.dequeue()   # Output: Dequeued 1 from the queue.
print(queue)      # Output: Queue([2, 3, 4])

queue.dequeue()   # Output: Dequeued 2 from the queue.
queue.dequeue()   # Output: Dequeued 3 from the queue.
queue.dequeue()   # Output: Dequeued 4 from the queue.
print(queue)      # Output: Queue([])

# Uncommenting the next line will raise an exception because the queue is empty
# queue.dequeue()
