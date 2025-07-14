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