import random
import time

# Parameters
num_numbers = 999
range_start = 1
range_end = 1000

# Ensure the range can accommodate the required number of unique numbers
if num_numbers > (range_end - range_start + 1):
    raise ValueError("The range is too small to generate the required number of unique numbers.")

# Generate unique random numbers
random_numbers = random.sample(range(range_start, range_end + 1), num_numbers)
# print(f"Random numbers: {random_numbers}")

# Calculate the sum of all numbers from 1 to 1000
def calculate_expected_sum(end_number):
    return end_number * (end_number + 1) // 2

# Find the sum of the numbers in a list
def find_sum_of_numbers(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers

def find_missing_number(numbers, range_end):
    expected_sum = calculate_expected_sum(range_end)
    actual_sum = find_sum_of_numbers(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number

# Measure time taken to find the missing number
start_time = time.time()
max_number = find_missing_number(random_numbers, range_end)
end_time = time.time()
total_time = end_time - start_time

print(f"Missing number: {max_number}") # Print the missing number
print(f"Time taken: {total_time} seconds")  # Print the time taken to find the missing number