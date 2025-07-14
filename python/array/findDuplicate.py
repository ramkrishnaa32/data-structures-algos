class Solution:
    def findDuplicate1(self, nums: list[int]) -> int:
        numList = []
        for num in nums:
            if num in numList:
                return num
            else:
                numList.append(num)

    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break;

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

nums = [1, 3, 4, 2, 2]
s = Solution()
result = s.findDuplicate(nums)
print(f"Result: {result}")