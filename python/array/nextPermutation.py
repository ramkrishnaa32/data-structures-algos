class Solution:
    def nextPermutation(self, nums: list[int]) -> list[int]:
        """
        Rearranges the numbers into the lexicographically next greater permutation.
        If such arrangement is not possible, it rearranges into the lowest possible order (ascending).

        Parameters:
        nums (list[int]): The current permutation of numbers.

        Returns:
        list[int]: The next permutation of numbers.
        """

        # Step 1: Find the pivot (first number from the end where nums[i] < nums[i+1])
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            # If no pivot found, the array is in descending order, reverse it to get the smallest permutation
            nums.reverse()
            return nums.copy()

        # Step 2: Find the next bigger element from the right side to swap with pivot
        for j in range(len(nums) - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[j], nums[pivot] = nums[pivot], nums[j]
                break

        # Step 3: Reverse the elements to the right of pivot to get the next smallest lexicographical order
        left = pivot + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums.copy()

# Example usage
sol = Solution()
nums = [1, 2, 3, 4, 5]
result = sol.nextPermutation(nums)
print(result)  # Output: [1, 2, 3, 5, 4]
