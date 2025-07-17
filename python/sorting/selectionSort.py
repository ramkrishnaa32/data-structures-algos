"""
Selection Sort Algorithm

Overview:
    Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly
    selecting the minimum (or maximum) element from the unsorted portion and moving it
    to the beginning (or end) of the sorted portion.

    This version implements both ascending and descending order sorting.

Time Complexity:
    - Best, Average, Worst: O(n^2)
Space Complexity:
    - O(1) (in-place sorting)

Functions:
    - selection_sort_ascending(nums): Sorts a list in ascending order using Selection Sort.
    - selection_sort_descending(nums): Sorts a list in descending order using Selection Sort.
"""

def selection_sort_ascending(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def selection_sort_descending(nums):
    n = len(nums)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums


# Example usage
nums = [5, 3, 8, 4, 2]
print("Original List:", nums)

desc_sorted = selection_sort_descending(nums.copy())
print("Descending Order:", desc_sorted)

asc_sorted = selection_sort_ascending(nums.copy())
print("Ascending Order:", asc_sorted)
