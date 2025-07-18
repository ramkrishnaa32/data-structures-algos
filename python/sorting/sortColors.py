"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


class Solution:
    def sortColorsBruteForce(self, nums: list[int]) -> None:
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            if num in count:
                count[num] += 1

        idx = 0
        for key in count:
            for _ in range(count[key]):
                nums[idx] = key
                idx += 1

        return nums

    def sortColorsDNFA(self, nums: list[int]) -> None:
        """
        Sorts the list `nums` containing 0s, 1s, and 2s (representing red, white, and blue)
        in-place using the Dutch National Flag Algorithm.
        """
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums

nums = [2, 0, 2, 1, 1, 0]
sol = Solution()

result = sol.sortColorsBruteForce(nums.copy())
print(result)

result = sol.sortColorsDNFA(nums.copy())
print(result)