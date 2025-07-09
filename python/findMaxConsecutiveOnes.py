class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount, count)
                print(f"index: {i}, num: {nums[i]}, count: {count}, maxCount: {maxCount}")
            else:
                count = 0

        return maxCount


nums = [1, 1, 0, 1, 1, 1]
s = Solution()
result = s.findMaxConsecutiveOnes(nums)
print(result)