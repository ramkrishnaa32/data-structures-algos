"""
Problem Statement:

Given a sorted array of integers nums, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def searchRangeTwoPointer(self, nums, target):
        left = 0
        right = len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]

        while left < right:
            print(f"left: {nums[left]}, right: {nums[right]}")
            if nums[left] == target and nums[right] == target:
                return [left, right]

            elif nums[left] == target and nums[right] != target:
                right -= 1

            elif nums[left] != target and nums[right] == target:
                left += 1

            else:
                left += 1
                right -= 1

        return [-1, -1]

    def searchRangeBinarySearch(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        index = mid
                    right = mid - 1
            return index

        def findRight():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        index = mid
                    left = mid + 1
            return index

        return [findLeft(), findRight()]


nums = [5,7,7,8,8,8,10]
target = 8
sol = Solution()
result = sol.searchRangeTwoPointer(nums, target)
print(result)

result = sol.searchRangeBinarySearch(nums, target)
print(result)