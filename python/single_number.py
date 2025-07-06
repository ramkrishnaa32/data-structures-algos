
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [2,2,1]
Output: 1
"""

class Solution:

    # Approach: Brute Force
    def singleNumberBruteForce(self, nums: list[int]) -> int:
        for num in nums:
            count = 0
            for num2 in nums:
                if num == num2:
                    count += 1
            if count == 1:
                return num
                break

    # Approach: Hashmap
    def singleNumberHashmap(self, nums: list[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict: 
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for key, value in nums_dict.items():
            if value == 1:
                return key
    
    # Approach: Bit Manipulation
    def singleNumberBitManipulation(self, nums: list[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
    
    # Approach: Math
    def singleNumberMath(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
            
nums = [2, 2, 1, 5, 6, 6, 5, 3, 1]
s = Solution()

print(f'Resule from Brute Force: {s.singleNumberBruteForce(nums)}')
print(f'Result from Hashmap: {s.singleNumberHashmap(nums)}')
print(f'Result from Bit Manipulation: {s.singleNumberBitManipulation(nums)}')
print(f'Result from Math: {s.singleNumberMath(nums)}')
