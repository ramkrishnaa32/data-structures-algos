"""
Binary Search is an efficient algorithm for finding an item from a sorted list by repeatedly dividing the search interval in half.
Time Complexity: O(log n)
Space Complexity: O(1) (iterative version)

Sort the array (if not already sorted).
Set two pointers: left at the start, right at the end.

While left <= right:
Calculate mid as the middle index.
If nums[mid] == target, return True.
If nums[mid] < target, move left to mid + 1.
If nums[mid] > target, move right to mid - 1.
If the loop ends, return False.
"""

class Solution:
    def binary_search(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Example usage
s = Solution()
nums = [8, 7, 2, 1]
result = s.binary_search(nums, 2)

# Output result
if result:
    print("Target number found")
else:
    print("Target number not found")

