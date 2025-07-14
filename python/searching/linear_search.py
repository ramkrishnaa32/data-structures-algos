"""
Linear Search is a simple searching algorithm that checks every element in the list sequentially until the target element is found or the list ends.

Time Complexity: O(n)
Space Complexity: O(1)
Works on both sorted and unsorted lists
"""
class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i  # Return index when found
        return False  # Return False if not found

# Sample input
nums = [1, 1, 2, 2, 4, 5, 5]
target = 5

# Function call
s = Solution()
result = s.linearSearch(nums, target)

# Output
if result is not False:
    print(f"Target found at index: {result}")
else:
    print("Target not found.")

