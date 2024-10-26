
import random
import string
import time



def generate_random_b62(length: int =10):

    b62_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(b62_chars) for _ in range(length))

# print(generate_random_b62())

execution_times = []
num_runs = 100

for _ in range(num_runs):

    # Start time
    start_time = time.time()

    # Your code block
    for i in range(1000000):
        generate_random_b62()

    # End time
    end_time = time.time()

    # Execution time
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    print(f"Execution time: {execution_time} seconds")

average_time = sum(execution_times) / num_runs
print(f"Average execution time: {average_time} seconds")
