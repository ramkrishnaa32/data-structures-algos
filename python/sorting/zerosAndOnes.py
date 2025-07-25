"""
Problem Statement:
Given a list of integers containing only 0s and 1s, rearrange the list in-place
so that all 0s appear before all 1s.

What is required:
- Modify the original list so that all 0s are on the left side,
  and all 1s are on the right side.
- The relative order of 0s and 1s does not matter.

Example:
Input: [0, 1, 0, 1, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]
"""

class Solution:
    def zerosAndOnes(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                left += 1
            if nums[right] == 1:
                right -= 1

            if nums[left] == 1 and nums[right] == 0:
                nums[left] = 0
                nums[right] = 1

        return nums


nums = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
s = Solution()
result = s.zerosAndOnes(nums)
print(result)