"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""


class Solution:
    def threeSumBruteForce(self ,nums: list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in ans:
                            ans.append(triplet)
        return ans

    def threeSumHashing(self, nums: list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in seen:
                    triplet = sorted([nums[i], nums[j], target])

                    if triplet not in ans:
                        ans.append(triplet)
                else:
                    seen.add(nums[j])

        return ans

    def threeSumTwoPointer(self, nums: list[int]) -> list[list[int]]:
        answer_set = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                    answer_set.add(triplet)
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(l) for l in answer_set]



nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
result = sol.threeSumBruteForce(nums)
print(f"threeSumBruteForce: {result}")

result = sol.threeSumHashing(nums)
print(f"threeSumHashing: {result}")

result = sol.threeSumTwoPointer(nums)
print(f"threeSumTwoPointer: {result}")