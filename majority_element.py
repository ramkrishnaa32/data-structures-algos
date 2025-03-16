"""
Majority Element

Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def bruteForce(self, nums: list[int]) -> int:
        for num in nums:
            count = 0
            for num2 in nums:
                if num == num2:
                    count += 1
            if count > len(nums) // 2:
                return num
                break
    
    def hashmap(self, nums: list[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for key, value in nums_dict.items():
            if value > len(nums) // 2:
                return key
            
    def sortMethod(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
    def boyerMooreVotingAlgorithm(self, nums: list[int]) -> int:
        count = 0
        condidate = None
        for num in nums:
            if count == 0:
                condidate = num
            if num == condidate: count += 1 
            else:  count -= 1 
        return condidate
    
nums = [2, 2, 1, 1, 1, 2, 2]
nums2 = [3, 2, 3, 3, 3, 3, 3]

s = Solution()
print(f"Brute force approach: {s.bruteForce(nums)}")
print(f"Hashmap approach: {s.hashmap(nums)}")
print(f"Sort method approach: {s.sortMethod(nums)}")
print(f"Boyer-Moore Voting Algorithm approach: {s.boyerMooreVotingAlgorithm(nums)}")

print(f"Brute force approach: {s.bruteForce(nums2)}")
print(f"Hashmap approach: {s.hashmap(nums2)}")
print(f"Sort method approach: {s.sortMethod(nums2)}")
print(f"Boyer-Moore Voting Algorithm approach: {s.boyerMooreVotingAlgorithm(nums2)}")