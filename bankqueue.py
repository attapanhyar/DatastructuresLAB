# A simple simulation using a list-based queue
import random

bank_queue = []
tellers = 2
simulation_time = 10

print("--- Bank Simulation Start ---")
for time_step in range(1, simulation_time + 1):
    print(f"\nTime Step: {time_step}")
    
    # Customer arrival (random chance)
    if random.random() < 0.5: # 50% chance of new customer
        customer_id = f"Cust-{time_step}"
        bank_queue.append(customer_id)
        print(f"New Arrival: {customer_id}, Queue: {bank_queue}")
    
    # Tellers serving customers
    for i in range(tellers):
        if bank_queue: # Check if queue is not empty
            served = bank_queue.pop(0)
            print(f"Teller {i+1} serving: {served}")
        else:
            print(f"Teller {i+1} is idle")

print("\n--- Simulation End ---")
print(f"Customers remaining in queue: {bank_queue}")