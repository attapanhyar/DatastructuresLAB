from collections import deque

# Create a deque
d = deque()

# Add to the right (rear)
d.append(10)
print("Append (right):", d)

# Add to the left (front)
d.appendleft(5)
print("Append left (front):", d)

d.append(20)
print("Append (right):", d)

# Remove from the right (rear)
print(f"Popped (right): {d.pop()}")
print("Deque after pop:", d)

# Remove from the left (front)
print(f"Popped left (front): {d.popleft()}")
print("Deque after popleft:", d)