"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:

1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

Example:
    [[1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]]
"""

class Solution:
    def searchMatrix(self, arr: list[list[int]], target: int) -> bool:
        m, n = len(arr), len(arr[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            if arr[row][col] == target:
                return True
            elif target < arr[row][col]:
                col -= 1
            else:
                row += 1

        return False


s = Solution()
matrix = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]


# True case
target = 9
result = s.searchMatrix(matrix, target)
if result:
    print(f"Target is present")
else:
    print(f"Target is not present")

# False case
target = 20
result = s.searchMatrix(matrix, target)

if result:
    print(f"Target is present")
else:
    print(f"Target is not present")