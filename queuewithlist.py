# Simple Queue Implementation using a List
queue = []

def enqueue(element):
    queue.append(element)
    print(f"Enqueued: {element}")

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        # pop(0) removes from the front (FIFO)
        print(f"Dequeued: {queue.pop(0)}")

def front():
    if queue:
        print(f"Front Element: {queue[0]}")

enqueue(10)
enqueue(20)
enqueue(30)
front()
dequeue()
front()
dequeue()