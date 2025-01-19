import random
import time

# Parameters
num_numbers = 1000
range_start = 1
range_end = 1000

# Generate 1000 random numbers with duplicates
random_numbers = random.choices(range(range_start, range_end + 1), k=num_numbers)

# Find the maximum number
def find_max_number(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Measure time taken to check for duplicates
start_time = time.time()
max_number = find_max_number(random_numbers)
end_time = time.time()
total_time = end_time - start_time

print(f"Maximum number: {max_number}")
print(f"Time taken: {total_time} seconds")