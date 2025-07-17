"""
Insertion Sort Algorithm

Overview:
    Insertion Sort is a comparison-based sorting algorithm that builds the final sorted array
    one item at a time. It works similar to how we sort playing cards in our hands.

Algorithm:
    1. Start from the second element.
    2. Compare it with elements before it.
    3. Shift all greater elements to the right.
    4. Insert the current element into its correct position.

Time Complexity:
    - Best: O(n) [when the list is already sorted]
    - Average/Worst: O(n^2)
Space Complexity:
    - O(1) (in-place sorting)
"""

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        current = nums[i]
        previous = i - 1
        while previous >= 0 and nums[previous] > current:
            nums[previous + 1] = nums[previous]
            previous -= 1
        nums[previous + 1] = current
    return nums


# Example usage
nums = [5, 3, 8, 4, 2]
print(f"Original Array: {nums}")
sorted_nums = insertion_sort(nums.copy())
print(f"Sorted (Ascending): {sorted_nums}")
