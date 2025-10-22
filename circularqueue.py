# Circular Queue Implementation
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        # Check if first element
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(f"Enqueued: {data}")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f"Enqueued: {data}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty (Underflow)")
        # Check if last element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print(f"Dequeued: {temp}")
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(f"Dequeued: {temp}")

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4) # Queue Full
cq.dequeue()
cq.enqueue(4) # Wraps around
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue() # Queue Empty