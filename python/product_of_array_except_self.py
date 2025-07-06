class Solution:

    # 1st approach brutforce
    def productExceptSelf(self, nums):
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]

            result.append(product)
        return result


    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length
        # prefix
        prefix = 1
        for i in (range(length)):
            result[i] = prefix
            prefix *= nums[i]
        print(result)

        # suffix
        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


solution = Solution()
print(solution.productExceptSelf(nums=[1,2,3,4]))