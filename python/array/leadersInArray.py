class Solution:
    def leadersInArray(self, nums):
        maxNum = 0
        answer = []
        for i in range(len(nums)-1, -1, -1):
            if maxNum < nums[i]:
                maxNum = max(maxNum, nums[i])
                answer.append(nums[i])
                print(f"index: {i}, num: {nums[i]}, maxNum: {maxNum}, answer: {answer}")
        return answer

nums = [16, 17, 4, 3, 5, 2, 3]
s = Solution()
result = s.leadersInArray(nums)
print(result)