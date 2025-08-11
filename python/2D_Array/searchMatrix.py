"""
74. Search a 2D Matrix

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Example:
    [[1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]]
"""

class Solution:
    def search(self, arr: list[int], target: int):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False


    def searchMatrix(self, arr: list[list[int]], target: int):
        start = 0
        end = len(arr) - 1
        # Step 1: Binary search to find the correct row
        while start <= end:
            mid = (start + end) // 2
            length = len(arr[mid])
            print(f"Searching in arr: {arr[mid]}, target: {target}")
            if arr[mid][0] <= target <= arr[mid][length - 1]:
                return self.search(arr[mid], target)
            elif target > arr[mid][length - 1]:
                start = mid + 1
            else:
                end = mid - 1

        return False


s = Solution()
matrix =  [[1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]]

target = 34
result = s.searchMatrix(matrix, target)

if result:
    print(f"Target is present")
else:
    print(f"Target is not present")

matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]]
target = 13
result = s.searchMatrix(matrix, target)

if result:
    print(f"Target is present")
else:
    print(f"Target is not present")