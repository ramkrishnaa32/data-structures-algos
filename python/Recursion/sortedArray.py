class Solution:
    def sortedArray(self, nums: list[int], n: int) -> bool:
        """
        Recursively checks if a list of integers is sorted in non-decreasing order.

        Parameters:
        nums (list[int]): The list of integers to check.
        n (int): The number of elements to consider from the list (typically len(nums)).

        Returns:
        bool: True if the first 'n' elements of the list are sorted in non-decreasing order, False otherwise.

        Example:
        s = Solution()
        s.sortedArray([1, 2, 3, 4, 5], 5)
        True
        s.sortedArray([1, 3, 2, 4, 5], 5)
        False
        """
        if n == 0 or n == 1:
            return True

        if nums[n - 1] >= nums[n - 2]:
            return self.sortedArray(nums, n - 1)

        return False


s = Solution()
nums = [1, 2, 3, 4, 5]
n = 5
print(s.sortedArray(nums, n))

nums = [1, 2, 6, 5]
n = 4
print(s.sortedArray(nums, n))