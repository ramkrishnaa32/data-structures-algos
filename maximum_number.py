import random
import time

# Parameters
num_numbers = 1000
range_start = 100
range_end = 10000

# Generate 1000 random numbers with duplicates
random_numbers = random.choices(range(range_start, range_end + 1), k=num_numbers)

# Find the maximum number
def find_max_number(numbers): # Define a function that takes a list of numbers as input
    max_number = numbers[0] # Initialize max_number to the first number
    for number in numbers: # Iterate through the list of numbers
        if number > max_number: # If the current number is greater than max_number
            max_number = number  # Update max_number to the current number
    return max_number # Return the maximum number

# Measure time taken to check for duplicates
start_time = time.time()
max_number = find_max_number(random_numbers)
end_time = time.time()
total_time = end_time - start_time

print(f"Maximum number: {max_number}") # Print the maximum number
print(f"Time taken: {total_time} seconds")  # Print the time taken to find the maximum number