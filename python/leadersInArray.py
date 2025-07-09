class Solution:
    def leadersInArray(self, nums):
        maxNum = 0
        answer = []
        for i in range(len(nums)-1,-1,-1 ):
            if  nums[i] > maxNum:
                maxNum = max(maxNum, nums[i])
                answer.append(nums[i])
                print(f"num: {nums[i]}, maxNum: {maxNum}, answer: {answer}")
        return answer


nums = [16, 17, 4, 3, 5, 2]
s = Solution()
result = s.leadersInArray(nums)
print(result)