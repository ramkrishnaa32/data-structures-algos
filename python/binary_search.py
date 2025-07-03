class Solution:
    def binary_search(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

s = Solution()
nums = [8, 7, 2, 1]
result = s.binary_search(nums, 16)

if result:
    print(f"Target number found")
else:
    print(f"Target number not found")
