import heapq

# A priority queue is just a list managed by heapq
pq = []

# heapq implements a min-heap (lowest value has highest priority)
# Push items with (priority, data)
heapq.heappush(pq, (3, 'Task C'))
heapq.heappush(pq, (1, 'Task A'))
heapq.heappush(pq, (2, 'Task B'))

print("Priority Queue (min-heap):", pq)

# Pop the item with the highest priority (lowest number)
print(f"Popped: {heapq.heappop(pq)}")
print(f"Popped: {heapq.heappop(pq)}")
print("Priority Queue after pops:", pq)