"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""


class Solution(object):
    def fourSum(self, nums, target):
        result = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                left = j + 1
                right = n - 1

                while left < right:
                    totalSum = total + nums[left] + nums[right]

                    if totalSum == target:
                        arr = [nums[i], nums[j], nums[left], nums[right]]
                        arr.sort()
                        result.add(tuple(arr))

                        left += 1
                        right -= 1

                    elif totalSum > target:
                        right -= 1

                    else:
                        left += 1

        return [list(i) for i in result]


nums = [1, 0, -1, 0, -2, 2]
target = 0
s = Solution()
result = s.fourSum(nums, target)
print(result)

nums = [2, 2, 2, 2, 2]
target = 8
result = s.fourSum(nums, target)
print(result)
