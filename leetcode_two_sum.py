"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    # Approach: Brute Force
    def twoSum(self, nums: list[int], target: int):
        try:
            for index in range(len(nums)):
                for index2 in range(index + 1, len(nums)):
                    if nums[index] + nums[index2] == target and index != index2:
                        return [index, index2]
        except Exception as error:
            print(f" Exception occurred: {error}")
        return []
    
    # Approach: Sorting and Two Pointers
    def twoSum2(self, nums: list[int], target: int):
    
        indexed_nums = [(val, idx) for idx, val in enumerate(nums)] # Store values along with their original indices
        indexed_nums.sort() # Sort based on values

        index1 = 0
        index2 = len(indexed_nums) - 1

        while index1 < index2:
            sum_value = indexed_nums[index1][0] + indexed_nums[index2][0]
            if sum_value == target:
                return [indexed_nums[index1][1], indexed_nums[index2][1]] 
            elif sum_value < target:
                index1 += 1 
            else:
                index2 -= 1
        return []
    
    # Approach: Hash Table
    def twoSum3(self, nums: list[int], target: int):
        nums_dict = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in nums_dict:
                return [nums_dict[difference], index]
            nums_dict[value] = index
        return []
   
    
s = Solution()
nums = [3, 2, 5, 3, 10]
target = 6


index_list = s.twoSum(nums, target)
if len(index_list) == 0:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print("No two numbers add up to the target.")
else:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print(f"Indices of the two numbers that add up to the target: {index_list}")

index_list = s.twoSum2(nums, target)
if len(index_list) == 0:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print("No two numbers add up to the target.")
else:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print(f"Indices of the two numbers that add up to the target: {index_list}")

index_list = s.twoSum3(nums, target)
if len(index_list) == 0:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print("No two numbers add up to the target.")
else:
    print(f"Input array: {nums}")
    print(f"Input target: {target}")
    print(f"Indices of the two numbers that add up to the target: {index_list}")